#!/usr/bin/env python3
"""Independent finite checks for an exact dihedral character formula.
Only standard-library integer arithmetic is used.
The proof for arbitrary polygon length is in RESULT.md.
"""
from itertools import combinations


def arcs(m):
    return [(v,s) for v in range(m) for s in (1,-1)]


def valid(m, selected):
    aa=arcs(m)
    src=set(); target=set(); unor=set()
    for j in selected:
        v,s=aa[j]; w=(v+s)%m
        edge=frozenset((v,w))
        if v in src or w in target or edge in unor: return False
        src.add(v);target.add(w);unor.add(edge)
    if len(selected)==m and all(aa[j][1]==1 for j in selected): return False
    if len(selected)==m and all(aa[j][1]==-1 for j in selected): return False
    return True


def idx_perm(m, kind, r):
    aa=arcs(m);index={a:j for j,a in enumerate(aa)}
    if kind=='rot': return [index[((v+r)%m,s)] for v,s in aa]
    return [index[((r-v)%m,-s)] for v,s in aa]


def pred_lefschetz(m, kind, r):
    if kind=='rot':
        from math import gcd
        d=gcd(m,r)
        return 3 if d%4==2 else -1
    t=(m-3)//2 if m%2 else m//2-2+(r%2)
    return -1 if ((t-1)//2)%2 else 1


def brute_all_faces(m):
    aa=arcs(m); out=[]
    for mask in range(1<<(2*m)):
        b=[i for i in range(2*m) if mask>>i&1]
        if valid(m,b):out.append(b)
    return out


def signed_lefschetz(faces,p):
    ans=0
    for face in faces:
        if not face: continue
        fs=set(face);image=[p[j] for j in face]
        if set(image)!=fs: continue
        inv=sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)))
        ans+= (-1)**(len(face)-1+inv)
    return ans-1  # reduced Lefschetz removes the augmentation trace


def orbit_check(m,kind,r):
    p=idx_perm(m,kind,r);seen=set();good=[]
    for j in range(2*m):
        if j in seen: continue
        orb=[]; k=j
        while k not in seen:
            seen.add(k);orb.append(k);k=p[k]
        if valid(m,orb): good.append(tuple(orb))
    conflicts=[0]*len(good)
    for i in range(len(good)):
        for j in range(i+1,len(good)):
            if not valid(m, good[i]+good[j]):
                conflicts[i]|=1<<j
                conflicts[j]|=1<<i
    def rec(i,deny,chosen,sign):
        if i==len(good):
            union=[v for j in chosen for v in good[j]]
            return sign if valid(m,union) else 0
        a=rec(i+1,deny,chosen,sign)
        if not (deny>>i)&1:
            a+=rec(i+1,deny|conflicts[i],chosen+(i,),-sign)
        return a
    return -rec(0,0,(),1)


def gf2_rank(columns):
    pivots={}
    for x in columns:
        while x:
            j=x.bit_length()-1
            if j not in pivots:
                pivots[j]=x;break
            x ^=pivots[j]
    return len(pivots)


def betti(m,faces):
    fs={}
    for f in faces:
        fs.setdefault(len(f)-1,[]).append(tuple(f))
    ranks={}
    for d in range(1,max(fs)+1):
        lower={f:j for j,f in enumerate(fs[d-1])}
        cols=[]
        for f in fs.get(d,[]):
            mask=0
            for a in range(len(f)):
                mask^=1<<lower[f[:a]+f[a+1:]]
            cols.append(mask)
        ranks[d]=gf2_rank(cols)
    return [len(fs[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(max(fs)+1)]


def betti_pred(m):
    n=m-1; h=(n-1)//2+(1 if n%4==0 else 0)
    b=[0]*(n)
    b[0]=1
    b[n-1]+=2
    b[h]+=3 if n%4==3 else 1
    return b


def main():
    face_total=0;checks=0
    for m in range(3,9):
        f=brute_all_faces(m);face_total+=len(f)
        actual=betti(m,f)
        target=betti_pred(m)
        assert actual==target,(m,actual,target)
        for kind in ('rot','refl'):
            for r in range(m):
                actual=signed_lefschetz(f,idx_perm(m,kind,r))
                expected=pred_lefschetz(m,kind,r)
                assert actual==expected,(m,kind,r,actual,expected)
                checks+=1
    print('DIRECT_OK',face_total,'faces',checks,'signed simplicial traces, exact F2 boundary ranks')
    orbchecks=0
    for m in range(3,14):
        for kind in ('rot','refl'):
            for r in range(m):
                actual=orbit_check(m,kind,r)
                expected=pred_lefschetz(m,kind,r)
                assert actual==expected,(m,kind,r,actual,expected)
                orbchecks+=1
    print('ORBIT_OK',orbchecks,'dihedral elements checked')
    # Compare graded traces derived from Lefschetz formulas with the stated representations.
    for m in range(3,81):
        h=(m-2)//2+(1 if (m-1)%4==0 else 0)
        for r in range(m):
            le=pred_lefschetz(m,'rot',r)
            d=__import__('math').gcd(m,r)
            top=2*(-1)**(m-d)
            low=(-1)**h*(le-(-1)**(m-2)*top)
            expected=(3 if r%4==0 else -1) if m%4==0 else 1
            assert low==expected,(m,r,low,expected)
        for r in range(m):
            le=pred_lefschetz(m,'refl',r)
            low=(-1)**h*le
            if m%4==0: expected=(-1)**(m//4-1+r)
            elif m%2: expected=(-1)**((m-5)//4)
            else: expected=(-1)**((m-6)//4)
            assert low==expected,(m,r,low,expected)
    print('CHARACTER_OK','m=3..80, complete dihedral representation identities')
    print('VERIFY_OK')

if __name__=='__main__':main()
