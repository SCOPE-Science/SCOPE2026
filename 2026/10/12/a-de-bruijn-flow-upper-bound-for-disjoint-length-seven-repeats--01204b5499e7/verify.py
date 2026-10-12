#!/usr/bin/env python3
import json
from pathlib import Path
from itertools import product

def least_period(w):
    n=len(w)
    for p in range(1,n+1):
        if all(w[i] == w[i+p] for i in range(n-p)):
            return p
    raise AssertionError

root=Path(__file__).resolve().parent
cert=json.loads((root/"certificate.json").read_text(encoding="utf-8"))
assert cert["schema_version"] == 1
assert cert["alphabet"] == ["0","1"]
n=cert["n"]
assert n == 7

vertices=["".join(x) for x in product("01", repeat=n-1)]
vid={v:i for i,v in enumerate(vertices)}
assert cert["vertices"] == vertices
edges=[]
caps=[]
for x in product("01", repeat=n):
    w="".join(x)
    u=vid[w[:-1]]
    v=vid[w[1:]]
    p=least_period(w)
    cap=(n+p-1)//p
    edges.append((u,v,w))
    caps.append(cap)

rows=cert["edge_capacity"]
assert len(rows)==len(edges)==128
for row,(u,v,w),cap in zip(rows,edges,caps):
    assert row == {"word":w,"capacity":cap}
assert sum(caps)==cert["full_capacity_windows"]==236

V=len(vertices)
g=[0]*V
for (u,v,w),cap in zip(edges,caps):
    g[u]+=cap
    g[v]-=cap

expected={(None,None)}
expected.update((s,t) for s in range(V) for t in range(V) if s!=t)
seen=set()
global_lower=10**9

for row in cert["all_endpoint_duals"]:
    s=row["start"]; t=row["end"]
    key=(s,t)
    assert key in expected and key not in seen
    seen.add(key)
    b=[0]*V
    if s is not None:
        assert 0<=s<V and 0<=t<V and s!=t
        b[s]=1
        b[t]=-1
    else:
        assert t is None
    h=[g[i]-b[i] for i in range(V)]
    pi=row["potential"]
    assert len(pi)==V and all(isinstance(z,int) for z in pi)
    dual=sum(pi[i]*h[i] for i in range(V))
    for (u,v,w),cap in zip(edges,caps):
        dual += cap*min(0, 1-pi[u]+pi[v])
    assert dual == row["minimum_deleted_windows"]
    assert dual >= 16
    global_lower=min(global_lower,dual)

assert seen==expected
assert len(seen)==1+V*(V-1)==4033
assert global_lower==16

wit=cert["sharp_relaxation_witness"]
s=wit["start"]; t=wit["end"]
assert (s,t) in expected and s is not None
d=wit["deleted_edge_multiplicity"]
assert len(d)==len(edges) and all(isinstance(z,int) for z in d)
assert all(0<=z<=cap for z,cap in zip(d,caps))
b=[0]*V
b[s]=1; b[t]=-1
h=[g[i]-b[i] for i in range(V)]
lhs=[0]*V
for z,(u,v,w) in zip(d,edges):
    lhs[u]+=z
    lhs[v]-=z
assert lhs==h
assert sum(d)==16

assert cert["conclusion"] == {
    "minimum_deleted_windows":16,
    "maximum_kept_windows":220,
    "word_length_upper_bound":226
}
print("VERIFY_OK vertices=64 edges=128 total_capacity=236 endpoint_cases=4033 min_deleted=16 max_windows=220 C27_upper=226")
