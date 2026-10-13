#!/usr/bin/env python3
import json, os, pathlib, subprocess, tempfile
from collections import deque

root=pathlib.Path(__file__).resolve().parent
cert=json.loads((root/"certificate.json").read_text(encoding="utf-8"))

with tempfile.TemporaryDirectory() as td:
    exe=pathlib.Path(td)/"census"
    subprocess.run(
        ["g++","-O3","-march=native","-fopenmp","-std=c++17",str(root/"census.cpp"),"-o",str(exe)],
        check=True
    )
    env=os.environ.copy()
    env["OMP_NUM_THREADS"]=str(max(1,min(8,os.cpu_count() or 1)))
    p=subprocess.run([str(exe)],check=True,text=True,capture_output=True,env=env,timeout=180)
out=p.stdout.strip()
assert out.startswith("VERIFY_OK maxima=0,1,2,3,4,5,6,7,9"), out

a=(0,0,1,2,4,4,5,5,8)
b=(0,2,3,4,4,6,7,8,8)
start=(1,6)

def step(pair, trans):
    x,y=trans[pair[0]],trans[pair[1]]
    return (min(x,y),max(x,y))

# Independent forward BFS on the explicit witness.
q=deque([start]); dist={start:0}; word={start:""}
while q:
    s=q.popleft()
    if s[0]==s[1]:
        target=s; break
    for ch,t in (("a",a),("b",b)):
        u=step(s,t)
        if u not in dist:
            dist[u]=dist[s]+1
            word[u]=word[s]+ch
            q.append(u)
else:
    raise AssertionError("witness pair did not synchronize")

assert dist[target]==9
assert word[target]=="babbaabbb"
trajectory=[list(start)]
s=start
for ch in word[target]:
    s=step(s,a if ch=="a" else b)
    trajectory.append(list(s))
assert trajectory==cert["first_representative_pair_trajectory"]

# Check the second normalized extremal is obtained by chain reversal plus letter swap.
def reverse_conjugate(t):
    n=len(t)
    return tuple(n-1-t[n-1-i] for i in range(n))
a2=(0,0,1,2,4,4,5,6,8)
b2=(0,3,3,4,4,6,7,8,8)
assert reverse_conjugate(a)==b2
assert reverse_conjugate(b)==a2

# Direct combinatorial count of nondecreasing maps: C(2n-1,n).
import math
for n,expected in cert["number_of_nondecreasing_maps"].items():
    n=int(n)
    assert math.comb(2*n-1,n)==expected

print(out)
print("WITNESS_OK word=babbaabbb trajectory="+";".join(map(str,trajectory)))
