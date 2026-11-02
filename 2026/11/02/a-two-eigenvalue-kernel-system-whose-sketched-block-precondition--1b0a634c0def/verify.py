"""Exact finite sanity checks for the rank-one sketched block preconditioner theorem.
Analytical arbitrary-q proof is in RESULT.md, not inferred from these tests.
Requires sympy; run: python verify.py
"""
import sympy as sp


def matrices(q, uniform=False):
    assert q >= 2
    S = q if uniform else q*(q+1)*(2*q+1)//6
    ts = [sp.Rational(1, q) if uniform else sp.Rational(j*j, S) for j in range(1,q+1)]
    C = sp.zeros(2*q)
    for j in range(q):
        for k in range(q):
            C[2*j, 2*k] = sp.Rational(1,q) if uniform else sp.Rational((j+1)*(k+1), S)
    H = 2*sp.eye(2*q) + 4*C
    base = q*(q+1)
    diag = []
    for s in ts:
        beta = q*(1+s)*(q*(1+s)+1)
        diag.extend([beta,base])
    B = sp.diag(*diag)
    return H,B,ts


def main():
    checks=0
    for q in range(2,8):
        H,B,s = matrices(q)
        assert all(0 < x < 1 for x in s) and sum(s)==1
        assert len(set(s))==q
        checks+=3
        n=2*q
        lam0 = sp.Rational(2,q*(q+1))
        secular_at_lam0 = 1-2*(q+1)*sum(1/(q*(2+x)+1) for x in s)
        assert secular_at_lam0 <= 1-q < 0
        checks+=1
        act=list(range(0,n,2))
        A=(B.inv()*H)
        Aact=A.extract(act,act)
        x=sp.symbols('x')
        cp=Aact.charpoly(x).as_expr()
        p=sp.Poly(cp,x)
        assert sp.degree(sp.gcd(p,p.diff()))==0
        assert p.eval(lam0) !=0
        checks+=2
        b=sp.zeros(n,1);b[0]=b[1]=1
        assert sp.Matrix.hstack(b,H*b).rank()==2
        assert sp.Matrix.hstack(*[H**k*b for k in range(3)]).rank()==2
        checks+=2
        g=B.inv()*b
        assert sp.Matrix.hstack(*[A**k*g for k in range(q+1)]).rank()==q+1
        assert sp.Matrix.hstack(*[A**k*g for k in range(q+2)]).rank()==q+1
        checks+=2
        Hu,Bu,_=matrices(q,uniform=True)
        assert sp.expand(Hu.charpoly(x).as_expr()-(x-6)*(x-2)**(2*q-1)) == 0
        beta=q*(q+1)
        beta1=(q+1)*(q+2)
        Au=Bu.inv()*Hu
        expected=[sp.Rational(2,beta1)]*(q-1) + [sp.Rational(2,beta)]*q + [sp.Rational(6,beta1)]
        got=[z for z,m in Au.eigenvals().items() for _ in range(m)]
        assert sorted(got)==sorted(expected)
        assert max(got)/min(got)==3
        checks+=3
        print('q=',q,'symbolic checks passed; distinct levels=',q+1,'uniform levels=3')
    print('PASS:',checks,'exact symbolic checks, plus infinitely many q addressed by proof')

if __name__=='__main__': main()


def pcg_exact(H,B,b):
    n=H.rows
    x=sp.zeros(n,1);r=b; z=B.inv()*r; p=z; rz=(r.T*z)[0]
    for k in range(1,n+1):
        Hp=H*p
        alpha=sp.factor(rz/(p.T*Hp)[0])
        x=x+alpha*p
        r=sp.simplify(r-alpha*Hp)
        if all(entry==0 for entry in r):
            assert all(v==0 for v in H*x-b)
            return k
        z=B.inv()*r
        rz_new=(r.T*z)[0]
        p=sp.simplify(z+sp.factor(rz_new/rz)*p)
        rz=rz_new
    raise AssertionError('PCG did not terminate')

if __name__=='__main__':
    for q in range(2,6):
        H,B,_=matrices(q)
        b=sp.zeros(2*q,1); b[0]=1; b[1]=1
        assert pcg_exact(H,sp.eye(2*q),b)==2
        assert pcg_exact(H,B,b)==q+1
        print('exact CG iteration counts q=',q,': 2 versus',q+1)
