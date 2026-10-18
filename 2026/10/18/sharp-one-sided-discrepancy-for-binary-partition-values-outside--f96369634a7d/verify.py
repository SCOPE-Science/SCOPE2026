"""Independent finite arithmetic checks for the stated discrepancy theorem.

Usage: python3 verify.py. Requires only Python 3.9+.
Finite checks corroborate but do not replace the symbolic proof in RESULT.md.
"""
from functools import lru_cache
from itertools import product

E={(0,1):(0,-1,-2,3),(0,-1):(0,-1,-2,-3),
   (1,1):(3,2,1,0),(1,-1):(-3,-4,-5,0)}
U={(0,1):0,(0,-1):2,(1,1):-1,(1,-1):3}
H={(0,1):-1,(0,-1):-2,(1,1):-2,(1,-1):0}
def step(state,r):
    p,t=state
    return (r&1,t*(-1)**(p+(r>>1)))
for state in E:
    for r,weight in enumerate(E[state]):
        target=step(state,r)
        assert weight <= U[target]-U[state]
        assert weight+3 >= H[target]-H[state]
print('PASS: all 16 directed edges satisfy both exact rational-integer certificates')

def t(m): return 1 if m.bit_count()%2==0 else -1
@lru_cache(None)
def q(Y):
    if Y==0: return 0
    m,r=divmod(Y,8)
    return m+int(r>=(3 if t(m)==1 else 7))+q(Y//4)
def p0(X):
    m,r=divmod(X,8)
    return m+int(r>=(5 if t(m)==1 else 1))
def T(X): return p0(X)+q(X//4)
def d(Y): return 6*q(Y)-Y

def exception(n):
    if n==0: return False
    a=0
    while n%4==0:
        n//=4
        a+=1
    if n%2==0: return False
    m,r=divmod(n,8)
    return (r==(5 if t(m)==1 else 1)) if a==0 else (r==(3 if t(m)==1 else 7))

LIMIT=60000
# Check the underlying partition recurrence independently, without any graph formula.
b=[0]*(2*LIMIT+1)
b[0]=1
for j in range(1,len(b)):
    b[j]=b[j-1] if j%2 else (b[j-2]+b[j//2])%16
count=0
for n in range(1,LIMIT+1):
    observed=b[2*n]==14
    assert observed==exception(n),(n,b[2*n])
    count+=observed
    assert T(n)==count,(n,T(n),count)
    assert 6*T(n)-n<=7
print('PASS: 60,000 partition congruences, index predicates and exact cumulative counts')
for n in range(1,120001):
    y=n//4
    p,tv=(y%2,t(y//2))
    assert d(y)<=U[(p,tv)]
print('PASS: 120,000 state-potential upper checks')
assert 6*T(17)-17==7
print('PASS: X=17 attains global bound D(X)=7')
for k in range(9):
    X=(768*16**k-28)//5
    Y=X//4
    assert d(Y)==-7-6*k
    assert 6*T(X)-X==-10-6*k
    assert X%8==4 and t(X//8)==1
print('PASS: nine exact subsequence identities (arbitrarily large integer arguments)')
print('ALL FINITE CHECKS PASSED')
