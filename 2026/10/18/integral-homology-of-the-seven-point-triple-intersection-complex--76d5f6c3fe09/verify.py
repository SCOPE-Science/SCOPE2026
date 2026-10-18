#!/usr/bin/env python3
"""Exact integral homology verifier for the seven-point triple-intersection complex.

Requires Python >=3.9 and a C++17 compiler named g++ on PATH.
The companion program exhausts the simplices and verifies the matching gradient DAG.
This script independently validates all boundary compositions and gives explicit
unimodular unit-pivot reductions of the integral Morse boundary matrices.
"""
from pathlib import Path
from collections import Counter
import subprocess
import tempfile
import sys

HERE = Path(__file__).resolve().parent
FACEVECTOR = [1,35,525,4445,23555,81942,191170,300855,317730,221865,100296,29295,5950,910,105,7]
EXPECTED = {
    'forward': {'pairs': 639293, 'arcs': 501581, 'critical': {7:45,8:27,9:16,10:12}, 'ranks': {7:16,8:11,9:5}},
    'reverse': {'pairs': 639283, 'arcs': 540642, 'critical': {7:60,8:41,9:11,10:8}, 'ranks': {7:31,8:10,9:1}},
}


def parse(text):
    lines = text.splitlines()
    assert len(lines) >= 6, 'incomplete output'
    assert lines[-1] == 'FINISHED', 'missing completion marker'
    assert lines[0].startswith('FACEVECTOR ')
    fv = [int(x) for x in lines[0].split()[1:]]
    pairs = int(lines[1].split()[1]); arcs=int(lines[2].split()[1])
    assert lines[1].startswith('PAIRS ') and lines[2].startswith('GRADIENT_ARCS ')
    assert lines[3].startswith('CRITICAL ')
    critical = [int(x) for x in lines[3].split()[1:]]
    ptr=4; matrices={}
    while lines[ptr]!='FINISHED':
        header=lines[ptr].split(); ptr+=1
        assert len(header)==4 and header[0]=='MATRIX'
        d, rows, cols=map(int,header[1:]); assert d not in matrices
        M=[]
        for _ in range(rows):
            row=[int(x) for x in lines[ptr].split()];ptr+=1
            assert len(row)==cols
            M.append(row)
        matrices[d]=M
    assert ptr==len(lines)-1
    return fv,pairs,arcs,critical,matrices


def is_zero_composition(left, right):
    if len(left[0]) != len(right): return False
    r=len(left);m=len(right);c=len(right[0])
    for i in range(r):
        for k in range(c):
            if sum(left[i][j]*right[j][k] for j in range(m))!=0:
                return False
    return True


def unit_rank(M):
    """Unimodular row/column operations reducing a matrix to diag(1,...,1,0...)."""
    a=[row[:] for row in M]
    r=len(a);c=len(a[0]); h=0
    while h<min(r,c):
        p=next(((i,j) for i in range(h,r) for j in range(h,c)
                if abs(a[i][j])==1),None)
        if p is None: break
        i,j=p; a[h],a[i]=a[i],a[h]
        for row in a: row[h],row[j]=row[j],row[h]
        if a[h][h]<0: a[h]=[-x for x in a[h]]
        assert a[h][h]==1
        for i in range(r):
            if i!=h and a[i][h]:
                m=a[i][h]
                a[i]=[x-m*y for x,y in zip(a[i],a[h])]
        for j in range(c):
            if j!=h and a[h][j]:
                m=a[h][j]
                for i in range(r):a[i][j]-=m*a[i][h]
        assert all(a[t][h]==int(t==h) for t in range(r))
        assert all(a[h][t]==int(t==h) for t in range(c))
        h+=1
    assert all(a[i][j]==int(i==j and i<h) for i in range(r) for j in range(c)), \
        'matrix has a nonzero nonunit residual block'
    return h


def run_mode(program, mode):
    frozen=(HERE / f'matrices_{mode}.txt').read_bytes()
    proc=subprocess.run([str(program)] + (['reverse'] if mode=='reverse' else []),
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=110,check=True)
    assert proc.stdout==frozen, f'generator disagrees with embedded {mode} certificate'
    fv,pairs,arcs,critical,mats=parse(proc.stdout.decode('utf-8'))
    exp=EXPECTED[mode]
    assert fv==FACEVECTOR and sum(fv)==1278686
    assert pairs==exp['pairs'] and arcs==exp['arcs']
    assert sum(critical)+2*pairs==sum(fv)
    assert {i:x for i,x in enumerate(critical) if x}==exp['critical']
    assert set(mats)=={7,8,9}
    assert is_zero_composition(mats[7],mats[8])
    assert is_zero_composition(mats[8],mats[9])
    ranks={i:unit_rank(mats[i]) for i in [7,8,9]}
    assert ranks==exp['ranks']
    h6=critical[7]-ranks[7]
    h7=critical[8]-ranks[7]-ranks[8]
    h8=critical[9]-ranks[8]-ranks[9]
    h9=critical[10]-ranks[9]
    assert (h6,h7,h8,h9)==(29,0,0,7)
    print(f'{mode}: faces={sum(fv)}, matched_pairs={pairs}, gradient_arcs={arcs}, '
          f'critical={exp["critical"]}, ranks={ranks}, homology=(H6:Z^29,H9:Z^7), '
          'all Smith factors units')


def main():
    with tempfile.TemporaryDirectory(prefix='kg73_') as tmp:
        out=Path(tmp)/'kg73_morse'
        subprocess.run(['g++','-O2','-std=c++17',str(HERE/'kg73_morse.cpp'),'-o',str(out)],
                       check=True,timeout=110)
        for mode in ['forward','reverse']:run_mode(out,mode)
    print('INTEGRAL_HOMOLOGY_VERIFIED')


if __name__=='__main__':
    main()
