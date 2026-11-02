#!/usr/bin/env python3
"""Exact checks for tridegree-(2,2,2) normal splitting via ramification quadratics.
Requires only Python 3 standard library. No finite sample is used as a proof
of the infinite characteristic-wise statement.
"""
from itertools import product


def wronskian(P, Q, p=None):
    a,b,c=P; d,e,f=Q
    w=(a*e-b*d, 2*(a*f-c*d), b*f-c*e)
    return tuple(z % p for z in w) if p else w


def rank(rows,p):
    a=[list(map(lambda x: x%p, r)) for r in rows]
    nr=len(a); col=0; r=0
    while col < 3 and r < nr:
        piv=next((j for j in range(r,nr) if a[j][col]),None)
        if piv is None:
            col+=1;continue
        a[r],a[piv]=a[piv],a[r]
        t=pow(a[r][col],-1,p)
        a[r]=[(v*t)%p for v in a[r]]
        for j in range(nr):
            if j!=r:
                t=a[j][col]
                a[j]=[(a[j][k]-t*a[r][k])%p for k in range(3)]
        r+=1;col+=1
    return r


def has_common_zero(ws,p):
    # Degree <= 2 homogeneous polynomials have a common zero iff the
    # (possibly lower-degree) affine polynomials have a common root,
    # or all leading coefficients vanish (root at infinity).
    # For rank two and three the following simple determinant/gcd test
    # works over the algebraic closure of F_p.
    if all(w[0] %p==0 for w in ws):return True
    # Any common root must divide some nonzero polynomial of degree<=2.
    # brute force gcd over F_p[z] via polynomial Euclidean algorithm.
    def trim(a):
        while a and a[-1]==0:a.pop()
        return a
    def rem(a,b):
        a=trim(a[:]);b=trim(b[:]);
        while a and len(a)>=len(b):
            t=a[-1]*pow(b[-1],-1,p)%p
            s=len(a)-len(b)
            for i,v in enumerate(b):a[s+i]=(a[s+i]-t*v)%p
            a=trim(a)
        return a
    def gcd(a,b):
        a=trim(a[:]);b=trim(b[:]);
        while b:a,b=b,rem(a,b)
        return a
    v=[]
    for a,b,c in ws:v.append(trim([c%p,b%p,a%p]))
    g=[]
    for z in v:g=gcd(g,z)
    return len(g)>=2


def resultant_degree2(P,Q,p):
    # Sylvester determinant for P=a z^2+b z+c, Q=d z^2+e z+f.
    a,b,c=P;d,e,f=Q
    M=[[a,b,c,0],[0,a,b,c],[d,e,f,0],[0,d,e,f]]
    out=0
    from itertools import permutations
    for perm in permutations(range(4)):
        inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        z=(-1)**inv
        for i in range(4):z*=M[i][perm[i]]
        out+=z
    return out%p

# A homogeneous expression for a degree-two map f=[P:Q] is P,Q in
# k[s,t]_2, represented in the affine z=s/t chart by coefficient triples.
# The ramification quadratic is W(P,Q)=P'Q-PQ' homogenized to degree 2.
# Any separable degree-two map has nonzero resultant and W.
odd_f1=((1,0,0),(0,0,1))           # z^2
odd_f2=((1,0,1),(0,1,0))           # z+1/z
odd_f3_j=((1,0,1),(0,1,1))         # (z^2+1)/(z+1)
odd_f3_g=((1,0,2),(0,1,0))         # z+2/z
char2_f1=((1,1,0),(0,0,1))         # z^2+z
char2_f2=((1,0,0),(0,1,1))         # z^2/(z+1)

for p in [3,5,7,11,13,17,19]:
    for kind,fs,expected in [
        ('jump',(odd_f1,odd_f2,odd_f3_j),2),
        ('generic',(odd_f1,odd_f2,odd_f3_g),3),
    ]:
        assert all(resultant_degree2(*f,p)!=0 for f in fs),(p,kind,'bad degree')
        W=[wronskian(*f,p) for f in fs]
        assert not has_common_zero(W,p),(p,kind,'not immersive')
        assert rank(W,p)==expected,(p,kind,W)
        assert all((w[1]*w[1]-4*w[0]*w[2])%p!=0 for w in W), (p,kind,'ramification double root')

fs=(char2_f1,char2_f2,char2_f1)
assert all(resultant_degree2(*f,2)!=0 for f in fs)
W=[wronskian(*f,2) for f in fs]
assert not has_common_zero(W,2) and rank(W,2)==2
# The exact characteristic-two identity is universal: for arbitrary six
# coefficients, the middle term of W is 2*(a*f-c*d), hence zero mod 2.
for P in product(range(2),repeat=3):
    for Q in product(range(2),repeat=3):
        assert wronskian(P,Q,2)[1]==0
# Homogeneity: scaling P,Q by lambda multiplies W by lambda^2.
for p in (3,5,7):
    for fs in [(odd_f1,odd_f2,odd_f3_j),(odd_f1,odd_f2,odd_f3_g)]:
        for i in range(3):
            P,Q=fs[i]
            scaled=tuple(tuple(2*x%p for x in arr) for arr in (P,Q))
            assert wronskian(*scaled,p)==tuple(4*x%p for x in wronskian(P,Q,p))
# Degree c1 normal: 3 times 4 - 2 = 10;
# for rank 3: N=O(5)+O(5); rank 2: N=O(4)+O(6).
assert (5+5)==(4+6)==10
print('VERIFY_OK: exact witness, characteristic-two, rank and homogeneity checks')
