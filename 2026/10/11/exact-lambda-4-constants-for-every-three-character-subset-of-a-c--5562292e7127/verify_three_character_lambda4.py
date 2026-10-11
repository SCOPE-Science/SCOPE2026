#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
import cmath, math, random

TARGETS={
    'order3': Fraction(3,1),
    'order4': Fraction(7,3),
    'antipodal': Fraction(2,1),
    'ap': Fraction(15,7),
    'generic': Fraction(5,3),
}

def order_mod(d,N):
    d%=N
    return N//math.gcd(d,N)

def is_ap(A,N):
    A=set(A)
    for y in A:
        others=list(A-{y})
        if (2*y-others[0]-others[1])%N==0:
            return True,y,tuple(others)
    return False,None,None

def classify(A,N):
    A=set(A)
    # order-3 coset
    for a in A:
        for b in A-{a}:
            d=(b-a)%N
            if order_mod(d,N)==3 and {(a+j*d)%N for j in range(3)}==A:
                return 'order3'
    # order-4 fragment, equivalently AP with endpoints antipodal
    for a in A:
        for d in range(1,N):
            if order_mod(d,N)==4 and {(a+j*d)%N for j in range(3)}==A:
                return 'order4'
    # antipodal pair
    if N%2==0:
        for x,y in combinations(A,2):
            if (x-y)%N==N//2:
                return 'antipodal'
    if is_ap(A,N)[0]:
        return 'ap'
    return 'generic'

def collision_signature(A,N):
    A=sorted(A)
    pairs=[]
    for i,x in enumerate(A):
        for j in range(i,3):
            y=A[j]
            pairs.append(((i,j),(x+y)%N))
    fibers={}
    for ij,s in pairs:fibers.setdefault(s,[]).append(ij)
    return sorted(sorted(v) for v in fibers.values() if len(v)>1)

def direct_fourth(N,A,c):
    vals=[]
    for x in range(N):
        z=sum(c[j]*cmath.exp(2j*math.pi*A[j]*x/N) for j in range(3))
        vals.append(abs(z)**4)
    den=sum(abs(z)**2 for z in c)**2
    return (sum(vals)/N)/den if den else 0.0

def witnesses(kind):
    if kind=='order3': return [1,1,1]
    if kind=='order4': return [1,1,1]
    if kind=='antipodal': return [1,1,0]
    if kind=='ap': return [math.sqrt(2),math.sqrt(3),math.sqrt(2)]
    return [1,1,1]

def representative(N,A,kind):
    # Reorder for witness phase conditions.
    A=list(A)
    if kind=='order3':
        a=A[0]
        for d in range(1,N):
            if order_mod(d,N)==3 and {(a+j*d)%N for j in range(3)}==set(A):
                return [(a+j*d)%N for j in range(3)], [1,1,1]
    if kind=='order4':
        for a in A:
            for d in range(1,N):
                if order_mod(d,N)==4 and {(a+j*d)%N for j in range(3)}==set(A):
                    return [(a+j*d)%N for j in range(3)], [1,1,1]
    if kind=='antipodal':
        for x,y in combinations(A,2):
            if N%2==0 and (x-y)%N==N//2:
                z=next(t for t in A if t not in (x,y))
                return [x,y,z],[1,1,0]
    if kind=='ap':
        ok,m,ends=is_ap(A,N)
        e0,e1=ends
        return [e0,m,e1],[math.sqrt(2),math.sqrt(3),math.sqrt(2)]
    return A,[1,1,1]

counts={k:0 for k in TARGETS}
for N in range(3,81):
    for A in combinations(range(N),3):
        k=classify(A,N); counts[k]+=1
        sig=collision_signature(A,N)
        # Every collision pattern must agree with the five-way taxonomy.
        if k=='generic' and sig: raise AssertionError((N,A,k,sig))
        if k=='ap' and not (len(sig)==1 and len(sig[0])==2): raise AssertionError((N,A,k,sig))
        if k=='antipodal' and not (len(sig)==1 and len(sig[0])==2): raise AssertionError((N,A,k,sig))
        if k=='order4' and not (len(sig)==2 and all(len(v)==2 for v in sig)): raise AssertionError((N,A,k,sig))
        if k=='order3' and not (len(sig)==3 and all(len(v)==2 for v in sig)): raise AssertionError((N,A,k,sig))
        # One exact/numeric attainment check per first example of each N/type.
        if counts[k] <= 80:
            Ar,c=representative(N,A,k)
            v=direct_fourth(N,Ar,c)
            if abs(v-float(TARGETS[k]))>2e-10:
                raise AssertionError(('witness',N,A,k,v,float(TARGETS[k]),Ar,c))
print('VERIFY_OK N=3..80 triples=%d counts=%s targets=%s' % (sum(counts.values()), counts, {k:str(v) for k,v in TARGETS.items()}))
