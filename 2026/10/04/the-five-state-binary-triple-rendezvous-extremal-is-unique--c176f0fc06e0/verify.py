#!/usr/bin/env python3
from collections import deque
from itertools import permutations
from pathlib import Path
import shutil, subprocess, tempfile

ROOT=Path(__file__).resolve().parent
EXPECTED=(ROOT/'census_output.txt').read_text(encoding='utf-8')
A=(0,4,1,2,3)
B=(4,1,2,1,0)
N=5

def image(mask, t):
    r=0
    for i in range(N):
        if mask>>i & 1:
            r |= 1<<t[i]
    return r

def shortest(start):
    q=deque([start]); parent={start:(None,'')}
    goal=None
    while q:
        s=q.popleft()
        if s and s & (s-1)==0:
            goal=s; break
        for ch,t in [('a',A),('b',B)]:
            u=image(s,t)
            if u not in parent:
                parent[u]=(s,ch); q.append(u)
    assert goal is not None
    w=[]; u=goal
    while parent[u][0] is not None:
        u0,ch=parent[u]; w.append(ch); u=u0
    return ''.join(reversed(w))

triples={
 (0,1,2):(9,'babaaabab'),
 (0,1,3):(8,'bbaaabab'),
 (0,2,3):(9,'babaaabab'),
 (1,2,3):(9,'aabaaabab'),
 (0,1,4):(11,'aababaaabab'),
 (0,2,4):(9,'abbaaabab'),
 (1,2,4):(8,'abaaabab'),
 (0,3,4):(10,'ababaaabab'),
 (1,3,4):(7,'baaabab'),
 (2,3,4):(10,'aaabaaabab'),
}
for S,(L,w) in triples.items():
    m=sum(1<<i for i in S)
    got=shortest(m)
    assert len(got)==L and got==w, (S,got,L,w)
assert min(L for L,_ in triples.values())==7
rw=shortest((1<<N)-1)
assert rw=='baaababaaabab' and len(rw)==13

def relabel(a,b,p,swap=False):
    inv=[0]*N
    for old,new in enumerate(p): inv[new]=old
    u,v=(b,a) if swap else (a,b)
    aa=tuple(p[u[inv[j]]] for j in range(N))
    bb=tuple(p[v[inv[j]]] for j in range(N))
    return aa,bb
orbit=set()
for p in permutations(range(N)):
    orbit.add(relabel(A,B,p,False)); orbit.add(relabel(A,B,p,True))
assert len(orbit)==240

# Replay the exhaustive C census when a C compiler is available.
cc=shutil.which('cc')
assert cc is not None, 'C compiler required for exhaustive replay'
with tempfile.TemporaryDirectory() as td:
    exe=Path(td)/'census'
    subprocess.run([cc,'-O3','-std=c11',str(ROOT/'census.c'),'-o',str(exe)],check=True)
    got=subprocess.run([str(exe)],check=True,text=True,capture_output=True).stdout
assert got==EXPECTED, 'exhaustive census output mismatch'
print('VERIFY_OK')
