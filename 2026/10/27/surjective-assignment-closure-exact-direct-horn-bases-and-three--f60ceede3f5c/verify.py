"""Finite brute-force checks for surjection-incidence closure and direct Horn bases."""
from itertools import combinations,product
from math import comb,factorial


def stirling(n,k):
    z=[[0]*(k+1) for _ in range(n+1)];z[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            z[i][j]=z[i-1][j-1]+j*z[i-1][j]
    return z[n][k] if k<=n else 0

def associated(n,k):
    z=[[0]*(k+1) for _ in range(n+1)];z[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(k,i//2)+1):
            z[i][j]=j*z[i-1][j]+(i-1)*z[i-2][j-1]
    return z[n][k] if k<=n else 0

def formula(n,q):
    assert n>=q>=3
    forced=n*q*factorial(q-1)*stirling(n-1,q-1)
    pairs=n*comb(q,2)
    bad=sum(comb(n,r)*comb(q,q-r-1)*factorial(q-r-1)*associated(n-r,q-r-1)
            for r in range(0,q-1))
    return forced,pairs,bad

def surjection_models(n,q):
    return [sum(1<<(i*q+a) for i,a in enumerate(w))
            for w in product(range(q),repeat=n) if len(set(w))==q]

def exact_closure(S,models,N):
    meet=(1<<N)-1; num=0
    for m in models:
        if S&m==S:
            num+=1; meet &=m
    return meet if num else (1<<N)-1

def rules(n,q):
    assert n>=q>=3
    allbits=(1<<(n*q))-1
    f=[];c=[];b=[]
    for j in range(n):
        pos=[i for i in range(n) if i!=j]
        for missing in range(q):
            palette=set(range(q))-{missing}
            for w in product(sorted(palette),repeat=n-1):
                if set(w)!=palette: continue
                premise=sum(1<<(i*q+a) for i,a in zip(pos,w))
                f.append((premise,1<<(j*q+missing)))
    for i in range(n):
        for a,x in combinations(range(q),2):
            c.append(((1<<(i*q+a)) | (1<<(i*q+x)),allbits))
    for r in range(q-1):
        k=n-r;t=q-r-1
        if k<2*t:continue
        for pos in combinations(range(n),k):
            for pal in combinations(range(q),t):
                for w in product(pal,repeat=k):
                    if any(w.count(a)<2 for a in pal): continue
                    premise=sum(1<<(i*q+a) for i,a in zip(pos,w))
                    b.append((premise,allbits))
    assert len({p for p,_ in f+c+b})==len(f+c+b)
    return f,c,b

def verify(n,q,exhaustive=True):
    models=surjection_models(n,q);N=n*q;full=(1<<N)-1
    f,c,b=rules(n,q); rr=f+c+b
    assert tuple(map(len,(f,c,b)))==formula(n,q),(n,q,tuple(map(len,(f,c,b))),formula(n,q))
    for j,(p,out) in enumerate(rr):
        assert (exact_closure(p,models,N)&out)==out
        # Removing any one rule breaks directness on its own premise.
        got=p
        for h,(a,y) in enumerate(rr):
            if h!=j and p&a==a: got|=y
        assert got!=exact_closure(p,models,N),(n,q,j)
    seen=set();closed=0
    if exhaustive:
        inputs=range(1<<N)
    else:
        import random
        rng=random.Random(20261018+n*13+q)
        inputs=sorted(set([0,full]+[rng.getrandbits(N) for _ in range(15000)] + [p for p,_ in rr]))
    for S in inputs:
        got=S
        for p,out in rr:
            if S&p==p: got|=out
        exact=exact_closure(S,models,N)
        assert got==exact,(n,q,S,got,exact)
        if got==S:closed+=1
    print('CHECK n=%d q=%d models=%d rules=%d forced=%d conflicts=%d shortage=%d inputs=%d%s' %
          (n,q,len(models),len(rr),len(f),len(c),len(b),len(inputs),
           ' closed='+str(closed) if exhaustive else ''))
    if q==3:
        count=3*(n+2)*2**(n-1)-6*(n+1)
        assert len(rr)==count
        if exhaustive:
            lattice=4**n-3*2**n-3*n*2**(n-1)+3*n+4
            assert closed==lattice,(n,closed,lattice)
    return len(inputs)

if __name__=='__main__':
    tested=0
    for n,q in [(3,3),(4,3),(5,3),(4,4)]:
        tested+=verify(n,q)
    for n,q in [(6,3),(5,4),(5,5)]:
        tested+=verify(n,q,False)
    print('VERIFY_OK', 'candidate_subsets',tested,
          'exact_surjection_closure=PASS', 'necessary_premises=PASS',
          'sharp_one_round_basis=PASS', 'associated_stirling_count=PASS',
          'tricolor_lattice_count=PASS')
