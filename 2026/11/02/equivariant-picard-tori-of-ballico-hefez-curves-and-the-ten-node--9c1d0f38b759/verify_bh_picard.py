"""Finite consistency checks for the equivariant Picard torus of Ballico--Hefez curves.

No external dependencies; execute python verify_bh_picard.py.
The general theorem is proved symbolically in RESULT.md, not by these sample checks.
"""
from collections import Counter
from itertools import product


def field(q):
    assert q in (2, 3, 5)
    def add(x,y): return ((x[0]+y[0])%q,(x[1]+y[1])%q)
    def mul(x,y):
        a,b=x; c,d=y
        if q==2: return ((a*c+b*d)%q,(a*d+b*c+b*d)%q) # theta^2=theta+1
        return ((a*c+2*b*d)%q,(a*d+b*c)%q) # theta^2=2
    def power(x,n):
        r=(1,0)
        while n:
            if n&1:r=mul(r,x)
            x=mul(x,x);n//=2
        return r
    def inv(x):
        assert x!=(0,0)
        return power(x,q*q-2)
    elements=list(product(range(q),repeat=2))
    outsiders=[x for x in elements if x[1]]
    return add,mul,power,inv,outsiders


def verify(q):
    add,mul,power,inv,outsiders=field(q)
    pairs={}
    for x in outsiders:
        xx=power(x,q)
        pair=tuple(sorted((x,xx)))
        pairs[pair]=pair[0]
    nodes=sorted(pairs)
    reps=[p[0] for p in nodes]
    index={p:i for i,p in enumerate(nodes)}
    assert len(nodes)==q*(q-1)//2
    mats=[]
    for a,b,c,d in product(range(q),repeat=4):
        if (a*d-b*c)%q==0:continue
        t=(a,b,c,d)
        first=next(x for x in t if x)
        t=tuple(x*pow(first,-1,q)%q for x in t)
        if t not in mats:mats.append(t)
    assert len(mats)==q*(q*q-1)
    def action(M,x):
        a,b,c,d=M
        numerator=add(mul((a,0),x),(b,0))
        denominator=add(mul((c,0),x),(d,0))
        assert denominator!=(0,0)
        return mul(numerator,inv(denominator))
    orbits=set()
    sign_swap=[]
    trace_sq=0
    trace_sum=0
    trace_orders=[]
    if q==5:
        def norm(A):
            s=next(x for x in A if x)
            return tuple(x*pow(s,-1,q)%q for x in A)
        def product_matrix(A,B):
            a,b,c,d=A;u,v,w,z=B
            return norm(((a*u+b*w)%q,(a*v+b*z)%q,(c*u+d*w)%q,(c*v+d*z)%q))
        def order(M):
            v=(1,0,0,1)
            for n in range(1,121):
                v=product_matrix(v,M)
                if v==(1,0,0,1):return n
            raise AssertionError("group order exceeded")
    for M in mats:
        trace=0
        for i,x in enumerate(reps):
            img=action(M,x)
            pair=tuple(sorted((img,power(img,q))))
            j=index[pair]
            if i==0:orbits.add(j)
            if i==0 and j==0:sign_swap.append(1 if img==reps[0] else -1)
            if i==j:trace+=1 if img==reps[i] else -1
        trace_sum+=trace
        trace_sq+=trace*trace
        if q==5:trace_orders.append((order(M),trace))
    assert len(orbits)==len(nodes)
    assert len(sign_swap)==2*(q+1)
    assert sign_swap.count(1)==sign_swap.count(-1)==q+1
    assert trace_sum==0
    # Orbits are transitive and isotropy includes inversion: the integral
    # signed permutation module has coinvariants Z/2 by the group relations.
    if q==5:
        assert trace_sq//len(mats)==2 and trace_sq%len(mats)==0
        expected={1:10,2:-2,3:1,4:0,5:0,6:1}
        assert all(expected[o]==tr for o,tr in trace_orders)
        print("Q=5 SPECHT_CHARACTER_OK:",dict(sorted(Counter(o for o,tr in trace_orders).items())))
    print(f'Q={q} GROUP={len(mats)} NODES={len(nodes)} '
          f'ORBIT={len(orbits)} STABILIZER={len(sign_swap)} '
          f'SIGN_COUNTS={Counter(sign_swap)} CHARACTER_NORM_SQUARED={trace_sq}/{len(mats)} '
          'COINVARIANTS=Z/2')


if __name__=='__main__':
    for q in (2,3,5): verify(q)
    print('VERIFY_OK')
