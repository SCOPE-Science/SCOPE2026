#!/usr/bin/env python3
"""Independent Lie-bracket closure checks for a five-dimensional upper-triangular Lie algebra."""
from itertools import product
from fractions import Fraction
import random

def bracket(x,y,p):
    a,b,u,v,w=x; c,d,s,t,z=y
    return (0,0, ((a-b)*s-(c-d)*u)%p,
            ((a+2*b)*t-(c+2*d)*v)%p,
            ((2*a+b)*z-(2*c+d)*w+u*t-s*v)%p)

def echelon_add(rows, vec, p):
    v=[int(x)%p for x in vec]
    for pivot,row in rows:
        if v[pivot]:
            z=v[pivot]
            v=[(a-z*b)%p for a,b in zip(v,row)]
    j=next((i for i,a in enumerate(v) if a),None)
    if j is None: return False
    inv=pow(v[j],-1,p)
    v=[x*inv%p for x in v]
    for i,(pivot,row) in enumerate(rows):
        if row[j]:
            z=row[j]
            rows[i]=(pivot,[(a-z*b)%p for a,b in zip(row,v)])
    rows.append((j,v))
    rows.sort(key=lambda z:z[0])
    return True

def closure_dimension(gens,p):
    rows=[]
    for g in gens: echelon_add(rows,g,p)
    while True:
        old=len(rows)
        vectors=[r for _,r in rows]
        for a in vectors:
            for b in vectors:
                echelon_add(rows,bracket(a,b,p),p)
                if len(rows)==5: return 5
        if len(rows)==old: return old

def rowrank(rows,p):
    r=[]
    for v in rows:echelon_add(r,v,p)
    return len(r)

def criterion(gens,p):
    a=[g[0] for g in gens]; b=[g[1] for g in gens]
    if rowrank([a,b],p)<2:return False
    alpha=[(x-y)%p for x,y in zip(a,b)]
    beta=[(x+2*y)%p for x,y in zip(a,b)]
    u=[g[2] for g in gens]; v=[g[3] for g in gens]
    if p==3:return rowrank([alpha,u,v],p)==3
    return rowrank([alpha,u],p)==2 and rowrank([beta,v],p)==2

def formula(p,k):
    q=Fraction(1,p)
    if p==3:return (1-q**k)*(1-q**(k-1))**2*(1-q**(k-2))
    return (1-q**k)*(1-q**(k-1))**3



def gf4mul(a,b):
    # F_2[z]/(z^2+z+1), bits encode coefficients of 1,z.
    c=0
    for i in range(2):
        if (a>>i)&1:
            for j in range(2):
                if (b>>j)&1:
                    c^=1<<(i+j)
    if c&4:c^=7
    return c

def gf4add(rows,vec):
    v=list(vec)
    inv={1:1,2:3,3:2}
    for j,row in rows:
        if v[j]:
            c=v[j]
            v=[a^gf4mul(c,b) for a,b in zip(v,row)]
    j=next((i for i,a in enumerate(v) if a),None)
    if j is None:return False
    v=[gf4mul(inv[v[j]],a) for a in v]
    for i,(p,row) in enumerate(rows):
        if row[j]:
            c=row[j]
            rows[i]=(p,[a^gf4mul(c,b) for a,b in zip(row,v)])
    rows.append((j,v));rows.sort(key=lambda z:z[0]);return True

def gf4bracket(x,y):
    a,b,u,v,w=x;c,d,s,t,z=y
    return (0,0,
            gf4mul(a^b,s)^gf4mul(c^d,u),
            gf4mul(a,t)^gf4mul(c,v),
            gf4mul(b,z)^gf4mul(d,w)^gf4mul(u,t)^gf4mul(s,v))

def gf4closure(gens):
    rows=[]
    for x in gens:gf4add(rows,x)
    while True:
        old=len(rows)
        vs=[x for _,x in rows]
        for x in vs:
            for y in vs:
                gf4add(rows,gf4bracket(x,y))
                if len(rows)==5:return 5
        if len(rows)==old:return old

def gf4rank(vectors):
    rows=[]
    for v in vectors:gf4add(rows,v)
    return len(rows)

def gf4criterion(gens):
    a=[x[0] for x in gens];b=[x[1] for x in gens]
    if gf4rank([a,b])<2:return False
    alpha=[x^y for x,y in zip(a,b)]
    u=[x[2] for x in gens];v=[x[3] for x in gens]
    return gf4rank([alpha,u])==2 and gf4rank([a,v])==2

def test_gf4():
    rng=random.Random(789665)
    for k,trials in [(2,3000),(3,1500)]:
        yes=0
        for _ in range(trials):
            xs=[tuple(rng.randrange(4) for j in range(5)) for i in range(k)]
            actual=(gf4closure(xs)==5)
            predicted=gf4criterion(xs)
            if actual!=predicted:raise AssertionError(('F4',k,xs,actual,predicted))
            yes+=actual
        print('SAMPLED_F4',k,'trials',trials,'generated',yes,'formula',formula(4,k))

def main():
    for p,k in [(2,1),(2,2),(2,3),(3,2)]:
        xs=list(product(range(p),repeat=5))
        yes=0;total=0
        for ids in product(range(len(xs)),repeat=k):
            gs=[xs[i] for i in ids]
            actual=(closure_dimension(gs,p)==5)
            predicted=criterion(gs,p)
            if actual!=predicted:raise AssertionError((p,k,ids,gs,actual,predicted))
            yes+=actual; total+=1
        pred=formula(p,k)
        assert Fraction(yes,total)==pred,(p,k,yes,total,pred)
        print('EXHAUSTIVE',p,k,'count',yes,'/',total,'probability',pred)
    rng=random.Random(409111)
    for p,k,trials in [(3,3,2500),(5,2,2500),(5,3,1500),(7,2,1500)]:
        yes=0
        for _ in range(trials):
            gs=[tuple(rng.randrange(p) for i in range(5)) for j in range(k)]
            actual=(closure_dimension(gs,p)==5)
            predicted=criterion(gs,p)
            if actual!=predicted:raise AssertionError((p,k,gs,actual,predicted))
            yes+=actual
        print('SAMPLED',p,k,'trials',trials,'generated',yes,'formula',formula(p,k))
    test_gf4()
    print('VERIFY_OK')

if __name__=='__main__':main()
