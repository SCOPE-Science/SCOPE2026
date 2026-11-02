"""Independent genus-three zeta verification by F9, F81 and F729 points.
GF(9) uses primitive theta with theta^2+theta+2=0, distinct from
GF(9)'s imaginary-unit representation in verify_formula.py.
F81 adjoins u with u^2=theta; F729 adjoins v with v^3-v-1=0.
"""
from collections import Counter

def a9(x,y):return (x%3+y%3)%3+3*((x//3+y//3)%3)
def n9(x):return (-x%3)%3+3*((-(x//3))%3)
def s9(x,y):return a9(x,n9(y))
def m9(x,y):
    a,b=x%3,x//3;c,d=y%3,y//3
    return (a*c+b*d)%3+3*((a*d+b*c+2*b*d)%3)
def p9(x,n):
    s=1
    while n:
        if n&1:s=m9(s,x)
        x=m9(x,x);n//=2
    return s
assert len({p9(t,2) for t in range(1,9)})==4
assert 3 not in {p9(t,2) for t in range(1,9)} # theta represented by 0+1 theta
assert all(s9(s9(p9(t,3),t),1)!=0 for t in range(9))

def add(u,v):return tuple(a9(x,y) for x,y in zip(u,v))
def neg(u):return tuple(n9(x) for x in u)
def sub(u,v):return add(u,neg(v))
def mul(u,v):
    n=len(u)
    tmp=[0]*(2*n-1)
    for i,x in enumerate(u):
        for j,y in enumerate(v):tmp[i+j]=a9(tmp[i+j],m9(x,y))
    if n==2:
        # u^2=theta (coefficient 3)
        tmp[0]=a9(tmp[0],m9(tmp[2],3));return tuple(tmp[:2])
    if n==3:
        # v^3=v+1, v^4=v^2+v
        for j in (4,3):
            vj=tmp[j]
            tmp[j-3]=a9(tmp[j-3],vj)
            tmp[j-2]=a9(tmp[j-2],vj)
        return tuple(tmp[:3])
    raise ValueError(n)
def power(x,n):
    y=(1,)+(0,)*(len(x)-1)
    while n:
        if n&1:y=mul(y,x)
        x=mul(x,x);n//=2
    return y

def count(A,B,n):
    q=9**n; ext=2 if n==2 else 3
    assert n in (2,3)
    one=(1,)+(0,)*(ext-1)
    AA=(A,)+(0,)*(ext-1);BB=(B,)+(0,)*(ext-1)
    squares={power(tuple((k//(9**i))%9 for i in range(ext)),2) for k in range(1,q)}
    assert len(squares)==(q-1)//2
    total=0
    for k in range(q):
        x=tuple((k//(9**i))%9 for i in range(ext))
        x2=mul(x,x);x4=mul(x2,x2)
        rhs=mul(add(sub(x4,mul(AA,x2)),one),add(sub(x4,mul(BB,x2)),one))
        total+=0 if not any(rhs) else (1 if rhs in squares else -1)
    return q+2+total

def curve_9(A,B):
    squares={p9(k,2) for k in range(1,9)}
    total=0
    for x in range(9):
        x2=m9(x,x);x4=m9(x2,x2)
        rhs=m9(a9(s9(x4,m9(A,x2)),1),a9(s9(x4,m9(B,x2)),1))
        total+=(0 if rhs==0 else (1 if rhs in squares else -1))
    return 11+total

def elliptic_trace(A,B,k):
    sq={p9(j,2) for j in range(1,9)};total=0
    for x in range(9):
        x2=m9(x,x)
        if k==0:
            rhs=m9(s9(x2,s9(A,1)),s9(x2,s9(B,1)))
        elif k==1:
            rhs=m9(s9(x2,a9(A,1)),s9(x2,a9(B,1)))
        else:
            rhs=m9(a9(s9(x2,m9(A,x)),1),a9(s9(x2,m9(B,x)),1))
        total+=(0 if rhs==0 else (1 if rhs in sq else -1))
    return -1-total

result=Counter()
for A in range(9):
    for B in range(9):
        if A in (1,2) or B in (1,2) or A==B:continue
        ts=tuple(sorted(elliptic_trace(A,B,k) for k in range(3)))
        n1=curve_9(A,B)
        assert n1==10-sum(ts),(A,B,n1,ts)
        for degree in (2,3):
            # Frobenius power sums for the three elliptic factors
            def pp(t):
                p0,p1=2,t
                for j in range(2,degree+1):p0,p1=p1,t*p1-9*p0
                return p1
            expected=9**degree+1-sum(pp(t) for t in ts)
            actual=count(A,B,degree)
            assert actual==expected,(A,B,degree,actual,expected,ts)
        result[ts]+=1
assert result==Counter({(-6,-2,-2):6,(-6,2,2):4,(-2,-2,2):12,
                       (-2,-2,6):8,(-2,2,2):12}),result
print('EXTENSIONS_VERIFY_OK: 42 smooth triples; F9, F81, F729 point counts agree with all five degree-six zeta numerators')
