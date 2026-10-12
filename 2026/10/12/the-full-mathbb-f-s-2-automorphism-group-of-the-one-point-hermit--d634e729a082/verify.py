"""Exact small-field checks for the automorphism formula of a one-point Hermitian-relative curve."""
from itertools import product

def field(p):
    # t^2 + B*t + C irreducible over F_p.
    B,C = (1,1) if p == 2 else ((0,1) if p == 3 else (0,-2))
    q=p*p
    def add(a,b):return ((a%p+b%p)%p)+p*((a//p+b//p)%p)
    def neg(a):return (-(a%p))%p+p*((-(a//p))%p)
    def mul(a,b):
        a0,a1=a%p,a//p; b0,b1=b%p,b//p
        return ((a0*b0-C*a1*b1)%p)+p*((a0*b1+a1*b0-B*a1*b1)%p)
    def power(a,n):
        ans=1
        while n:
            if n&1:ans=mul(ans,a)
            a=mul(a,a);n//=2
        return ans
    return q,add,neg,mul,power

def check(p):
    q,add,neg,mul,power=field(p);s=p; vals=range(q)
    trace=lambda a:add(a,power(a,s))
    norm=lambda a:mul(a,power(a,s))
    eta=next(a for a in vals if power(a,s)!=a)
    # The curve has exactly one rational point, checked projectively.
    projective=set()
    for x,y,z in product(vals,repeat=3):
        if x==y==z==0:continue
        xyz=(x,y,z)
        first=next(t for t in xyz if t)
        inv=power(first,q-2)
        xyz=tuple(mul(t,inv) for t in xyz)
        X,Y,Z=xyz
        F=add(add(norm(X),mul(eta,norm(Y))),
              add(mul(power(Y,s),Z),mul(Y,power(Z,s))))
        if F==0:projective.add(xyz)
    assert projective == {(0,0,1)}, (p,projective)
    # coefficient indexed by monomial (x,y,z) exponents, using F = x^(s+1)+eta y^(s+1)+y^s z + y z^s.
    def preserved(a,b,c,e,f):
        terms={}
        def push(k,z):terms[k]=add(terms.get(k,0),z)
        push((s+1,0,0), norm(a))
        push((s,1,0),mul(power(a,s),b))
        push((1,s,0),mul(a,power(b,s)))
        push((0,s+1,0),add(norm(b),eta))
        push((1,s,0),c)
        push((0,s+1,0),e)
        push((0,s,1),f)
        push((s,1,0),power(c,s))
        push((0,s+1,0),power(e,s))
        push((0,1,s),power(f,s))
        lam=norm(a)
        return (all(terms.get(m,0)==0 for m in [(s,1,0),(1,s,0)]) and
                terms[(0,s+1,0)]==mul(lam,eta) and terms[(0,s,1)]==lam and terms[(0,1,s)]==lam)
    formula=set()
    for u in vals:
        if norm(u)!=1:continue
        for v in vals:
            for w in vals:
                if trace(w)==neg(norm(v)):
                    formula.add((u,v,neg(mul(u,power(v,s))),w,1))
    assert len(formula)==s**3*(s+1), (p,len(formula))
    for row in formula:
        assert preserved(*row), (p,row)
    # Verify the stated multiplication law, independently by multiplying matrices.
    sample=sorted(formula) if p<=3 else sorted(formula)[::19]
    def mat(row):
        u,v,c,w,f=row
        return ((u,v,0),(0,1,0),(c,w,1))
    def prod(A,B):
        return tuple(tuple(add(add(mul(A[i][0],B[0][j]),mul(A[i][1],B[1][j])),
                          mul(A[i][2],B[2][j])) for j in range(3)) for i in range(3))
    for a in sample:
        for b in sample:
            u,v,_,w,_=a;u0,v0,_,w0,_=b
            uu=mul(u,u0)
            vv=add(mul(u,v0),v)
            ww=add(add(w,w0),neg(mul(mul(u,power(v,s)),v0)))
            predicted=(uu,vv,neg(mul(uu,power(vv,s))),ww,1)
            assert predicted in formula and mat(predicted)==prod(mat(a),mat(b)), (p,a,b)

    # Enumerate every candidate upper triangular PGL_3 matrix fixing the unique rational point and tangent line.
    if p<=3:
        actual=set()
        for a in vals:
            if a==0:continue
            for b,c,e in product(vals,repeat=3):
                for f in vals:
                    if f and preserved(a,b,c,e,f):actual.add((a,b,c,e,f))
        assert actual==formula, (p,len(actual),len(formula),actual-formula,formula-actual)
    print(f"F_{q}: VERIFIED {len(formula)} automorphisms", 'including exhaustive stabilizer census' if p<=3 else 'by direct polynomial identities')

if __name__=='__main__':
    for p in [2,3,5]:check(p)
    print('VERIFY_OK')
