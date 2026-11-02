#!/usr/bin/env python3
"""Reproduce the finite core and independently check the rational coefficient law."""
import collections
import pathlib
import subprocess
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
EXPECTED = {
 (6, ()):4, (7, ()):18, (8, ()):50, (8,(1,)):2,
 (9, ()):58, (9,(1,)):18, (10, ()):48, (10,(1,)):36,
 (10,(2,)):2, (11, ()):20, (11,(1,)):24, (11,(1,1)):6,
 (12, ()):10, (12,(1,)):8, (12,(1,1)):4,
 (13, ()):4, (13,(1,)):2, (13,(3,)):2,
}

def classes_from_profiles(lines):
    grouped = collections.Counter()
    for line in lines.splitlines():
        left, right = line.split(':')
        entries = [int(v) for v in left.split()]
        assert len(entries) == 10
        s,t,*m = entries
        assert 0 <= s <=3 and 0 <= t <= 3 and all(0 <= x <= 12 for x in m)
        cycles = tuple(sorted(int(v) for v in right.split()))
        grouped[(2 + sum(m), cycles)] += 1
    assert sum(grouped.values()) == 316
    assert grouped == EXPECTED, (grouped - EXPECTED, EXPECTED - grouped)
    return grouped

def coeffs(groups, upto):
    result = [0]*(upto+1)
    for (base,cycles),mul in groups.items():
        a=[0]*(upto+1)
        if base>upto:continue
        a[base]=mul
        for cycle_length in cycles:
            for i in range(base+cycle_length,upto+1):
                a[i]+=a[i-cycle_length]
        for i in range(base,upto+1):result[i]+=a[i]
    return result

def predicted(n):
    early={6:4,7:18,8:52,9:78,10:106,11:106,12:116,13:122}
    if n<14:return early.get(n,0)
    return 10*n-14+2*(n%2==0)+2*(n%3==1)

with tempfile.TemporaryDirectory() as td:
    enum = pathlib.Path(td)/'enum'
    direct=pathlib.Path(td)/'direct'
    for source,target in [('enumerate.cpp',enum),('direct_census.cpp',direct)]:
        subprocess.run(['g++','-std=c++17','-O2',str(HERE/source),'-o',str(target)],check=True)
    run = subprocess.run([str(enum),'12'],capture_output=True,text=True,check=True)
    generated=run.stdout
    saved=(HERE/'PROFILES.tsv').read_text(encoding='utf-8')
    assert generated==saved
    assert 'bases 316' in run.stderr, run.stderr
    groups=classes_from_profiles(generated)
    values=coeffs(groups,120)
    for n in range(2,121):
        assert values[n]==predicted(n), (n,values[n],predicted(n))
    # Independent direct enumeration of every word and collection by its
    # three-mer spectrum plus both two-bit endpoint states.
    direct_output = subprocess.check_output([str(direct)],text=True)
    for line in direct_output.splitlines():
        fields=list(map(int,line.split()))
        n=fields[0];count_size_two=fields[5]
        assert count_size_two == values[n], (n,count_size_two,values[n])
    print('VERIFY_OK 316 bases, 18 groups, coefficients n=2..120, independent direct census n=4..21')
