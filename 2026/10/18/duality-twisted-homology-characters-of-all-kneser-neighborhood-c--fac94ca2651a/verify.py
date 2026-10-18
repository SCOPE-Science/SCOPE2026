#!/usr/bin/env python3
"""Independent finite checks for duality-twisted Kneser neighborhood homology characters."""
from itertools import combinations
from collections import Counter
from math import comb

def parts(n, maximum=None):
    if n==0:
        yield ()
        return
    if maximum is None: maximum=n
    for j in range(min(maximum,n),0,-1):
        for q in parts(n-j,j):yield (j,)+q

def euler_of_states(states, le):
    states=sorted(states,key=lambda p:p[1])
    values={}
    for label,weight in states:
        values[label]=1-sum(values[v] for v,w in states if w<weight and le(v,label))
    return sum(values.values())

def character_formula(cycle_lengths,k):
    n=sum(cycle_lengths); r=n-2*k
    even=[v//2 for v in cycle_lengths if v%2==0]
    e=len(even); mid=n/2
    Q=[]
    from itertools import product
    for opts in product((0,1,2),repeat=e):
        weight=sum(w for z,w in zip(opts,even) if z)
        if k<=weight<mid:Q.append((opts,weight))
    leq=lambda a,b: all(x==0 or x==y for x,y in zip(a,b))
    chiQ=euler_of_states(Q,leq)
    chiB=0
    if e==len(cycle_lengths):
        B=[]
        for opts in product((0,1),repeat=e):
            weight=sum(w for z,w in zip(opts,even) if z)
            if k<=weight<mid:B.append((opts,weight))
        chiB=euler_of_states(B,lambda a,b:all(x<=y for x,y in zip(a,b)))
    return (-1)**r*(-1+chiQ+(2**e*(1-chiB) if e==len(cycle_lengths) else 0))

def permutation_for_parts(mu):
    n=sum(mu); p=list(range(n)); pos=0
    for l in mu:
        for j in range(l):p[pos+j]=pos+(j+1)%l
        pos+=l
    return tuple(p)

def chain_lefschetz(mu,k):
    n=sum(mu); p=permutation_for_parts(mu); r=n-2*k
    U=[sum(1<<i for i in c) for z in range(k,n-k+1) for c in combinations(range(n),z)]
    U.sort(key=lambda x:(x.bit_count(),x))
    compperm={}
    mask=(1<<n)-1
    for s in U:
        sig_s=sum(1<<p[i] for i in range(n) if s>>i&1)
        compperm[s]=mask^sig_s
    # each chain fixed by cσ must have lower ranks paired with upper ranks.
    # Count all chains via direct generation, not via weighted cycle states.
    stable=[]
    L=0
    # generate chains recursively; within requested n small
    def rec(chain,start):
        nonlocal L
        if chain:
            image=[compperm[t] for t in chain]
            if sorted(image)==sorted(chain):
                t=len(chain)
                L+=(-1)**(t-1+(t*(t-1)//2))
        for j in range(start,len(U)):
            new=U[j]
            if not chain or chain[-1]!=new and chain[-1]&new==chain[-1]:
                rec(chain+[new],j+1)
    rec([],0)
    return (-1)**r*(L-1)

def verify():
    checks=0
    for n,k in [(4,2),(5,2),(6,2),(7,3),(8,3),(9,4)]:
        for mu in parts(n):
            got=character_formula(mu,k)
            actual=chain_lefschetz(mu,k)
            assert got==actual,(n,k,mu,got,actual)
            checks+=1
        assert character_formula((1,)*n,k)==(-1)**(n-2*k+1)
        print('checked',n,k,'classes',sum(1 for _ in parts(n)))
    print('VERIFY_OK',checks)

# Complete-homogeneous to Schur expansion using Pieri horizontal strips.
def horizontal_add(partition, extra):
    target=sum(partition)+extra
    for mu in parts(target):
        if len(mu)>len(partition)+1:continue
        if all((mu[i] if i<len(mu) else 0)>=partition[i]>=
               (mu[i+1] if i+1<len(mu) else 0) for i in range(len(partition))):
            yield mu

def homogeneous_product(shape):
    counts=Counter({():1})
    for block in shape:
        updated=Counter()
        for lam,multiplicity in counts.items():
            for mu in horizontal_add(lam,block):
                updated[mu]+=multiplicity
        counts=updated
    return counts

def ribbon_schur(alpha):
    result=Counter()
    for mask in range(1<<(len(alpha)-1)):
        coarse=[];p=alpha[0]
        for i in range(len(alpha)-1):
            if mask & (1<<i): coarse.append(p);p=alpha[i+1]
            else:p+=alpha[i+1]
        coarse.append(p)
        for shape,multiplicity in homogeneous_product(coarse).items():
            result[shape]+=multiplicity*(-1)**(len(alpha)-len(coarse))
    return {shape:a for shape,a in result.items() if a}

def verify_ribbons():
    checked=0
    for k in range(1,6):
        for r in range(0,5):
            n=2*k+r
            expected={tuple([2*k-j,j]+[1]*r):1 for j in range(1,k+1)}
            assert ribbon_schur([k]+[1]*r+[k])==expected,(n,k)
            checked+=1
    print('RIBBON_OK',checked)

if __name__=='__main__':
    verify()
    verify_ribbons()
