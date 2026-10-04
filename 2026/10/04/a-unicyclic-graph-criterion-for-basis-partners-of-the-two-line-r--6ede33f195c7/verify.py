#!/usr/bin/env python3
"""Exact finite replay for the unicyclic basis-partner criterion.

Uses only integer arithmetic modulo primes q == 1 (mod p).  The theorem itself is
proved over C in RESULT.md; these finite checks are consistency tests, not the proof.
"""
from itertools import combinations
from math import gcd


def invmod(a,q):
    return pow(a, q-2, q)


def det_mod(A,q):
    A=[row[:] for row in A]
    n=len(A); d=1
    for j in range(n):
        piv=next((i for i in range(j,n) if A[i][j]%q),None)
        if piv is None: return 0
        if piv!=j:
            A[j],A[piv]=A[piv],A[j]; d=(-d)%q
        a=A[j][j]%q; d=d*a%q
        ia=invmod(a,q)
        for i in range(j+1,n):
            if A[i][j]%q:
                f=A[i][j]*ia%q
                for k in range(j,n): A[i][k]=(A[i][k]-f*A[j][k])%q
    return d%q


def order_p_root(p,q):
    assert (q-1)%p==0
    for g in range(2,q):
        r=pow(g,(q-1)//p,q)
        if r!=1 and pow(r,p,q)==1:
            return r
    raise RuntimeError('no pth root')


def eval_matrix(p,B,r,q):
    E=[(0,y) for y in range(p)] + [(t,t) for t in range(1,p)] + [(1,0)]
    return [[pow(r,(a*x+b*y)%p,q) for (a,b) in B] for (x,y) in E]


def graph_data(p,B):
    # Edge e=(a,b) joins left b to right c=a+b.
    edges=[(b,(a+b)%p,a) for a,b in B]
    Ladj=[[] for _ in range(p)]; Radj=[[] for _ in range(p)]
    for i,(b,c,a) in enumerate(edges): Ladj[b].append(i); Radj[c].append(i)
    nonL=sum(bool(x) for x in Ladj); nonR=sum(bool(x) for x in Radj)
    n=nonL+nonR
    seenE=set(); comps=0
    for ei in range(len(edges)):
        if ei in seenE: continue
        comps+=1; stack=[ei]; seenE.add(ei)
        while stack:
            e=stack.pop(); b,c,_=edges[e]
            for f in Ladj[b]+Radj[c]:
                if f not in seenE: seenE.add(f); stack.append(f)
    beta=len(edges)-n+comps
    spanning=(n==2*p)
    connected=(comps==1)
    if not (spanning and connected and beta==1):
        return {'beta':beta,'spanning':spanning,'connected':connected,'cycle':None,'signs':None,'edges':edges}
    # Peel leaves; remaining edges are the unique cycle.
    alive=[True]*len(edges); dL=[len(x) for x in Ladj]; dR=[len(x) for x in Radj]
    queue=[('L',i) for i,d in enumerate(dL) if d==1]+[('R',i) for i,d in enumerate(dR) if d==1]
    qi=0
    while qi<len(queue):
        side,v=queue[qi]; qi+=1
        adj=Ladj[v] if side=='L' else Radj[v]
        e=next((e for e in adj if alive[e]),None)
        if e is None: continue
        alive[e]=False; b,c,_=edges[e]; dL[b]-=1; dR[c]-=1
        if dL[b]==1: queue.append(('L',b))
        if dR[c]==1: queue.append(('R',c))
    cyc=[i for i,x in enumerate(alive) if x]
    signs={cyc[0]:1}
    changed=True
    while changed:
        changed=False
        for adj in Ladj+Radj:
            es=[e for e in adj if alive[e]]
            if len(es)==2:
                x,y=es
                if x in signs and y not in signs: signs[y]=-signs[x]; changed=True
                elif y in signs and x not in signs: signs[x]=-signs[y]; changed=True
    assert len(signs)==len(cyc)
    return {'beta':beta,'spanning':spanning,'connected':connected,'cycle':cyc,'signs':signs,'edges':edges}


def cycle_coeffs(p,gd):
    d=[0]*p
    for e in gd['cycle']:
        d[gd['edges'][e][2]%p]+=gd['signs'][e]
    assert sum(d)==0
    return d

def cycle_sum_mod(p,gd,r,q):
    return sum(gd['signs'][e]*pow(r,gd['edges'][e][2]%p,q) for e in gd['cycle'])%q


def predicts_basis(p,B,r,q):
    gd=graph_data(p,B)
    if gd['cycle'] is None: return False,gd,0
    s=cycle_sum_mod(p,gd,r,q)
    # For complex pth roots, S=0 iff the coefficient polynomial is zero modulo Phi_p.
    # Reduction at this q is only a replay witness; accepted samples below use primes
    # at which S and its conjugate product are nonzero.
    return s!=0,gd,s


def explicit_B(p):
    BC={(0,0),(0,1),(1,0),(1,1)} # graph edges (b,c)
    BC.update((b,0) for b in range(2,p))
    BC.update((0,c) for c in range(2,p))
    return sorted((((c-b)%p,b) for b,c in BC))


def lcg_subsets(p,count):
    # deterministic, dependency-free sample of distinct 2p-subsets
    freqs=[(a,b) for a in range(p) for b in range(p)]
    x=0x243f6a8885a308d3 & ((1<<64)-1)
    seen=set(); out=[]
    while len(out)<count:
        keys=[]
        for i in range(len(freqs)):
            x=(6364136223846793005*x+1442695040888963407)&((1<<64)-1)
            keys.append((x,i))
        idx=tuple(sorted(i for _,i in sorted(keys)[:2*p]))
        if idx not in seen:
            seen.add(idx); out.append([freqs[i] for i in idx])
    return out


def check_one(p,B,qs):
    gd0=graph_data(p,B)
    # Graph criterion over C: if not spanning connected unicyclic, singular analytically.
    for q in qs:
        r=order_p_root(p,q)
        M=eval_matrix(p,B,r,q); d=det_mod(M,q)
        if gd0['cycle'] is None:
            assert d==0, (p,q,'structural singularity failed')
        else:
            s=cycle_sum_mod(p,gd0,r,q)
            # Exact determinant-norm identity after specializing zeta_p -> r:
            # det(r)*det(r^{-1}) = p^(2p) S(r) S(r^{-1}).
            rinv=invmod(r,q)
            dc=det_mod(eval_matrix(p,B,rinv,q),q)
            sc=cycle_sum_mod(p,gd0,rinv,q)
            assert d*dc%q == pow(p,2*p,q)*s*sc%q, (p,q,'det norm')
    return True


def main():
    # Exhaust all C(9,6)=84 candidates for p=3 at two exact specializations.
    p=3; freqs=[(a,b) for a in range(p) for b in range(p)]
    bases=0
    for B in combinations(freqs,2*p):
        B=list(B); gd=graph_data(p,B)
        check_one(p,B,[7,13])
        # Complex-zero criterion for p=3 can be checked coefficientwise: S=0 iff
        # plus/minus exponent multiplicities agree after Phi_3 reduction.  Direct
        # modular agreement at both q is sufficient for this finite replay census.
        ok=(gd['cycle'] is not None and any(cycle_coeffs(p,gd)))
        if ok: bases+=1
    assert bases==75

    total=84
    # Structured explicit family and deterministic samples in larger prime dimensions.
    for p,qs,count in [(5,[11,31],120),(7,[29,43],120),(11,[23,67],80)]:
        B=explicit_B(p); check_one(p,B,qs); total+=1
        gd=graph_data(p,B); assert gd['cycle'] is not None and len(gd['cycle'])==4 and any(cycle_coeffs(p,gd))
        for B in lcg_subsets(p,count):
            check_one(p,B,qs); total+=1
    print(f'VERIFY_OK exact_modular_cases={total} exhaustive_p3=84 p3_bases=75')

if __name__=='__main__': main()
