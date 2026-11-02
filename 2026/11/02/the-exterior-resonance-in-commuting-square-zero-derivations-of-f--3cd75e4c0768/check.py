#!/usr/bin/env python3
"""Independent finite-field checks for square-zero derivations of four-dimensional quantum complete intersections."""
from itertools import product
from collections import Counter


def build_field(q):
    if q in (3,5,7):
        return (lambda a,b:(a+b)%q),(lambda a,b:(a*b)%q),lambda a:(-a)%q
    if q==9:
        # F_3[t]/(t*t+1), with a+b*t represented by a+3*b.
        def add(a,b):
            return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
        def mul(a,b):
            x,y=a%3,a//3; u,v=b%3,b//3
            return ((x*u-y*v)%3)+3*((x*v+y*u)%3)
        def neg(a):return ((-(a%3))%3)+3*((-(a//3))%3)
        return add,mul,neg
    raise ValueError(q)


def field_test(q,t,exhaustive=True):
    add,mul,neg=build_field(q)
    sub=lambda a,b:add(a,neg(b))
    zero=(0,0,0,0)
    E=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
    def vecadd(u,v):return tuple(add(x,y) for x,y in zip(u,v))
    def scale(a,u):return tuple(mul(a,x) for x in u)
    def mult(u,v):
        a,b,c,d=u;f,g,h,j=v
        return (mul(a,f),add(mul(a,g),mul(b,f)),add(mul(a,h),mul(c,f)),
                add(add(add(mul(a,j),mul(d,f)),mul(b,h)),mul(t,mul(c,g))))
    def apply(D,u):
        out=zero
        for col,coef in zip(D,u):
            if coef:out=vecadd(out,scale(coef,col))
        return out
    def compose(D,E):return tuple(apply(D,col) for col in E)
    def D_of_params(p):
        D1=(0,p[0],p[1],p[2]);D2=(0,p[3],p[4],p[5])
        D3=vecadd(mult(D1,E[2]),mult(E[1],D2))
        return (zero,D1,D2,D3)
    def is_derivation(D):
        for u in E:
            for v in E:
                if apply(D,mult(u,v))!=vecadd(mult(apply(D,u),v),mult(u,apply(D,v))):return False
        return True
    def is_zero_comp(D,E):return all(c==zero for c in compose(D,E))
    def is_commuting(D,E):return compose(D,E)==compose(E,D)
    # Iterate over all possible D(x),D(y) with zero scalar terms. In odd characteristic
    # this is exhaustive since D(x*x)=D(y*y)=0 forces both scalar terms to vanish.
    good=[];count_der=0
    for p in product(range(q),repeat=6):
        D=D_of_params(p)
        if not is_derivation(D):continue
        count_der+=1
        if is_zero_comp(D,D):good.append(D)
    assert len(set(good))==len(good)
    outside=(t!=neg(1))
    expected=q*q if outside else q**3+q*q-q
    assert len(good)==expected,(q,t,len(good),expected)
    # Every nonzero square-zero derivation has rank one on the original algebra.
    def rank(D):
        cols=[list(c) for c in D]
        rows=[[cols[j][i] for j in range(4)] for i in range(4)]
        piv=0
        for j in range(4):
            k=next((i for i in range(piv,4) if rows[i][j]!=0),None)
            if k is None:continue
            rows[piv],rows[k]=rows[k],rows[piv]
            inv=next(a for a in range(1,q) if mul(a,rows[piv][j])==1)
            rows[piv]=[mul(inv,a) for a in rows[piv]]
            for i in range(piv+1,4):
                a=rows[i][j]
                if a:rows[i]=[sub(x,mul(a,y)) for x,y in zip(rows[i],rows[piv])]
            piv+=1
        return piv
    ranks={D:rank(D) for D in good}
    assert all(r==(D!=(zero,zero,zero,zero)) for D,r in ranks.items())
    if outside:
        assert all(is_zero_comp(D,E) for D in good for E in good)
    else:
        valencies=Counter();hist=Counter();pairs=0;fail=0
        for D in good:
            c=0
            for E in good:
                if is_commuting(D,E):
                    c+=1
                    hist[(ranks[D],ranks[E])]+=1
                    if not is_zero_comp(D,E):fail+=1
            valencies[c]+=1
            pairs+=c
        assert fail==0
        assert valencies==Counter({expected:1,2*q*q-q:q*q-1,q*q:q**3-q}),(q,valencies)
        assert pairs==q**4+(q+1)*(q*q-1)*q*q
        for r1 in range(2):
            for r2 in range(2):
                s=r1+r2
                expect=(q+2)*(q*q-1)**s-(q+1)*(q-1)**s
                assert hist[(r1,r2)]==expect,(q,r1,r2,hist,expect)
    print('field',q,'parameter',t,'derivations',count_der,'square_zero',len(good),
          'commuting_pairs', (q**4+(q+1)*(q*q-1)*q*q) if not outside else len(good)**2,
          'valid_all_square_zero',True)
    return good


def main():
    for q,t in [(3,2),(5,4),(7,6),(5,1),(5,2),(7,1)]:
        field_test(q,t)
    # Exact extension-field verification using the original associative product.
    # The coefficients are sampled structurally from all square-zero matrices/covectors.
    q=9;t=2 # exterior relation y*x=-x*y in F_9
    add,mul,neg=build_field(q)
    z=(0,0,0,0)
    one=(1,0,0,0);x=(0,1,0,0);y=(0,0,1,0);xy=(0,0,0,1)
    def vadd(a,b):return tuple(add(u,v) for u,v in zip(a,b))
    def scale(s,a):return tuple(mul(s,u) for u in a)
    def prod(a,b):
        s,u,v,w=a;S,U,V,W=b
        return (mul(s,S),add(mul(s,U),mul(u,S)),add(mul(s,V),mul(v,S)),
                add(add(add(mul(s,W),mul(w,S)),mul(u,V)),mul(t,mul(v,U))))
    def act(D,a):
        out=z
        for ai,di in zip(a,D):out=vadd(out,scale(ai,di))
        return out
    def candidate(p):
        dx=(0,p[0],p[1],p[2]);dy=(0,p[3],p[4],p[5]);dxy=vadd(prod(dx,y),prod(x,dy))
        return (z,dx,dy,dxy)
    derivs=[]
    for p in product(range(q),repeat=6):
        # For q=9 use the explicit matrix square-zero conditions, then verify all
        # sixteen original products independently, rather than enumerating 531441 matrices.
        a,b,c,d,e,f=p
        if (add(mul(a,a),mul(b,d)) or add(mul(a,b),mul(b,e)) or
            add(mul(d,a),mul(e,d)) or add(mul(d,b),mul(e,e))):continue
        if add(mul(c,a),mul(f,b)) or add(mul(c,d),mul(f,e)):continue
        D=candidate(p)
        assert all(act(D,prod(U,V))==vadd(prod(act(D,U),V),prod(U,act(D,V))) for U in (one,x,y,xy) for V in (one,x,y,xy))
        assert all(act(D,act(D,U))==z for U in (one,x,y,xy))
        derivs.append(D)
    assert len(derivs)==q**3+q*q-q
    print('field',9,'parameter',t,'square_zero',len(derivs),'all_direct_checked',True)
    print('QUANTUM_EXTERIOR_DIFFERENTIAL_COMPATIBILITY_OK')

if __name__=='__main__':main()
