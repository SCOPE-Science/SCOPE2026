"""Finite-field reproducibility checks for central three-dimensional Poisson algebras.
No external dependencies. Run: python verify.py
"""
from itertools import product

def finite_field(q):
    if q == 4:
        # F4 = F2[alpha]/(alpha^2+alpha+1), values 0,1,alpha,1+alpha.
        def add(x, y): return x ^ y
        def mul(x, y):
            z = 0
            for i in range(2):
                for j in range(2):
                    if ((x >> i) & 1) and ((y >> j) & 1): z ^= 1 << (i+j)
            if z & 8: z ^= 0b1110  # unnecessary for quadratic inputs but safe
            if z & 4: z ^= 0b111
            return z
    else:
        add = lambda x,y: (x+y)%q
        mul = lambda x,y: (x*y)%q
    neg = lambda x: next(y for y in range(q) if add(x,y)==0)
    sub = lambda x,y: add(x,neg(y))
    return add,mul,neg,sub

def experiment(q):
    add,mul,neg,sub=finite_field(q)
    def mm(A,B):
        return tuple(add(mul(A[2*i],B[j]),mul(A[2*i+1],B[2+j])) for i in range(2) for j in range(2))
    def det(A):return sub(mul(A[0],A[3]),mul(A[1],A[2]))
    I=(1,0,0,1)
    zero=(0,0,0,0)
    mats=list(product(range(q),repeat=4))
    gl=[A for A in mats if det(A)]
    def inv(A):
        d=det(A)
        d_inv=next(y for y in range(1,q) if mul(y,d)==1)
        return tuple(mul(d_inv,x) for x in (A[3],neg(A[1]),neg(A[2]),A[0]))
    gi={A:inv(A) for A in gl}
    Tset=set()
    for a,b,c in product(range(q),repeat=3):
        T=(neg(b),neg(c),a,b)
        assert add(T[0],T[3])==0
        Tset.add(T)
    assert len(Tset)==q**3
    Tset.discard(zero)
    seen=set(); reps=[];counts=[]
    for T in sorted(Tset):
        if T in seen:continue
        orbit={mm(mm(gi[G],T),G) for G in gl}
        assert orbit<=Tset
        stab=sum(mm(G,T)==mm(T,G) for G in gl)
        assert len(orbit)*stab==len(gl)
        assert not seen.intersection(orbit)
        seen|=orbit
        reps.append(T);counts.append((len(orbit),stab))
    assert seen==Tset and sum(k for k,s in counts)==q**3-1
    scalar=lambda T:T[1]==T[2]==0 and T[0]==T[3]
    non_scalar=0;scalar_reps=0
    for T,(orb,stab) in zip(reps,counts):
        scalar_rep=scalar(T)
        if scalar_rep:
            scalar_reps+=1
            assert q%2==0
            assert stab==len(gl) and orb==1
        else:
            non_scalar+=1
            if q%2==0 or det(T)==0:expected=q*(q-1)
            else:
                sqs={mul(x,x) for x in range(q)}
                expected=(q-1)**2 if neg(det(T)) in sqs else q**2-1
            assert stab==expected,(q,T,stab,expected)
        S=mm((0,1,neg(1),0),T)  # S=JT: symmetric product form.
        assert S[1]==S[2]
        for A in mats:
            commutes=mm(A,T)==mm(T,A)
            # Leibniz constraint on B: S A + A^t S = tr(A) S.
            SA=mm(S,A); ATS=mm((A[0],A[2],A[1],A[3]),S)
            tr=add(A[0],A[3])
            d_condition=all(add(SA[i],ATS[i])==mul(tr,S[i]) for i in range(4))
            assert commutes==d_condition,(q,T,A)
        d0=sum(mm(A,T)==mm(T,A) for A in mats)
        assert d0==(q**4 if scalar_rep else q**2)
        assert q*q*d0==(q**6 if scalar_rep else q**4)
    expected_classes=2*q-1 if q%2==0 else q
    assert len(reps)==expected_classes,(q,len(reps),expected_classes)
    assert scalar_reps==(q-1 if q%2==0 else 0)
    assert non_scalar==(q if q%2==0 else q)
    print('q=%d: %d nonzero product forms, %d isomorphism classes, %d scalar-jump classes, orbits=%s'%(
        q, len(Tset),len(reps),scalar_reps,sorted(counts)))

for q in (2,3,4,5):experiment(q)
print('VERIFY_OK')
