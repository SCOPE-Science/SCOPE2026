"""Exact-rational checks of the transient clock of a max-plus feedback map."""
from fractions import Fraction as Q


def F(x, y, m, B):
    return (y, B-max(Q(0),m*x))


def next_return(x,m,B):
    """Next return to x>0,y=B, or terminal hit to (B,B)."""
    a,b=x,B
    for k in range(1,7):
        a,b=F(a,b,m,B)
        if b==B and a>0:
            return k,a
        if (a,b)==(B,B):
            return k,B
    raise AssertionError((x,m,B))


def predictor(x,m,B):
    left=(m-1)*B/m**2
    right=B/m
    if x<=left: return 5,B
    if x<right: return 4,m*m*x+(1-m)*B
    return 4,B


def capture(x,m,B):
    """Physical time to first (B,B), excluding initial time."""
    a,b=x,B
    for k in range(1,3000):
        a,b=F(a,b,m,B)
        if a==B and b==B:
            return k
    return None


def predicted_clock(x,m,B):
    c=B/(m+1)
    if x==c: return None
    n=1
    while True:
        ln=c-B/(m**(2*n)*(m+1))
        rn=c+B/(m**(2*n-1)*(m+1))
        if not ln<x<rn: break
        n+=1
    # If after n-1 mid excursions x on the branch boundary, take exact iterates.
    z=c+m**(2*(n-1))*(x-c)
    return 4*n+(int(z<=(m-1)*B/m**2))


def check():
    trials=0
    for m in [Q(11,10),Q(5,4),Q(3,2),Q(2),Q(3),Q(5)]:
      for B in [Q(1),Q(2),Q(7,3)]:
        c=B/(m+1)
        left=(m-1)*B/(m*m)
        right=B/m
        for x in [left,right,c,B,Q(0),left/2,(left+c)/2,(c+right)/2,(right+B)/2]:
            if 0<x<=B:
                assert next_return(x,m,B)==predictor(x,m,B)
                trials+=1
        for j in range(1,118):
            x=B*Q(j,117)
            if x==c: continue
            assert next_return(x,m,B)==predictor(x,m,B)
            actual=capture(x,m,B)
            calc=predicted_clock(x,m,B)
            assert actual==calc,(m,B,j,actual,calc)
            trials+=2
        for n in range(0,12):
            ln=c-B/(m**(2*n)*(m+1))
            rn=c+B/(m**(2*n-1)*(m+1))
            assert rn-ln==B/m**(2*n)
            assert (rn-c)/(c-ln)==m
            if n:
                mid_l=c-B/(m**(2*(n-1))*(m+1))
                mid_r=c+B/(m**(2*(n-1)-1)*(m+1))
                assert mid_l<ln<c<rn<mid_r
            trials+=4
        # Verify geometric factor and terminal Bernoulli probabilities by exact interval lengths.
        for n in range(1,13):
            L=B/(m+1)*(m**(-2*(n-1))-m**(-2*n))
            R=B*m/(m+1)*(m**(-2*(n-1))-m**(-2*n))
            tot=B*(1-m**(-2))*m**(-2*(n-1))
            assert L+R==tot
            assert (L/tot)==1/(m+1)
            assert (R/tot)==m/(m+1)
            trials+=3
    print('PASS',trials,'exact-rational return, physical-time, survivor and probability checks')

if __name__=='__main__': check()
