#!/usr/bin/env python3
"""Independent finite-field checks for left-regular Jordan types in the 4-generator exterior algebra.

Only the exterior basis multiplication and finite-field arithmetic are used to construct operators.
Run: python3 exterior4_verify.py
"""
from collections import Counter
from itertools import product
import random

MASKS = tuple(range(16))
DEG = tuple(i.bit_count() for i in MASKS)
V = tuple(i for i in MASKS if DEG[i] == 1)
W = tuple(i for i in MASKS if DEG[i] == 2)
Z = tuple(i for i in MASKS if DEG[i] == 3)


def basis_product(i, j):
    if i & j:
        return None
    inversions = sum(((j & ((1 << k) - 1)).bit_count()) for k in range(4) if i & (1 << k))
    return (i | j, -1 if inversions % 2 else 1)

MULT = {(i, j): basis_product(i, j) for i in MASKS for j in MASKS}


class Field:
    def __init__(self, q):
        self.q = q
        if q in (2, 3, 5, 7):
            self.p = q
            self.ext = False
        elif q in (4, 9):
            self.p = {4: 2, 9: 3}[q]
            self.ext = True
            self.t2_a, self.t2_b = ((1, 1) if q == 4 else (2, 0))
        else:
            raise ValueError(q)
        self.add = [[0] * q for _ in range(q)]
        self.mul = [[0] * q for _ in range(q)]
        self.neg = [0] * q
        for a in range(q):
            for b in range(q):
                if not self.ext:
                    self.add[a][b] = (a + b) % self.p
                    self.mul[a][b] = (a * b) % self.p
                else:
                    p = self.p
                    u, v = a % p, a // p
                    x, y = b % p, b // p
                    self.add[a][b] = ((u + x) % p) + p * ((v + y) % p)
                    self.mul[a][b] = ((u*x + v*y*self.t2_a) % p) + p * ((u*y + v*x + v*y*self.t2_b) % p)
        for a in range(q):
            self.neg[a] = next(b for b in range(q) if self.add[a][b] == 0)
        self.inv = [None] * q
        for a in range(1, q):
            self.inv[a] = next(b for b in range(1, q) if self.mul[a][b] == 1)


def exterior_left_matrix(field, x):
    add, mul, neg = field.add, field.mul, field.neg
    rows = [[0] * 16 for _ in MASKS]
    for i in MASKS:
        if not x[i]:
            continue
        for j in MASKS:
            outcome = MULT[(i, j)]
            if outcome is None:
                continue
            mask, sign = outcome
            val = x[i] if sign > 0 else neg[x[i]]
            rows[mask][j] = add[rows[mask][j]][val]
    return rows


def exterior_product(field, a, b):
    out = [0] * 16
    for i, c in enumerate(a):
        if not c:
            continue
        for j, d in enumerate(b):
            if not d:
                continue
            result = MULT[(i,j)]
            if result is None:
                continue
            mask, sign = result
            val = field.mul[c][d]
            if sign < 0:
                val = field.neg[val]
            out[mask] = field.add[out[mask]][val]
    return out


def rank(field, rows):
    q = field.q
    add, mul, neg, inv = field.add, field.mul, field.neg, field.inv
    A = [row[:] for row in rows]
    lead = 0
    for col in range(16):
        pivot = next((i for i in range(lead,16) if A[i][col]), None)
        if pivot is None:
            continue
        A[lead], A[pivot] = A[pivot], A[lead]
        scale = inv[A[lead][col]]
        A[lead] = [mul[scale][v] for v in A[lead]]
        for row in range(lead+1,16):
            v = A[row][col]
            if v:
                nv = neg[v]
                A[row] = [add[u][mul[nv][w]] for u,w in zip(A[row], A[lead])]
        lead += 1
        if lead == 16:
            break
    return lead


def predict(field, x):
    """Independent rank-condition classifier in terms of graded input coordinates."""
    q = field.q
    if any(x[v] for v in V):
        if field.p == 2:
            return '(2^8)',8,0
        v = [x[i] if i in V else 0 for i in MASKS]
        w = [x[i] if i in W else 0 for i in MASKS]
        if any(exterior_product(field,v,w)):
            return '(3^2,2^4,1^2)',8,2
        return '(2^8)',8,0
    if any(x[w] for w in W):
        a,b,c,d,e,f = (x[3],x[5],x[9],x[6],x[10],x[12])
        # Pfaffian for basis (e1e2,e1e3,e1e4,e2e3,e2e4,e3e4): a*f-b*e+c*d
        p = field
        pf = p.add[p.add[p.mul[a][f]][p.neg[p.mul[b][e]]]][p.mul[c][d]]
        if pf:
            return ('(2^6,1^4)' if field.p == 2 else '(3,2^4,1^5)'),6,(0 if field.p == 2 else 1)
        return '(2^4,1^8)',4,0
    if any(x[z] for z in Z):
        return '(2^2,1^12)',2,0
    if x[15]:
        return '(2,1^14)',1,0
    return '(1^16)',0,0


def gf2_rank_columns(columns):
    pivot = [0]*16
    r=0
    for v in columns:
        while v:
            b=v.bit_length()-1
            if pivot[b]:
                v ^= pivot[b]
            else:
                pivot[b]=v
                r+=1
                break
    return r


def exhaustive_binary():
    field=Field(2)
    counter=Counter()
    maps=[[0]*16 for _ in MASKS]
    for i in MASKS:
        for j in MASKS:
            t=MULT[(i,j)]
            if t is not None:
                maps[i][j]=1<<t[0]
    for raw in range(1<<15):
        xs=[0] + [(raw>>(k-1))&1 for k in range(1,16)]
        columns=[0]*16
        for i in range(1,16):
            if xs[i]:
                row=maps[i]
                for j in range(16):
                    columns[j]^=row[j]
        got=gf2_rank_columns(columns)
        part,r1,r2=predict(field,xs)
        assert got==r1, ('binary',raw,got,r1)
        counter[part]+=1
    q=2
    exp={'(2^8)':(q**4-1)*q**11,
         '(2^6,1^4)':q**2*(q-1)*(q**3-1)*q**5,
         '(2^4,1^8)':(q-1)*(q*q+1)*(q*q+q+1)*q**5,
         '(2^2,1^12)':(q**4-1)*q,
         '(2,1^14)':q-1,
         '(1^16)':1}
    assert dict(counter)==exp,(counter,exp)
    print('GF2_ALL_32768_EXHAUSTIVE_OK', sorted(counter.items()))


def check_element(f, x):
    assert x[0] == 0
    matrix=exterior_left_matrix(f,x)
    rank1=rank(f,matrix)
    y=exterior_product(f,x,x)
    if sum(x)!=0 and sum(x) % 17 == 0:
        for j in range(16):
            ej=[0]*16
            ej[j]=1
            direct=exterior_product(f,x,exterior_product(f,x,ej))
            from_square=exterior_product(f,y,ej)
            assert direct==from_square, (f.q,x,j)
    rank2=rank(f,exterior_left_matrix(f,y))
    typ,r1,r2=predict(f,x)
    assert (rank1,rank2)==(r1,r2),(f.q,x,typ,(rank1,rank2),(r1,r2))
    return typ


def algebraic_samples():
    rng=random.Random(20261028)
    for q in (3,4,5,7,9):
        f=Field(q)
        counter=Counter()
        for _ in range(550):
            x=[0]+[rng.randrange(q) for i in range(1,16)]
            counter[check_element(f,x)]+=1
        # Force all strata, including nonzero top degree and all possible alternating ranks.
        special=[]
        for items in ({3:1,12:1},{3:1},{1:1,6:1},{1:1},{7:1},{15:1},{}):
            x=[0]*16
            for j,c in items.items():x[j]=c
            special.append(x)
        for x in special:
            counter[check_element(f,x)]+=1
        print('GF'+str(q)+'_557_MATRIX_RANK_TESTS_OK',sorted(counter.items()))
    for q in (3,4):
        f=Field(q)
        # exhaustively enumerate 2-form subspaces at two different slices
        counter=Counter()
        for coord in product(range(q), repeat=6):
            x=[0]*16
            for j,c in zip(W,coord):x[j]=c
            counter[check_element(f,x)]+=1
        R2=(q-1)*(q*q+1)*(q*q+q+1)
        R4=q*q*(q-1)*(q**3-1)
        assert counter['(2^4,1^8)']==R2
        assert counter[('(2^6,1^4)' if f.p==2 else '(3,2^4,1^5)')]==R4
        assert counter['(1^16)']==1
        print('GF'+str(q)+'_EXHAUSTIVE_2FORM_SLICE_OK',q**6)


def main():
    exhaustive_binary()
    algebraic_samples()
    print('EXTERIOR4_REGULAR_JORDAN_SPECTRUM_OK')

if __name__=='__main__':main()
