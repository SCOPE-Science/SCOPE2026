from fractions import Fraction as Q

def maps(delta,c):
    def f0(x):return x/2 if x<Q(1,2)+delta else 2*x-1
    def f1(x):return 2*x if x<Q(1,2)-delta else (x+1)/2
    def h0(x):return f1(x) if x<c else f0(x)
    def h1(x):return f0(x) if x>=1-c else f1(x)
    return f0,f1,h0,h1

def trial(delta,r):
    a=Q(1,3*2**r)
    assert a<4*delta
    c=(a+min(2*a,4*delta))/2
    f0,f1,h0,h1=maps(delta,c)
    left=[a*2**j for j in range(r+1)]
    right=[1-x for x in reversed(left)]
    states=left+right
    assert len(states)==len(set(states))
    assert all(c/2<=x<1-c/2 for x in states)
    edges=[]
    for i,x in enumerate(states):
        successors=(states.index(h0(x)),states.index(h1(x)))
        predicted=(i+1,i+1) if i==0 else ((i-1,i+1) if i<len(states)-1 else (i-1,i-1))
        assert successors==predicted,(delta,c,r,i,x,successors,predicted)
        edges.append(successors)
    weights=[Q(1,2) if i in(0,len(states)-1) else Q(1) for i in range(len(states))]
    weights=[w/sum(weights) for w in weights]
    assert sum(weights)==1
    after=[Q(0) for _ in states]
    for i,(u,v) in enumerate(edges):
        after[u]+=weights[i]/2;after[v]+=weights[i]/2
    assert after==weights
    assert weights[0]>0 and weights[-1]>0
    print('PASS delta',delta,'r',r,'c',c,'atoms',len(states),'outer mass',weights[0])

for d in [Q(1,1000000),Q(1,1000),Q(1,192),Q(1,96),Q(1,48),Q(1,24),Q(1,17),Q(1,12),Q(1,9),Q(1,8),Q(1,6)]:
    r=1
    while Q(1,3*2**r)>=4*d:r+=1
    trial(d,r)
