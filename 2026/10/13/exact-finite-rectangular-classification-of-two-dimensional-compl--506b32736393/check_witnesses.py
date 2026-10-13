#!/usr/bin/env python3
"""Independently check the upper-bound witnesses for a small rectangular difference-cover census."""
import itertools
import json
from pathlib import Path

witnesses = json.loads(Path(__file__).with_name("witnesses.json").read_text(encoding="utf-8"))
expected = {(1,1):4,(1,2):5,(1,3):6,(1,4):7,(1,5):8,
            (2,2):7,(2,3):8,(2,4):9,(2,5):10,
            (3,3):9,(3,4):11,(3,5):12,
            (4,4):12,(4,5):13,(5,5):15}
assert len(witnesses) == len(expected)
seen = set()
for entry in witnesses:
    a,b = entry["span_x"],entry["span_y"]
    assert 1 <= a <= b <= 5
    assert (a,b) not in seen
    seen.add((a,b))
    pts = [tuple(pt) for pt in entry["points"]]
    assert len(set(pts)) == len(pts) == expected[(a,b)] == entry["minimum_marks"]
    assert all(0 <= x <= a and 0 <= y <= b for x,y in pts)
    diffs = {(x-u,y-v) for (x,y),(u,v) in itertools.product(pts, repeat=2)}
    required = {(u,v) for u in range(-a,a+1) for v in range(-b,b+1)}
    assert required <= diffs, (a,b,required-diffs)
assert seen == set(expected)
print("WITNESSES_OK 15 rectangular difference covers, including M2(6,6)=15")
