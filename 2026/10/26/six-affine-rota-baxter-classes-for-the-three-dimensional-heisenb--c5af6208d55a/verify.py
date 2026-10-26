#!/usr/bin/env python3
"""Exact finite-field tests for affine Rota--Baxter operators on the Heisenberg Lie affgebra.

Standard-library only. The field tests do not replace the all-field proof.
"""
from itertools import product


def vecs(q):
    return list(product(range(q), repeat=3))


def normalize(v, q):
    for a in v:
        if a % q:
            k = pow(a, -1, q)
            return tuple(k*x % q for x in v)
    return None


def add(u, v, q):
    return tuple((x+y) % q for x,y in zip(u,v))


def scale(s,u,q):
    return tuple(s*x % q for x in u)


def bracket(u,v,q):
    return (0,0,(u[0]*v[1]-u[1]*v[0]) % q)


def mul(A,B,q):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) % q for j in range(3)) for i in range(3))


def mv(A,v,q):
    return tuple(sum(A[i][j]*v[j] for j in range(3)) % q for i in range(3))


def inv(M,q):
    H=[list(row)+[int(i==j) for j in range(3)] for i,row in enumerate(M)]
    for j in range(3):
        i=next((k for k in range(j,3) if H[k][j] % q),None)
        if i is None: return None
        H[j],H[i]=H[i],H[j]
        H[j]=[(k*pow(H[j][j],-1,q)) % q for k in H[j]]
        for k in range(3):
            if k!=j:
                t=H[k][j]
                H[k]=[(H[k][l]-t*H[j][l]) % q for l in range(6)]
    return tuple(tuple(row[3:]) for row in H)


def matrix_from_columns(cols):
    return tuple(tuple(cols[j][i] for j in range(3)) for i in range(3))


def projection(coords,rank,q):
    basis=matrix_from_columns(coords)
    inverse=inv(basis,q)
    assert inverse is not None
    mask=tuple(1 if k<rank else 0 for k in range(3))
    return tuple(tuple(sum(basis[i][k]*mask[k]*inverse[k][j] for k in range(3)) % q for j in range(3)) for i in range(3))


def state(R,p):
    return tuple(x for row in R for x in row) + p


def unstate(st):
    return (tuple(tuple(st[3*i+j] for j in range(3)) for i in range(3)), tuple(st[9:]))


def build(q):
    z=(0,0,1)
    lines=sorted({normalize(v,q) for v in vecs(q)}-{None})
    planes=[(1,t,0) for t in range(q)]+[(0,1,0)]
    ops=set()
    for a in lines:
        for b in planes:
            if inv(matrix_from_columns((a,b,z)),q) is None:
                continue
            # rank one: span(a) image, span(b,z) kernel, p central
            R=projection((a,b,z),1,q)
            for t in range(q):
                ops.add(state(R,(0,0,t)))
            # rank two: span(b,z) image, span(a) kernel, p in span(a)
            R=projection((b,z,a),2,q)
            for t in range(q):
                ops.add(state(R,scale(t,a,q)))
    Z=((0,0,0),)*3
    I=tuple(tuple(int(i==j) for j in range(3)) for i in range(3))
    for p in vecs(q):
        ops.add(state(Z,p))
    ops.add(state(I,(0,0,0)))
    return ops


def affine_bracket(x,y,q):
    return add(bracket(x,y,q),y,q)


def check_identity(R,p,x,y,q):
    P=lambda v: add(mv(R,v,q),p,q)
    a=affine_bracket(P(x),y,q)
    b=affine_bracket(x,y,q)
    c=affine_bracket(x,P(y),q)
    descendant=add(add(a,scale(-1,b,q),q),c,q)
    return P(descendant)==affine_bracket(P(x),P(y),q)


def automorphisms(q):
    for a,b,c,d in product(range(q),repeat=4):
        det=(a*d-b*c)%q
        if not det: continue
        for s,t in product(range(q),repeat=2):
            M=((a,b,0),(c,d,0),(s,t,det))
            N=inv(M,q)
            assert N is not None
            for k in range(q):
                yield M,N,(0,0,k)


def image_of(state0,M,N,t,q):
    R,p=unstate(state0)
    S=mul(mul(M,R,q),N,q)
    r=mv(M,p,q)
    translated=add(r,add(t,scale(-1,mv(S,t,q),q),q),q)
    return state(S,translated)


def main():
    for q in (3,5):
        S=build(q)
        target=q**3*(2*q+3)+1
        assert len(S)==target, (q,len(S),target)
        ranks={r:0 for r in range(4)}
        for st in S:
            R,p=unstate(st)
            assert mul(R,R,q)==R
            assert mv(R,p,q)==(0,0,0)
            rank=sum(R[i][i] for i in range(3))%q
            if R==tuple(tuple(int(i==j) for j in range(3)) for i in range(3)): rr=3
            elif R==((0,0,0),)*3: rr=0
            elif rank==1: rr=1
            elif rank==2: rr=2
            else: raise AssertionError((q,R))
            ranks[rr]+=1
        assert ranks=={0:q**3,1:q**3*(q+1),2:q**3*(q+1),3:1},ranks
        if q==3:
            for st in S:
                R,p=unstate(st)
                for x in vecs(q):
                    for y in vecs(q):
                        assert check_identity(R,p,x,y,q),(st,x,y)
            M=list(automorphisms(q))
            assert len(M)==q**3*(q*q-1)*(q*q-q)
            # Use all affine automorphisms, not a presumed generating set.
            unseen=set(S)
            components=[]
            while unseen:
                seed=next(iter(unseen))
                orbit={image_of(seed,A,B,t,q) for A,B,t in M}
                assert orbit<=S
                assert seed in orbit
                components.append((seed,len(orbit)))
                unseen-=orbit
            components.sort(key=lambda x:x[1])
            assert len(components)==6,components
            print('field F_3: 244 operators, all 729 input pairs per operator checked,',len(M),'affine automorphisms, six orbits:',[c[1] for c in components])
        else:
            sample=[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,2,3)]
            for st in S:
                R,p=unstate(st)
                for x in sample:
                    for y in sample:
                        assert check_identity(R,p,x,y,q)
            print('field F_5: 1626 operators, all 25 sampled input pairs checked for each; rank counts',ranks)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
