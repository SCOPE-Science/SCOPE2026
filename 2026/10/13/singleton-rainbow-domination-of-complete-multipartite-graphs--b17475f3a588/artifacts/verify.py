from itertools import product
from math import factorial

def profiles(total,last=1,cur=()):
    if total==0:
        if len(cur)>=2:
            yield cur
        return
    for x in range(last,total+1):
        yield from profiles(total-x,x,cur+(x,))

def part_of(profile):
    out=[]
    for i,n in enumerate(profile):
        out += [i]*n
    return out

def feasible_direct(profile,k,lab):
    p=part_of(profile)
    N=len(p)
    for v in range(N):
        if lab[v]!=0:
            continue
        seen=set()
        for u in range(N):
            if p[u]!=p[v] and lab[u]!=0:
                seen.add(lab[u])
        if seen != set(range(1,k+1)):
            return False
    return True

def count_matrix(profile,k,lab):
    p=part_of(profile)
    a=[[0]*(k+1) for _ in profile]
    for v,x in enumerate(lab):
        a[p[v]][x]+=1
    return a

def feasible_counts(profile,k,a):
    totals=[sum(a[i][c] for i in range(len(profile))) for c in range(k+1)]
    for i in range(len(profile)):
        if a[i][0]>0:
            for c in range(1,k+1):
                if totals[c]-a[i][c] < 1:
                    return False
    return True

def min_formula(profile,k):
    r=len(profile)
    N=sum(profile)
    best=N
    for mask in range(1<<r):
        if mask==(1<<r)-1:
            continue
        F=[i for i in range(r) if (mask>>i)&1]
        W=sum(profile[i] for i in F)
        if W>=k:
            best=min(best,W)
        else:
            q=k-W
            cap=sum(min(profile[i]-1,q) for i in range(r) if i not in F)
            if cap>=2*q:
                best=min(best,2*k-W)
    return best

def multinomial(row):
    n=sum(row)
    z=factorial(n)
    for x in row:
        z//=factorial(x)
    return z

profiles_checked=0
labelings_checked=0
enumerators_checked=0
for N in range(2,8):
    for profile in profiles(N):
        profiles_checked += 1
        for k in range(1,5):
            direct=[0]*(N+1)
            min_direct=N
            grouped={}
            for lab in product(range(k+1), repeat=N):
                labelings_checked += 1
                a=count_matrix(profile,k,lab)
                fd=feasible_direct(profile,k,lab)
                fc=feasible_counts(profile,k,a)
                if fd!=fc:
                    raise AssertionError(("classification",profile,k,lab,a,fd,fc))
                if fd:
                    w=sum(x!=0 for x in lab)
                    direct[w]+=1
                    min_direct=min(min_direct,w)
                    key=tuple(tuple(row) for row in a)
                    grouped[key]=grouped.get(key,0)+1
            via_counts=[0]*(N+1)
            for key,mult in grouped.items():
                a=[list(row) for row in key]
                expected=1
                for row in a:
                    expected*=multinomial(row)
                if expected!=mult:
                    raise AssertionError(("multinomial",profile,k,key,mult,expected))
                w=sum(sum(row[1:]) for row in a)
                via_counts[w]+=expected
            if via_counts!=direct:
                raise AssertionError(("enumerator",profile,k,direct,via_counts))
            mf=min_formula(profile,k)
            if min_direct!=mf:
                raise AssertionError(("minimum",profile,k,min_direct,mf,direct))
            enumerators_checked += 1

print(
    "ALL CHECKS PASSED; "
    f"profiles={profiles_checked}; "
    f"enumerators={enumerators_checked}; "
    f"labelings_checked={labelings_checked}; "
    "orders=2..7; colors=1..4"
)
