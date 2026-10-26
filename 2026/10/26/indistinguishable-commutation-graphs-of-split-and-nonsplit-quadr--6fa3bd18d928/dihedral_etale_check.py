"""Reproduce finite-prime-field checks for quadratic-etale skew truncations.

A=k[z,t]/(z*z=d,t**(2*m+1),t*z=-z*t), with ordered normal
basis z**b*t**i (b=0,1; 0<=i<2*m+1).  This program recomputes
centralizer dimensions using the full multiplication table, independently
of the chain-ring exterior-minor normal form in the theorem.
"""
from itertools import product
from collections import Counter
from random import Random


def mat_rank(mat, p):
    rows=[list(r) for r in mat]
    n=len(rows); k=len(rows[0])
    piv=0
    for col in range(k):
        ix=next((i for i in range(piv,n) if rows[i][col]%p),None)
        if ix is None: continue
        rows[piv],rows[ix]=rows[ix],rows[piv]
        inv=pow(rows[piv][col],-1,p)
        rows[piv]=[(v*inv)%p for v in rows[piv]]
        for i in range(n):
            if i!=piv and rows[i][col]:
                factor=rows[i][col]
                rows[i]=[(a-factor*b)%p for a,b in zip(rows[i],rows[piv])]
        piv+=1
        if piv==n: break
    return piv


def products(p,d,m):
    length=2*m+1
    n=2*length
    table=[]
    for ix in range(n):
        b,i=divmod(ix,length)
        row=[]
        for jx in range(n):
            c,j=divmod(jx,length)
            e=i+j
            if e>=length: row.append((None,0))
            else: row.append(((b+c)%2, e, (-1 if i*c%2 else 1)*(d if b*c else 1)))
        table.append(row)
    return table


def centralizer_dim(x,p,d,m,table):
    length=2*m+1; n=2*length
    ad=[[0]*n for _ in range(n)]
    for i,a in enumerate(x):
        if not a:continue
        for j in range(n):
            a1=table[i][j]
            a2=table[j][i]
            if a1[0] is not None:
                b,t,coef=a1
                ad[b*length+t][j]=(ad[b*length+t][j]+a*coef)%p
            if a2[0] is not None:
                b,t,coef=a2
                ad[b*length+t][j]=(ad[b*length+t][j]-a*coef)%p
    return n-mat_rank(ad,p)


def predicted_dim(x,m):
    length=2*m+1
    # Basis 1,t,...,t**(2m), z,zt,...,zt**(2m).
    # Noncentral coordinates: h=z times even t powers below 2m,
    # e=t times even powers, f=z*t times even powers.
    vals=[]
    for j in range(m):
        if x[length+2*j]!=0 or x[2*j+1]!=0 or x[length+2*j+1]!=0:
            vals.append(j)
    return 4*m+2 if not vals else 2*m+2+2*min(vals)


def run(p,d,m,exhaustive,seed=207):
    assert p%2==1 and d%p!=0 and m>0
    length=2*m+1; n=2*length
    table=products(p,d,m)
    samples=product(range(p),repeat=n) if exhaustive else (
        tuple(Random(seed+z).randrange(p) for z in range(n)) for _ in range(120))
    # Independent RNG for nonexhaustive tests
    if not exhaustive:
        rng=Random(seed)
        samples=(tuple(rng.randrange(p) for _ in range(n)) for _ in range(200))
    census=Counter()
    count=0
    for x in samples:
        actual=centralizer_dim(x,p,d,m,table)
        expect=predicted_dim(x,m)
        assert actual==expect, (p,d,m,x,actual,expect)
        census[actual]+=1;count+=1
    if exhaustive:
        theoretical=Counter({4*m+2:p**(m+2)})
        for j in range(m):
            theoretical[2*m+2+2*j]=(p**(m+2))*(p**(3*(m-j))-p**(3*(m-j-1)))
        assert census==theoretical, (census,theoretical)
        pairs=sum((p**dim)*quantity for dim,quantity in census.items())
        # Use exact integer formula independently.
        exact=p**(2*(m+2))*(p**(3*m)+sum(
            (p**(3*(m-j))-p**(3*(m-j-1)))*p**(m+2*j) for j in range(m)))
        assert pairs==exact
        print('EXHAUSTIVE',p,d,m,'elements',count,'dimensions',dict(census),
              'commuting_pairs',pairs)
    else:
        print('SAMPLED',p,d,m,'elements',count,'dimensions_seen',dict(census))

if __name__=='__main__':
    run(3,1,1,True)
    run(3,2,1,True)
    run(3,1,2,False)
    run(3,2,2,False)
    run(5,1,2,False)
    run(5,2,2,False)
