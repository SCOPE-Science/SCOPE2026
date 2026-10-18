#!/usr/bin/env python3
"""Exact geometric smoothness and finite dynamics census for (2,2) forms over F2.
Uses standalone F16 arithmetic; no computer algebra dependency.
"""
from collections import Counter

MOD = 0b10011  # t^4+t+1

def gf_mul(a,b):
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a&16:a^=MOD
    return z

def gp(a,n):
    z=1
    for _ in range(n):z=gf_mul(z,a)
    return z

proj=[(1,a) for a in range(16)]+[(0,1)]
mons=[(i,j) for i in range(3) for j in range(3)]

def eval_at(mask,x,y):
    a,b=x;c,d=y
    ax=[1,a,gf_mul(a,a)]
    bx=[1,b,gf_mul(b,b)]
    cy=[1,c,gf_mul(c,c)]
    dy=[1,d,gf_mul(d,d)]
    f=fxa=fxb=fyc=fyd=0
    for k,(i,j) in enumerate(mons):
        if not (mask>>k)&1:continue
        xm=gf_mul(ax[2-i],bx[i]);ym=gf_mul(cy[2-j],dy[j]);f^=gf_mul(xm,ym)
        if i==1:
            fxa^=gf_mul(b,ym);fxb^=gf_mul(a,ym)
        if j==1:
            fyc^=gf_mul(xm,d);fyd^=gf_mul(xm,c)
    return f,fxa,fxb,fyc,fyd

def smooth(mask):
    for x in proj:
        for y in proj:
            if eval_at(mask,x,y)==(0,0,0,0,0):return False
    return True

qpts=[(1,0),(1,1),(0,1)]

def profile(mask):
    p=[(i,j) for i,x in enumerate(qpts) for j,y in enumerate(qpts) if eval_at(mask,x,y)[0]==0]
    n=len(p)
    def swap_fibre(axis):
        mapping={}
        for a in p:
            ps=[b for b in p if b[axis]==a[axis]]
            assert 1<=len(ps)<=2,(mask,axis,a,ps)
            mapping[a]= next((b for b in ps if b!=a),a)
        return mapping
    a=swap_fibre(0);b=swap_fibre(1)
    t={z:b[a[z]] for z in p}
    cur={z:z for z in p}
    for order in range(1,7):
        cur={z:t[cur[z]] for z in p}
        if all(cur[z]==z for z in p):break
    else:raise AssertionError('not periodic')
    ram=tuple(sorted(sum(sum(z[k]==v for z in p)==1 for v in range(3)) for k in (0,1)))
    return n,ram,order

# Homogeneous coordinate-generator substitution on binary quadratics.
# 0: X0' = X1; X1' = X0, 1: X0'=X0+X1; X1'=X1.
def subquad(index,kind):
    if kind=='swap':pairs=((0,1),(1,0))
    elif kind=='shear':pairs=((1,1),(0,1))
    else:raise ValueError(kind)
    def mul_pair(v,w):
        return (v[0]&w[0],(v[0]&w[1])^(v[1]&w[0]),v[1]&w[1])
    return mul_pair(pairs[0],pairs[0]) if index==0 else (mul_pair(pairs[0],pairs[1]) if index==1 else mul_pair(pairs[1],pairs[1]))

def act(mask,what):
    ans=0
    for k,(i,j) in enumerate(mons):
        if not (mask&(1<<k)):continue
        if what=='interchange':ans^=1<<(3*j+i)
        else:
            ax,kind=what
            vs=subquad(i if ax==0 else j,kind)
            for new,b in enumerate(vs):
                if b:ans^=1<<(3*(new if ax==0 else i)+(new if ax==1 else j))
    return ans

def compute():
    gens=[(0,'swap'),(0,'shear'),(1,'swap'),(1,'shear'),'interchange']
    smooths={m for m in range(1,512) if smooth(m)}
    # An independent check of the observed sharp singularity-witness field.
    all_singular=Counter()
    for m in range(1,512):
        if m in smooths:continue
        pts=[(a,b) for a in proj for b in proj if eval_at(m,a,b)==(0,0,0,0,0)]
        assert pts
        def degree(coord):
            if coord==(0,1) or coord[1] in (0,1):return 1
            if gp(coord[1],4)==coord[1]:return 2
            return 4
        all_singular[min(max(degree(a),degree(b)) for a,b in pts)]+=1
    print('MINIMAL_SINGULAR_DEGREES',sorted(all_singular.items()))
    assert all_singular==Counter({1:318,2:49})
    seen=set();groups=[]
    for m in sorted(smooths):
        if m in seen:continue
        orbit={m};stack=[m]
        for u in stack:
            for g in gens:
                v=act(u,g)
                if v not in orbit:orbit.add(v);stack.append(v)
        assert orbit<=smooths and not (orbit&seen)
        seen|=orbit
        prof={profile(u) for u in orbit}
        assert len(prof)==1,(m,prof)
        groups.append((m,len(orbit),next(iter(prof))))
    assert seen==smooths
    hist=Counter();nclasses=Counter()
    for m,count,pr in groups:
        hist[pr]+=count;nclasses[pr]+=1
    print('SMOOTH_FORMS',len(smooths))
    print('NUMBER_ORBITS',len(groups))
    print('PROFILE,FORMS,ORBITS,REPRESENTATIVE')
    for m,count,pr in groups:print(pr,count,1,m)
    print('HISTOGRAM',sorted(hist.items()))
    assert len(smooths)==144 and len(groups)==6
    assert sorted((m,l,p) for m,l,p in groups)==[(98,36,(3,(1,1),3)),(99,36,(5,(1,1),5)),(113,9,(4,(2,2),2)),(121,18,(2,(0,2),2)),(122,36,(4,(0,2),4)),(186,9,(4,(0,0),2))]
    print('VERIFIED_OK')
if __name__=='__main__':compute()
