from math import comb

def mul(a,b):
    c=[0j]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def check(Q,P,N):
    m=len(Q)-1
    assert len(P)<=m+1 and Q[0]==1 and N>=2*m
    kappa=Q[-1].conjugate()
    Qsharp=[Q[m-j].conjugate() for j in range(m+1)]
    assert Qsharp==[kappa*x for x in Q]
    Ppad=P+[0j]*(m+1-len(P))
    Psharp=[Ppad[m-j].conjugate() for j in range(m+1)]
    D=mul(Q,Q)
    A=mul(Ppad,Psharp)
    W=[x+y/kappa for x,y in zip(D,A)]
    f=[0j]*(N+1)
    for n in range(N+1):
        f[n]=(P[n] if n<len(P) else 0)-sum(Q[t]*f[n-t] for t in range(1,min(n,m)+1))
    G=[[int(j==k)+sum(f[j-r].conjugate()*f[k-r] for r in range(min(j,k)+1)) for k in range(N+1)] for j in range(N+1)]
    # The examples are Gaussian-integer arithmetic. These conservative
    # magnitude bounds ensure every intermediate integer product and sum
    # is exactly representable by binary64 (strictly below 2**53).
    assert all(max(abs(v.real),abs(v.imag)) < 2**24 for v in f)
    assert all(max(abs(v.real),abs(v.imag)) < 2**32 for row in G for v in row)
    assert all(max(abs(v.real),abs(v.imag)) < 2**8 for v in D)
    assert all(max(abs(v.real),abs(v.imag)) < 2**32 for v in W)
    for v in f+W+[x for row in G for x in row]:
        assert v.real == round(v.real) and v.imag == round(v.imag)
    for j in range(N-2*m+1):
        for k in range(N+1):
            val=sum(D[r]*G[j+r][k] for r in range(2*m+1))
            expected=W[k-j] if 0<=k-j<=2*m else 0
            assert val==expected,(m,j,k,val,expected)
    return (N-2*m+1)*(N+1)

Q1=[1,-2,1];Q2=[1,0,-1];Q3=[1,-1-1j,1j];Q4=[1,-1,-1,1];Q5=mul(Q2,[1,-1j]);Q6=mul(Q1,Q1)
cases=[(Q1,[1,2,3],12),(Q2,[2,1,-1],12),(Q3,[1,2+1j,3-1j],13),(Q4,[1+1j,3,0,2-1j],13),(Q5,[1,1,1j,1],13),(Q6,[1,1j,2,1-1j,4],15)]
checks=[check(*x) for x in cases]
print("CHECK_OK", sum(checks), "entrywise comparisons in", len(cases), "examples")
