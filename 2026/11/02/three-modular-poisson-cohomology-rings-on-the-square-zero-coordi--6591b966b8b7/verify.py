#!/usr/bin/env python3
"""Direct finite-field verification of Poisson brackets on square-zero coordinate plane.
Independent finite-field implementation and explicit automorphism action.
"""
from itertools import product

def gf_data(q):
    # GF(2), GF(4) with u^2+u+1, GF(8) with u^3+u+1.
    poly={2:0b11,4:0b111,8:0b1011}[q]
    k=q.bit_length()-1
    def mul(a,b):
        r=0
        while b:
            if b&1: r^=a
            b >>=1
            a <<=1
            if a & (1<<k): a ^= poly
        return r
    inv={a:next(b for b in range(1,q) if mul(a,b)==1) for a in range(1,q)}
    return mul,inv

def test(q, exhaustive=True):
    mul,inv=gf_data(q)
    def amul(A,B):
        # coefficient order 1,x,y,xy
        a,b,c,d=A; e,f,g,h=B
        return (mul(a,e), mul(a,f)^mul(b,e), mul(a,g)^mul(c,e), mul(a,h)^mul(d,e)^mul(b,g)^mul(c,f))
    def bracket(G,A,B):
        # derivative formula for bracket with {x,y}=G
        dxA=(A[1],0,A[3],0); dyA=(A[2],A[3],0,0)
        dxB=(B[1],0,B[3],0); dyB=(B[2],B[3],0,0)
        s=tuple(t^u for t,u in zip(amul(dxA,dyB),amul(dyA,dxB)))
        return amul(G,s)
    basis=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
    for G in product(range(q), repeat=4):
        # Bracket must satisfy Lie, Leibniz, alternating; verify all basis triples.
        for i in range(4):
            assert bracket(G,basis[i],basis[i])==(0,0,0,0)
            for j in range(4):
                for k in range(4):
                    jac=tuple(x^y^z for x,y,z in zip(bracket(G,basis[i],bracket(G,basis[j],basis[k])),bracket(G,basis[j],bracket(G,basis[k],basis[i])),bracket(G,basis[k],bracket(G,basis[i],basis[j]))))
                    assert jac==(0,0,0,0), (q,G,i,j,k)
                    lhs=bracket(G,amul(basis[i],basis[j]),basis[k])
                    r1=amul(basis[i],bracket(G,basis[j],basis[k]));r2=amul(basis[j],bracket(G,basis[i],basis[k]))
                    assert lhs==tuple(x^y for x,y in zip(r1,r2))
    if not exhaustive:
        print('GF',q,'all',q**4,'brackets satisfy original identities')
        return
    # enumerate all algebra automorphisms from image generators, preserving XY.
    aut=[]
    for u,v,r,s in product(range(q),repeat=4):
        delta=mul(u,s)^mul(v,r)
        if delta:
            for w,t in product(range(q),repeat=2):
                aut.append((u,v,w,r,s,t,delta))
    assert len(aut)==q*q*(q*q-1)*(q*q-q)
    seen=set()
    orbits=[]
    all_g=list(product(range(q),repeat=4))
    for G in all_g:
        if G in seen:continue
        orbit=set()
        a,b,c,d=G
        for u,v,w,r,s,t,delta in aut:
            di=inv[delta]
            C=mul(u,t)^mul(w,r); D=mul(w,s)^mul(v,t)
            Cx=mul(b,u)^mul(c,r); Cy=mul(b,v)^mul(c,s)
            out=(mul(a,di),mul(Cx,di)^mul(mul(a,C),mul(di,di)),mul(Cy,di)^mul(mul(a,D),mul(di,di)),d)
            # independently verify phi({x,y}_G) = {phi(x),phi(y)}_{out}
            X=(0,u,v,w);Y=(0,r,s,t)
            left=(a,Cx,Cy,mul(b,w)^mul(c,t)^mul(d,delta))
            right=bracket(out,X,Y)
            assert left==right, (q,G,out,(u,v,w,r,s,t),left,right)
            orbit.add(out)
        assert G in orbit
        assert len(set(o[3] for o in orbit))==1
        seen|=orbit
        orbits.append(orbit)
    assert len(seen)==q**4
    assert len(orbits)==3*q,(q,len(orbits))
    bytype={('unit' if O.__iter__().__next__()[0] else 'linear' if O.__iter__().__next__()[1:3]!=(0,0) else 'socle'):[] for O in orbits}
    for O in orbits:
        h=next(iter(O));typ='unit' if h[0] else 'linear' if h[1:3]!=(0,0) else 'socle'
        bytype.setdefault(typ,[]).append(len(O))
    assert sorted(bytype['unit'])==[(q-1)*q*q]*q
    assert sorted(bytype['linear'])==[q*q-1]*q
    assert sorted(bytype['socle'])==[1]*q
    print(f'GF({q}): {q**4} Poisson brackets; {len(aut)} algebra automorphisms; {len(orbits)} Poisson-isomorphism orbits; orbit sizes unit={(q-1)*q*q},linear={q*q-1},socle=1, each {q} times')

if __name__=='__main__':
    for q in (2,4):test(q)
    test(8,exhaustive=False)
    print('CHAR2_POISSON_TRUNCATED_PLANE_DIRECT_OK')
