"""Standalone exact finite checks for the two-orbit isolated flat-band construction.

Usage: python3 verify.py (standard library only). These checks do not prove
statements over all cell sizes or momenta; see the accompanying proof.
"""
from collections import Counter

def golomb(X):
    d=[a-b for a in X for b in X if a!=b]
    return len(d)==len(set(d)) and len(d)==len(X)*(len(X)-1)

def data(X,Y):
    aa=set(a-b for a in X for b in X if a!=b)
    bb=set(a-b for a in Y for b in Y if a!=b)
    ss=[a-b for a in X for b in Y]
    assert golomb(X) and golomb(Y)
    assert len(set(ss))==len(X)*len(Y)
    assert aa=={-a for a in aa} and bb=={-a for a in bb}
    assert 0 not in aa|bb and 0 in ss and 1 in aa
    return aa,bb,set(ss)

def check_compact(X,Y):
    aa,bb,ss=data(X,Y)
    r=len(X)
    A={y:-1 for y in Y}
    B={x:1 for x in X}
    support=set(A)|set(B)
    a_sites=support | {v-h for v in A for h in aa}|{v-h for v in B for h in ss}
    b_sites=support | {v-h for v in B for h in bb}|{v+h for v in A for h in ss}
    for j in a_sites:
        lhs=sum(A.get(j+h,0) for h in aa)+sum(B.get(j+s,0) for s in ss)
        assert lhs == -r*A.get(j,0),(j,'A',lhs)
    for j in b_sites:
        lhs=sum(B.get(j+h,0) for h in bb)+sum(A.get(j-s,0) for s in ss)
        assert lhs == -r*B.get(j,0),(j,'B',lhs)
    return len(a_sites)+len(b_sites)

def mul(p,q):
    c=Counter()
    for a,ca in p.items():
        for b,cb in q.items():
            c[a+b]+=ca*cb
    return {k:v for k,v in c.items() if v}

def add(p,q):
    c=Counter(p);c.update(q)
    return {k:v for k,v in c.items() if v}

def neg(p):return {k:-v for k,v in p.items()}
def invert(p):return {-k:v for k,v in p.items()}

def laurent(X):return {x:1 for x in X}

def check_floquet(X,Y):
    aa,bb,ss=data(X,Y);r=len(X)
    p=laurent(X); q=laurent(Y)
    assert add(mul(p,invert(p)),{0:-r})=={h:1 for h in aa}
    assert add(mul(q,invert(q)),{0:-r})=={h:1 for h in bb}
    assert mul(p,invert(q))=={h:1 for h in ss}
    return len(aa)+len(bb)+len(ss)

def modtrim(a):
    while a and a[-1]==0:a.pop()
    return a

def rem_mod(a,b,p):
    a=list(a);inv=pow(b[-1],-1,p)
    while len(a)>=len(b):
        t=a[-1]*inv%p;shift=len(a)-len(b)
        for j,x in enumerate(b):a[j+shift]=(a[j+shift]-t*x)%p
        modtrim(a)
    return a

def gcd_mod(a,b,p):
    while b:a,b=b,rem_mod(a,b,p)
    return modtrim(a)

def coef(X,M):
    a=[0]*(max(X)*M+1)
    for x in X:a[M*x]=1
    return a

def check_r3_gap_identity():
    # Prove P(z)P(1/z)+Q(z)Q(1/z)-2=4(1+ab+ac+bc)
    # where a=cos(t), b=cos(3t), c=cos(4t), and z=e^{it}.
    X=[0,1,4]; Y=[0,2,7]
    left=add(mul(laurent(X),invert(laurent(X))),mul(laurent(Y),invert(laurent(Y))))
    left=add(left,{0:-2})
    rhs={0:4}
    for j,k in ((1,3),(1,4),(3,4)):
        for h in (j+k,j-k,-j+k,-j-k):
            rhs[h]=rhs.get(h,0)+1
    assert left==rhs, (left,rhs)
    # The identity 1+ab+ac+bc = ((1+a)(1+b)(1+c)
    # +(1-a)(1-b)(1-c))/2 gives nonnegativity on [-1,1]^3.
    # At t=pi: a=b=-1,c=1, so equality and exact minimum 2.
    assert sum((-1)**x for x in X)**2 + sum((-1)**y for y in Y)**2==2
    assert len(X)*(len(X)-1)+len(X)*len(Y)==15
    return len(left)

def main():
    recurrence=0;floquet=0; coprime=[]
    for r in range(2,6):
        X=[0]+[4**i for i in range(r-1)]
        M=max(X)+1
        Y=[M*x for x in X]
        floquet+=check_floquet(X,Y)
        if r<=4:recurrence+=check_compact(X,Y)
        f=coef(X,1);g=coef(X,M)
        gc=gcd_mod(f,g,1009)
        assert len(gc)==1, (r,M,len(gc))
        coprime.append((r,M))
    X=[0,1,4];Y=[0,2,7]
    floquet+=check_floquet(X,Y)
    recurrence+=check_compact(X,Y)
    gap=check_r3_gap_identity()
    print('VERIFY_OK isolated_negative_flat_bands modular_coprime_rM=%s exact_compact_sites=%s laurent_coefficients=%s sharp_r3_gap=2 identity_coefficients=%s'%(coprime,recurrence,floquet,gap))
if __name__=='__main__':main()
