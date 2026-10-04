#!/usr/bin/env python3
from collections import deque
from itertools import permutations
from pathlib import Path
import subprocess, tempfile

ROOT=Path(__file__).resolve().parent
expected=(ROOT/'CENSUS.txt').read_text()
with tempfile.TemporaryDirectory() as td:
    exe=Path(td)/'census'
    subprocess.run(['cc','-O3','-std=c99',str(ROOT/'census.c'),'-o',str(exe)],check=True)
    got=subprocess.check_output([str(exe)],text=True)
assert got==expected

reps=[
((3,1,1,0,0),(0,2,3,4,2),'abbbabba'),
((3,2,1,0,0),(0,3,1,4,1),'baababba'),
((3,2,1,0,0),(0,2,3,4,1),'abaabbba'),
((3,2,1,0,0),(0,4,3,1,3),'baabbaba'),
]

def image(mask,f):
    out=0
    for q in range(5):
        if mask>>q&1: out|=1<<f[q]
    return out

def dist_and_word(a,b,target):
    par={31:(None,None)}; dq=deque([31])
    while dq:
        s=dq.popleft()
        if not (s>>target&1):
            w=[]
            while par[s][0] is not None:
                ps,ch=par[s]; w.append(ch); s=ps
            return len(w),''.join(reversed(w))
        for ch,f in [('a',a),('b',b)]:
            t=image(s,f)
            if t not in par:
                par[t]=(s,ch); dq.append(t)
    return None,None

def strongly_connected(a,b):
    for start in range(5):
        seen={start}; st=[start]
        while st:
            q=st.pop()
            for f in (a,b):
                r=f[q]
                if r not in seen: seen.add(r); st.append(r)
        if len(seen)!=5:return False
    return True

def orbit(pair):
    a,b=pair; out=set()
    for p in permutations(range(5)):
        inv=[0]*5
        for i,x in enumerate(p):inv[x]=i
        aa=tuple(p[a[inv[j]]] for j in range(5))
        bb=tuple(p[b[inv[j]]] for j in range(5))
        out.add((aa,bb));out.add((bb,aa))
    return out

orbits=[]
for a,b,w in reps:
    assert strongly_connected(a,b)
    ds=[]
    for q in range(5):
        d,_=dist_and_word(a,b,q); ds.append(d)
    assert max(ds)==8
    d,ww=dist_and_word(a,b,0)
    assert d==8 and ww==w
    O=orbit((a,b)); assert len(O)==240
    orbits.append(O)
for i in range(4):
    for j in range(i): assert orbits[i].isdisjoint(orbits[j])
assert sum(map(len,orbits))==960

# The A_5 construction in Ferens--Szykula--Vorel 2021.
A5=((1,0,0,4,3),(0,2,3,4,1))
assert A5 in orbits[2]

vals={}
for line in expected.strip().splitlines():
    if '=' in line and line.split('=',1)[0].startswith(('ordered_pairs','synchronizing','max_','extremal_ordered_labeled','hist_','extremal_orbits')):
        k,v=line.split('=',1); vals[k]=int(v)
assert vals['ordered_pairs']==3125**2
assert vals['synchronizing']==8063385
assert vals['max_1_avoiding_threshold']==8
assert vals['extremal_ordered_labeled']==960
assert vals['extremal_orbits']==4
assert sum(v for k,v in vals.items() if k.startswith('hist_'))==vals['synchronizing']
print('VERIFY_OK')
