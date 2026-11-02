"""Exact rational and modular checks for the dyadic iterated-harmonic theorem.
No external packages. Finite checks accompany the general proof.
"""
from fractions import Fraction

MOD = 256
N = 512
H = [Fraction(0)] * (N+1)
for k in range(1, N+1):
    H[k] = H[k-1]+Fraction(1,k)

def v2(n):
    if n == 0: return 10**9
    n = abs(n)
    return (n & -n).bit_length()-1

def residue(q,mod):
    v=v2(q.numerator)-v2(q.denominator)
    assert v>=0
    num=q.numerator >> v2(q.numerator)
    den=q.denominator >> v2(q.denominator)
    return (num*pow(den,-1,mod)*(2**v))%mod

P=[0]*(N+1)
for k in range(1,N+1):
    term=Fraction(1,k)/H[k]
    assert v2(term.numerator)-v2(term.denominator) == (k.bit_length()-1)-v2(k)
    P[k]=(P[k-1]+residue(term,512))%512
    assert P[k]%2 == ((k.bit_length())%2)

observed={3:94,4:207,5:64,6:177,7:34,8:147}
for r,v in observed.items():
    assert P[2**r]%MOD==v,(r,P[2**r]%MOD,v)
    assert P[2**r]%MOD==(113*r+11)%MOD
for r in range(1,9):
    d=(P[2**r]-P[2**(r-1)])%512
    if r>=4: assert d%MOD==113
for r in range(1,8):
    d1=(P[2**r]-P[2**(r-1)])%512
    d2=(P[2**(r+1)]-P[2**r])%512
    assert (d2-d1)%(2**r)==0,r

checks=0
for a in [1,3,5,7,9,11,13,15,17,19,21,23,25,31]:
    ell=a.bit_length()-1
    for t in range(0,5):
        n=a*2**t
        if 2*n>N: continue
        Wt=2**(ell+t)*H[n]
        Wnext=2**(ell+t+1)*H[2*n]
        assert v2(Wt.numerator)-v2(Wt.denominator)==0
        assert v2(Wnext.numerator)-v2(Wnext.denominator)==0
        diff=Wnext-Wt
        assert v2(diff.numerator)-v2(diff.denominator)>=ell+t+1
        qt=Fraction(1,n)/H[n]
        qnext=Fraction(1,2*n)/H[2*n]
        gap=qnext-qt
        assert v2(gap.numerator)-v2(gap.denominator)>=2*ell+t+1
        checks+=1
print('VERIFY_OK: modular second-iterate residues for 512 indices; exact six dyadic bases; '+str(checks)+' normalized-harmonic lifting inequalities')
