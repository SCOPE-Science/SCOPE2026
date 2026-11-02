"""Finite checks of Fibonacci-minus-two shifted-word state distinguishers.
Independent integer/Zeckendorf implementation; not a substitute for the infinite proof.
"""
F=[0,1]
for _ in range(320): F.append(F[-1]+F[-2])
def zbits(n):
    if n<0: raise ValueError
    b=[]
    for i in range(len(F)-1,1,-1):
        if F[i]<=n:
            b.append(i); n-=F[i]
    assert n==0
    return b
def f(n):return int(2 in zbits(n))
def shiftzeros(n,j):return sum(F[i+j] for i in zbits(n))
for k in range(5,101):
    c=F[k]-2
    b=int(k%2==0)
    q=4 if k%2 else 6
    candidates=[0]+[F[i] for i in range(2,k)]+[q]
    signatures=[]
    for n in candidates:
        signatures.append(tuple(f(shiftzeros(n,j)+c) for j in range(k+2)))
    assert len(set(signatures))==k, (k,signatures)
    assert set(signatures[0])=={b}
    for i in range(2,k):
        s=signatures[i-1]
        assert max((j for j,v in enumerate(s) if v!=b),default=-1)==k-1-i,(k,i,s)
    assert signatures[-1][0]!=signatures[1][0]
    assert signatures[-1][1:]==signatures[1][1:]
    for t in range(2,k+12):
        x=f(c+F[t]); expected=(int(t%2==0 and t<k) if k%2 else int(t>=k or (4<=t<k and t%2==0)))
        assert x==expected,(k,t,x,expected)
print('PASS integer Zeckendorf independent residual tests k=5..100, all unary witnesses and h_k(t) identities')
