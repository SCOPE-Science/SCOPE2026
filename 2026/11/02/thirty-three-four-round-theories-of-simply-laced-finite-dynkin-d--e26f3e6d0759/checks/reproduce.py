#!/usr/bin/env python3
"""Reproduce exact four-round type classifications for simply laced diagrams.

Requires a standard C++17 compiler and Python 3. No network or third-party packages.
"""
from pathlib import Path
from collections import defaultdict
from tempfile import TemporaryDirectory
import subprocess
import sys

HERE=Path(__file__).resolve().parent

def expected(max_order):
    labels=[]
    for n in range(1,max_order+1):
        labels.append('A'+str(n))
        if n>=4:labels.append('D'+str(n))
        if 6<=n<=8:labels.append('E'+str(n))
    a_tail=tuple('A'+str(n) for n in range(16,max_order+1))
    d_tail=tuple('D'+str(n) for n in range(17,max_order+1))
    clusters=[]
    for x in labels:
        if x in a_tail:
            if x==a_tail[0]:clusters.append(a_tail)
        elif x in d_tail:
            if x==d_tail[0]:clusters.append(d_tail)
        else:clusters.append((x,))
    return {frozenset(p) for p in clusters}

def parse_cpp(text):
    lines=text.splitlines()
    assert lines[0]=='CLUSTERS 33', lines[0]
    out=[]
    for line in lines[1:]:
        if line.startswith('TYPE_COUNT '):continue
        left,right=line.split(': ',1)
        assert left.isdigit()
        out.append(frozenset(right.split()))
    return set(out)

def parse_py(text):
    lines=text.splitlines()
    assert lines[0]=='INDEPENDENT_PYTHON_CLASSES 33', lines[0]
    out=[]
    for line in lines[1:]:
        k,names=line.split(' ',1)
        assert k.isdigit()
        out.append(frozenset(names.split(',')))
    return set(out)

def main():
    with TemporaryDirectory() as directory:
        binary=str(Path(directory)/'classify')
        subprocess.run(['g++','-std=c++17','-O2',str(HERE/'types.cpp'),'-o',binary],check=True)
        c=subprocess.run([binary,'40'],capture_output=True,text=True,check=True).stdout
    p=subprocess.run([sys.executable,str(HERE/'types.py'),'22'],capture_output=True,text=True,check=True).stdout
    assert parse_cpp(c)==expected(40), 'C++ class partition disagrees with the stated theorem'
    assert parse_py(p)==expected(22), 'Python class partition disagrees with the stated theorem'
    print('PASS: exhaustive rank-four classes for A1..A40, D4..D40, E6/E7/E8')
    print('PASS: 33 distinct classes; stabilization A16 and D17')
    print('PASS: independent Python reconstruction for A1..A22 and D4..D22')
    print('NOTE: the all-order tail bound follows from the separate gap-game lemma in RESULT.md')

if __name__=='__main__':main()
