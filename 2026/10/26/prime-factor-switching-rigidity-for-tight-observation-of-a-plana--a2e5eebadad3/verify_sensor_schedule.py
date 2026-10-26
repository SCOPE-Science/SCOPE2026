"""Exact finite-instance checks for a rotating two-sensor information model.

No external dependencies. Finite enumeration is corroboration, not a proof of the all-size theorem.
"""
from math import gcd, pi, cos, sin

def trim(a):
    a = list(a)
    while len(a)>1 and a[-1]==0:
        a.pop()
    return a

def div_monic(num,den):
    num=trim(num); den=trim(den)
    q=[0]*max(1,len(num)-len(den)+1)
    r=num[:]
    while len(r)>=len(den) and any(r):
        d=len(r)-len(den)
        c=r[-1]
        q[d]=c
        for j,v in enumerate(den):
            r[j+d]-=c*v
        r=trim(r)
    return trim(q),r

def cyclotomic(m):
    C={}
    for n in range(1,m+1):
        if m%n: continue
        a=[-1]+[0]*(n-1)+[1]
        for d in sorted(C):
            if n%d==0:
                a,rem=div_monic(a,C[d]); assert rem==[0]
        C[n]=a
    return C[m]

def vanish(a,phi):
    return div_monic(a,phi)[1]==[0]

def smallest_odd(n):
    for p in range(3,n+1,2):
        if n%p==0 and all(p%d for d in range(2,int(p**.5)+1)):
            return p
    return None

cnt=0
for n in range(2,17):
    phi=cyclotomic(2*n)
    p=smallest_odd(n)
    expected=(p-1 if p else None)
    optimal=[]; zeros=[]
    for bits in range(1<<(n-1)):
        seq=[1]+[1 if (bits>>(j-1))&1 else -1 for j in range(1,n)]
        k=sum(seq[j]!=seq[j-1] for j in range(1,n))
        v=vanish(seq,phi)
        if v:
            zeros.append(tuple(seq))
            if expected is None or k < expected:
                raise AssertionError((n,'unexpected zero',seq,k))
            if k == expected:
                optimal.append(tuple(seq))
        cnt+=1
    if expected is None:
        assert not zeros
    else:
        b=n//p
        construction=tuple((-1)**(j//b) for j in range(n))
        assert optimal==[construction],(n,optimal,construction)
        assert vanish(construction,phi)
        odd=n
        while odd%2==0:odd//=2
        while odd%p==0:odd//=p
        if odd==1:
            b=n//p
            family={tuple(((-1)**(j//b))*base[j%b] for j in range(n)) for base in __import__('itertools').product((-1,1),repeat=b) if base[0]==1}
            assert set(zeros)==family,(n,len(zeros),len(family))
print('EXACT_CYCLOTOMIC_OK n=2..16 schedules=',cnt)
for n in (3,6,9,10,12,15,18,20,21,25,27,30,33,35,36,42,50,75):
    p=smallest_odd(n); b=n//p
    sign=[(-1)**(j//b) for j in range(n)]
    assert vanish(sign,cyclotomic(2*n)),n
print('CONSTRUCTIVE_CYCLOTOMIC_OK additional n=18..75')
for n in (3,4,5,6,7,8,9,10,12,15,16,24,27,32,45):
    th=pi/(2*n)
    seq=[1]*n if smallest_odd(n) is None else [(-1)**(j//(n//smallest_odd(n))) for j in range(n)]
    wc=sum(s*cos(j*pi/n) for j,s in enumerate(seq))
    ws=sum(s*sin(j*pi/n) for j,s in enumerate(seq))
    a=(n+wc)/2;d=(n-wc)/2;off=ws/2
    eig=(n+(wc*wc+ws*ws)**.5)/2,(n-(wc*wc+ws*ws)**.5)/2
    assert abs(a+d-n)<1e-9 and abs(a*d-off*off-eig[0]*eig[1])<1e-7
    if smallest_odd(n):assert abs(wc)<1e-8 and abs(ws)<1e-8
print('GRAM_SPECTRUM_OK exact finite model; floating angular cross-check')
