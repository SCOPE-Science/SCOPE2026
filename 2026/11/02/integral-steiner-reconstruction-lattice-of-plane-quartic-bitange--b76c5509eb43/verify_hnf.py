#!/usr/bin/env python3
"""Independent exact Hermite-form and rational reconstruction check (requires sympy)."""
from collections import Counter
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from sympy.polys.domains import ZZ

def parity(z): return z.bit_count()&1
odd=[(a,b) for a in range(8) for b in range(8) if parity(a&b)]
vec=range(1,64)
def incident(a,b,v):
    x=v&7; y=v>>3
    return 1-(parity(x&y)^parity(a&x)^parity(b&y))
M=sp.Matrix([[incident(a,b,v) for v in vec] for a,b in odd])
assert M.shape==(28,63)
H=hermite_normal_form(M)
assert H.shape==(28,28)
assert abs(H.det())==805306368
D=smith_normal_form(M,domain=ZZ)
assert Counter(abs(D[i,i]) for i in range(28))==Counter({1:7,2:14,4:6,12:1})
orders=[]
Hinv=H.inv()
for i in range(28):
    col=Hinv[:,i]
    from math import lcm
    orders.append(lcm(*[int(t.q) for t in col]))
assert orders==[12]*28,orders
print('HNF_VERIFY_OK: index 805306368; independent Smith factors 1^7,2^14,4^6,12; all 28 basis-vector orders 12')
