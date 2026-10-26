"""Standalone finite-field checks for cotangent images of log-canonical Poisson automorphisms.
Run with Python 3; no third-party dependencies.
"""
from itertools import product


def operations(q):
    if q != 4:
        return lambda a,b:(a+b)%q, lambda a,b:(a*b)%q
    # F_4=F_2[t]/(t^2+t+1); bit polynomial representation.
    def mul(a,b):
        z=0
        for bit in range(2):
            if (b >> bit)&1: z ^= a<<bit
        if z&4: z ^= 0b111  # t^2 = t+1
        return z
    return lambda a,b:a^b, mul


def vec_ops(m,q):
    add,mul=operations(q)
    e=1<<m
    zero=(0,)*e
    def plus(u,v):return tuple(add(a,b) for a,b in zip(u,v))
    def times(u,v,bracket=False):
        out=[0]*e
        for a,ca in enumerate(u):
            if not ca: continue
            for b,cb in enumerate(v):
                if not cb or (a&b): continue
                v0=mul(ca,cb)
                if bracket:
                    k=0
                    for i in range(m):
                        if not ((a>>i)&1):continue
                        for j in range(m):
                            if not ((b>>j)&1) or i==j:continue
                            k += (1 if i<j else -1)
                    if not k: continue
                    v0=mul(v0,k%q if q!=4 else (k&1))
                out[a|b]=add(out[a|b],v0)
        return tuple(out)
    def x(i):
        y=list(zero);y[1<<i]=1;return tuple(y)
    return add,mul,zero,plus,times,x


def det_nonzero2(M,q):
    a,mul=operations(q)
    return a(mul(M[0][0],M[1][1]),mul(M[0][1],M[1][0]) if q in (2,4) else -mul(M[0][1],M[1][0]))!=0


def det_nonzero3(M,q):
    a,mul=operations(q)
    # general elimination mod finite-field arithmetic
    T=[list(row) for row in M]
    for col in range(3):
        k=next((r for r in range(col,3) if T[r][col]),None)
        if k is None: return False
        T[col],T[k]=T[k],T[col]
        for r in range(col+1,3):
            if T[r][col]==0:continue
            for t in range(col+1,3):
                val=mul(T[r][t],T[col][col]);b=mul(T[col][t],T[r][col])
                T[r][t]=a(val, b if q in (2,4) else -b)
            T[r][col]=0
    return True


def test_m2(q):
    add,mul,zero,plus,times,x=vec_ops(2,q)
    candidates=[]
    for c in product(range(q), repeat=3):
        u=list(zero)
        for i,mask in enumerate((1,2,3)):u[mask]=c[i]
        candidates.append((tuple(u),c))
    count=0
    jets={}
    for U,a in candidates:
        if times(U,U)!=zero:continue
        for V,b in candidates:
            if not det_nonzero2([a[:2],b[:2]],q):continue
            if times(V,V)!=zero:continue
            if times(U,V,True)!=times(U,V):continue
            count+=1
            key=(a[0],a[1],b[0],b[1]);jets[key]=jets.get(key,0)+1
    linear=(q*q-1)*(q*q-q) if q%2==0 else (q-1)**2
    expected=q*q*linear
    assert count==expected,(q,count,expected)
    assert len(jets)==linear and set(jets.values())=={q*q},(q,len(jets))
    return count,len(jets)


def test_m3(q):
    assert q in (2,3)
    _,_,zero,plus,times,x=vec_ops(3,q)
    accepted=0;invertible=0
    for flat in product(range(q), repeat=9):
        M=[flat[i*3:(i+1)*3] for i in range(3)]
        if not det_nonzero3(M,q):continue
        invertible+=1
        imgs=[]
        for row in M:
            Z=list(zero)
            for j,c in enumerate(row): Z[1<<j]=c
            imgs.append(tuple(Z))
        if any(times(v,v)!=zero for v in imgs):continue
        if any(times(imgs[i],imgs[j],True)!=times(imgs[i],imgs[j]) for i in range(3) for j in range(i+1,3)):continue
        accepted+=1
    expected=168 if q==2 else (q-1)**3
    assert accepted==expected,(q,accepted,expected)
    return accepted,invertible

if __name__=='__main__':
    for q in (2,3,4,5):
        a,b=test_m2(q)
        print('m=2,q=%d: full_Poisson_automorphisms=%d, first_jets=%d'%(q,a,b))
    for q in (2,3):
        a,b=test_m3(q)
        print('m=3,q=%d: admissible_linear_jets=%d, tested_GL3_matrices=%d'%(q,a,b))
    print('LOGCANONICAL_POISSON_JET_OK')
