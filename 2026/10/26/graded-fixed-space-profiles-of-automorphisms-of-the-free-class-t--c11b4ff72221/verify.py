"""Exact checks for the fixed-point-free automorphism census of the free class-two Lie algebra on three generators.
Only Python standard library is used. Execute: python verify_free_class2.py
"""
from itertools import product
from math import prod


def finite_field(q):
    if q == 4:
        add = lambda a, b: a ^ b
        def mul(a, b):
            p = ((a & 1) * (b & 1)) ^ ((((a & 1) * ((b >> 1) & 1)) ^ (((a >> 1) & 1) * (b & 1))) << 1)
            if ((a >> 1) & 1) and ((b >> 1) & 1):
                p ^= 3  # t^2 = t+1 in F_2[t]/(t^2+t+1).
            return p
        neg = lambda a: a
    else:
        add = lambda a, b: (a + b) % q
        mul = lambda a, b: (a * b) % q
        neg = lambda a: (-a) % q
    return add, mul, neg


def det3(m, add, mul, neg):
    a, b, c, d, e, f, g, h, i = m
    x = add(mul(a, add(mul(e,i), neg(mul(f,h)))), neg(mul(b, add(mul(d,i), neg(mul(f,g))))))
    return add(x, mul(c, add(mul(d,h), neg(mul(e,g)))))


def kernel_dim3(m, q, add, mul, neg):
    inv = {a:next((b for b in range(1,q) if mul(a,b)==1), None) for a in range(1,q)}
    a=[list(m[3*i:3*i+3]) for i in range(3)]
    pivot=0
    for col in range(3):
        row=next((j for j in range(pivot,3) if a[j][col]!=0),None)
        if row is None: continue
        a[row],a[pivot]=a[pivot],a[row]
        fac=inv[a[pivot][col]]
        a[pivot]=[mul(fac,z) for z in a[pivot]]
        for i in range(pivot+1,3):
            z=a[i][col]
            if z:
                a[i]=[add(a[i][h],neg(mul(z,a[pivot][h]))) for h in range(3)]
        pivot += 1
    return 3-pivot


def gaussian(n,k,q):
    if not 0<=k<=n:return 0
    a,b=1,1
    for j in range(k):
        a*=q**(n-j)-1
        b*=q**(k-j)-1
    return a//b


def expected_profile(q):
    add,mul,neg=finite_field(q)
    def sl(r):
        assert r>=1
        return prod(q**r-q**i for i in range(r))//(q-1)
    out={}
    for d in range(1,q):
        F={}
        if d==1:
            for k in range(4):
                r=3-k
                F[k]=gaussian(3,k,q)*q**(k*r)*(sl(r) if r else 1)
            N={}
            for a in range(4):
                N[a]=sum((-1)**(k-a)*q**((k-a)*(k-a-1)//2)*gaussian(k,a,q)*F[k]
                         for k in range(a,4))
                out[a,a]=out.get((a,a),0)+N[a]
        else:
            for k in range(4):
                for ell in range(4-k):
                    r=3-k-ell
                    z=(sl(r) if r else int(ell==1 or (ell==3 and mul(d,d)==1)))
                    F[k,ell]=(gaussian(3,k,q)*gaussian(3-k,ell,q)*
                              q**(k*ell+(k+ell)*r)*z)
            for a in range(4):
                for b in range(4):
                    N=sum((-1)**(k-a+l-b)*q**(((k-a)*(k-a-1)+(l-b)*(l-b-1))//2)*
                          gaussian(k,a,q)*gaussian(l,b,q)*F.get((k,l),0)
                          for k in range(a,4) for l in range(b,4))
                    assert N>=0,(q,d,a,b,N)
                    out[a,b]=out.get((a,b),0)+N
    return {key:v for key,v in out.items() if v}


def brute(q):
    add, mul, neg = finite_field(q)
    one = 1
    count, by_det, joint = 0, {}, {}
    for m in product(range(q), repeat=9):
        d = det3(m,add,mul,neg)
        if d == 0:
            continue
        mm = list(m)
        for i in (0,4,8):
            mm[i] = add(mm[i], neg(one))
        a = kernel_dim3(mm,q,add,mul,neg)
        # Assemble the exterior-square matrix in basis (e0^e1,e0^e2,e1^e2).
        pairs = ((0,1),(0,2),(1,2))
        w = []
        for x,y in pairs:
            for i,j in pairs:
                w.append(add(mul(m[3*x+i],m[3*y+j]),neg(mul(m[3*x+j],m[3*y+i]))))
        for i in (0,4,8):
            w[i] = add(w[i],neg(one))
        b=kernel_dim3(w,q,add,mul,neg)
        joint[a,b]=joint.get((a,b),0)+1
        if a==0 and b==0:
            count += 1
            by_det[d] = by_det.get(d,0) + 1
    return count, by_det, joint


def theoretical(q):
    def gl(n):
        return prod(q**n-q**i for i in range(n))
    def gauss(n,k):
        if k < 0 or k > n: return 0
        a,b=1,1
        for j in range(k):
            a *= q**(n-j)-1
            b *= q**(k-j)-1
        return a//b
    def count_for_det(d):
        if d==1:
            z = 0
            for k in range(4):
                r=3-k
                z += (-1)**k * q**(k*(k-1)//2 +k*r)*gauss(3,k)*(gl(r)//(q-1) if r else 1)
            return z
        z=0
        for k in range(4):
            for ell in range(4-k):
                r=3-k-ell
                if r:
                    factor=gl(r)//(q-1)
                else:
                    factor=int(pow(d,ell-1,q)==1) if ell else 0
                z += ((-1)**(k+ell)*q**(k*(k-1)//2 +ell*(ell-1)//2 +k*ell +(k+ell)*r)*
                      gauss(3,k)*gauss(3-k,ell)*factor)
        return z
    values={d:count_for_det(d) for d in range(1,q)} if q!=4 else None
    # The branch for extension fields is evaluated independently by the closed formula below.
    polynomial=q**3*(q**6-3*q**5+q**4+4*q**3+q**2-3*q-8-(q%2))
    if values is not None:
        assert sum(values.values()) == polynomial, (q,values,polynomial)
        if q>2:
            assert values[1] == q**3*(q+1)*(q**4-2*q**3+2)
    return polynomial, values


def run():
    for q in (2,3,4):
        observed, stratified, joint=brute(q)
        formula, counts=theoretical(q)
        theory_joint=expected_profile(q)
        assert joint==theory_joint,(q,joint,theory_joint)
        assert observed==formula, (q,observed,formula)
        if counts is not None: assert stratified==counts, (q,stratified,counts)
        print('q',q,'base matrices',observed,'strata',stratified,'joint',sorted(joint.items()))
    # Polynomial versus exact subspace-lattice sums for prime fields beyond brute range.
    for q in (5,7,11,13,17,19,23):
        theoretical(q)
    print('VERIFY_OK')

if __name__=='__main__':
    run()
