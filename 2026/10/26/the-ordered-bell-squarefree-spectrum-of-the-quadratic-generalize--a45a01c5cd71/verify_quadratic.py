"""Independent finite checks for the quadratic floor-recursion theorem.

Run: python3 verify_quadratic.py
Standard-library integer arithmetic only.
"""
from math import factorial

N=40000
# The identity obtained by adjacent-index subtraction is checked separately
# against the original floor recursion on a smaller domain.
small=600
floor_star=[0]*(small+1)
floor_star[1]=1
for n in range(2,small+1):
    floor_star[n]=1-n-sum(floor_star[d]*(n//d)**2 for d in range(2,n))

proper=[[] for _ in range(N+1)]
for d in range(2,N//2+1):
    for n in range(2*d,N+1,d):
        proper[n].append(d)
star=[0]*(N+1)
star[1]=1
for n in range(2,N+1):
    star[n]=-1-sum(star[d]*(2*(n//d)-1) for d in proper[n])
assert star[:small+1]==floor_star

# Sieve to get the full prime support and Möbius function independently.
spf=list(range(N+1))
for p in range(2,int(N**0.5)+1):
    if spf[p]==p:
        for k in range(p*p,N+1,p):
            if spf[k]==k:
                spf[k]=p

# Ordered Bell (Fubini) numbers, independently via Stirling recursion.
R=7
stirling=[[0]*(R+1) for _ in range(R+1)]
stirling[0][0]=1
for n in range(1,R+1):
    for k in range(1,n+1):
        stirling[n][k]=stirling[n-1][k-1]+k*stirling[n-1][k]
F=[sum(factorial(k)*stirling[n][k] for k in range(n+1)) for n in range(R+1)]
assert F[:7]==[1,1,3,13,75,541,4683]

squarefree_checks=0
nonsquarefree_checks=0
for n in range(2,N+1):
    v=n
    ps=[]
    sqfree=True
    while v>1:
        p=spf[v]
        expo=0
        while v%p==0:
            v//=p
            expo+=1
        ps.append(p)
        if expo>1:
            sqfree=False
    if sqfree:
        x=[p-1 for p in ps]
        e=[1]+[0]*len(x)
        for a in x:
            for j in range(len(x),0,-1):
                e[j]+=a*e[j-1]
        predicted=(-1)**len(x)*(1+2*sum(F[j]*e[j] for j in range(1,len(x))))
        assert star[n]==predicted,(n,star[n],predicted)
        assert (star[n]==-1)==(len(x)==1)
        squarefree_checks+=1
    else:
        assert star[n]%2==0,(n,star[n])
        nonsquarefree_checks+=1
assert squarefree_checks+nonsquarefree_checks==N-1
print('VERIFY_OK',N,small,squarefree_checks,nonsquarefree_checks)
