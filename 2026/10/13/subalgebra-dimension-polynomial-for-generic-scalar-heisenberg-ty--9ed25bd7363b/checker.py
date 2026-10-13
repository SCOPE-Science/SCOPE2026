"""Direct finite-field RREF check for a split non-Lie Heisenberg Leibniz algebra."""
from itertools import combinations, product
from math import prod

def gauss(n,k,q):
    if k<0 or k>n: return 0
    num=prod(q**(n-j)-1 for j in range(k))
    den=prod(q**(k-j)-1 for j in range(k))
    return num//den

def gl(d,q): return prod(q**d-q**i for i in range(d))

def formula(m,q):
    c={k+1:gauss(2*m,k,q) for k in range(2*m+1)}
    for a in range(m+1):
        for b in range(m-a+1):
            base=gauss(m,a,q)*gauss(m-a,b,q)
            for d in range(min(a,b)+1):
                r=a+b-d
                c[r]=c.get(r,0)+base*gauss(a,d,q)*gauss(b,d,q)*gl(d,q)*q**r
    return dict(sorted(c.items()))

def fadd(a,b,q): return (a^b) if q==4 else (a+b)%q

def fmul(a,b,q):
    if q!=4: return a*b%q
    w=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&1 and (b>>j)&1: w^=(1<<(i+j))
    if w&4: w^=7 # x^2=x+1 mod x^2+x+1
    return w

def subspaces(n,q):
    for k in range(n+1):
        for p in combinations(range(n),k):
            slots=[(i,j) for i in range(k) for j in range(p[i]+1,n) if j not in p]
            for vals in product(range(q),repeat=len(slots)):
                rows=[[0]*n for _ in range(k)]
                for i,j in enumerate(p): rows[i][j]=1
                for (i,j),v in zip(slots,vals): rows[i][j]=v
                yield p,rows

def verify(m,q,lam):
    assert lam and lam!=1 and (q==4 or lam!=q-1)
    n=2*m+1
    actual={}
    for piv,rows in subspaces(n,q):
        good=True
        if n-1 not in piv:
            for u in rows:
                for v in rows:
                    ab=0; ba=0
                    for j in range(m):
                        ab=fadd(ab,fmul(u[j],v[m+j],q),q)
                        ba=fadd(ba,fmul(u[m+j],v[j],q),q)
                    if fadd(ab,fmul(lam,ba,q),q):
                        good=False
                        break
                if not good: break
        if good: actual[len(rows)]=actual.get(len(rows),0)+1
    expected=formula(m,q)
    assert actual==expected,(q,m,actual,expected)
    return actual

if __name__=='__main__':
    for m,q,lam in [(1,4,2),(2,4,2),(1,5,2),(2,5,2),(1,7,2)]:
        r=verify(m,q,lam)
        print(f'(m,q,lambda)=({m},{q},{lam}): {r}; total={sum(r.values())}')
    print('VERIFY_OK')
