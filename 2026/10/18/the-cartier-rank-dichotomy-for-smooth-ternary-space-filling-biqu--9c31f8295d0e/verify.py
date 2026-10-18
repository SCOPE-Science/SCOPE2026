#!/usr/bin/env python3
"""Exact, reproducible census and Hasse--Witt verification over F_3.

Python >= 3.10; sympy >= 1.12. No external datasets or online access.
"""
from itertools import product
from math import comb
from sympy import symbols, groebner, Poly

p=3
P=[0,1,0,2,0]  # U0^3 U1 - U0 U1^3
pow3=[3**i for i in range(9)]

def dec(k): return tuple((k//pow3[i])%3 for i in range(9))
def enc(v): return sum(d*pow3[i] for i,d in enumerate(v))
def unf(v): return list(v[:5]),[v[5],0,v[6],v[7],v[8]]
def canon(a,b):
    t=b[1]%3
    a=[(a[i]+t*P[i])%3 for i in range(5)]
    b=[(b[i]-t*P[i])%3 for i in range(5)]
    assert b[1]==0
    return tuple(a)+(b[0],b[2],b[3],b[4])
def normal(v):
    s=next((d for d in v if d),0)
    return tuple((s*d)%3 for d in v) if s else tuple(v)

def transform4(a,H):
    r,s,t,u=H
    out=[0]*5
    for i,c in enumerate(a):
        for j in range(5-i):
            for k in range(i+1):
                f=comb(4-i,j)*comb(i,k)*r**(4-i-j)*s**j*t**(i-k)*u**k
                out[j+k]=(out[j+k]+c*f)%3
    return out

def transform(v,H,axis):
    a,b=unf(v);r,s,t,u=H;det=(r*u-s*t)%3
    if axis=='x': return canon([(det*d)%3 for d in a],transform4(b,H))
    return canon(transform4(a,H),[(det*d)%3 for d in b])

def generators():
    Ms=[]
    for axis in 'xy':
        for H in [(0,1,1,0),(1,1,0,1),(2,0,0,1)]:
            cols=[]
            for i in range(9):
                e=[0]*9;e[i]=1;cols.append(transform(e,H,axis))
            Ms.append(tuple(zip(*cols)))
    cols=[]
    for i in range(9):
        e=[0]*9;e[i]=1;a,b=unf(e);cols.append(canon(b,a))
    return Ms,tuple(zip(*cols))

def act(v,M):
    return normal(tuple(sum(M[i][j]*v[j] for j in range(9))%3 for i in range(9)))

def orbits(indices,Ms):
    unseen=set(indices);out=[]
    while unseen:
        rep=min(unseen);todo=[rep];unseen.remove(rep);n=0
        while todo:
            k=todo.pop();n+=1;v=dec(k)
            for M in Ms:
                x=enc(act(v,M))
                if x in unseen:
                    unseen.remove(x);todo.append(x)
        out.append((rep,n))
    return out

def eval4(a,t):
    if t==3:return a[4]
    return sum(a[i]*pow(t,i,3) for i in range(5))%3

def rational_smooth(v):
    a,b=unf(v)
    return all(eval4(a,t)!=0 for t in range(4)) or all(eval4(b,t)!=0 for t in range(4))

x,y=symbols('x y')
def poly4(a,c,z):return sum(a[i]*z**(i if c==0 else 4-i) for i in range(5))
def geometric_smooth(v):
    a,b=unf(v)
    for cx in (0,1):
        for cy in (0,1):
            f=poly4(P,cx,x)*poly4(a,cy,y)+poly4(P,cy,y)*poly4(b,cx,x)
            g=groebner((f,f.diff(x),f.diff(y)),x,y,modulus=3,order='grevlex')
            if not (len(g.polys)==1 and g.polys[0].as_expr()==1):return False
    return True

def coeff_F(v):
    a,b=unf(v);return {(i,j):(P[i]*a[j]+b[i]*P[j])%3 for i in range(5) for j in range(5)}
def hasse_witt(v):
    fs=coeff_F(v);sq={}
    for (i,j),a in fs.items():
        for (k,l),b in fs.items():
            ij=(i+k,j+l)
            sq[ij]=(sq.get(ij,0)+a*b)%3
    idx=list(product(range(1,4),repeat=2))
    return [[sq.get((3*i-k,3*j-l),0) for k,l in idx] for i,j in idx]

def mm(A,B):
    return [[sum(u*v for u,v in zip(row,col))%3 for col in zip(*B)] for row in A]

def rank(A):
    A=[list(row) for row in A];rows=len(A);columns=len(A[0]);r=0
    for j in range(columns):
        k=next((k for k in range(r,rows) if A[k][j]),None)
        if k is None:continue
        A[r],A[k]=A[k],A[r]
        inv=1 if A[r][j]==1 else 2
        A[r]=[(v*inv)%3 for v in A[r]]
        for k in range(rows):
            if k!=r and A[k][j]:
                c=A[k][j];A[k]=[(u-c*v)%3 for u,v in zip(A[k],A[r])]
        r+=1
        if r==rows:break
    return r

def finite_field(n):
    # Fixed monic irreducibles of degrees 1,2,3,4 over F_3.
    mods={1:[0,1],2:[1,0,1],3:[1,2,0,1],4:[2,1,0,0,1]}
    poly=mods[n];q=3**n
    z=symbols("z")
    assert Poly(sum(poly[i]*z**i for i in range(n+1)),z,modulus=3).is_irreducible
    def digits(k):return [(k//3**i)%3 for i in range(n)]
    ds=[digits(k) for k in range(q)]
    def encd(z):return sum((v%3)*3**i for i,v in enumerate(z))
    add=[[encd([(a[i]+b[i])%3 for i in range(n)]) for b in ds] for a in ds]
    mul=[]
    for a in ds:
        row=[]
        for b in ds:
            w=[0]*(2*n-1)
            for i,u in enumerate(a):
                for j,v in enumerate(b):w[i+j]=(w[i+j]+u*v)%3
            for k in range(2*n-2,n-1,-1):
                for j in range(n):w[k-n+j]=(w[k-n+j]-w[k]*poly[j])%3
            row.append(encd(w[:n]))
        mul.append(row)
    return add,mul

def point_count(v,n):
    a,b=unf(v);add,mul=finite_field(n);q=3**n
    def eval_poly(c,t):
        if t==q:return c[4]
        s=0
        for w in reversed(c):s=add[mul[s][t]][w]
        return s
    def eval_P(t):
        if t==q:return 0
        t2=mul[t][t];t3=mul[t2][t]
        return add[t][mul[2][t3]]
    va=[eval_poly(a,t) for t in range(q+1)]
    vb=[eval_poly(b,t) for t in range(q+1)]
    vp=[eval_P(t) for t in range(q+1)]
    return sum(add[mul[vp[u]][va[v]]][mul[vp[v]][vb[u]]]==0 for u in range(q+1) for v in range(q+1))

def projective_group_order():
    hs=[(0,1,1,0),(1,1,0,1),(2,0,0,1)]
    def nc(a):
        k=next(v for v in a if v)
        return tuple((k*v)%3 for v in a)
    def times(a,b):
        r,s,t,u=a;v,w,z,h=b
        return ((r*v+s*z)%3,(r*w+s*h)%3,(t*v+u*z)%3,(t*w+u*h)%3)
    seen={nc((1,0,0,1))};todo=list(seen)
    while todo:
        x=todo.pop()
        for h in hs:
            y=nc(times(x,h))
            if y not in seen:seen.add(y);todo.append(y)
    return len(seen)

def main():
    assert projective_group_order()==24
    Ms,swap=generators()
    projective=[k for k in range(1,3**9) if next(w for w in dec(k) if w)!=2]
    assert len(projective)==9841
    rational=[k for k in projective if rational_smooth(dec(k))]
    assert len(rational)==3504
    group_orbits=orbits(rational,Ms)
    assert len(group_orbits)==56
    smooth=[(rep,size) for rep,size in group_orbits if geometric_smooth(dec(rep))]
    assert len(smooth)==7 and sorted(size for rep,size in smooth)==[18,18,24,24,36,72,72]
    assert sum(size for rep,size in smooth)==264
    # Extend from factor-preserving group to the full rational automorphism group.
    # Representatives plus swapping determine the full classes: BFS under all seven generators.
    owned={}
    for rep,size in smooth:
        todo=[rep];seen={rep}
        while todo:
            v=dec(todo.pop())
            for M in Ms:
                z=enc(act(v,M))
                if z not in seen:seen.add(z);todo.append(z)
        assert len(seen)==size
        for k in seen:owned[k]=rep
    assert len(owned)==264
    # All three syzygy presentations of every smooth scalar class have
    # root-free binary quartics in both factors; including two scalar
    # choices yields the published 1584-presentation count.
    pair_presentations=0
    for k in owned:
        a,b=unf(dec(k))
        for t in range(3):
            aa=[(a[i]-t*P[i])%3 for i in range(5)]
            bb=[(b[i]+t*P[i])%3 for i in range(5)]
            if all(eval4(aa,u)!=0 for u in range(4)) and all(eval4(bb,u)!=0 for u in range(4)):
                pair_presentations+=2
    assert pair_presentations==1584
    full_unseen=set(owned);full_sizes=[];ordinary_sizes=[];nonordinary_sizes=[]
    while full_unseen:
        seed=next(iter(full_unseen));todo=[seed];full_unseen.remove(seed);n=0;representative_orbits=set()
        while todo:
            k=todo.pop();n+=1;representative_orbits.add(owned[k]);v=dec(k)
            for M in Ms+[swap]:
                z=enc(act(v,M))
                assert z in owned
                if z in full_unseen:full_unseen.remove(z);todo.append(z)
        full_sizes.append(n)
        H=hasse_witt(dec(seed));r=rank(H)
        if r==9:ordinary_sizes.append(n)
        else:nonordinary_sizes.append(n)
    assert sorted(full_sizes)==[36,36,48,144]
    assert sorted(ordinary_sizes)==[48] and sorted(nonordinary_sizes)==[36,36,144]
    for rep,size in sorted(smooth):
        v=dec(rep);H=hasse_witt(v);r=rank(H)
        Q=H
        for _ in range(8):Q=mm(Q,H)
        stable=rank(Q)
        assert (r,stable) in {(8,8),(9,9)}
        for n in range(1,5):
            N=point_count(v,n)
            power=H
            for _ in range(n-1):power=mm(power,H)
            assert N%3==(1-sum(power[i][i] for i in range(9)))%3
        print(f'orient_rep={rep} orbit_size={size} Cartier_rank={r} p_rank={stable} a_number={9-r} finite_point_checks=4/4')
    print('PASS projective=9841 rational_smooth=3504 geometrically_smooth=264 pair_presentations=1584')
    print('PASS factor_preserving_orbits=7 full_orbit_sizes='+str(sorted(full_sizes)))
    print('PASS ordinary=48 nonordinary=216; p_ranks=9,8; a_numbers=0,1')

if __name__=='__main__':main()
