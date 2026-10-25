#!/usr/bin/env python3
"""Replay two independent complete five-state binary-automaton censuses.
No third-party dependencies.  Only deterministic local source files are used.
"""
from pathlib import Path
import itertools
from collections import Counter
import re
import subprocess
import tempfile

N=5
ROOT=Path(__file__).resolve().parent
EXPECTED=[3444345,3763200,738000,108720,9120]

def decode(code):
    rows=[]
    for _ in range(2):
        row=[]
        for _ in range(N):
            row.append(code%N)
            code//=N
        rows.append(tuple(row))
    assert code==0
    return tuple(rows)

def encode(rows):
    code=0; power=1
    for row in rows:
        for x in row:
            code += x*power; power*=N
    return code

def orbit(code):
    rows=decode(code)
    ans=set()
    for perm in itertools.permutations(range(N)):
        inv=[0]*N
        for old,new in enumerate(perm): inv[new]=old
        moved=tuple(tuple(perm[row[inv[i]]] for i in range(N)) for row in rows)
        ans.add(encode(moved))
        ans.add(encode(moved[::-1]))
    return ans

def word_distance(code):
    rows=decode(code)
    mins=[None]*N
    for k in range(1,6):
        for letters in itertools.product(range(2),repeat=k):
            out=list(range(N))
            for letter in letters: out=[rows[letter][z] for z in out]
            for q in range(N):
                if mins[q] is None and out.count(out[q])>=2:
                    mins[q]=k
        if all(v is not None for v in mins):break
    return mins

def compile_run(src,exe,args):
    subprocess.run(['g++','-O3','-std=c++17','-o',str(exe),str(ROOT/src)],check=True)
    return subprocess.check_output([str(exe),*map(str,args)],text=True)

with tempfile.TemporaryDirectory() as tmp:
    tmp=Path(tmp)
    primary=compile_run('census.cpp',tmp/'census',[N])
    independent=compile_run('check_independent.cpp',tmp/'independent',[tmp/'extremals.txt'])
    assert primary == (ROOT/'census_report.txt').read_text(), 'primary census log mismatch'
    assert independent == (ROOT/'check_report.txt').read_text(), 'independent census log mismatch'
    assert 'total=9765625' in primary and 'synchronizing=8063385' in primary
    assert 'strong=2554344' in primary
    assert 'max=5 extremal=9120' in primary
    assert 'synchronizing=8063385 threshold5=9120' in independent
    for threshold,count in enumerate(EXPECTED,1):
        assert f'automaton_tau_{threshold}={count}' in primary
        assert f'independent tau_{threshold}={count}' in independent
    reps=[(int(a),int(b)) for a,b in re.findall(r'class code=(\d+) labeled_orbit=(\d+)',primary)]
    assert len(reps)==38 and len(set(a for a,b in reps))==38
    claimed_ids=set(map(int,(tmp/'extremals.txt').read_text().splitlines()))
    assert len(claimed_ids)==9120
    assert (ROOT/'extremal_ids.txt').read_bytes()==(tmp/'extremals.txt').read_bytes(), 'extremal ID certificate differs from independent enumeration'
    orbits=set()
    rank_types=Counter()
    for rep,size in reps:
        orbit_set=orbit(rep)
        assert len(orbit_set)==size==240, (rep,len(orbit_set),size)
        assert rep==min(orbit_set),'noncanonical representative'
        assert not(orbits & orbit_set), 'overlapping orbits'
        orbits.update(orbit_set)
        maps=decode(rep)
        rank_types[tuple(sorted(len(set(row)) for row in maps))]+=1
        d=word_distance(rep)
        assert max(d)==5 and all(isinstance(x,int) for x in d), (rep,d)
    assert orbits==claimed_ids,'orbit union differs from independent exhaustive enumeration'
    assert rank_types == {(3,4):8,(4,4):12,(4,5):18}
    for code in claimed_ids:
        maps=decode(code)
        for source in range(N):
            seen={source}
            while True:
                next_seen=seen | {maps[c][q] for q in seen for c in range(2)}
                if len(next_seen)==len(seen): break
                seen=next_seen
            assert len(seen)==N, f'extremal {code} is not strongly connected'
    assert sum(EXPECTED)==8063385
    print('VERIFY_OK')
    print('All 9,765,625 labeled ordered binary five-state transition tables visited by each of two independent algorithms.')
    print('Synchronizing: 8,063,385; histogram by worst compress-with-another threshold: '+str(EXPECTED))
    print('Maximum 5; 9,120 labeled extremals; 38 disjoint canonical symmetry classes, each of size 240.')
    print('All 38 extremal representatives independently tested by literal words of lengths 1 through 5.')
    print('All 9,120 extremals strongly connected; orbit types by unordered letter ranks: (3,4):8, (4,4):12, (4,5):18.')
