#!/usr/bin/env python3
import json
from pathlib import Path
from itertools import product

def graph(n,k):
    vertices=list(product(range(k), repeat=n))
    index={v:i for i,v in enumerate(vertices)}
    edges=set()
    for v in vertices:
        i=index[v]
        for a in range(k):
            w=v[1:]+(a,)
            j=index[w]
            if i != j:
                edges.add(tuple(sorted((i,j))))
    return vertices,index,edges

root=Path(__file__).resolve().parent
cert=json.loads((root/"coloring.json").read_text(encoding="utf-8"))
V,I,E=graph(4,3)

assert cert["graph"] == "S(4,3)"
assert len(V) == cert["vertex_count"] == 81
assert len(E) == cert["edge_count"] == 237

colors={}
for row in cert["colors"]:
    v=tuple(int(x) for x in row["vertex"])
    assert v in I
    assert row["color"] in (0,1,2)
    assert v not in colors
    colors[v]=row["color"]
assert len(colors)==81

for a,b in E:
    assert colors[V[a]] != colors[V[b]]

sizes=[sum(colors[v]==c for v in V) for c in range(3)]
assert sizes == cert["color_class_sizes"] == [28,30,23]

tri=[tuple(int(x) for x in s) for s in cert["triangle"]]
assert tri == [(0,0,0,0),(0,0,0,1),(1,0,0,0)]
for i in range(3):
    for j in range(i+1,3):
        assert tuple(sorted((I[tri[i]],I[tri[j]]))) in E

# A proper 3-colouring gives chi <= 3; the triangle gives chi >= 3.
print("VERIFY_OK vertices=81 edges=237 color_classes=28,30,23 triangle=0000,0001,1000 chi=3")
