#!/usr/bin/env python3
"""Reproduce a complete census and independently inspect its extremal witness."""
from itertools import permutations, product
from pathlib import Path
import re
import subprocess

here = Path(__file__).resolve().parent

def run(source):
    import tempfile
    with tempfile.TemporaryDirectory() as temp:
        exe = Path(temp) / 'census'
        subprocess.run(['g++', '-std=c++17', '-O3', str(here / source), '-o', str(exe)], check=True)
        return subprocess.check_output([str(exe)], text=True)

def parse_one(s):
    lengths, multiplicities = {}, {}
    for line in s.splitlines():
        if line.startswith('LEN '):
            m = re.fullmatch(r'LEN (\d+) (\d+) UNIQUE (\d+) TOTAL_WAYS (\d+)', line)
            assert m, line
            lengths[int(m[1])] = tuple(map(int, m.groups()[1:]))
        if line.startswith('M '):
            m = re.fullmatch(r'M (\d+) (\d+)', line)
            assert m, line
            multiplicities[int(m[1])] = int(m[2])
    return lengths, multiplicities

def parse_two(s):
    lengths, multiplicities = {}, {}
    for line in s.splitlines():
        if line.startswith('LEN '):
            m = re.fullmatch(r'LEN (\d+) COUNT (\d+) UNIQUE (\d+) SUMWORDS (\d+)', line)
            assert m, line
            lengths[int(m[1])] = tuple(map(int, m.groups()[1:]))
        if line.startswith('MULT '):
            m = re.fullmatch(r'MULT (\d+) COUNT (\d+)', line)
            assert m, line
            multiplicities[int(m[1])] = int(m[2])
    return lengths, multiplicities

out1, out2 = run('count.cpp'), run('count_reverse.cpp')
lengths1, multiplicities1 = parse_one(out1)
lengths2, multiplicities2 = parse_two(out2)
assert lengths1 == lengths2 and multiplicities1 == multiplicities2
assert sum(x[0] for x in lengths1.values()) == 8_063_385
assert sum(multiplicities1.values()) == 8_063_385
assert sum(x[1] for x in lengths1.values()) == multiplicities1[1] == 5_071_440
assert 3125 * 3125 - 8_063_385 == 1_702_240
assert max(multiplicities1) == 64 and multiplicities1[64] == 240
assert max(k for k,v in lengths1.items() if v[0]) == 16

# For the witness, enumerate *all* words up to length 13 and count resets.
a = (2, 3, 1, 0, 0)
b = (2, 3, 1, 4, 0)
patterns = set()
for length in range(1, 14):
    resets = []
    for word in product('ab', repeat=length):
        image = set(range(5))
        for letter in word:
            image = { (a if letter == 'a' else b)[s] for s in image }
        if len(image) == 1:
            resets.append(''.join(word))
    if length < 13:
        assert not resets
    else:
        assert len(resets) == 64
        patterns = set(resets)
# Independently specified six free binary choices among fixed letters.
expected = set()
for x0,x1,x2,x3,x4,x5 in product('ab', repeat=6):
    expected.add('ab' + x0 + x1 + 'a' + x2 + 'b' + x3 + 'a' + x4 + x5 + 'ba')
assert patterns == expected and len(expected) == 64

# All conjugates under relabeling and swapping letters form a 240-element orbit.
def conjugate(t, perm):
    inv = [0]*5
    for i,x in enumerate(perm): inv[x] = i
    return tuple(perm[t[inv[j]]] for j in range(5))

orbit = set()
for perm in permutations(range(5)):
    aa, bb = conjugate(a,perm), conjugate(b,perm)
    orbit.add((aa,bb)); orbit.add((bb,aa))
assert len(orbit) == 240

print('independent enumerations agree on every length and multiplicity cell')
print('synchronizing=8063385 nonsynchronizing=1702240 unique=5071440')
print('multiplicity_max=64 extremal_automata=240 symmetry_orbit=240')
print('extremal_witness: no reset length<13; exactly 64 length-13 reset words')
print('all 64 witness words match the six-choice regular expression')
print('multiplicity histogram:', sorted(multiplicities1.items()))
