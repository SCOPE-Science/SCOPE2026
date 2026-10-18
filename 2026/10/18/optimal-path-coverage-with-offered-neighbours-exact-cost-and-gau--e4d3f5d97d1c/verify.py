#!/usr/bin/env python3
"""Exact rational finite-state verification for independent offered-neighbour choice on paths."""
from fractions import Fraction as F

def expected(n,c):
    assert n>=1 and c>=1
    if c==1:
        cross=[F(n*n-x*x) for x in range(n+1)]
        exits=[F(d*(n-d)) for d in range(n//2+1)]
    else:
        q=F(1,2**c); p=1-q; delta=p-q; tau=q/p
        cross=[F(n-x)/delta-2*p*q/(delta**2)*(tau**x-tau**n) for x in range(n+1)]
        m=n//2
        if n%2==0:
            exits=[F(d)/delta-2*p*q/(delta**2)*tau**(m-d)*(1-tau**d) for d in range(m+1)]
        else:
            exits=[F(d)/delta-q/(delta**2)*tau**(m-d)*(1-tau**d) for d in range(m+1)]
    return cross,exits

def markov_choice_value(vals, neighbours, c):
    # Compute expected min of c independent uniform offers, no floating-point arithmetic.
    from itertools import product
    d=len(neighbours)
    out=F(0)
    for tup in product(neighbours,repeat=c):
        out+=min(vals[x] for x in tup)
    return out/F(d**c)

def second_moment_variance(n,c):
    # Independent first-step second-moment recurrences, using float to assess asymptotics.
    cross, exits=expected(n,c)
    H=list(map(float,cross)); E=list(map(float,exits))
    p=1-2.0**(-c); q=1-p
    h=[0.0]*n
    h[0]=2*H[0]-1
    for i in range(1,n):
        h[i]=(2*H[i]-1+q*h[i-1])/p
    v_cross=sum(h)-H[0]**2
    m=n//2
    if m==0: return v_cross
    g=[0.0]*(m+1)
    g[m]=(2*E[m]-1)*(1 if n%2==0 else 1/p)
    for i in range(m-1,0,-1):
        g[i]=(2*E[i]-1+q*g[i+1])/p
    v_exit=sum(g[1:])-E[m]**2
    return v_cross+v_exit

def check():
    total=0
    for c in range(1,6):
        for n in range(1,31):
            cross, exits=expected(n,c)
            assert cross[n]==0 and exits[0]==0
            assert all(cross[x]>cross[x+1] for x in range(n))
            assert all(exits[d+1]>exits[d] for d in range(n//2))
            for x in range(n):
                neighbors=([1] if x==0 else [x-1,x+1])
                assert cross[x]==1+markov_choice_value(cross,neighbors,c),(n,c,x,'cross')
                total+=1
            m=n//2
            for d in range(1,m+1):
                if d<m: adj=[d-1,d+1]
                elif n%2==0: adj=[d-1]  # two physical neighbours with same distance
                else: adj=[d-1,d]  # two physical neighbours, one across midpoint
                assert exits[d]==1+markov_choice_value(exits,adj,c),(n,c,d,'exit')
                total+=1
            # All possible starting vertices reduce to two stages, with same cross value.
            assert max((cross[0]+exits[min(i,n-i)] for i in range(n+1)))==cross[0]+exits[m]
            total+=1
    print('PASS:',total,'exact rational Bellman/boundary/optimality checks across 150 cases.')
    for c in [2,3,4]:
        q=2.0**(-c); p=1-q; delta=p-q
        predicted=6*p*q/delta**3
        for n in [100,500,1000]:
            ratio=second_moment_variance(n,c)/n
            assert abs(ratio/predicted-1)<0.1, (n,c,ratio,predicted)
        print('variance/n for c=',c,'at 1000:',round(ratio,7),'limit:',round(predicted,7))
    for n in [1,2,3,4,10]:
        C,E=expected(n,2)
        print('two choices, n=',n,'optimal worst cover=',C[0]+E[-1])
if __name__=='__main__': check()
