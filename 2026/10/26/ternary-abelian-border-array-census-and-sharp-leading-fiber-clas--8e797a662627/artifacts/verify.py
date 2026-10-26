#!/usr/bin/env python3
"""Recompute all ternary Abelian-border-array counts in two representations."""
import pathlib
import subprocess
import tempfile
import re
import csv

here=pathlib.Path(__file__).resolve().parent
with (here/'expected_counts.tsv').open(encoding='utf-8') as f:
    expected={int(r['n']):int(r['realizable_arrays']) for r in csv.DictReader(f,delimiter='\t')}
assert sorted(expected)==list(range(1,17))
with tempfile.TemporaryDirectory() as d:
    records=[]
    for name in ('abelian_census','abelian_independent'):
        exe=pathlib.Path(d)/name
        subprocess.run(['g++','-O3','-std=c++17',str(here/(name+'.cpp')),'-o',str(exe)],check=True,timeout=60)
        out=subprocess.run([str(exe)],check=True,capture_output=True,text=True,timeout=120).stdout
        lines=out.splitlines()
        assert len(lines)==16
        records.append(lines)
for n in range(1,17):
    first=records[0][n-1].split(' histogram=')
    fields=first[0].split()
    assert len(fields)==7
    k,total,distinct,maxfiber,maxcount,singletons,squares=map(int,fields)
    assert k==n and total==(3**n+3)//6
    assert distinct==expected[n]
    assert singletons>=1 and squares>=total
    assert maxfiber==2**max(0,n-2)
    if n>=3: assert maxcount==1
    hist={int(f):int(c) for f,c in (x.split(':') for x in first[1].split(',') if x)}
    assert sum(hist.values())==distinct
    assert sum(f*c for f,c in hist.items())==total
    assert sum(f*f*c for f,c in hist.items())==squares
    assert hist[maxfiber]==maxcount
    if n>=4: assert hist[2**(n-3)]==2
    fields2=records[1][n-1].split()
    assert list(map(int,fields2))==[n,3**(n-1),expected[n]]
print('ABELIAN_TERNARY_PASS lengths=1..16 methods=restricted_growth,all_first_zero structural_runner_up=4..16')
