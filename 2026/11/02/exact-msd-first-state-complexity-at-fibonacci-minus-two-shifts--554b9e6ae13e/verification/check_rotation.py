"""Independent decimal-rotation cross-check; finite only, not an infinite proof.
Uses Python standard-library arbitrary-precision Decimal arithmetic.
"""
from decimal import Decimal, localcontext, ROUND_FLOOR
F=[0,1]
for _ in range(320):F.append(F[-1]+F[-2])
def zrep(n):
    r=[]
    for i in range(len(F)-1,1,-1):
        if F[i]<=n:r.append(i);n-=F[i]
    assert n==0
    return r
def after(n,j):return sum(F[i+j] for i in zrep(n))
with localcontext() as ctx:
    ctx.prec=150
    phi=(Decimal(1)+Decimal(5).sqrt())/2
    gamma=phi**(-2)
    def rotbit(n):
        x=Decimal(n)*phi
        theta=x-x.to_integral_value(rounding=ROUND_FLOOR)
        return int(gamma<theta<2*gamma)
    for k in range(5,71):
        c=F[k]-2
        qs=4 if k&1 else 6
        for j in range(k+5):
            a=rotbit(c+after(F[2],j));b=rotbit(c+after(qs,j))
            assert (a!=b if j==0 else a==b),(k,j,a,b)
        for i in range(2,k):
            wrong=[j for j in range(k+5) if rotbit(c+F[i+j]) != int(k%2==0)]
            assert wrong and wrong[-1]==k-1-i,(k,i,wrong)
        assert rotbit(c)==int(k%2==0)
print('PASS 150-digit stdlib Decimal rotation cross-check k=5..70')
