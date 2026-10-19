#!/usr/bin/env python3
"""Finite-field and local-chart checks for the abelian-plane variety of a Takiff algebra."""
from itertools import combinations,product
import sympy as S

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def count(q):
    counts={0:0,1:0}
    rref_total=0
    for i,j in combinations(range(6),2):
        a=[0]*6;b=[0]*6;a[i]=1;b[j]=1
        free_a=[c for c in range(i+1,6) if c!=j]
        free_b=[c for c in range(j+1,6)]
        for v in product(range(q),repeat=len(free_a)+len(free_b)):
            for c,x in zip(free_a,v[:len(free_a)]):a[c]=x
            for c,x in zip(free_b,v[len(free_a):]):b[c]=x
            rref_total+=1
            A,B,C,D=a[:3],a[3:],b[:3],b[3:]
            uv=cross(A,C)
            vw=tuple(x+y for x,y in zip(cross(A,D),cross(B,C)))
            if all(z%q==0 for z in uv+vw):
                if any(A) or any(C):counts[1]+=1
                else:counts[0]+=1
    assert counts[0]==q*q+q+1,(q,counts)
    assert counts[1]==(q*q+q+1)*q*q,(q,counts)
    return {'field':q,'rref_planes':rref_total,'abelian_planes':sum(counts.values()),'open':counts[1],'boundary':counts[0]}

def symbolic():
    a1,a2,a3,b1,c1,c2,c3,b2=S.symbols('a1 a2 a3 b1 c1 c2 c3 b2')
    A=S.Matrix([a1,a2,a3]); C=S.Matrix([c1,c2,c3]); B=S.Matrix([1,0,b1]);D=S.Matrix([0,1,b2]);
    eps=A.cross(D)+B.cross(C)
    # eps[2]=a1+c2; eps[0]=a2*b2-a3-b1*c2; eps[1]=-a1*b2+b1*c1-c3
    vals={c2:-a1,a3:a2*b2+b1*a1,c3:b1*c1-a1*b2}
    assert all(S.expand(e.subs(vals))==0 for e in eps)
    scalar=a1*a1+a2*c1
    base=A.cross(C)
    triple=[S.expand(e.subs(vals)) for e in base]
    assert all(S.expand(x-y)==0 for x,y in zip(triple,[b1*scalar,b2*scalar,-scalar]))
    print('LOCAL_EQUATIONS', [str(e) for e in triple],'ZERO_SET_IS_A1_CONE_TIMES_A2')

if __name__=='__main__':
    symbolic()
    for q in [3,5]: print('FINITE_FIELD',count(q))
    print('VERIFY_OK')
