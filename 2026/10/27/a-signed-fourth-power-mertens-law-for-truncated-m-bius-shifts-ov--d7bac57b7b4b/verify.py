from fractions import Fraction
from itertools import product

# Polynomials are little-endian tuples over prime fields.
def trim(v):
    v=list(v)
    while len(v)>1 and v[-1]==0: v.pop()
    return tuple(v)
def add(u,v,q):
    return trim(((u[i] if i<len(u) else 0)+(v[i] if i<len(v) else 0))%q for i in range(max(len(u),len(v))))
def divmodp(u,v,q):
    u=list(trim(u)); v=trim(v)
    if v==(0,): raise ZeroDivisionError
    r=[0]*max(1,len(u)-len(v)+1)
    leading_inverse=pow(v[-1],-1,q)
    while len(u)>=len(v) and any(u):
        offset=len(u)-len(v); coef=u[-1]*leading_inverse%q;r[offset]=coef
        for i,x in enumerate(v):u[i+offset]=(u[i+offset]-coef*x)%q
        while len(u)>1 and u[-1]==0:u.pop()
    return trim(r),trim(u)
def is_divisible(a,b,q):
    return divmodp(a,b,q)[1]==(0,)
def gcdp(u,v,q):
    while v!=(0,): u,v=v,divmodp(u,v,q)[1]
    return u
def derivative(u,q):
    return trim((i*u[i])%q for i in range(1,len(u))) if len(u)>1 else (0,)
def monics(q,d):
    for cs in product(range(q),repeat=d):
        yield cs+(1,)
def irreducibles(q,M):
    out=[]
    for d in range(1,M+1):
        for p in monics(q,d):
            if all(not is_divisible(p,t,q) for t in out if len(t)-1<=d//2):out.append(p)
    return out
def small_factor(p,q,small_primes):
    if any(is_divisible(p,addp_square(P,q),q) for P in small_primes):return 0
    sign=(-1)**sum(is_divisible(p,P,q) for P in small_primes)
    return sign
def addp_square(p,q):
    z=[0]*(2*len(p)-1)
    for i,c in enumerate(p):
        for j,d in enumerate(p):z[i+j]=(z[i+j]+c*d)%q
    return trim(z)
def mu_trunc(p,q,small_primes):
    if len(gcdp(p,derivative(p,q),q))>1:return 0
    return (-1)**sum(is_divisible(p,P,q) for P in small_primes)
def local(q,a,P):
    Q=q**(len(P)-1)
    if not is_divisible(a,P,q):return Fraction(Q*Q-4*Q+2,Q*Q)
    Q1,r=divmodp(a,P,q)
    if is_divisible(Q1,P,q):return Fraction(Q*Q-1,Q*Q)
    return Fraction(Q*Q-2,Q*Q)
def check(q,N,M,a):
    small=irreducibles(q,M); D=2*sum(len(p)-1 for p in small)
    assert N>=D and len(a)<=N
    E=Fraction(1)
    for p in small:E*=local(q,a,p)
    total_full=total_small=0
    for low in product(range(q),repeat=N):
        f=low+(1,); fshift=add(f,a,q)
        total_small+=small_factor(f,q,small)*small_factor(fshift,q,small)
        total_full+=mu_trunc(f,q,small)*mu_trunc(fshift,q,small)
    assert Fraction(total_small,q**N)==E,(q,a,N,M,total_small,E)
    error=abs(Fraction(total_full,q**N)-E)
    tail=2*sum(Fraction(1,q**d*d) for d in range(M+1,N//2+1))
    assert error<=tail,(error,tail)
    print('CASE',q,N,M,tuple(a),'D',D,'local',str(E),'full',str(Fraction(total_full,q**N)),'error',str(error),'bound',str(tail))

if __name__=='__main__':
    for a in [(1,), (0,1), (0,0,1), (1,1)]:
        check(2,11,2,a)
    print('VERIFY_OK')
