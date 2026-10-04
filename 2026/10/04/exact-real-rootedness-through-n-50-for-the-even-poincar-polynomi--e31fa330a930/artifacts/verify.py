from pathlib import Path
from fractions import Fraction
from math import comb, factorial
from functools import lru_cache
import json

HERE=Path(__file__).resolve().parent
CERT=json.loads((HERE/'root_brackets.json').read_text())

def add(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def scale(a,k): return [k*v for v in a]
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y: c[i+j]+=x*y
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def powlin(sign,n): return [comb(n,i)*(sign**(n-i)) for i in range(n+1)]

@lru_cache(None)
def S2(n,k):
    if n==k==0: return 1
    if n==0 or k==0 or k>n: return 0
    return S2(n-1,k-1)+k*S2(n-1,k)

def alpha(i,j): return comb(2*j,i)-(comb(2*j,i-1) if i else 0)
def gamma(n,j):
    if j==1: return 1
    if j==2: return 2**(n-1)-1
    return S2(n,j)*factorial(j-1)//2

@lru_cache(None)
def T(n):
    res=[0]
    for j in range((n-1)//2+1):
        A=[-alpha(i,j) for i in range(j)]+[0,alpha(j,j)]
        res=add(res,scale(mul(powlin(1,n-1-2*j),A),comb(n-1,2*j)))
    s=add(powlin(1,n-1),powlin(-1,n-1)); assert all(v%2==0 for v in s)
    res=add(res,[v//2 for v in s])
    if n>=2:
        s=add(powlin(1,n-2),powlin(-1,n-2)); assert all(v%2==0 for v in s)
        res=add(res,scale([v//2 for v in s],gamma(n,2)))
    for j in range(3,n+1): res=add(res,scale(powlin(-1,n-j),gamma(n,j)))
    return res

@lru_cache(None)
def H(r,s):
    n=r+s; res=T(n)
    for j in range(1,min(r,n-2)+1):
        for k in range(0,n-j-1):
            proj=[0]+[1]*(n-j-k-1)
            res=add(res,scale(mul(H(j,k),proj),comb(n-j,k)))
    return res

def div_xplus1(p):
    n=len(p)-1; q=[0]*n; q[-1]=p[-1]
    for i in range(n-2,-1,-1): q[i]=p[i+1]-q[i+1]
    assert p[0]-q[0]==0
    return q

def yreduce(p):
    d=len(p)-1; assert d%2==0 and p==p[::-1]
    m=d//2; S=[[2]] if m==0 else [[2],[0,1]]
    for k in range(2,m+1): S.append(add([0]+S[-1],scale(S[-2],-1)))
    Q=[p[m]]
    for k in range(1,m+1): Q=add(Q,scale(S[k],p[m+k]))
    return Q

def sign_at(poly,x):
    v=Fraction(0)
    for a in reversed(poly): v=v*x+a
    return (v>0)-(v<0)

known={
1:[1,1],2:[1,2,1],3:[1,5,5,1],4:[1,12,23,12,1],5:[1,27,102,102,27,1],
6:[1,58,421,756,421,58,1],7:[1,121,1612,5077,5077,1612,121,1],
8:[1,248,5802,31072,52402,31072,5802,248,1],
9:[1,503,19925,175036,480097,480097,175036,19925,503,1],
10:[1,1014,66090,920263,3975949,6349238,3975949,920263,66090,1014,1]}

for n,c in known.items(): assert H(n,0)==c, ('source mismatch',n)
assert H(1,0)==[1,1]
assert H(2,0)==[1,2,1]
for n in range(1,51):
    p=H(n,0)
    assert len(p)==n+1 and p==p[::-1] and all(a>0 for a in p)
    if n<3: continue
    e=p if n%2==0 else div_xplus1(p)
    q=yreduce(e)
    rec=CERT[str(n)]
    assert q==rec['q_coeffs'], ('Q mismatch',n)
    B=[Fraction(a,b) for a,b in rec['bounds']]
    assert len(B)==len(q) and B==sorted(B) and B[-1]==-2
    signs=[sign_at(q,b) for b in B]
    assert signs==rec['signs'] and all(signs[i]*signs[i+1]<0 for i in range(len(signs)-1)), ('sign certificate',n)
    assert all(b<=-2 for b in B)
print('SOURCE_VALUES_OK n=1..10')
print('PALINDROMIC_POSITIVE_OK n=1..50')
print('EXACT_RATIONAL_ROOT_BRACKETS_OK n=3..50')
print('REAL_ROOTED_OK n=1..50')
print('VERIFY_OK')
