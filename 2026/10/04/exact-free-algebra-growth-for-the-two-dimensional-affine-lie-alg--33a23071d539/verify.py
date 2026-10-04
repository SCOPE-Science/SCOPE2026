#!/usr/bin/env python3
from itertools import product


def inv_mod(a,p):
    return pow(a % p, p-2, p)


def add_to_basis(v, basis, p):
    v = [x % p for x in v]
    for pivot in sorted(basis):
        if v[pivot]:
            c = v[pivot]
            row = basis[pivot]
            v = [(x-c*y) % p for x,y in zip(v,row)]
    if not any(v):
        return False
    pivot = next(i for i,x in enumerate(v) if x)
    z = inv_mod(v[pivot],p)
    v = [(z*x) % p for x in v]
    for q,row in list(basis.items()):
        if row[pivot]:
            c = row[pivot]
            basis[q] = [(x-c*y) % p for x,y in zip(row,v)]
    basis[pivot] = v
    return True


def bracket(u,v,p):
    out = [0]*len(u)
    for j in range(0,len(u),2):
        a,b = u[j],u[j+1]
        c,d = v[j],v[j+1]
        out[j] = 0
        out[j+1] = (a*d-c*b) % p
    return out


def term_dimension(p,n):
    inputs = list(product(range(p), repeat=2*n))
    generators=[]
    for i in range(n):
        vec=[]
        for pt in inputs:
            vec.extend((pt[2*i],pt[2*i+1]))
        generators.append(vec)
    basis={}
    elems=[]
    for g in generators:
        if add_to_basis(g,basis,p):
            elems.append(g)
    changed=True
    while changed:
        changed=False
        current=list(basis.values())
        for i in range(len(current)):
            for j in range(i+1,len(current)):
                w=bracket(current[i],current[j],p)
                if add_to_basis(w,basis,p):
                    changed=True
        # loop recomputes all pairs after each rank increase batch
    return len(basis)


def formula(q,n):
    return n+(n-1)*(q**n-1)

cases=[(2,1),(2,2),(2,3),(3,1),(3,2)]
for q,n in cases:
    got=term_dimension(q,n)
    want=formula(q,n)
    print(f"q={q} n={n} computed={got} formula={want}")
    assert got==want
print("CHECK_OK")
