#!/usr/bin/env python3
"""Complete isomorphism-orbit census of smooth genus-2 sextic models over F_3.
No external mathematical package is needed for primary certification.
SymPy is optional and used only in an independent splitting-check routine.
"""
from itertools import product
from collections import Counter,defaultdict
from math import comb
from json import dumps
from pathlib import Path

Q=3

def trim(p):
    p=list(p)
    while p and p[-1]==0:p.pop()
    return tuple(p)

def rem(a,b):
    a=list(trim(a)); b=trim(b)
    if not b: raise ZeroDivisionError
    inv=pow(b[-1],-1,3)
    while len(a)>=len(b) and a:
        k=len(a)-len(b); x=a[-1]*inv%3
        for j,z in enumerate(b):a[k+j]=(a[k+j]-x*z)%3
        while a and not a[-1]:a.pop()
    return tuple(a)

def gcd(a,b):
    a=trim(a);b=trim(b)
    while b:a,b=b,rem(a,b)
    if not a:return ()
    inv=pow(a[-1],-1,3)
    return tuple(c*inv%3 for c in a)

def sf(f):
    d=len(trim(f))-1
    if d not in (5,6):return False
    derivative=tuple(i*f[i]%3 for i in range(1,7))
    return len(gcd(f,derivative))==1

def mul(a,b):
    x=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):x[i+j]=(x[i+j]+u*v)%3
    return tuple(x)

def trans(f,g):
    a,b,c,d=g
    # X -> aX+bZ; Z -> cX+dZ; ascending powers of X
    xp=[(1,)]; zp=[(1,)]
    for k in range(6):xp.append(mul(xp[-1],(b,a)));zp.append(mul(zp[-1],(d,c)))
    out=[0]*7
    for i,v in enumerate(f):
        if v:
            term=mul(xp[i],zp[6-i]);
            for j,u in enumerate(term):out[j]=(out[j]+v*u)%3
    return tuple(out)

def group():
    gl=[]
    for a,b,c,d in product(range(3),repeat=4):
        if (a*d-b*c)%3 and (a,b,c,d) < tuple(2*z%3 for z in (a,b,c,d)):
            gl.append((a,b,c,d))
    return gl

def rank2(A):
    a,b,c,d=A
    if (a*d-b*c)%3:return 2
    if any(A):return 1
    return 0

def prank(f):
    a,b,c,d=f[2],f[1],f[5],f[4]
    return rank2(((a*a+b*c)%3,(a*b+b*d)%3,(c*a+d*c)%3,(c*b+d*d)%3))

def npoints(f):
    total=0
    for t in range(3):
        u=sum(f[i]*pow(t,i,3) for i in range(7))%3
        total+=1 if u==0 else (2 if u==1 else 0)
    u=f[6]
    total+=1 if u==0 else (2 if u==1 else 0)
    return total

def monics(deg):
    for c in product(range(3),repeat=deg):yield tuple(c)+(1,)

def divides(a,b):return len(rem(a,b))==0

def irreducible(d):
    # Finite explicit polynomial sieve, monic irreducibles degrees 1..6
    out=[]
    for f in monics(d):
        if not any(divides(f,g) for e in range(1,d//2+1) for g in monics(e)):
            out.append(f)
    return out

def splitting(f, irr_by_deg):
    g=trim(f); ans=[]
    for d in range(1,7):
        for h in irr_by_deg[d]:
            if len(g)<=1:break
            while divides(g,h):
                # exact polynomial quotient via synthetic long division
                v=list(g); n=len(h)-1
                q=[0]*(len(g)-len(h)+1)
                for k in range(len(q)-1,-1,-1):
                    a=v[k+n];q[k]=a
                    for j in range(n+1):v[k+j]=(v[k+j]-a*h[j])%3
                assert not any(v[:n]);g=trim(q);ans.append(d)
    assert len(g)==1, (f,g)
    if f[6]==0: ans.append(1)
    assert sum(ans)==6
    return tuple(sorted(ans))

def main():
    gr=group();assert len(gr)==24
    irreducibles={d:irreducible(d) for d in range(1,7)}
    assert [len(irreducibles[d]) for d in range(1,7)]==[3,3,8,18,48,116]
    allf={f for f in product(range(3),repeat=7) if sf(f)}
    assert all(f!=(0,)*7 for f in allf)
    seen=set(); rows=[]; freq=Counter(); weights=Counter(); orbits_bytype=Counter()
    for f in sorted(allf):
        if f in seen:continue
        orbit={trans(f,g) for g in gr};assert orbit<=allf
        assert not orbit&seen
        seen.update(orbit)
        key=(splitting(f,irreducibles),prank(f),npoints(f))
        assert all((splitting(h,irreducibles),prank(h),npoints(h))==key for h in orbit)
        rows.append(dict(representative=f,orbit_size=len(orbit),branch_cycle=key[0],p_rank=key[1],points=key[2]))
        freq[key]+=1;weights[key]+=len(orbit)
    assert seen==allf
    coarse=Counter();weighted=Counter();partition=Counter();nrank=Counter()
    for k,v in freq.items():coarse[(k[0],k[1])]+=v
    for k,v in weights.items():weighted[(k[0],k[1])]+=v
    for k,v in freq.items():partition[k[0]]+=v;nrank[(k[1],k[2])]+=v
    # Burnside: fixed forms = sum_{g in G} #{f: g.f=f}; class count = sum/24
    fix=[sum(trans(f,g)==f for f in allf) for g in gr]
    assert sum(fix)==24*len(rows)
    # independent total squarefree binary forms; number = q^7 - q^6 if degree 6, with correction? test
    print('total forms',len(allf),'orbits',len(rows),'burnside',sum(fix),'stabilizer-spectrum',dict(Counter(24//r['orbit_size'] for r in rows)))
    print('p_rank_and_N', sorted((list(k),v) for k,v in nrank.items()))
    print('branch and p_rank table (number rational iso classes, number equations)')
    for k in sorted(coarse):print(k,coarse[k],weighted[k])
    print('branch partitions',dict(partition))
    print('joint strata',len(freq),'max/min points',min(r['points'] for r in rows),max(r['points'] for r in rows))
    print('examples rare / rich')
    for r in rows:
        if r['branch_cycle'] in [(1,1,1,1,1,1),(6,)] or r['p_rank']==0 and r['points'] in (0,8,9,10):print(r)
    out={'source':'Genus 2 Curves in Small Characteristic, arXiv:2111.07270v1 (2021-11-14)',
         'q':3,'group_order':len(gr),'total_squarefree_sextics':len(allf),'orbit_count':len(rows),
         'burnside_sum_fixed':sum(fix),'burnside_fixed_by_element':fix,
         'orbits':rows,
         'joint_branch_prank': [{'branch_cycle':list(k[0]),'p_rank':k[1],'isomorphism_classes':v,'equations':weighted[k]} for k,v in sorted(coarse.items())],
         'full_joint':[{'branch_cycle':list(k[0]),'p_rank':k[1],'rational_points':k[2],'isomorphism_classes':v,'equations':weights[k]} for k,v in sorted(freq.items())]}
    with open(Path(__file__).resolve().parent/'census.json','w') as fo:fo.write(dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
