#!/usr/bin/env python3
"""Independent finite arithmetic checks for a Proth numerical-semigroup Frobenius formula."""
from heapq import heappush, heappop

def greedy(magnitude,k):
    values=[0]*k
    residual=magnitude
    for i in range(k,0,-1):
        coin=(1<<i)-1
        values[i-1],residual=divmod(residual,coin)
    assert residual==0
    return values

def formula(n,m):
    assert n>=3 and m>=3 and (m&1) and m<(1<<n)
    r=m.bit_length()-1
    k=n+r
    M=m<<n
    x=greedy(M,k)
    t=next(i+1 for i,a in enumerate(x) if a)
    s=sum(x)
    a=M+1
    return s*a+M*M-M-1+(t-1),t,s,x

def direct(n,m):
    M=m<<n
    a=M+1
    k=n+m.bit_length()-1
    # independently shortest path over all classes modulo a, using the actual generators
    generators=[m*(1<<(n+i))+1 for i in range(1,k+1)]
    distance=[None]*a
    distance[0]=0
    todo=[(0,0)]
    done=0
    while todo:
        v,u=heappop(todo)
        if distance[u]!=v:
            continue
        done+=1
        for g in generators:
            vv=(u+g)%a
            z=v+g
            if distance[vv] is None or distance[vv]>z:
                distance[vv]=z
                heappush(todo,(z,vv))
    assert done==a
    mx=max(distance)
    return mx-a, [i for i,x in enumerate(distance) if x==mx], distance

def main():
    tests=0; checked_nodes=0; exceptional=[]
    for n in range(3,9):
        for m in range(3,1<<n,2):
            if (m<<n)>22000:
                continue
            F,t,s,x=formula(n,m)
            F2,indices,_=direct(n,m)
            assert F==F2,(n,m,F,F2)
            j=(m<<n)-(t-1)
            assert indices==[(-j)%(m*(1<<n)+1)],(n,m,indices,j)
            tests+=1;checked_nodes+=m*(1<<n)+1
            if t>=3:exceptional.append((n,m,t,s,F))
    print('PASS independent Dijkstra comparison',tests,'semigroups',checked_nodes,'residue vertices')
    print('Cases outside the earlier t=1,2 regimes:',len(exceptional), exceptional[:15])
    for r in range(6,9):
        n=r+1
        m=(1<<r)+63
        F,t,s,x=formula(n,m)
        assert t>=3,(n,m,t,x)
        F2,_,_=direct(n,m)
        assert F==F2
        print('first-omitted branch','n',n,'m',m,'t',t,'digit_sum',s,'F',F)
    for k in range(1,26):
        b=(1<<k)-1
        for h in range(1,k+1):
            val=greedy(b-h,k)
            w=sum((1<<i)*q for i,q in enumerate(val,1))
            assert w == (1<<k) - (2 if h==k else 0),(k,h,w)
    print('PASS all local carry identities k <=25')
    for n in range(3,11):
        for m in range(3,1<<n,2):
            M=m<<n
            r=m.bit_length()-1
            full=greedy(M,n+r)
            h=m.bit_count()
            short=greedy(h,n+r)
            expected=[short[i] for i in range(n+r)]
            for bit in range(r+1):
                expected[n+bit-1]=((m>>bit)&1)
            assert full==expected,(n,m,full,expected)
            c=sum(short)
            t=next(i+1 for i,z in enumerate(short) if z)
            F,tf,s,_=formula(n,m)
            assert F==M*M+(h+c-1)*M+(h+c+t-2)
            assert tf==t and s==h+c
    print('PASS high-bit and compressed formula identities for all odd m, 3 <= n <= 10')
    print('VERIFIED')

if __name__=='__main__': main()
