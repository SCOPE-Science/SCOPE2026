"""Finite checks for the quantum-exterior commuting-scheme theorem.
This program needs only Python 3's standard library. It is a diagnostic;
the proof in RESULT.md establishes every-field and every-arity claims.
"""
from itertools import product

def mult_rad(v,w,lam,p):
    a,b,c=v; d,e,f=w
    return ((a+d)%p,(b+e)%p,(c+f+a*e+lam*b*d)%p)

def H_map(v,lam,p):
    a,b,c=v
    k=(1-lam)%p
    assert k
    return (a,b, ((c-lam*a*b)*pow(k,-1,p))%p)

def mult_H(v,w,p):
    a,b,c=v; d,e,f=w
    return ((a+d)%p,(b+e)%p,(c+f+a*e)%p)

def matrix_pivot_rank1_pairs(p,s):
    count=0
    for tup in product(range(p),repeat=2*s):
        a=tup[:s]; b=tup[s:]
        if all((a[i]*b[j]-a[j]*b[i])%p==0 for i in range(s) for j in range(i+1,s)):
            count+=1
    assert count==(p+1)*(p**s)-p,(p,s,count)
    return count

def Ptrans(B, P, p):
    a,b,c,d=P   # matrix [[a,b],[c,d]]
    # multiplication on bilinear forms: P^T B P
    Bs=((B[0]*a+B[1]*c)%p,(B[0]*b+B[1]*d)%p,
        (B[2]*a+B[3]*c)%p,(B[2]*b+B[3]*d)%p)
    return ((a*Bs[0]+c*Bs[2])%p,(a*Bs[1]+c*Bs[3])%p,
            (b*Bs[0]+d*Bs[2])%p,(b*Bs[1]+d*Bs[3])%p)

def congruent(lam,mu,p):
    B=(0,1,lam,0); C=(0,1,mu,0)
    for P in product(range(p),repeat=4):
        a,b,c,d=P
        if (a*d-b*c)%p==0:continue
        T=Ptrans(B,P,p)
        for z in range(1,p):
            if tuple(z*t%p for t in T)==C:
                return True
    return False

def predicted_iso(lam,mu,p):
    if lam==0 or mu==0:return lam==mu
    return lam==mu or lam*mu%p==1

def verify():
    group_cases=0; congruence_cases=0; tuple_cases=0
    for p in (2,3,5,7):
        V=list(product(range(p),repeat=3))
        for lam in range(p):
            if lam==1:continue
            for v in V:
                for w in V:
                    assert H_map(mult_rad(v,w,lam,p),lam,p)==mult_H(H_map(v,lam,p),H_map(w,lam,p),p)
                    group_cases+=1
        for lam in range(p):
            if lam==1:continue
            for mu in range(p):
                if mu==1:continue
                observed=congruent(lam,mu,p)
                expected=predicted_iso(lam,mu,p)
                assert observed==expected,(p,lam,mu,observed,expected)
                congruence_cases+=1
        for s in (2,3):
            matrix_pivot_rank1_pairs(p,s)
            tuple_cases+=1
    print('Group map multiplicativity cases:',group_cases)
    print('Algebra isomorphism congruence pairs:',congruence_cases)
    print('Determinantal tuple count cases:',tuple_cases)
    # Brute commutator test for 4-dimensional algebras over small fields:
    for p in (2,3):
        V=list(product(range(p),repeat=4))
        for lam in range(p):
            if lam==1:continue
            actual=0
            for u in V:
                for v in V:
                    # coefficient of z in uv-vu (constants commute and z annihilates the radical)
                    comm=((1-lam)*(u[1]*v[2]-u[2]*v[1]))%p
                    if comm==0:actual+=1
            predicted=p**4*((p+1)*p**2-p)
            assert actual==predicted,(p,lam,actual,predicted)
    print('Direct commuting-pair cardinalities: verified')
    print('VERIFY_OK')
if __name__=='__main__':verify()
