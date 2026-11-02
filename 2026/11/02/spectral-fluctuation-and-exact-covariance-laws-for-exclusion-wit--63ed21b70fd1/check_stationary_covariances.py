"""Exact finite-state checks for SEP with site-resampling reservoirs.

Only Python's standard library is required. Computations do not replace
proofs for arbitrary graph order, weights, or bath densities.
"""
from fractions import Fraction as F
from itertools import combinations
import random

assertions = 0

def check(cond, message='failed'):
    global assertions
    assertions += 1
    if not cond:
        raise AssertionError(message)

def solve(A, b):
    n = len(b)
    aug = [[F(x) for x in row]+[F(y)] for row,y in zip(A,b)]
    for j in range(n):
        piv = next((i for i in range(j,n) if aug[i][j]), None)
        if piv is None:
            raise ValueError('singular system')
        aug[j],aug[piv] = aug[piv],aug[j]
        fac=aug[j][j]
        aug[j]=[x/fac for x in aug[j]]
        for i in range(n):
            if i!=j and aug[i][j]:
                c=aug[i][j]
                aug[i]=[x-c*y for x,y in zip(aug[i],aug[j])]
    return [row[-1] for row in aug]

def mat_inv(A):
    n=len(A)
    cols=[solve(A,[F(i==j) for i in range(n)]) for j in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))

def graph_system(n,edges,xi,h):
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    for (i,j),w in edges.items():
        L[i][i]+=w;L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
    K=[[L[i][j]+(xi if i==j else F(0)) for j in range(n)] for i in range(n)]
    R=mat_inv(K)
    mu=[xi*dot(row,h) for row in R]
    m=sum(h,F(0))/n
    d=[a-m for a in h]
    global_var=F(n)*m*(1-m)-xi*dot(d,[dot(row,d) for row in R])
    return L,R,mu,global_var


def pair_green(n, edges, xi, mu):
    pairs=list(combinations(range(n),2))
    index={p:i for i,p in enumerate(pairs)}
    m=len(pairs)
    Q=[[F(0) for _ in range(m)] for _ in range(m)]
    for idx,(i,j) in enumerate(pairs):
        current={i,j}
        for (u,v),w in edges.items():
            hasu=u in current;hasv=v in current
            if hasu!=hasv:
                after=tuple(sorted((current-{u,v}) | ({v} if hasu else {u})))
                k=index[after]
                Q[idx][k]+=w;Q[idx][idx]-=w
    M=[[(2*xi if i==j else F(0))-Q[i][j] for j in range(m)] for i in range(m)]
    forcing=[edges.get((i,j),F(0))*(mu[i]-mu[j])**2 for i,j in pairs]
    result=solve(M,[-x for x in forcing])
    return dict(zip(pairs,result))

def stationary(n,edges,xi,h):
    k=1<<n
    Q=[[F(0) for _ in range(k)] for _ in range(k)]
    for s in range(k):
        for (i,j),w in edges.items():
            if (s>>i&1)!=(s>>j&1):
                t=s^(1<<i)^(1<<j)
                Q[s][t]+=w;Q[s][s]-=w
        for i in range(n):
            t=s^(1<<i)
            rate=xi*((1-h[i]) if (s>>i&1) else h[i])
            Q[s][t]+=rate;Q[s][s]-=rate
    A=[[Q[s][t] for s in range(k)] for t in range(k)]
    A[-1]=[F(1)]*k
    b=[F(0)]*(k-1)+[F(1)]
    return solve(A,b)

def direct_moments(n,p):
    mu=[sum((v*F(s>>i&1) for s,v in enumerate(p)),F(0)) for i in range(n)]
    cov={}
    for i,j in combinations(range(n),2):
        val=sum((v*F((s>>i&1)*(s>>j&1)) for s,v in enumerate(p)),F(0))
        cov[(i,j)]=val-mu[i]*mu[j]
    M=sum((v*F(s.bit_count()) for s,v in enumerate(p)),F(0))
    var=sum((v*F(s.bit_count()**2) for s,v in enumerate(p)),F(0))-M*M
    return mu,cov,var

def complete_formula(n,w,xi,h):
    mean=sum(h,F(0))/n
    d=[x-mean for x in h]
    s2=sum((x*x for x in d),F(0))
    a=xi/(xi+n*w)
    d0=2*s2/(n-1)
    u=[(n*x*x-s2)/(n-2) for x in d]
    out={}
    for i,j in combinations(range(n),2):
        diff=(d[i]-d[j])**2
        d2=diff-d0-u[i]-u[j]
        out[(i,j)]=-w*a*a*(d0/(2*xi)+(u[i]+u[j])/(2*xi+n*w)+d2/(2*xi+2*(n-1)*w))
    return out

rng=random.Random(20261029)
edgecases=0
for n in range(2,6):
    all_edges=list(combinations(range(n),2))
    for typ in range(4):
        if typ==0: chosen=all_edges
        elif typ==1: chosen=[(i,i+1) for i in range(n-1)]
        elif typ==2: chosen=[(0,i) for i in range(1,n)]
        else: chosen=sorted(set([(i,i+1) for i in range(n-1)]+[(0,n-1)]))
        for repeat in range(4):
            edges={e:F(rng.randrange(1,5),rng.randrange(1,4)) for e in chosen}
            xi=F(rng.randrange(1,5),rng.randrange(1,4))
            h=[F(rng.randrange(0,6),5) for _ in range(n)]
            L,R,mu,v=graph_system(n,edges,xi,h)
            p=stationary(n,edges,xi,h)
            dmu,cov,dv=direct_moments(n,p)
            check(sum(p)==1)
            for k in range(n):check(dmu[k]==mu[k],f'mean n={n}')
            check(dv==v,f'variance n={n}, {dv}!={v}')
            predicted_cov=pair_green(n,edges,xi,mu)
            for pair in cov:check(cov[pair]==predicted_cov[pair],f'pair Green n={n}')
            energy=sum((weight*(mu[i]-mu[j])**2 for (i,j),weight in edges.items()),F(0))
            check(sum(cov.values(),F(0))==-energy/(2*xi),'Dirichlet covariance sum')
            check(all(c<=0 for c in cov.values()),f'sign {n} {cov}')
            if len(set(h))>1:
                check(all(c<0 for c in cov.values()),f'strict sign {n}')
            if typ==0 and n>=3 and len(set(edges.values()))==1:
                expected=complete_formula(n,next(iter(edges.values())),xi,h)
                for pair in cov:check(cov[pair]==expected[pair])
            for e,weight in edges.items():
                i,j=e
                incr=F(1,3)
                altered=dict(edges);altered[e]+=incr
                L2,R2,mu2,v2=graph_system(n,altered,xi,h)
                b=[F(int(k==i)-int(k==j)) for k in range(n)]
                resist=dot(b,[dot(row,b) for row in R])
                exact_diff=incr*(mu[i]-mu[j])**2/(xi*(1+incr*resist))
                check(v2-v==exact_diff,'finite edge response')
            edgecases+=1

# Uniform-edge complete graphs: full stationary distribution versus all harmonic modes.
for n in range(3,6):
    edges={(i,j):F(2,3) for i,j in combinations(range(n),2)}
    xi=F(4,5)
    for h in [[F((3*i+1) % 7,7) for i in range(n)], [F(i % 2) for i in range(n)]]:
        p=stationary(n,edges,xi,h)
        mu,cov,var=direct_moments(n,p)
        exact=complete_formula(n,F(2,3),xi,h)
        for pair in cov:check(cov[pair]==exact[pair],f'complete closed-form n={n}')

# Multiple complete-graph profiles with rational but identical edge weights.
for n in range(3,8):
    for repeat in range(12):
        w=F(rng.randrange(1,7),rng.randrange(1,5))
        xi=F(rng.randrange(1,7),rng.randrange(1,5))
        h=[F(rng.randrange(0,9),8) for _ in range(n)]
        cov=complete_formula(n,w,xi,h)
        m=sum(h,F(0))/n
        d=[x-m for x in h]
        s2=sum((x*x for x in d),F(0))
        a=xi/(xi+n*w)
        check(sum(cov.values(),F(0))==-n*w*a*a*s2/(2*xi))
        check(all(v<=0 for v in cov.values()))
        if len(set(h))>1:check(all(v<0 for v in cov.values()))

print(f'PASS {assertions} exact rational assertions, {edgecases} full finite-state regimes')
