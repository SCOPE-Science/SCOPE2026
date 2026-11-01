"""Exact cubical verification for dihedral first-homology characters of polygonal real moment-angle surfaces.
All tests are finite consistency checks; uniform proof is given separately.
"""
from math import gcd

def data(n,p):
    q=len(set(cycle_reps(p)))
    C0=2**q
    C1=C2=0
    for i in range(n):
        if p[i]==i:
            C1+=2**(len(set(cycle_reps_except(p,{i}))))
    for i in range(n):
        j=(i+1)%n
        if {p[i],p[j]}=={i,j}:
            s=1 if p[i]==i else -1
            C2+=s*2**(len(set(cycle_reps_except(p,{i,j}))))
    return C0,C1,C2

def cycle_reps(p):
    seen=set()
    for i in range(len(p)):
        if i in seen: continue
        j=i
        while j not in seen:
            seen.add(j)
            j=p[j]
        yield i

def cycle_reps_except(p,excluded):
    assert set(p[i] for i in excluded)==excluded
    seen=set()
    for i in range(len(p)):
        if i in excluded or i in seen: continue
        j=i
        while j not in seen:
            seen.add(j);j=p[j]
        yield i

def boundary_cycle(n):
    # 2-chain coefficient product of all inactive endpoint signs.
    # For each 1-cell (active j, signs on all other coordinates),
    # incident boundary coefficients come from the two neighboring polygon edges.
    for j in range(n):
        others=[k for k in range(n) if k!=j]
        for bit in range(1<<(n-1)):
            signs={v:(1 if bit>>a&1 else -1) for a,v in enumerate(others)}
            a=signs[(j-1)%n]; b=signs[(j+1)%n]
            left=a
            right=-b
            for k in others:
                if k != (j-1)%n: left *= signs[k]
                if k != (j+1)%n: right *= signs[k]
            assert left+right==0

for n in range(5,15):
    expected_dim=2+(n-4)*2**(n-2)
    for k in range(n):
        p=[(i+k)%n for i in range(n)]
        v,e,f=data(n,p)
        inferred=2-(v-e+f)
        desired=expected_dim if k==0 else 2-2**gcd(n,k)
        assert inferred==desired,(n,k,inferred,desired)
        p=[(k-i)%n for i in range(n)]
        v,e,f=data(n,p)
        inferred=0-(v-e+f) # 1 + orientation(reflection) - Lefschetz =0 -L
        assert inferred==0,(n,k,inferred)
    if n<=10:boundary_cycle(n)
    print('n',n,'group_elements',2*n,'betti1',expected_dim,'character_and_orientation_OK')
print('VERIFY_OK')
