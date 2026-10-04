#!/usr/bin/env python3
from itertools import product
from collections import Counter
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
cert = json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

# Encode a+u*b by a + 2*b, with a,b in F2 and u^2=0.
def add(x,y): return x ^ y
def mul(x,y):
    a=x&1; b=(x>>1)&1
    c=y&1; d=(y>>1)&1
    return (a*c) | (((a*d)^(b*c))<<1)

def inv(x):
    for y in range(4):
        if mul(x,y)==1:
            return y
    return None

def matmul(A,B):
    return [[
        sum_ring([mul(A[i][t],B[t][j]) for t in range(len(B))])
        for j in range(len(B[0]))
    ] for i in range(len(A))]

def sum_ring(xs):
    z=0
    for x in xs: z=add(z,x)
    return z

def matinv(A):
    n=len(A)
    M=[A[i][:]+[1 if i==j else 0 for j in range(n)] for i in range(n)]
    for c in range(n):
        p=next((i for i in range(c,n) if inv(M[i][c]) is not None),None)
        if p is None: return None
        M[c],M[p]=M[p],M[c]
        q=inv(M[c][c])
        M[c]=[mul(q,x) for x in M[c]]
        for i in range(n):
            if i!=c and M[i][c]:
                f=M[i][c]
                M[i]=[add(M[i][j],mul(f,M[c][j])) for j in range(2*n)]
    return [row[n:] for row in M]

def rowcomb(G, coeff):
    return [sum_ring([mul(coeff[i],G[i][j]) for i in range(len(G))]) for j in range(len(G[0]))]

def gray_symbol(x):
    a=x&1; b=(x>>1)&1
    return (b,a^b)

def gray_word(w):
    out=[]
    for x in w:
        out.extend(gray_symbol(x))
    return out

def rank2(rows):
    ints=[]
    for row in rows:
        z=0
        for j,b in enumerate(row):
            z |= (b&1)<<j
        ints.append(z)
    r=0
    n=max((z.bit_length() for z in ints), default=0)
    for c in range(n-1,-1,-1):
        p=next((i for i in range(r,len(ints)) if (ints[i]>>c)&1),None)
        if p is None: continue
        ints[r],ints[p]=ints[p],ints[r]
        for i in range(len(ints)):
            if i!=r and ((ints[i]>>c)&1):
                ints[i]^=ints[r]
        r+=1
    return r

def binary_generator(G):
    out=[]
    for row in G:
        out.append(gray_word(row))
        out.append(gray_word([mul(2,x) for x in row]))
    return out

def hull_dim_binary(H):
    k=len(H)
    gram=[[sum(H[i][j]*H[t][j] for j in range(len(H[0])))%2 for t in range(k)] for i in range(k)]
    return k-rank2(gram)

G=cert["base_generator_encoding"]["G"]
U=cert["base_generator_encoding"]["U"]
Ui=matinv(U)
assert Ui is not None

Ds=[]
for vals in product(range(4),repeat=4):
    D=[list(vals[:2]),list(vals[2:])]
    if matinv(D) is not None:
        Ds.append(D)
assert len(Ds)==96

seen=set()
census=Counter()
opt_we=Counter()
all_lcd=True

for D in Ds:
    for e in product(range(4),repeat=2):
        B=matmul(Ui,[D[0],D[1],list(e)])
        key=tuple(x for row in B for x in row)
        assert key not in seen
        seen.add(key)
        GX=[G[i]+B[i] for i in range(3)]

        rw=Counter()
        gw=Counter()
        for coeff in product(range(4),repeat=3):
            w=rowcomb(GX,coeff)
            rw[sum(x!=0 for x in w)] += 1
            bw=gray_word(w)
            gw[sum(bw)] += 1

        rd=min(x for x in rw if x)
        gd=min(x for x in gw if x)
        census[(rd,gd)] += 1

        H=binary_generator(GX)
        assert rank2(H)==6
        if hull_dim_binary(H)!=0:
            all_lcd=False

        if gd==8:
            opt_we[tuple(sorted(gw.items()))] += 1

assert len(seen)==1536
assert census==Counter({(3,6):768,(4,7):720,(4,8):48})
assert all_lcd

expected_opt=Counter()
for obj in cert["optimal_gray_weight_enumerators"]:
    expected_opt[tuple(sorted((int(k),v) for k,v in obj["weight_distribution"].items()))]=obj["count"]
assert opt_we==expected_opt

Bp=cert["source_displayed_B_encoding"]
Gp=[G[i]+Bp[i] for i in range(3)]
gp=Counter()
for coeff in product(range(4),repeat=3):
    gp[sum(gray_word(rowcomb(Gp,coeff)))] += 1
expected_source={int(k):v for k,v in cert["source_displayed_gray_weight_distribution"].items()}
assert dict(sorted(gp.items()))==dict(sorted(expected_source.items()))
assert min(x for x in gp if x)==8

print("VERIFY_OK")
