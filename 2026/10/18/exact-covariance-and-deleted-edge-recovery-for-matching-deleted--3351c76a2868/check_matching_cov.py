"""Independent exact lattice-sum verifier for covariance of deleted-matching metrics.
Anchored Ehrhart weighted-moment interpolation; no use of extrema disintegration.
"""
from fractions import Fraction
from itertools import product
from math import comb, factorial


def matched(i,j,m):
    return i<2*m and j<2*m and i//2==j//2

def lattice_sums(n,m,t):
    if t==0: return (1,0,0,0,0)
    out=[i for i in range(2,n)]
    ct=ww=pp=uu=cc=0
    for a in product(range(-t,t+1),repeat=n-2):
        # All other vertices are graph-neighbors of anchor 0.
        if any(abs(a[i]-a[j])>t for i in range(n-2) for j in range(i+1,n-2) if not matched(i+2,j+2,m)):
            continue
        lo=max(-2*t,max(a)-t)
        hi=min(2*t,min(a)+t)
        if lo>hi:continue
        num=hi-lo+1
        sy=num*(lo+hi)//2
        sy2=(hi*(hi+1)*(2*hi+1)-(lo-1)*lo*(2*lo-1))//6
        ct+=num
        ww+=sy2
        if m>=2:
            z=a[0]+a[1]
            pp+=sy2-2*z*sy+z*z*num
        if n-2*m>=2:
            w=a[2*m-2]-a[2*m-1]
            uu+=w*w*num
        if n-2*m>=1:
            s=n-2*m
            d=s*sum(a[:2*m-2])-2*m*sum(a[2*m-2:])
            cc+=s*s*sy2+2*s*d*sy+d*d*num
    return ct,ww,pp,uu,cc

def lead(vals,deg):
    return Fraction(sum((-1)**(deg-i)*comb(deg,i)*vals[i] for i in range(deg+1)), factorial(deg))

def predicted(n,m):
    s=n-2*m
    T=n*(n-1)+2*m
    A=Fraction((n-1)*(n*n+3*n+2*m+2),12*(n+1)*T)
    B=Fraction(n*n+3*n+4,n*(n+1)*T)
    C=Fraction(n-1,6*(n+1)*T)
    return Fraction(T,n-1), (A+B-C), (A-C if m>=2 else None), (A if s>=2 else None), (A-C*Fraction(s,n) if s>=1 else None)

def main():
    count=0
    for n in (3,4,5,6):
        for m in range(1,n//2+1):
            pts=[lattice_sums(n,m,t) for t in range(n+2)]
            v=lead([x[0] for x in pts],n-1)
            integ=[lead([x[i] for x in pts],n+1) for i in range(1,5)]
            s=n-2*m
            actual=(v, integ[0]/(2*v), integ[1]/(4*v) if m>=2 else None,
                    integ[2]/(2*v) if s>=2 else None,
                    integ[3]/(2*m*s*n*v) if s>=1 else None)
            theory=predicted(n,m)
            assert actual==theory,(n,m,actual,theory)
            print('PASS n=%d m=%d; volume=%s; lambda=[%s,%s,%s,%s]; lattice_tmax=%d pts_tmax=%d'%(n,m,*[str(x) for x in actual],n+1,pts[-1][0]))
            count+=1
    print(f'PASS {count} distinct graph configurations; rational weighted Ehrhart moments')
if __name__=='__main__':main()
