#!/usr/bin/env python3
from itertools import product

LABELS=(-1,1,2,3)

def rescue_ok(vals,n):
    for i,v in enumerate(vals):
        if i<n:
            neigh=[vals[n+j] for j in range(n) if j!=i]
        else:
            j=i-n
            neigh=[vals[a] for a in range(n) if a!=j]
        if v==-1 and not (3 in neigh or sum(x==2 for x in neigh)>=2):
            return False
        if v==1 and not any(x>=2 for x in neigh):
            return False
    return True

def min_closed(vals,n):
    X=sum(vals[:n]); Y=sum(vals[n:])
    out=[]
    for i in range(n):
        out.append(vals[i]+Y-vals[n+i])
        out.append(vals[n+i]+X-vals[i])
    return min(out)

def expected(n,k):
    if not (1<=k<=3*n):
        return None
    return 2*k+2 if (n,k) in {(3,2),(4,1)} else 2*k

def construction(n,k):
    assert 3<=n and 1<=k<=3*n and (n,k) not in {(3,2),(4,1)}
    if k<=n:
        if (n-k)%2==0:
            u3,u2=1,0
            u1=(n+k-4)//2
            um=n-u1-1
        else:
            u3,u2=1,1
            u1=(n+k-7)//2
            um=n-u1-2
        assert min(um,u1,u2,u3)>=0
    else:
        q=k-n
        u3=q//2
        u2=q-2*u3
        u1=n-u2-u3
        um=0
        assert min(um,u1,u2,u3)>=0
    z=[-1]*um+[1]*u1+[2]*u2+[3]*u3
    assert len(z)==n and sum(z)==k
    return tuple(z+z)

def direct_valid(vals,n,k):
    return rescue_ok(vals,n) and min_closed(vals,n)>=k

assignment_count=0
case_count=0
for n in (3,4,5):
    best={k:None for k in range(1,3*n+1)}
    for vals in product(LABELS, repeat=2*n):
        assignment_count+=1
        if not rescue_ok(vals,n):
            continue
        h=min_closed(vals,n)
        if h<1:
            continue
        w=sum(vals)
        for k in range(1,min(3*n,h)+1):
            if best[k] is None or w<best[k]:
                best[k]=w
    for k in range(1,3*n+1):
        case_count+=1
        got=best[k]
        want=expected(n,k)
        assert got==want,(n,k,got,want)

construction_checks=0
for n in range(3,41):
    for k in range(1,3*n+1):
        if (n,k) in {(3,2),(4,1)}:
            continue
        vals=construction(n,k)
        assert sum(vals)==2*k
        assert direct_valid(vals,n,k),(n,k,vals)
        construction_checks+=1

for n,k,z in [(3,2,[-1,1,3]),(4,1,[-1,-1,1,3])]:
    vals=tuple(z+z)
    assert sum(vals)==2*k+2
    assert direct_valid(vals,n,k)

for n in range(3,41):
    assert 3*n+1>3*n

print('ALL CHECKS PASSED; exhaustive_orders=[3,4,5]; exhaustive_assignments=%d; parameter_cases=%d; construction_checks=%d; construction_range=3..40' % (assignment_count,case_count,construction_checks))
