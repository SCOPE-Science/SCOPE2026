"""Exact exhaustive F_3 point/line census for a nodal desmic quartic."""
import itertools
from collections import Counter
from math import comb
P=3

def F(v):
    return sum(v[i]*v[i]*v[j]*v[j] for i in range(4) for j in range(i+1,4))%P

def norm(v):
    k=next(i for i,x in enumerate(v) if x%P)
    return tuple((x*pow(v[k],-1,P))%P for x in v)

def points():
    for k in range(4):
        for tail in itertools.product(range(P),repeat=3-k):
            yield (0,)*k+(1,)+tail

def planes2():
    # Unique reduced row echelon bases for every F_3-line in P^3.
    for a,b in itertools.combinations(range(4),2):
        free=[(0,j) for j in range(a+1,4) if j!=b]+[(1,j) for j in range(b+1,4)]
        for vals in itertools.product(range(P),repeat=len(free)):
            rows=[[0]*4,[0]*4]
            rows[0][a]=rows[1][b]=1
            for (i,j),v in zip(free,vals):rows[i][j]=v
            yield tuple(rows[0]),tuple(rows[1])

def restriction(u,v):
    # Homogeneous quartic F(su+tv), coefficient of s^(4-k)*t^k.
    ans=[0]*5
    for i in range(4):
        for j in range(i+1,4):
            for a in range(3):
                for b in range(3):
                    k=a+b
                    ans[k]+=comb(2,a)*comb(2,b)*u[i]**(2-a)*v[i]**a*u[j]**(2-b)*v[j]**b
    return tuple(x%P for x in ans)

def linepoints(u,v):
    return {norm(u)} | {norm(tuple((u[i]*t+v[i])%P for i in range(4))) for t in range(P)}

if __name__=='__main__':
    full=list(planes2())
    assert len(full)==130 and len(set(full))==130
    L=[(u,v) for u,v in full if restriction(u,v)==(0,)*5]
    assert len(L)==24
    onX=[x for x in points() if F(x)==0]
    assert len(onX)==28
    nodes=[x for x in onX if all(x[i]*(x[i]*x[i]-sum(y*y for y in x))%P==0 for i in range(4))]
    assert len(nodes)==12
    incidence={x:0 for x in onX}
    types=Counter()
    for u,v in L:
        ps=linepoints(u,v)
        assert len(ps)==4 and ps<=set(onX)
        types[len(ps.intersection(nodes))]+=1
        for x in ps:incidence[x]+=1
    assert types=={3:16,0:8}
    assert Counter(incidence[x] for x in nodes)=={4:12}
    assert Counter(incidence[x] for x in onX if x not in nodes)=={3:16}
    extras=set()
    for a,b,c,d in itertools.product((1,2),repeat=4):
        if (a*c+b*d)%P==0:
            extras.add(((1,0,a,b),(0,1,c,d)))
    assert len(extras)==8 and extras<=set(L)
    assert all(not (linepoints(*line)&set(nodes)) for line in extras)
    assert set(line for line in L if not(linepoints(*line)&set(nodes)))==extras
    # Independently check the defining equation on the fifth F_9 point of each line:
    # alpha^2=2, basis 1,alpha; binomial multiplication mod 3.
    def mul(z,w):return ((z[0]*w[0]+2*z[1]*w[1])%3,(z[0]*w[1]+z[1]*w[0])%3)
    def sq(z):return mul(z,z)
    def plus(z,w):return ((z[0]+w[0])%3,(z[1]+w[1])%3)
    for u,v in L:
        x=[(u[i],v[i]) for i in range(4)]
        total=(0,0)
        for i in range(4):
            for j in range(i+1,4):total=plus(total,mul(sq(x[i]),sq(x[j])))
        assert total==(0,0)
    print('VERIFY_OK: P3(F3)=40 points, 130 lines; X(F3)=28; 12 nodes; 24 lines = 16 Reye + 8 extra.')
