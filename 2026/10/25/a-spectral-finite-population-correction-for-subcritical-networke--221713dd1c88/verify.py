"""Exact finite-state and resolvent checks for the subcritical block-SIR expansion."""
from fractions import Fraction as F
from functools import lru_cache

def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]

def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def inv(a):
    n=len(a); b=[list(a[i])+eye(n)[i] for i in range(n)]
    for k in range(n):
        q=next(j for j in range(k,n) if b[j][k]); b[k],b[q]=b[q],b[k]
        c=b[k][k]; b[k]=[u/c for u in b[k]]
        for j in range(n):
            if j != k:
                c=b[j][k]; b[j]=[b[j][i]-c*b[k][i] for i in range(2*n)]
    return [x[n:] for x in b]

def coefficient(p,r):
    n=len(p); b=[[F(int(i==j))-r*p[i][j] for j in range(n)] for i in range(n)]
    bi=inv(b); val=mul(p,mul(bi,bi)); return r*sum(val[i][i] for i in range(n))/(n*(1-r)**2)

def sir_mean(m,p,r):
    n=len(p)
    @lru_cache(None)
    def u(state):
        active=[state[2*i] for i in range(n)]
        removed=[state[2*i+1] for i in range(n)]
        if not any(active): return F(0)
        transitions=[]
        for j in range(n):
            sj=m-active[j]-removed[j]
            rate=r*sj*sum(p[i][j]*active[i] for i in range(n))/m
            if rate:
                ns=list(state);ns[2*j]+=1; transitions.append((rate,tuple(ns),1))
            if active[j]:
                ns=list(state);ns[2*j]-=1;ns[2*j+1]+=1
                transitions.append((F(active[j]),tuple(ns),0))
        denom=sum(rate for rate,_,_ in transitions)
        return sum(rate*(inc+u(ns))/denom for rate,ns,inc in transitions)
    return F(1)+sum(u(tuple(1 if j==2*i else 0 for j in range(2*n))) for i in range(n))/n

r=F(1,2); q=[[F(0),F(1)],[F(1),F(0)]]
for theta,wanted in [(F(0),F(32,9)),(F(1,2),F(4)),(F(1),F(8))]:
    p=[[theta*F(int(i==j))+(1-theta)*q[i][j] for j in range(2)] for i in range(2)]
    assert coefficient(p,r)==wanted
    for m in range(1,5):
        mu=sir_mean(m,p,r)
        assert 1 <= mu < 1/(1-r), (m,theta,mu)
assert coefficient([[F(1)]],r)==8
for m in range(1,9):
    mu=sir_mean(m,[[F(1)]],r)
    assert 1 <= mu < 2
# Invertible three-block example, check matrix identity and positive coefficient.
p=[[F(1,2),F(1,2),F(0)],[F(1,2),F(0),F(1,2)],[F(0),F(1,2),F(1,2)]]
b=[[F(int(i==j))-r*p[i][j] for j in range(3)] for i in range(3)]
assert mul(b,inv(b))==eye(3)
assert coefficient(p,r)>0

# Check the integrated first/second branching moment equations with exact rationals.
def check_moments(p,r):
    n=len(p); a=1-r
    d=[[F(int(i==j))-r*p[i][j] for j in range(n)] for i in range(n)]
    di=inv(d)
    y=[[di[i][j]/(n*a) for j in range(n)] for i in range(n)]
    x=mul(di,di)
    x=[[x[i][j]/(n*a) for j in range(n)] for i in range(n)]
    lhs=[[mul(d,y)[i][j]+mul(y,d)[i][j] for j in range(n)] for i in range(n)]
    assert lhs==[[F(2 if i==j else 0,n*a) for j in range(n)] for i in range(n)]
    dx=mul(d,x); yp=mul(y,p)
    rhs=[[F(int(i==j),n)+r*yp[i][j]+(r/(n*a) if i==j else 0) for j in range(n)] for i in range(n)]
    assert dx==rhs

for p in ([[F(1)]],q,[[F(1,2),F(1,2)],[F(1,2),F(1,2)]],[[F(1,2),F(1,2),F(0)],[F(1,2),F(0),F(1,2)],[F(0),F(1,2),F(1,2)]]):
    check_moments(p,r)

print('PASS: exact rational resolvents, 3 block mixing examples, and finite epidemic dynamic-programming checks')
