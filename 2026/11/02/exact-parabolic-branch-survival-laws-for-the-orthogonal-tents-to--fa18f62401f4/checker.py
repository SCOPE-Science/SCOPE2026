"""Exact rational grid checks for orthogonal tent-shear survival formulas.
All arithmetic is integer; boundaries are omitted from pointwise comparisons.
This finite checker is supporting evidence, not proof for every survival time.
"""
from fractions import Fraction as Q


def direct_survives(i, j, den, n):
    x, y = i, j
    for _ in range(n):
        fx=(x+2*(y if 2*y<den else den-y))%den
        if not(2*y>den and 0<2*fx<den):
            return False
        y=(y+2*(fx if 2*fx<den else den-fx))%den
        x=fx
    return True


def analytic_survives(i,j,den,n):
    y=Q(j,den); t=Q((i-j)%den,den)
    if not(0<t<1):return False
    s=min(t,1-t)
    if t<Q(1,2):
        if n==1: return Q(1,2)+s<y<1
        k=n//2
        if s<=Q(1,4):
            lo=Q(1,2)+s
            hi=(Q(1,2)+2*s-(k-1)*(1-4*s)) if n%2==0 else (1-k*(1-4*s))
        else:
            lo=3*s+(k-1)*(4*s-1) if n%2==0 else Q(1,2)+s+k*(4*s-1)
            hi=Q(1)
    else:
        if n==1: return Q(1,2)<y<1-s
        k=n//2
        if s<=Q(1,4):
            lo=(1-2*s+(k-1)*(1-4*s)) if n%2==0 else (Q(1,2)+k*(1-4*s))
            hi=1-s
        else:
            lo=Q(1,2)
            hi=(Q(3,2)-3*s-(k-1)*(4*s-1)) if n%2==0 else (1-s-k*(4*s-1))
    return lo<y<hi


def area(n):
    if n==1:return Q(1,4)
    k=n//2
    if n%2==0:return Q(2*k-1,4*(4*k-1)*(4*k-3))
    return Q(k,2*(16*k*k-1))


def main():
    checks=0
    for den in (53,97,131):
        for i in range(1,den):
            for j in range(1,den):
                if (i-j)%den==0: continue
                for n in range(1,14):
                    assert direct_survives(i,j,den,n)==analytic_survives(i,j,den,n),(den,i,j,n)
                    checks+=1
    assert [area(n) for n in range(1,7)]==[Q(1,4),Q(1,12),Q(1,30),Q(3,140),Q(1,63),Q(5,396)]
    for k in range(1,100):
        # independently integrate triangular cross sections, as derived from their breakpoints
        a=Q(k-1,4*k-3); b=Q(k,4*k-1)
        assert area(2*k)==Q(1,4)*(b-a)
        a=Q(2*k-1,2*(4*k-1)); b=Q(2*k+1,2*(4*k+1))
        assert area(2*k+1)==Q(1,4)*(b-a)
    print('PASS: %s pointwise original-map vs exact-section tests; 198 area identities.' % checks)

if __name__=='__main__':main()
