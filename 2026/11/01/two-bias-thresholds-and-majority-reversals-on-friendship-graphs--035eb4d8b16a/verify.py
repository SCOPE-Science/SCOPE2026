"""Brute-force labelled majority dynamics and exact bias census on friendship graphs."""
from math import comb, factorial


def graph(n):
    N=2*n+1
    adj=[[] for _ in range(N)]
    for j in range(n):
        a,b=2*j+1,2*j+2
        adj[0].extend((a,b))
        adj[a].extend((0,b))
        adj[b].extend((0,a))
    return adj


def majority_step(bits,adj):
    out=0
    for v, neighbors in enumerate(adj):
        s=sum((bits>>u)&1 for u in neighbors)
        bit=(bits>>v)&1
        nxt= int(2*s>len(neighbors)) if 2*s!=len(neighbors) else bit
        out|=nxt<<v
    return out


def expected_unbiased(n):
    allstates=2*4**n
    permanent=2*(sum(comb(n,k)*3**(n-k) for k in range((n+1)//2,n+1))-(comb(n,n//2) if n%2==0 else 0))
    first=4**n-comb(2*n,n)
    fixed=2**n+(comb(n,n//2) if n%2==0 else 0)
    return (allstates,first,permanent,first-permanent,fixed)


def expected_biased(n,u,v):
    first=0
    for a in range(n+1):
        for b in range(a+1,n-a+1):
            m=n-a-b
            ways=factorial(n)//(factorial(a)*factorial(b)*factorial(m))
            first+=ways*((v-u)**2)**a*(u*u)**b*(2*u*(v-u))**m
    permanent=sum(comb(n,b)*(u*u)**b*(v*v-u*u)**(n-b) for b in range((n+1)//2,n+1))
    if n%2==0:
        permanent-=comb(n,n//2)*(u*(v-u))**n
    return first,permanent


total=0
for n in range(1,9):
    adj=graph(n)
    actual=[0]*5
    for bits in range(1<<(2*n+1)):
        one=majority_step(bits,adj)
        two=majority_step(one,adj)
        three=majority_step(two,adj)
        assert two==three,(n,bits,'not fixed after two rounds')
        initial_majority=int(bits.bit_count()>n)
        final_majority=int(two.bit_count()>n)
        assert (one&1)==initial_majority,(n,bits,'first-round hub')
        assert (two&1)==final_majority,(n,bits,'terminal hub')
        assert (one!=two)==(initial_majority!=final_majority),(n,bits,'reversal')
        actual[0]+=1
        actual[1]+=(bits&1)!=(one&1)
        actual[2]+=(bits&1)!=(two&1)
        actual[3]+=one!=two
        actual[4]+=bits==one
    assert tuple(actual)==expected_unbiased(n),(n,actual,expected_unbiased(n))
    total+=actual[0]
    print('n=%d initial=%d first_flip=%d permanent_flip=%d reversible_second_step=%d fixed=%d'%((n,)+tuple(actual)))
print('UNBIASED_CONFIGURATIONS',total)

checks=0
for n in range(1,8):
    adj=graph(n)
    for u,v in ((0,1),(1,4),(1,2),(2,3),(3,4),(1,1)):
        f=p=0
        for outer in range(1<<(2*n)):
            bits=outer<<1 # fixed original hub zero
            one=majority_step(bits,adj)
            two=majority_step(one,adj)
            weight=u**outer.bit_count()*(v-u)**(2*n-outer.bit_count())
            if one&1:f+=weight
            if two&1:p+=weight
        assert (f,p)==expected_biased(n,u,v),(n,u,v,(f,p),expected_biased(n,u,v))
        checks+=1
print('EXACT_WEIGHTED_CASES',checks)
print('FRIENDSHIP_MAJORITY_CENSUS_OK')
