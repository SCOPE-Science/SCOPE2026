"""Exact finite-size checks for the joint crossing/short-span theorem."""
from fractions import Fraction as F
from math import comb, factorial

def matchings(labels):
    if not labels:
        yield ()
        return
    first = labels[0]
    for j in range(1, len(labels)):
        second = labels[j]
        rest = labels[1:j] + labels[j+1:]
        for tail in matchings(rest):
            yield ((first, second),) + tail

def crossing(a,b):
    x,y = a
    u,v = b
    return (x < u < y < v) or (u < x < v < y)

def moments(n):
    N=2*n
    count=sx=st=sxx=stt=sxt=0
    for m in matchings(tuple(range(1,N+1))):
        x=sum(crossing(a,b) for i,a in enumerate(m) for b in m[i+1:])
        t=sum(min(v-u,N-(v-u))-1 for u,v in m)
        count+=1; sx+=x; st+=t; sxx+=x*x; stt+=t*t; sxt+=x*t
    ex=F(sx,count); et=F(st,count)
    vx=F(sxx,count)-ex**2; vt=F(stt,count)-et**2; cv=F(sxt,count)-ex*et
    return count,ex,et,vx,vt,cv

def formulas(n):
    return (F(n*(n-1),6),
            F(n*(n-1)**2,2*n-1),
            F(n*(n-1)*(n+3),45),
            F(2*n*n*(n-1)**2*(n*n-n+1),3*(2*n-3)*(2*n-1)**2),
            F(n**3*(n-1)**2,6*(2*n-3)*(2*n-1)))

def check():
    checks=0
    for n in range(2,8):
        num,*observed=moments(n)
        expected=formulas(n)
        for got,want in zip(observed,expected):
            assert got==want,(n,got,want)
            checks+=1
        print(f'n={n}: {num} matchings; moments verified')
    for n in range(2,301):
        ex,et,vx,vt,cv=formulas(n)
        assert ex>0
        assert et>=0
        assert vx>0
        assert vt>0
        assert cv>0
        assert cv*cv<=vx*vt
        assert cv*cv/(vx*vt)==F(15*n**3*(n-1),8*(n+3)*(2*n-3)*(n*n-n+1))
        assert cv/vt==F(n*(2*n-1),4*(n*n-n+1))
        checks+=8
    for n in range(2,151):
        N=2*n
        p=F(1,N-1); q=F(1,(N-1)*(N-3))
        s1=n**3; s2=F(n*n*(2*n*n+1),3); rows_sq=2*n**5
        v=(p+q)*s2-q*rows_sq+(q-p*p)*s1*s1
        assert v==formulas(n)[3]
        # conditional expected crossing given a chord with shorter distance h
        for h in range(1,n+1):
            cond=F((n-1)*(n-2),6)+F((h-1)*(2*n-h-1),2*n-3)
            assert cond>=0
            checks+=1
        checks+=1
    print('Verified exact assertions:',checks)

if __name__=='__main__':
    check()
