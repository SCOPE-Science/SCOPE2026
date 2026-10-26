#!/usr/bin/env python3
"""Exact finite tests for joint descent/inversion fluctuations in move-to-front shuffles.
This validates algebraic finite identities; it does not certify asymptotic CLTs.
"""
from fractions import Fraction as Q
from itertools import permutations, product
from collections import defaultdict
import math


def statistics(deck):
    n=len(deck)
    d=sum(deck[i]>deck[i+1] for i in range(n-1))
    inv=sum(deck[i]>deck[j] for i in range(n) for j in range(i+1,n))
    return d,inv


def moment(data):
    length=len(data)
    ed=Q(sum(x for x,y in data),length)
    ei=Q(sum(y for x,y in data),length)
    return (ed, ei, Q(sum(x*x for x,y in data),length)-ed*ed,
            Q(sum(y*y for x,y in data),length)-ei*ei,
            Q(sum(x*y for x,y in data),length)-ed*ei)


def conditional(n,k):
    pairs=[]; prefix=[]
    for perm in permutations(range(1,n+1)):
        d=sum(perm[i]>perm[i+1] for i in range(k-1))
        b=int(k<n and perm[k-1]>min(perm[k:]))
        inv=sum(perm[i]>perm[j] for i in range(k) for j in range(i+1,n))
        pairs.append((d+b, inv))
        prefix.append((d,inv))
    return moment(pairs),moment(prefix)


def shuffle(n,sequence):
    deck=tuple(range(1,n+1))
    for x in sequence:
        j=deck.index(x)
        deck=(x,)+deck[:j]+deck[j+1:]
    return deck


def check():
    tests=0
    for n in range(3,8):
        for k in range(2,n+1):
            (ed,ei,vd,vi,cv), (ep,_,vp,_,cp) = conditional(n,k)
            m=n-k+1
            assert ed==Q(k+1,2)-Q(1,m)
            assert ep==Q(k-1,2)
            assert vd==Q(k+1,12)+Q(m-1,m*m*(m+1))
            assert vp==Q(k+1,12)
            assert ei==Q(k*(2*n-k-1),4)
            assert cp==Q(k-1,4)
            weights=[n-2*t+1 if t<=k else -k for t in range(1,n+1)]
            edge_count=k*(2*n-k-1)//2
            assert vi==Q(sum(w*w for w in weights)+edge_count,12)
            tests+=7
    for n in range(3,6):
        for r in range(1,5):
            direct=moment([statistics(shuffle(n,s)) for s in product(range(1,n+1),repeat=r)])
            kw=defaultdict(int)
            for s in product(range(1,n+1),repeat=r):
                kw[len(set(s))]+=1
            weighted=[Q(0)]*5
            for k,w in kw.items():
                cond,_=conditional(n,k) if k>=2 else conditional(n,1)
                for j in range(5):
                    # Mix moments rather than centered variances below.
                    if j==0 or j==1: weighted[j]+=Q(w,n**r)*cond[j]
                    elif j==2 or j==3: weighted[j]+=Q(w,n**r)*(cond[j]+cond[j-2]**2)
                    else: weighted[j]+=Q(w,n**r)*(cond[j]+cond[0]*cond[1])
            mixed=(weighted[0],weighted[1],weighted[2]-weighted[0]**2,
                   weighted[3]-weighted[1]**2,weighted[4]-weighted[0]*weighted[1])
            assert mixed==direct,(n,r,mixed,direct)
            tests+=5
    try:
        import sympy as sp
        q,c=sp.symbols('q c',real=True)
        a=1-q
        tau=q-(1+c)*q*q
        vd=a/sp.Integer(12)+tau/4
        vi=(a-a*a+a*a*a/3)/12+q*q*tau/4
        assert sp.simplify(vd-(1+2*q-3*(1+c)*q*q)/12)==0
        assert sp.simplify(vi-(1+8*q**3-9*(1+c)*q**4)/36)==0
        tests+=2
    except ImportError:
        print('Sympy unavailable: symbolic comparisons not run')
    print(f'PASS: {tests} exact moment, variance, coupling, and formula checks')

if __name__=='__main__':
    check()
