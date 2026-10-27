"""Independent finite checks of periodic forbidden-pair entropy classifications.

Uses exact integer arithmetic for all transfer products and orbit counts.
Finite enumeration corroborates, but does not replace, the all-period proof.
"""
from itertools import product
from math import sqrt

WORDS = ('00', '01', '10', '11')
IDENTITY = (1, 0, 0, 1)
L = (1, 0, 1, 1)
F = (0, 1, 1, 1)

def matmul(a, b):
    return (a[0]*b[0]+a[1]*b[2],
            a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2],
            a[2]*b[1]+a[3]*b[3])

def trace(a):
    return a[0]+a[3]

def det(a):
    return a[0]*a[3]-a[1]*a[2]

def spectral(a):
    t, d = trace(a), det(a)
    return (t+sqrt(t*t-4*d))/2

def transfer(w):
    return tuple(int(str(i)+str(j) != w) for i in range(2) for j in range(2))

def monodromy(mats):
    m=IDENTITY
    for a in mats:
        m=matmul(m, a)
    return m

def direct_survivors(ws, n):
    return sum(all(''.join(bits[j:j+2]) != ws[j % len(ws)] for j in range(n))
               for bits in product('01', repeat=n+1))

def periodic_points(ws, m):
    p=len(ws)
    return sum(all((bits[j % (p*m)]+bits[(j+1) % (p*m)]) != ws[j % p]
                   for j in range(p*m))
               for bits in product('01', repeat=p*m))

schedules=0
for p in range(1, 8):
    counts=[0]*(p+1)
    minimum_positive=1e100
    for ws in product(WORDS, repeat=p):
        mon=monodromy(transfer(w) for w in ws)
        a=[int(w[0]) for w in ws]
        defects=sum(int(int(ws[i][1]) == a[(i+1)%p]) for i in range(p))
        gauges=[F if int(ws[i][1]) == a[(i+1)%p] else L for i in range(p)]
        gm=monodromy(gauges)
        # Entrywise conjugation by the initial-bit swap.
        swap=(0,1,1,0)
        transformed=matmul(matmul(swap,mon),swap) if a[0] else mon
        assert transformed==gm, (ws, transformed, gm)
        assert abs(det(mon))==1
        assert det(gm)==(-1)**defects
        counts[defects]+=1
        if defects==0:
            assert gm==(1,0,p,1) and trace(mon)==2 and det(mon)==1
        elif defects==1:
            assert trace(mon)==p and det(mon)==-1
        else:
            assert spectral(mon)>(p+sqrt(p*p+4))/2+1e-10
        if defects:
            minimum_positive=min(minimum_positive,spectral(mon))
        if p<=3:
            for n in range(0,9):
                x=(1,1)
                for i in range(n):
                    m=transfer(ws[i % p])
                    x=(x[0]*m[0]+x[1]*m[2], x[0]*m[1]+x[1]*m[3])
                assert sum(x)==direct_survivors(ws,n), (ws,n)
                if defects==0:
                    assert sum(x)==n+2
            for m in range(1,4):
                if p*m<=10:
                    pp=periodic_points(ws,m)
                    mm=IDENTITY
                    for _ in range(m):mm=matmul(mm,mon)
                    assert pp==trace(mm), (ws,m,pp,trace(mm))
        schedules+=1
    assert counts==[2**p*__import__('math').comb(p,k) for k in range(p+1)]
    assert abs(minimum_positive-(p+sqrt(p*p+4))/2)<1e-10
    print('PERIOD',p,'SCHEDULES',4**p,'DEFECT_COUNTS',counts,'MIN_ROOT',round(minimum_positive,12))
print('VERIFY_OK exact matrices and periodic-point counts; total schedules',schedules)
