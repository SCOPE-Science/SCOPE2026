from itertools import product
from collections import Counter

def inv_mod(a,p):
    return pow(a,-1,p)

def det(M,p):
    n=len(M)
    A=[list(row) for row in M]
    d=1
    for col in range(n):
        pivot=next((r for r in range(col,n) if A[r][col]%p),None)
        if pivot is None:
            return 0
        if pivot!=col:
            A[col],A[pivot]=A[pivot],A[col]
            d=-d
        v=A[col][col]%p
        d=d*v%p
        iv=inv_mod(v,p)
        for j in range(col,n):
            A[col][j]=A[col][j]*iv%p
        for r in range(col+1,n):
            f=A[r][col]%p
            if f:
                for j in range(col,n):
                    A[r][j]=(A[r][j]-f*A[col][j])%p
    return d%p

def gl_mats(m,p):
    if m==0:
        return [()]
    mats=[]
    for vals in product(range(p), repeat=m*m):
        M=tuple(tuple(vals[i*m+j] for j in range(m)) for i in range(m))
        if det(M,p):
            mats.append(M)
    return mats

def mat_vec(M,v,p):
    if not M:
        return ()
    return tuple(sum(M[i][j]*v[j] for j in range(len(v)))%p for i in range(len(M)))

def add(u,v,p):
    return tuple((a+b)%p for a,b in zip(u,v))

def aut_action(x,beta,b,B,p):
    u,c=x[0],x[1]
    v=x[2:]
    return (beta*u%p,c)+add(tuple(c*z%p for z in b),mat_vec(B,v,p),p)

for p in (2,3,5):
    for n in (2,3,4):
        m=n-2
        Bs=gl_mats(m,p)
        bs=list(product(range(p),repeat=m))
        aut=[(beta,b,B) for beta in range(1,p) for b in bs for B in Bs]
        elems=list(product(range(p),repeat=n))

        rem=set(elems)
        orbits=[]
        while rem:
            x=next(iter(rem))
            orb={aut_action(x,beta,b,B,p) for beta,b,B in aut}
            orbits.append(orb)
            rem-=orb

        if n==2:
            assert len(orbits)==2*p
            sizes=Counter(map(len,orbits))
            expected=Counter()
            expected[1]+=1
            expected[p-1]+=1
            for _ in range(p-1):
                expected[1]+=1
                expected[p-1]+=1
            assert sizes==expected
        else:
            qm=p**m
            assert len(orbits)==2*p+2
            expected_sizes=[1,p-1,qm-1,(p-1)*(qm-1)]
            for _ in range(p-1):
                expected_sizes.extend([qm,(p-1)*qm])
            assert sorted(map(len,orbits))==sorted(expected_sizes)

            # Check intrinsic labels distinguish every orbit.
            def label(x):
                u,c=x[0],x[1]
                v=x[2:]
                if c:
                    sq = (c*u)%p
                    return ("nonzero_chi",c,"square_zero" if sq==0 else "square_nonzero")
                if u==0 and all(z==0 for z in v): return ("zero",)
                if u!=0 and all(z==0 for z in v): return ("derived",)
                if u==0 and any(z!=0 for z in v): return ("center",)
                return ("mixed",)
            labels=[{label(x) for x in orb} for orb in orbits]
            assert all(len(s)==1 for s in labels)
            assert len({next(iter(s)) for s in labels})==len(orbits)

        assert sum(map(len,orbits))==p**n
        print({"q":p,"n":n,"aut_order":len(aut),"orbits":len(orbits),
               "orbit_sizes":dict(sorted(Counter(map(len,orbits)).items()))})

print("VERIFY_OK")
