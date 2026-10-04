from fractions import Fraction as F


def mat_add(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def outer(x,f):
    return [[xi*fj for fj in f] for xi in x]


def construct(n,k):
    assert n >= 2 and 1 <= k <= n
    if k == 1:
        rows=[[F(1,n) for _ in range(n)]]
    else:
        U=F(k-1,2); V=F(n-1,2)
        eps=F(1,1)/(4*n*U*V)
        us=[F(2*r-k-1,2) for r in range(1,k+1)]
        vs=[F(2*j-n-1,2) for j in range(1,n+1)]
        rows=[[F(1,n)+eps*u*v for v in vs] for u in us]
    xs=[]; fs=[]
    for j in range(n):
        x=[F(0) for _ in range(n)]; x[j]=F(1); xs.append(x)
        f=[-F(k,n) for _ in range(n)]; f[j]=F(1); fs.append(f)
    for row in rows:
        xs.append(row); fs.append([F(1) for _ in range(n)])
    return rows,xs,fs


def check(n,k):
    rows,xs,fs=construct(n,k)
    assert all(sum(r,F(0))==1 for r in rows)
    assert all(sum(rows[r][j] for r in range(k))==F(k,n) for j in range(n))
    assert all(a>0 for r in rows for a in r)
    assert len({tuple(x) for x in xs})==n+k
    assert all(sum(abs(t) for t in x)==1 for x in xs)
    assert all(max(abs(t) for t in f)==1 for f in fs)
    assert all(sum(f[t]*x[t] for t in range(n))==1 for x,f in zip(xs,fs))
    S=[[F(0) for _ in range(n)] for _ in range(n)]
    for x,f in zip(xs,fs): S=mat_add(S,outer(x,f))
    target=F(n+k,n)
    assert all(S[i][j]==(target if i==j else 0) for i in range(n) for j in range(n))


def explicit_5_2():
    n=5; k=2
    rows=[
      [F(1,10),F(3,20),F(1,5),F(1,4),F(3,10)],
      [F(3,10),F(1,4),F(1,5),F(3,20),F(1,10)]
    ]
    xs=[];fs=[]
    for j in range(n):
        x=[F(0)]*n; x[j]=1; xs.append(x)
        f=[-F(2,5)]*n; f[j]=1; fs.append(f)
    xs.extend(rows); fs.extend([[F(1)]*n,[F(1)]*n])
    assert len({tuple(x) for x in xs})==7
    S=[[F(0) for _ in range(n)] for _ in range(n)]
    for x,f in zip(xs,fs): S=mat_add(S,outer(x,f))
    assert all(S[i][j]==(F(7,5) if i==j else 0) for i in range(n) for j in range(n))

for n in range(2,13):
    for k in range(1,n+1): check(n,k)
explicit_5_2()
print('VERIFY_OK general_n_2_12 explicit_n5_k2')
