#!/usr/bin/env python3
"""Independent finite-field check of regularity counts in height-two incidence algebras.

Uses literal incidence-algebra multiplication and a linear-system solvability
check for a*b*a=a. No regularity criterion is used in the brute-force test.
"""
from itertools import product
from math import comb

PATH = ((0, 1), (2, 1), (2, 3))
STAR = ((0, 1), (0, 2), (0, 3))


def operations(q):
    if q in (2, 3):
        return lambda a, b: (a+b) % q, lambda a,b: (a*b) % q
    if q == 4:
        def mul(a,b):
            v = 0
            for j in range(2):
                if b & (1 << j): v ^= a << j
            if v & 8: v ^= 0b1100   # polynomial reduction modulo t^2+t+1
            if v & 4: v ^= 0b111
            return v
        return lambda a,b: a ^ b, mul
    raise ValueError(q)


def algebra_product(a,b,edges,add,mul):
    out = [mul(a[i],b[i]) for i in range(4)]
    for j,(u,v) in enumerate(edges):
        out.append(add(mul(a[u],b[4+j]),mul(a[4+j],b[v])))
    return out


def is_in_span(columns,target,q,add,mul):
    dim=len(target)
    rows=[[columns[col][r] for col in range(dim)]+[target[r]] for r in range(dim)]
    rank=0
    for col in range(dim):
        i=next((i for i in range(rank,dim) if rows[i][col]),None)
        if i is None: continue
        rows[rank],rows[i]=rows[i],rows[rank]
        inv=next(z for z in range(1,q) if mul(z,rows[rank][col])==1)
        rows[rank]=[mul(inv,z) for z in rows[rank]]
        for j in range(dim):
            if j!=rank and rows[j][col]:
                scale=rows[j][col]
                # subtraction equals addition only in characteristic two
                neg=scale if q in (2,4) else (-scale)%q
                rows[j]=[add(rows[j][k],mul(neg,rows[rank][k])) for k in range(dim+1)]
        rank+=1
    return all(any(rows[i][:dim]) or rows[i][-1]==0 for i in range(dim))


def direct_regular_count(edges,q):
    add,mul=operations(q)
    basis=[[1 if i==j else 0 for i in range(7)] for j in range(7)]
    nreg=0
    for a_tuple in product(range(q),repeat=7):
        a=list(a_tuple)
        cols=[]
        for e in basis:
            tmp=algebra_product(a,e,edges,add,mul)
            cols.append(algebra_product(tmp,a,edges,add,mul))
        nreg+=is_in_span(cols,a,q,add,mul)
    return nreg


def formula_regular_count(edges,q):
    total=0
    for mask in range(16):
        num_nonzero=mask.bit_count()
        bad=sum((mask>>u&1)==0 and (mask>>v&1)==0 for u,v in edges)
        total+=(q-1)**num_nonzero*q**(len(edges)-bad)
    return total


def brute_idempotent_commuting_pairs(edges,q):
    add,mul=operations(q)
    idems=[]
    for a in product(range(q),repeat=7):
        if algebra_product(a,a,edges,add,mul)==list(a):
            idems.append(a)
    commuting=0
    for a in idems:
        for b in idems:
            if algebra_product(a,b,edges,add,mul)==algebra_product(b,a,edges,add,mul):
                commuting+=1
    return len(idems),commuting


def main():
    for q in (2,3,4):
        got=[]
        for tag,edges in [('path',PATH),('star',STAR)]:
            brute=direct_regular_count(edges,q)
            predicted=formula_regular_count(edges,q)
            assert brute==predicted,(q,tag,brute,predicted)
            got.append(brute)
        assert got[1]-got[0]==q*(q-1)**3
        for edges in (PATH,STAR):
            idems,pairs=brute_idempotent_commuting_pairs(edges,q)
            assert idems==2*(1+q)**3,(q,idems)
            assert pairs==4*(1+3*q)**3,(q,pairs)
        print('q',q,'path',got[0],'star',got[1],'difference',got[1]-got[0])
    print('VERIFY_OK_INCIDENCE_REGULARITY_SEPARATION')

if __name__=='__main__':main()
