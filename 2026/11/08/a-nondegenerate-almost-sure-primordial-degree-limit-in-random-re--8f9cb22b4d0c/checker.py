"""Exact finite-state validation of the RRSC(2) primordial-degree transition law.
Only Python standard library; no external data or dependencies.
"""
from collections import defaultdict
from fractions import Fraction as F

def markov_states(nmax=9):
    states={(0,1):F(1)} # triangle count, primordial degree at n=2
    histories={2:states}
    tests=0
    for n in range(2,nmax):
        new=defaultdict(F)
        for (t,d),mass in states.items():
            edges=n-1+t
            denom=n+edges
            assert 1<=d<=n-1 and 0<=t<=n-2
            trans=[((t,d+1),F(1,denom)),((t,d),F(n-1,denom)),
                   ((t+1,d+1),F(d,denom)),((t+1,d),F(edges-d,denom))]
            assert sum((p for _,p in trans),F(0))==1
            assert sum((p for (tt,dd),p in trans if tt==t+1),F(0))==F(edges,denom)
            assert sum((p for (tt,dd),p in trans if dd==d+1),F(0))==F(d+1,denom)
            for key,p in trans:
                if p: new[key]+=mass*p
            tests+=3
        states=dict(new)
        assert sum(states.values(),F(0))==1
        histories[n+1]=states
        tests+=1
    return histories,tests

def shape_states(nmax=6):
    # Each state stores the complete labeled one-skeleton edge set.
    states={((1,2),):F(1)}
    histories={2:states}
    tests=0
    for n in range(2,nmax):
        nxt=defaultdict(F)
        for edges,mass in states.items():
            simplices=[(v,) for v in range(1,n+1)]+list(edges)
            assert len(simplices)==n+len(edges)
            for s in simplices:
                new_edges=tuple(sorted(set(edges)|{tuple(sorted((v,n+1))) for v in s}))
                nxt[new_edges]+=mass/F(len(simplices))
                tests+=1
        states=dict(nxt)
        assert sum(states.values(),F(0))==1
        histories[n+1]=states
        tests+=1
    return histories,tests

def test():
    history,a=markov_states(9)
    shapes,b=shape_states(6)
    total=a+b
    for n,dist in shapes.items():
        aggregate=defaultdict(F)
        for edges,p in dist.items():
            # Euler identity: triangles = edges - vertices + 1.
            t=len(edges)-n+1
            d=sum(1 for e in edges if 1 in e)
            aggregate[t,d]+=p
            total+=1
        assert dict(aggregate)==history[n],f'full shape mismatch n={n}'
        total+=1
    assert history[3]=={(0,2):F(1,3),(0,1):F(1,3),(1,2):F(1,3)}
    total+=1
    print('PASS',total,'exact rational graph/transition assertions',
          'full shape enumeration through n=6, Markov chains through n=9')
if __name__=='__main__': test()
