from itertools import product
from fractions import Fraction
from math import factorial

U=-1

def proper(state,m,n):
    A=state[:m]; B=state[m:]
    return all(a==U or b==U or a!=b for a in A for b in B)

def force(state,m,n,L):
    if not proper(state,m,n): return False
    s=list(state)
    N=m+n
    while True:
        move=None
        for v in range(N):
            if s[v]!=U: continue
            neigh=range(m,N) if v<m else range(0,m)
            cs={s[w] for w in neigh if s[w]!=U}
            if len(cs)==L-1:
                missing=next(c for c in range(L) if c not in cs)
                move=(v,missing); break
        if move is None: break
        s[move[0]]=move[1]
        if not proper(s,m,n): return False
    return U not in s and proper(s,m,n)

def stir2(n,k):
    if k<0 or k>n: return 0
    dp=[[0]*(k+1) for _ in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            dp[i][j]=dp[i-1][j-1]+j*dp[i-1][j]
    return dp[n][k]

def Q(n,k): return factorial(k)*stir2(n,k)

def falling(L,a):
    z=1
    for i in range(a): z*=L-i
    return z

def chrompoly_biclique(m,n,L):
    return sum(falling(L,a)*stir2(m,a)*(L-a)**n for a in range(1,min(m,L-1)+1))

def predicted_type(state,m,n,L):
    if not proper(state,m,n): return False
    if U not in state: return True
    A=state[:m]; B=state[m:]
    def one(X,Y):
        if U in X: return False
        cs=set(X)
        if len(cs)!=L-1: return False
        missing=next(c for c in range(L) if c not in cs)
        return all(y in (U,missing) for y in Y)
    return one(A,B) or one(B,A)

def formula(m,n,L,p):
    P=chrompoly_biclique(m,n,L)
    qm=Q(m,L-1); qn=Q(n,L-1)
    return (L*qm*p**m*(1-(L-1)*p)**n +
            L*qn*p**n*(1-(L-1)*p)**m +
            (P-L*qm-L*qn)*p**(m+n))

def brute_prob(m,n,L,p):
    r=1-L*p
    tot=Fraction(0)
    for st in product(range(-1,L), repeat=m+n):
        if force(st,m,n,L):
            k=sum(x!=U for x in st)
            tot += p**k*r**(m+n-k)
    return tot

profiles=0; states=0; evals=0
for L in (3,4):
  for m in range(1,4):
    for n in range(1,4):
      if m+n>6: continue
      profiles+=1
      for st in product(range(-1,L), repeat=m+n):
        states+=1
        a=force(st,m,n,L); b=predicted_type(st,m,n,L)
        if a!=b:
            raise AssertionError((L,m,n,st,a,b))
      for den in (2*L,3*L,L):
        p=Fraction(1,den)
        bp=brute_prob(m,n,L,p); fp=formula(m,n,L,p)
        evals+=1
        if bp!=fp: raise AssertionError(('prob',L,m,n,p,bp,fp))
# known printed / checked examples at lambda=3
from fractions import Fraction as F
# compare polynomial values against explicit corrected forms at several p
for p in (F(1,12),F(1,9),F(1,6),F(1,3)):
    assert formula(1,2,3,p)==6*p*p*(1-p)
    assert formula(1,3,3,p)==6*p**3*(3-5*p)
    assert formula(2,2,3,p)==6*p*p*(2-8*p+9*p*p)
print(f'ALL CHECKS PASSED; profiles={profiles}; states={states}; rational_probability_evaluations={evals}; lambda_values=3,4; max_order=6')
