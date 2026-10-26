"""Exact finite certificate for the first nonsquarefree multiplicity layer of sigma(n)=2*phi(n)."""
from fractions import Fraction as F
from math import isqrt

def prime(n):
    if n<2:return False
    for d in range(2,isqrt(n)+1):
        if n%d==0:return False
    return True

def next_prime(n):
    p=n+1
    while not prime(p):p+=1
    return p

def f(p):return F(p+1,p-1)
def g(p):return F(p*p+p+1,p*(p-1))

# When the squared prime is among the first three, the last prime is forced.
# If the squared prime is the largest, reduction modulo it excludes equality.
assert g(11)*f(13)*f(17)*f(19)==F(931,528)<2
assert g(7)*f(13)*f(17)*f(19)==F(95,48)<2
assert g(5)*f(23)*f(29)*f(31)==F(744,385)<2
assert f(5)*f(7)==2
pairs=((5,11),(5,13),(5,17),(5,19),(7,11))
expected_stops={
  (5,11):(53,F(7533,3770)),
  (5,13):(41,F(2387,1200)),
  (5,17):(29,F(279,140)),
  (5,19):(29,F(124,63)),
  (7,11):(19,F(152,77)),
}
expected_integral_candidates={
  (5,11,29,0,559),
  (5,11,31,0,249),
  (5,13,29,0,63),
  (5,17,19,0,63),
  (5,19,23,0,32),
  (7,11,13,0,39),
}
found=set()
counts={}
for p,q in pairs:
    r=next_prime(q)
    tested=0
    while True:
        upper=g(p)*f(q)*f(r)*f(next_prime(r))
        if upper<2:
            assert (r,upper)==expected_stops[(p,q)]
            break
        tested+=1
        for idx,t in enumerate((p,q,r)):
            ratio=F(1)
            for j,v in enumerate((p,q,r)):
                ratio*=g(v) if j==idx else f(v)
            if ratio>=2:continue
            s=(2+ratio)/(2-ratio)
            if s>r and s.denominator==1:
                found.add((p,q,r,idx,int(s)))
        r=next_prime(r)
    counts[(p,q)]=tested
assert found==expected_integral_candidates,(found,expected_integral_candidates)
assert all(not prime(s) for *_,s in found)

# Directly evaluate sigma and phi on each integer in a full finite interval.
N=300000
spf=list(range(N+1))
for p in range(2,isqrt(N)+1):
    if spf[p]!=p:continue
    for m in range(p*p,N+1,p):
        if spf[m]==m:spf[m]=p
checks=0
for n in range(2,N+1):
    x=n; fac=[]
    while x>1:
        p=spf[x];e=0
        while x%p==0:x//=p;e+=1
        fac.append((p,e))
    if len(fac)!=4 or sum(e for _,e in fac)!=5:continue
    checks+=1
    sig=1;phi=1
    for p,e in fac:
        sig*=(p**(e+1)-1)//(p-1)
        phi*=p**(e-1)*(p-1)
    assert sig!=2*phi,n

# The boundary is sharp: exactly four prime supports, with six factors total.
n=7**3*11*13*41
assert n==2011009
sig=(1+7+7**2+7**3)*(1+11)*(1+13)*(1+41)
phi=7**2*(7-1)*(11-1)*(13-1)*(41-1)
assert sig==2*phi
print('VERIFY_OK', 'prime-pair branches',len(pairs), 'third-prime cases',sum(counts.values()),
      'integral forced last candidates',len(found), 'all composite', 'direct cases',checks,
      'direct bound',N,'sharp witness',n)
print('PAIR_CASE_COUNTS',counts)
print('INTEGER_LAST_CANDIDATES',sorted(found))
