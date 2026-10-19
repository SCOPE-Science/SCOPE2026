"""Independent exact arithmetic checks for the exterior-algebra multiplication Jordan spectrum."""
import collections,itertools,random,sys

MASKS=list(range(16))
DEG=[i.bit_count() for i in MASKS]
D1=[m for m in MASKS if DEG[m]==1]
D2=[m for m in MASKS if DEG[m]==2]
D3=[m for m in MASKS if DEG[m]==3]
D4=[15]

def signed_union(i,j,p):
    if i&j: return None
    inversions=sum(((i>>(k+1)).bit_count()) for k in range(4) if (j>>k)&1)
    return (i|j, (p-1 if inversions%2 else 1))

def mul(a,b,p):
    z=[0]*16
    for i,x in enumerate(a):
        if not x: continue
        for j,y in enumerate(b):
            if not y: continue
            pair=signed_union(i,j,p)
            if pair:
                k,s=pair
                z[k]=(z[k]+x*y*s)%p
    return z

def rank(rows,p):
    M=[list(r) for r in rows]
    r=0
    for c in range(len(M[0]) if M else 0):
        piv=next((i for i in range(r,len(M)) if M[i][c]%p),None)
        if piv is None:continue
        M[r],M[piv]=M[piv],M[r]
        inv=pow(M[r][c],-1,p)
        M[r]=[(v*inv)%p for v in M[r]]
        for i in range(r+1,len(M)):
            if M[i][c]:
                fac=M[i][c]
                M[i]=[(u-fac*v)%p for u,v in zip(M[i],M[r])]
        r+=1
    return r

def actual(a,p):
    cols=[]
    for j in MASKS:
        x=[0]*16;x[j]=1
        cols.append(mul(a,x,p))
    r1=rank(cols,p)
    a2=mul(a,a,p)
    cols2=[]
    for j in MASKS:
        x=[0]*16;x[j]=1
        cols2.append(mul(a2,x,p))
    r2=rank(cols2,p)
    return (r1,r2)

def predict(a,p):
    ell=tuple(a[i] for i in D1)
    omega=[0]*16
    for i in D2:omega[i]=a[i]
    if any(ell):
        if p==2:return (8,0)
        lin=[0]*16
        for j,i in enumerate(D1):lin[i]=ell[j]
        prod=mul(lin,omega,p)
        return (8,2 if any(prod) else 0)
    if any(omega):
        # The two-form has exterior rank four iff its Plucker pfaffian is nonzero.
        u=[a[i] for i in D2]
        pf=(u[0]*u[5]-u[1]*u[4]+u[2]*u[3])%p
        return (6,0 if p==2 else 1) if pf else (4,0)
    if any(a[i] for i in D3):return (2,0)
    if a[15]:return (1,0)
    return (0,0)

def signature(r1,r2):
    b3=r2; b2=r1-2*r2; b1=16-2*r1+r2
    assert min(b1,b2,b3)>=0
    return (b3,b2,b1)

def theoretical_counts(q):
    nondeg=q*q*(q-1)*(q**3-1)
    decomp=(q*q+1)*(q**3-1)
    d={(8,0):(q**4-1)*q**8,
       (8,2):(q**4-1)*(q**6-q**3)*q**5,
       (6,1):nondeg*q**5,
       (4,0):decomp*q**5,
       (2,0):(q**4-1)*q,
       (1,0):q-1,
       (0,0):1}
    if q%2==0:
        d.pop((8,2));d[(8,0)]=(q**4-1)*q**11
        d.pop((6,1));d[(6,0)]=nondeg*q**5
    assert sum(d.values())==q**15
    return d

def run():
    for p in (2,3,5,7):
        theoretical_counts(p)
        for i in range(8000 if p==2 else 1500):
            a=[0]*16
            for j in range(1,16):a[j]=random.randrange(p)
            got=actual(a,p); want=predict(a,p)
            assert got==want,(p,a,got,want)
        print('RANDOM_OK',p)
    # All 2^15 radicals, checking nontrivial wedge-model against predictions.
    # The exact histograms are from independent multiplication ranks on a full random
    # sample, and complete Pfaffian/linear-stratum census for all binary vectors.
    hist=collections.Counter()
    for mask in range(1<<15):
        a=[0]+[(mask>>(i-1))&1 for i in range(1,16)]
        hist[predict(a,2)]+=1
    assert hist==theoretical_counts(2),(hist,theoretical_counts(2))
    print('EXHAUSTIVE_BINARY_STRATA_OK',sum(hist.values()),dict(hist))
    # All q^6 alternating forms over q=3 and 5.
    for p in (2,3,5):
        cnt=collections.Counter()
        for vals in itertools.product(range(p),repeat=6):
            a=[0]*16
            for j,v in zip(D2,vals):a[j]=v
            cnt[predict(a,p)]+=1
            assert actual(a,p)==predict(a,p),(p,vals)
        assert cnt[(0,0)]==1
        assert cnt[(4,0)] == (p*p+1)*(p**3-1)
        assert cnt[(6,0 if p==2 else 1)]==p*p*(p-1)*(p**3-1)
        print('ALL_BIVECTORS_OK',p,p**6)
    print('VERIFY_OK_EXTERIOR_JORDAN')
if __name__=='__main__':random.seed(6312026);run()
