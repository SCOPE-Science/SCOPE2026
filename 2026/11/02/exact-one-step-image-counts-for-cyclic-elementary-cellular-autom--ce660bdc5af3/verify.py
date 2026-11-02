#!/usr/bin/env python3
"""Self-contained exact certificate for cyclic Rule-110 one-step image counts.
Run: python3 verify.py. Python standard library only.
"""
from collections import deque

RULE = 110
PAIRS = ((0,0), (0,1), (1,0), (1,1))
COEFF = (-1,0,2,-4,4,1,-5,6,-4,1)  # p(t)=t^9-4t^8+6t^7-5t^6+t^5+4t^4-4t^3+2t^2-1
DEN = (1,-4,6,-5,1,4,-4,2,0,-1)
NUM = (1,-3,4,-2,-2,7,-10,8,-2,0,1)
EXPECTED = (1,1,2,5,10,22,41,79,154,302,582,1113,2125,4058,7737,14725)

def local(a,b,c):
    return (RULE >> (4*a+2*b+c))&1

def matrices():
    mats=[0,0]
    for i,(a,b) in enumerate(PAIRS):
        for c in (0,1):
            j=PAIRS.index((b,c))
            mats[local(a,b,c)] |= 1 << (4*i+j)
    assert tuple(mats)==(33025,17090)
    return mats

def boolean_product(x,y):
    out=0
    for i in range(4):
        mask=0
        for j in range(4):
            if (x>>(4*i+j))&1:
                mask |= (y>>(4*j))&15
        out |= mask<<(4*i)
    return out

def build():
    mats=matrices()
    identity=sum(1<<(5*i) for i in range(4))
    nodes=[identity]
    indices={identity:0}
    nxt=[]
    for x in nodes:
        children=[]
        for m in mats:
            y=boolean_product(x,m)
            if y not in indices:
                indices[y]=len(nodes)
                nodes.append(y)
            children.append(indices[y])
        nxt.append(tuple(children))
    assert len(nodes)==len(indices)==len(nxt)==75
    assert all(0<=child<75 for row in nxt for child in row)
    accept=[int(any(node & (1<<(5*i)) for i in range(4))) for node in nodes]
    assert sum(accept)==61
    return nodes,nxt,accept

def op(nxt,v):
    return [v[a]+v[b] for a,b in nxt]

def count(nxt,accept,N):
    distribution=[0]*len(nxt)
    distribution[0]=1
    seq=[]
    for _ in range(N+1):
        seq.append(sum(val*accept[i] for i,val in enumerate(distribution)))
        following=[0]*len(nxt)
        for i,val in enumerate(distribution):
            if val:
                for dest in nxt[i]:
                    following[dest]+=val
        distribution=following
    return seq

def independent_direct(n):
    outputs=set()
    for mask in range(1<<n):
        bits=[(mask>>i)&1 for i in range(n)]
        # Directly apply the rule to a periodic ring, even for n=1 or 2.
        image=0
        for i in range(n):
            image |= local(bits[(i-1)%n],bits[i],bits[(i+1)%n]) << i
        outputs.add(image)
    return len(outputs)

def newton_power_sums(coeff, maxn):
    # Monic polynomial x^4 + a1*x^3 + ... + a4.
    d=4
    s=[d]
    for n in range(1,maxn+1):
        if n<=d:
            value=-sum(coeff[k]*s[n-k] for k in range(1,n))-n*coeff[n]
        else:
            value=-sum(coeff[k]*s[n-k] for k in range(1,d+1))
        s.append(value)
    return s

def main():
    nodes,nxt,accept=build()
    seq=count(nxt,accept,120)
    assert tuple(seq[:len(EXPECTED)])==EXPECTED
    for n in range(1,17):
        assert seq[n]==independent_direct(n),(n,seq[n],independent_direct(n))
    # The genuinely finite, all-states identity T^2 p(T) f=0.
    iterates=[accept]
    for k in range(11):
        iterates.append(op(nxt,iterates[-1]))
    witness=[sum(COEFF[j]*iterates[j+2][i] for j in range(10)) for i in range(75)]
    assert witness==[0]*75
    # The all-state identity is sufficient for the all-length recurrence.
    assert sum(DEN[j]*seq[10-j] for j in range(10))==1
    for n in range(11,121):
        assert sum(DEN[j]*seq[n-j] for j in range(10))==0
    for n in range(11):
        assert NUM[n]==sum(DEN[j]*seq[n-j] for j in range(min(n,9)+1))
    # Companion-root trace formula, proved using Newton sums, exact integers.
    sb=newton_power_sums((0,-2,1,-1,-1),120)
    sc=newton_power_sums((0,-1,0,0,-1),120)
    for n in range(121):
        expected=1+sb[n]-sc[n]-(1 if n==1 else 0)
        assert expected==seq[n],(n,expected,seq[n])
    # Check the factorization of the denominator via integer polynomial multiplication.
    def multiply(a,b):
        x=[0]*(len(a)+len(b)-1)
        for i,v in enumerate(a):
            for j,w in enumerate(b):
                x[i+j]+=v*w
        return x
    assert tuple(multiply(multiply((1,-1),(1,-1,0,0,-1)),(1,-2,1,-1,-1)))==DEN
    print('VERIFY_OK')
    print('relation_states=75 accepting=61')
    print('direct_ring_check_lengths=1..16')
    print('exact_vector_identity=T^2*p(T)*f=0 (all 75 components)')
    print('first_counts_n1_to15=',seq[1:16])

if __name__=='__main__':
    main()
