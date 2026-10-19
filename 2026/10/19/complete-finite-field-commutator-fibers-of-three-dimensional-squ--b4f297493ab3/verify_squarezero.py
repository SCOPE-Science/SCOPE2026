"""Independent exhaustive verification of the 3x3 square-zero commutator fibers.
Run: python verify_squarezero.py. Only Python standard library is needed.
Finite-field elements are 0,...,q-1; q=4 uses F_2[t]/(t^2+t+1).
"""
from collections import Counter
from itertools import product


def field(q):
    if q == 4:
        add = lambda a,b:a^b
        def mul(a,b):
            r=0
            for i in range(2):
                for j in range(2):
                    if ((a>>i)&1) and ((b>>j)&1):r ^= 1 <<(i+j)
            if r & 4:r ^= 0b111 # t^2=t+1
            return r
        neg=lambda a:a
    else:
        add=lambda a,b:(a+b)%q
        mul=lambda a,b:(a*b)%q
        neg=lambda a:(-a)%q
    return add,mul,neg


def rank(mat, q, ad, mu, neg):
    a=[list(mat[i*3:(i+1)*3]) for i in range(3)]
    r=0
    for c in range(3):
        piv=next((i for i in range(r,3) if a[i][c]),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]
        inv=next(i for i in range(1,q) if mu(a[r][c],i)==1)
        a[r]=[mu(v,inv) for v in a[r]]
        for i in range(r+1,3):
            k=a[i][c]
            if k:a[i]=[ad(u,neg(mu(k,v))) for u,v in zip(a[i],a[r])]
        r+=1
        if r==3:break
    return r


def main(q):
    ad,mu,neg=field(q)
    elems=range(q)
    vectors=list(product(elems,repeat=3))
    lines=[u for u in vectors if any(u) and u[next(i for i in range(3) if u[i])]==1]
    # canonical projective representative for each line; first nonzero must be 1
    assert len(lines)==q*q+q+1
    nonzero=[]
    matrices=set()
    for u in lines:
        for v in vectors:
            if not any(v) or ad(ad(mu(u[0],v[0]),mu(u[1],v[1])),mu(u[2],v[2])):continue
            nonzero.append((u,v))
            m=tuple(mu(u[i],v[j]) for i in range(3) for j in range(3))
            assert m not in matrices
            matrices.add(m)
    N=(q*q+q+1)*(q*q-1)
    assert len(nonzero)==N
    squarezeros=[((0,0,0),(0,0,0))]+nonzero
    hist=Counter()
    for u,v in squarezeros:
        for x,y in squarezeros:
            alpha=ad(ad(mu(v[0],x[0]),mu(v[1],x[1])),mu(v[2],x[2]))
            beta=ad(ad(mu(y[0],u[0]),mu(y[1],u[1])),mu(y[2],u[2]))
            C=tuple(ad(mu(alpha,mu(u[i],y[j])),neg(mu(beta,mu(x[i],v[j]))))
                for i in range(3) for j in range(3))
            hist[C]+=1
    exp0=1+N*(2*q*q-q+1)
    exp1=2*q*q*(q-1)
    exp2=(q*(q*q-1) if q in (2,4) else 2*(q-1))
    count=Counter()
    z=(0,)*9
    for C,n in hist.items():
        if C==z:
            assert n==exp0,(q,'zero',n,exp0)
            count['zero']+=1
        else:
            rr=rank(C,q,ad,mu,neg)
            if rr==1:
                C2=tuple(ad(ad(mu(C[3*i],C[j]),mu(C[3*i+1],C[3+j])),mu(C[3*i+2],C[6+j])) for i in range(3) for j in range(3))
                assert C2==z,(q,'not squarezero',C)
                assert n==exp1,(q,'nilpotent',n,exp1)
                count['rank1_nilpotent']+=1
            else:
                assert rr==2,(q,'bad rank',rr)
                assert n==exp2,(q,'rank2',n,exp2)
                count['rank2_semisimple']+=1
    assert count['zero']==1
    assert count['rank1_nilpotent']==N,(q,count,N)
    if q in (2,4):
        target2=(q-1)*(q*q+q+1)*q*q
    else:
        target2=q*q*q*(q-1)*N//exp2
    assert count['rank2_semisimple']==target2,(q,count,target2)
    assert sum(hist.values())==(N+1)**2
    print('q=',q,'|Nil2|=',N+1,'fibers=',dict(count),
          'zero_fiber=',exp0,'nonzero_squarezero_fiber=',exp1,
          'rank2_fiber=',exp2,'pairs=',(N+1)**2)

if __name__=='__main__':
    for q in (2,3,4,5):main(q)
    print('ALL_EXACT_CHECKS_PASSED 4')
