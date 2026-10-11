"""Exact finite-field convolution cross-checks for the inverse-graph fourth moment.
Standalone Python 3 standard-library checker; finite tests supplement a general proof.
"""
from collections import defaultdict
from random import Random

POLY={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011}

def mul(a,b,m):
    p=POLY[m]
    z=0
    while b:
        if b&1: z^=a
        b>>=1
        a<<=1
        if a&(1<<m): a^=p
    return z

def power(a,k,m):
    y=1
    while k:
        if k&1:y=mul(y,a,m)
        a=mul(a,a,m)
        k//=2
    return y

def gadd(z,w):return(z[0]+w[0],z[1]+w[1])
def gmul(z,w):return(z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def gconj(z):return(z[0],-z[1])
def abs2(z):return z[0]*z[0]+z[1]*z[1]

def direct_energy(f,iv):
    fibers=defaultdict(lambda:(0,0))
    q=len(f)
    for x in range(q):
        for y in range(q):
            s=(x^y,iv[x]^iv[y])
            fibers[s]=gadd(fibers[s],gmul(f[x],f[y]))
    return sum(abs2(c) for c in fibers.values())

def formula_energy(f,iv,m):
    q=len(f); N=sum(abs2(c) for c in f)
    diag=(0,0)
    for z in f:diag=gadd(diag,gmul(z,z))
    out=abs2(diag)+2*N*N-2*sum(abs2(z)**2 for z in f)
    if m%2==0:
        omega=next(x for x in range(2,q) if mul(x,x,m)^x^1==0)
        for s in range(1,q):
            b=gmul(f[0],f[s]);c=gmul(f[mul(omega,s,m)],f[mul(mul(omega,omega,m),s,m)])
            out+=8*gmul(b,gconj(c))[0]
    return out

def check_fibers(m,iv):
    q=1<<m; cnt=defaultdict(list)
    for x in range(q):
        for y in range(x+1,q):
            cnt[x^y,iv[x]^iv[y]].append((x,y))
    k4=0
    for key,preimages in cnt.items():
        assert len(preimages) in (1,2), (m,key,preimages)
        if len(preimages)==2:
            k4+=1
            assert m%2==0
            s,t=key
            assert s!=0 and mul(s,t,m)==1
            assert (0,s) in preimages
    assert k4 == ((q-1) if m%2==0 else 0),(m,k4)

rng=Random(20261009)
tests=0
for m in POLY:
    q=1<<m
    iv=[0]+[power(x,q-2,m) for x in range(1,q)]
    assert all(mul(x,iv[x],m)==1 for x in range(1,q))
    check_fibers(m,iv)
    for trial in range(9):
        f=[(rng.randint(-2,2),rng.randint(-2,2)) for _ in range(q)]
        E=direct_energy(f,iv)
        assert E==formula_energy(f,iv,m),(m,trial,E,formula_energy(f,iv,m))
        N=sum(abs2(z) for z in f)
        if m%2:assert q*E <= (3*q-2)*N*N
        else:assert E<=4*N*N
        tests+=1
    if m%2:
        f=[(1 if rng.getrandbits(1) else -1,0) for _ in range(q)]
        N=q;E=direct_energy(f,iv)
        assert q*E==(3*q-2)*N*N
    else:
        omega=next(x for x in range(2,q) if mul(x,x,m)^x^1==0)
        for a in (1,2):
            supp={0,a,mul(a,omega,m),mul(a,mul(omega,omega,m),m)}
            assert len(supp)==4
            f=[(1 if t in supp else 0,0) for t in range(q)]
            N=4
            assert direct_energy(f,iv)==4*N*N
            bad=[(1,0) if t in supp else (0,0) for t in range(q)]
            bad[a]=(-1,0)
            assert direct_energy(bad,iv)<4*N*N
print('VERIFY_OK fields=F2,F4,F8,F16,F32,F64 exact_weighted_fibers=%d normalized_sharp_packets=PASS equality_phase_boundary=PASS'%tests)
