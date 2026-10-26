#!/usr/bin/env python3
"""Exact integer-ring verification of Hermitian spectra of oriented cycle bouquets.

The sixth root zeta satisfies zeta*zeta=zeta-1.  Matrices are evaluated
inside Z[zeta], without floating-point eigenvalue comparisons.
"""
import itertools
import random
from math import comb

Z=(0,0); ONE=(1,0); ZETA=(0,1); INV_ZETA=(1,-1)
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y):
    a,b=x;c,d=y
    return (a*c-b*d,a*d+b*c+b*d)

def graph(lengths):
    edges=[];cycles=[]; nxt=1
    for ell in lengths:
        verts=[0]+list(range(nxt,nxt+ell-1));nxt+=ell-1
        ids=[]
        for u,v in zip(verts,verts[1:]+[0]):
            ids.append(len(edges));edges.append((u,v))
        cycles.append(ids)
    return nxt,edges,cycles

def characteristic(n,edges,bits):
    # Faddeev-LeVerrier with exact arithmetic in Z[zeta].
    H=[[Z for _ in range(n)] for _ in range(n)]
    for j,(u,v) in enumerate(edges):
        w=ZETA if ((bits>>j)&1) else INV_ZETA
        H[u][v]=w;H[v][u]=(1-w[0],-w[1]) # conjugation: a+b*zeta -> (a+b)-b*zeta
    B=[[ONE if i==j else Z for j in range(n)] for i in range(n)]
    coeff=[1]
    for k in range(1,n+1):
        C=[[Z for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for t in range(n):
                if H[i][t]==Z: continue
                for j in range(n):
                    if B[t][j]!=Z:
                        C[i][j]=add(C[i][j],mul(H[i][t],B[t][j]))
        tr=(sum(C[i][i][0] for i in range(n)),sum(C[i][i][1] for i in range(n)))
        assert tr[0]%k==0 and tr[1]%k==0
        c=(-tr[0]//k,-tr[1]//k)
        assert c[1]==0, ('nonrational coefficient',k,c)
        coeff.append(c[0]);
        for i in range(n): C[i][i]=add(C[i][i],c)
        B=C
    return coeff

def polyadd(a,b):
    out=[0]*max(len(a),len(b))
    for i,v in enumerate(a):out[i]+=v
    for i,v in enumerate(b):out[i]+=v
    return out

def neg(a):return [-x for x in a]
def polymul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def pathpoly(k):
    x0=[1];x1=[0,1]
    if k==0:return x0
    for i in range(2,k+1):x0,x1=x1,polyadd([0]+x1,neg(x0))
    return x1

def cyclerealweight(cycle,bits):
    s=sum(1 if bits>>e & 1 else -1 for e in cycle)
    return {0:2,1:1,2:-1,3:-2,4:-1,5:1}[s%6]

def formula_poly(lengths,cycles,bits):
    p=[pathpoly(ell-1) for ell in lengths]
    # x * product(P_l-1) - 2 * sum(P_l-2 * product others)
    #                          - sum(gain_cycle * product others)
    out=[0]+list(__import__('functools').reduce(polymul,p,[1]))
    for j,ell in enumerate(lengths):
        rest=__import__('functools').reduce(polymul,(p[t] for t in range(len(p)) if t!=j),[1])
        piece=polymul(polyadd([2*x for x in pathpoly(ell-2)],[cyclerealweight(cycles[j],bits)]),rest)
        out=polyadd(out,neg(piece))
    return out

def prediction(lengths,cycles,bits):
    for ell in sorted(set(lengths)):
        if ell%2==0:continue
        if sum(cyclerealweight(cycles[i],bits) for i,t in enumerate(lengths) if t==ell)!=0:return False
    return True

def actual_count(lengths):
    n,edges,cycles=graph(lengths)
    if any(sum(ell==e for e in lengths)%3 for ell in set(lengths) if ell%2):return 0
    z=1
    for ell in sorted(set(lengths)):
        k=lengths.count(ell)
        if ell%2==0:z*=2**(ell*k)
        else:
            bad=(2**ell-2)//3;good=(2**(ell+1)+2)//3
            z*=comb(k,k//3)*bad**(k//3)*good**(2*k//3)
    return z

def run():
    rng=random.Random(48145)
    cases=0;counts={}
    for lengths in [(3,),(3,3),(3,3,3),(3,4),(3,3,3,4),(5,5,5),(3,3,3,5), (3,5,5,5),(3,4,5),(4,4),(3,3,3,3)]:
        n,edges,cycles=graph(lengths)
        m=len(edges)
        if lengths==(3,3,3):samples=list(range(1<<m))
        elif m<=7:samples=list(range(1<<m))
        else:
            samples=[0,(1<<m)-1]+[rng.randrange(1<<m) for _ in range(22)]
        found=0
        for bits in samples:
            cs=characteristic(n,edges,bits)
            expected=formula_poly(lengths,cycles,bits)
            assert cs==list(reversed(expected)),(lengths,bits,cs,expected)
            actual=all(cs[j]==0 for j in range(1,len(cs),2))
            expected_sym=prediction(lengths,cycles,bits)
            assert actual==expected_sym,(lengths,bits,cs)
            cases+=1;found+=actual
        counts[str(lengths)]=(len(samples),found,actual_count(lengths))
        if lengths==(3,3,3):
            assert found==216==actual_count(lengths)
    # Count cycle phases directly, for four different odd sizes.
    for ell in (3,5,7,9):
        _,_,cycles=graph([ell]);c=cycles[0];neg=sum(cyclerealweight(c,b)==-2 for b in range(1<<ell))
        assert neg==(2**ell-2)//3
    print('VERIFY_OK exact_characteristic_checks=%d cycle_phase_sizes=3,5,7,9'%cases)
    for k,v in counts.items():print('case=%s samples=%d matching=%d predicted_total=%d'%(k,*v))
if __name__=='__main__':run()
