"""Exact independent enumerations for proper conflict-free colorings of hairy cycles.

Run: python3 verify_sunlet.py. Python standard library only.
"""
from itertools import product
from math import comb


def falling(a, j):
    z = 1
    for i in range(j):
        z *= a-i
    return z


def local_formula(q, a):
    no_equal = sum((-1)**j*comb(q-2,j)*falling(a,j)*(q-1-j)**(a-j)
                   for j in range(min(a,q-2)+1))
    no_distinct = sum((-1)**j*comb(q-3,j)*falling(a,j)*
                      ((q-1-j)**(a-j)-2*(q-2-j)**(a-j)+(q-3-j)**(a-j))
                      for j in range(min(a,q-3)+1))
    return (q-1)**a-no_equal, (q-1)**a-no_distinct


def local_brute(q,a):
    r=[]
    for x,y in [(1,1),(1,2)]:
        count=0
        for z in product(range(1,q),repeat=a):
            v=(x,y)+z
            if any(v.count(t)==1 for t in set(v)):
                count+=1
        r.append(count)
    return tuple(r)


def core_sum(q,a,n):
    r,s=local_formula(q,a)
    acc=0
    for c in product(range(q),repeat=n):
        if any(c[i]==c[(i+1)%n] for i in range(n)):
            continue
        z=1
        for i in range(n):
            z *= r if c[(i-1)%n] == c[(i+1)%n] else s
        acc += z
    return acc


def spectral(q,a,n):
    r,s=local_formula(q,a)
    c=r+(q-2)*s
    v0,v1=2,-s
    if n==0: un=v0
    elif n==1: un=v1
    else:
        for _ in range(2,n+1):
            v0,v1=v1,-s*v1-(s-r)*c*v0
        un=v1
    return c**n+(q-1)*un+(q*(q-3)//2)*(r-s)**n+((q-1)*(q-2)//2)*(s-r)**n


def transfer_trace(q,a,n):
    r,s=local_formula(q,a)
    states=[(i,j) for i in range(q) for j in range(q) if i!=j]
    N=len(states)
    ind={s:i for i,s in enumerate(states)}
    T=[[0]*N for _ in range(N)]
    for i,(u,v) in enumerate(states):
        for w in range(q):
            if w!=v:
                T[i][ind[v,w]]=r if w==u else s
    acc=0
    for initial in range(N):
        z=[0]*N
        z[initial]=1
        for _ in range(n):
            zz=[0]*N
            for i,number in enumerate(z):
                if number:
                    for j,weight in enumerate(T[i]):
                        if weight: zz[j]+=number*weight
            z=zz
        acc += z[initial]
    return acc


def direct_full(q,a,n):
    """Brute enumerate core and every pendant color; test PCF directly."""
    total=0
    for c in product(range(q),repeat=n):
        if any(c[i]==c[(i+1)%n] for i in range(n)):
            continue
        choices=[[x for x in range(q) if x!=c[i]] for i in range(n)]
        for leaves in product(*([choices[i] for i in range(n) for _ in range(a)])):
            good=True
            for i in range(n):
                neighborhood=[c[(i-1)%n],c[(i+1)%n]]+list(leaves[i*a:(i+1)*a])
                if not any(neighborhood.count(x)==1 for x in set(neighborhood)):
                    good=False
                    break
            if good:
                total+=1
    return total


def main():
    local_tests=0; spectral_tests=0; exhaustive_tests=0; total_assignments=0
    for q in range(3,8):
        for a in range(1,7):
            assert local_brute(q,a)==local_formula(q,a), (q,a)
            local_tests+=1
    for q in range(3,7):
        for a in range(1,5):
            for n in range(3,9):
                p=spectral(q,a,n)
                assert transfer_trace(q,a,n)==p, (q,a,n)
                spectral_tests+=1
    for q in range(3,6):
        for a in range(1,4):
            for n in range(3,6):
                assert core_sum(q,a,n)==spectral(q,a,n), (q,a,n)
                exhaustive_tests+=1
    full_cases=[(3,1,3),(3,1,4),(3,1,5),(4,1,3),(4,1,4),
                (3,2,3),(3,2,4),(4,2,3),(3,3,3),(5,1,3)]
    for q,a,n in full_cases:
        assert direct_full(q,a,n)==spectral(q,a,n), (q,a,n)
        total_assignments+=q**(n*(a+1))
    for a in range(1,8):
        assert local_formula(3,a)==(a,2)
        for n in range(3,15):
            assert spectral(3,a,n)>0
    print(f'LOCAL_COUNTS_OK {local_tests}')
    print(f'TRANSFER_SPECTRAL_OK {spectral_tests}')
    print(f'CORE_ENUMERATION_OK {exhaustive_tests}')
    print(f'DIRECT_ASSIGNMENTS_OK {len(full_cases)} cases, {total_assignments} ambient color assignments')
    print('Q3_LOCAL_WEIGHTS_OK a,2; Q3_POSITIVITY_OK')
    for q,a,n in [(3,1,3),(3,2,3),(3,2,4),(4,1,4),(4,2,3),(5,1,3)]:
        print('EXAMPLE',q,a,n,spectral(q,a,n))
    print('VERIFY_OK')

if __name__=='__main__':main()
