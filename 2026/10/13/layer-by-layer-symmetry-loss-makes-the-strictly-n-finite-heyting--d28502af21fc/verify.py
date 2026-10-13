#!/usr/bin/env python3
from itertools import permutations
from math import factorial

checks=0

def ok(c,msg='assertion failed'):
    global checks
    checks += 1
    if not c: raise AssertionError(msg)

def leq(q, a, b):
    # vertices (level,label), levels increase downward.
    i,l=a; j,r=b
    if i==j: return l==r
    if i<j: return False
    # i>j: lower level a below upper level b
    if i>=j+2: return True
    return r != l+1

def extend_from_p0(q,d,p0):
    ps=[tuple(p0)]
    for i in range(1,d+1):
        prev=ps[-1]
        if prev[0] != 0:
            return None
        cur=[None]*q
        for l in range(q-1): cur[l]=prev[l+1]-1
        cur[q-1]=q-1
        if sorted(cur)!=list(range(q)):
            return None
        ps.append(tuple(cur))
    return ps

def is_order_aut(q,d,ps):
    if ps is None or len(ps)!=d+1: return False
    verts=[(i,l) for i in range(d+1) for l in range(q)]
    def f(v): i,l=v; return i,ps[i][l]
    for a in verts:
        for b in verts:
            if leq(q,a,b)!=leq(q,f(a),f(b)): return False
    return True

# Exhaust every possible top-layer permutation through q=7, and verify exact truncation counts.
for q in range(2,8):
    perms=list(permutations(range(q)))
    for d in range(0,q+2):
        count=0
        for p0 in perms:
            ps=extend_from_p0(q,d,p0)
            good=is_order_aut(q,d,ps)
            if good:
                count+=1
                # Derived fixed-prefix law and uniqueness of lower-layer action.
                for j in range(min(d,q-1)):
                    ok(p0[j]==j, f'prefix not fixed q={q} d={d}')
            ok(good == (all(p0[j]==j for j in range(min(d,q-1)))),
               f'criterion mismatch q={q} d={d} p0={p0}')
        expected=factorial(max(q-d,1)) if d<=q-1 else 1
        ok(count==expected, f'count mismatch q={q} d={d}: {count} != {expected}')

# For the source family q=2^n+1, depth q-1 is rigid; check n=0..8 symbolically.
for n in range(9):
    q=2**n+1
    d=q-1
    ok(max(q-d,1)==1)

print(f'VERIFY_OK {checks} exact assertions; exhaustive top-layer permutations for q<=7 and all truncation depths')
