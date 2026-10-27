#!/usr/bin/env python3
"""Exact finite-case checks for cyclic-color equivariant local maps of the proper 3-color shift.

The program uses only Python's standard library.  It does not establish
historical priority or replace the accompanying symbolic proof.
"""
from itertools import product

P = (-1, 1)
Q = (0, 1, 2)
PATTERNS = list(product(P, repeat=2))

def color_out(offsets, triple):
    a, b, c = triple
    u, v = (b-a) % 3, (c-b) % 3
    u = -1 if u == 2 else 1
    v = -1 if v == 2 else 1
    return (b + offsets[PATTERNS.index((u, v))]) % 3

def preserve_edge_formula(offsets):
    f = dict(zip(PATTERNS, offsets))
    return all((v + f[v, w] - f[u, v]) % 3 != 0 for u,v,w in product(P, repeat=3))

def preserve_direct_colors(offsets):
    for a, b, c, d in product(Q, repeat=4):
        if a == b or b == c or c == d:
            continue
        if color_out(offsets, (a,b,c)) == color_out(offsets,(b,c,d)):
            return False
    return True

def edge_rule(offsets):
    f = dict(zip(PATTERNS, offsets))
    r = 0
    for a,b,c in product((0,1), repeat=3):
        u,v,w = (2*a-1,2*b-1,2*c-1)
        inc = (v+f[v,w]-f[u,v]) % 3
        assert inc in (1,2)
        out = int(inc==1)
        index = (a<<2) | (b<<1) | c
        r |= out << index
    return r

def absent_preimage(rule, word):
    states = {(a,b) for a,b in product((0,1),repeat=2)}
    trail=[len(states)]
    for z in word:
        states = {(b,c) for a,b in states for c in (0,1)
                  if ((rule >> ((a<<2)|(b<<1)|c)) & 1) == int(z)}
        trail.append(len(states))
    return not states, trail

def s3_invariant(offsets):
    for permutation in product(Q, repeat=3):
        if len(set(permutation)) != 3:
            continue
        for triple in product(Q, repeat=3):
            a,b,c = triple
            if a==b or b==c:
                continue
            transformed = tuple(permutation[t] for t in triple)
            if color_out(offsets, transformed) != permutation[color_out(offsets, triple)]:
                return False
    return True

all_rules=list(product(Q,repeat=4))
via_edges={f for f in all_rules if preserve_edge_formula(f)}
via_colors={f for f in all_rules if preserve_direct_colors(f)}
assert via_edges==via_colors

base={
    'identity':(0,0,0,0),
    'shift_plus':(2,1,2,1),
    'shift_minus':(1,1,2,2),
    'traffic_right':(0,0,1,0),
    'traffic_left':(0,2,0,0),
}
expect={tuple((x+c)%3 for x in offsets) for offsets in base.values() for c in Q}
assert len(expect)==15 and via_edges==expect
assert len({t for t in via_edges})==15
rules={g:edge_rule(g) for g in via_edges}
assert sorted(set(rules.values()))==[170,184,204,226,240]
assert {r:sum(rule==r for rule in rules.values()) for r in set(rules.values())}=={170:3,184:3,204:3,226:3,240:3}
assert all(edge_rule(base[name])==r for name,r in [('identity',204),('shift_plus',170),('shift_minus',240),('traffic_right',184),('traffic_left',226)])
assert absent_preimage(184, '1100')==(True,[4,3,1,1,0])
assert absent_preimage(226, '0011')==(True,[4,3,1,1,0])
full_symmetry={g for g in via_edges if s3_invariant(g)}
assert full_symmetry=={base['identity'],base['shift_plus'],base['shift_minus']}

# independent full-word check of all 15 maps on cyclic 3-color rings up to size 7
for n in range(3,8):
    words=[w for w in product(Q, repeat=n) if all(w[i]!=w[(i+1)%n] for i in range(n))]
    for g in via_edges:
        images={tuple(color_out(g, (w[(i-1)%n],w[i],w[(i+1)%n])) for i in range(n)) for w in words}
        assert all(all(y[i]!=y[(i+1)%n] for i in range(n)) for y in images)
        if rules[g] in (170,204,240):
            assert len(images)==len(words)
        

print('VERIFY_OK: 81 cyclic-equivariant centered-radius-one local maps examined twice;')
print('15 proper-coloring endomorphisms = 3 rotations times [identity, 2 shifts, 2 traffic maps];')
print('binary edge factors exactly 170,184,204,226,240 (3 lifts each);')
print('9 automorphisms, 6 nonsurjective traffic lifts; forbidden binary edge words 1100 / 0011;')
print('full three-color permutation symmetry leaves exactly 3 coordinate shifts;')
print('all 15 maps checked independently on proper 3-color rings of lengths 3..7.')
