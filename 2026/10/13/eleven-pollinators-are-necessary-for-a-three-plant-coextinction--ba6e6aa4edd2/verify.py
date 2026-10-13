"""Exact finite certificate for three-plant coextinction variance reversal."""
from collections import defaultdict
from itertools import combinations
from math import comb

# Ordered pollinator types: {1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}.
A=(4,4,0,0,2,0,1)
B=(5,2,1,1,0,1,1)

def compositions(k,n):
    if k==1:
        yield (n,)
        return
    for j in range(n+1):
        for t in compositions(k-1,n-j):
            yield (j,)+t

def descriptor(v):
    a,b,c,d,e,f,g=v
    n=sum(v)
    plant_degrees=tuple(sorted((a+d+e+g,b+d+f+g,c+e+f+g)))
    pollinator_degrees=(a+b+c,d+e+f,g)
    union_profile=tuple(sorted((n-a,n-b,n-c)))
    return plant_degrees,pollinator_degrees,union_profile

def connected(v):
    a,b,c,d,e,f,g=v
    return all(descriptor(v)[0]) and sum(z>0 for z in (d+g,e+g,f+g))>=2

def polysign_transformed(a,b,n):
    """Coefficients in t of (1+t)^n [sum_i q^a_i - sum_i q^b_i], q=t/(1+t)."""
    ca=[sum(x==j for x in a)-sum(y==j for y in b) for j in range(n+1)]
    return [sum(ca[j]*comb(n-j,k-j) for j in range(k+1)) for k in range(n+1)]

def census():
    sums=[]; total_compositions=0; total_profile_pairs=0
    for n in range(1,11):
        classes=defaultdict(set); valid=0
        for v in compositions(7,n):
            if not connected(v): continue
            valid+=1
            plant,pollinator,unions=descriptor(v)
            classes[(plant,pollinator)].add(unions)
        pairs=0
        for profiles in classes.values():
            ar=list(profiles)
            for i,x in enumerate(ar):
                for y in ar[i+1:]:
                    pairs+=1
                    coeff=polysign_transformed(x,y,n)
                    assert all(z>=0 for z in coeff) or all(z<=0 for z in coeff), (n,x,y,coeff)
        total_compositions+=valid;total_profile_pairs+=pairs
        sums.append((n,valid,len(classes),sum(map(len,classes.values())),pairs))
    print('CENSUS_OK (pollinators,valid_type_vectors,degree_classes,union_profiles,comparisons)=',sums)
    print('CENSUS_OK connected_type_vectors=',total_compositions,'pair_comparisons=',total_profile_pairs)

def moments(v):
    n=sum(v); sets=[set() for _ in range(3)]; k=0
    for count,plantmask in zip(v,(1,2,4,3,5,6,7)):
        for _ in range(count):
            for i in range(3):
                if plantmask&(1<<i): sets[i].add(k)
            k+=1
    E=[0]*(n+1);E2=[0]*(n+1)
    for deleted in range(1<<n):
        d=deleted.bit_count();x=sum(all(deleted&(1<<j) for j in s) for s in sets)
        for k in range(n-d+1):
            weight=comb(n-d,k)*(-1)**k
            E[d+k]+=x*weight;E2[d+k]+=x*x*weight
    V=E2[:]
    for i,a in enumerate(E):
        for j,b in enumerate(E):
            if i+j<len(V):V[i+j]-=a*b
    return E,V

def witness():
    assert sum(A)==sum(B)==11 and connected(A) and connected(B)
    assert descriptor(A)[:2]==descriptor(B)[:2]==((3,5,7),(8,2,1))
    assert descriptor(A)[2]==(7,7,11) and descriptor(B)[2]==(6,9,10)
    Ea,Va=moments(A); Eb,Vb=moments(B)
    assert Ea==Eb
    diff=[x-y for x,y in zip(Va,Vb)]
    expected=[0]*12
    # 2q^6(1-q)^2(q^3+q^2-1) => coefficients q^6 ... q^11.
    for j,c in enumerate(( -1,2,0,-1,-1,1 )):
        expected[6+j]=2*c
    assert diff==expected,(diff,expected)
    print('WITNESS_OK plant_degrees=(3,5,7) pollinator_degrees=(1x8,2x2,3x1)')
    print('WITNESS_OK mean_coefficients=',Ea,'variance_difference=',diff)

if __name__=='__main__':
    witness();census()
    print('VERIFY_OK first_three_plant_reversal_at_eleven_pollinators')
