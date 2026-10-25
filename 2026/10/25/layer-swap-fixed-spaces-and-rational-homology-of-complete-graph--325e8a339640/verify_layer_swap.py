#!/usr/bin/env python3
"""Finite independent face-enumeration checks for the layer-swap theorem."""
from itertools import combinations

def build_faces(n,m):
    q=n*m; masks=(1<<q)-1
    cross_allowed=[]
    for i in range(n):
        for j in range(m):
            cross_allowed.append(sum(1<<(a*m+b) for a in range(n) for b in range(m) if a==i or b==j))
    faces=[]
    for A in range(1<<q):
        allowed=masks
        x=A
        while x:
            bit=x&-x;x-=bit
            allowed &= cross_allowed[bit.bit_length()-1]
        B=allowed
        while True:
            if A or B:faces.append(A|(B<<q))
            if not B:break
            B=(B-1)&allowed
    return faces

def gf2rank(cols):
    piv={}
    for col in cols:
        while col:
            j=col.bit_length()-1
            if j in piv:col^=piv[j]
            else:piv[j]=col;break
    return len(piv)

def betti_mod2(faces):
    bydim={}
    for face in faces:bydim.setdefault(face.bit_count()-1,[]).append(face)
    top=max(bydim);r={0:0}
    for d in range(1,top+1):
        low={b:i for i,b in enumerate(bydim[d-1])}
        cols=[]
        for f in bydim[d]:
            c=0;x=f
            while x:
                bit=x&-x;x-=bit;c^=1<<low[f^bit]
            cols.append(c)
        r[d]=gf2rank(cols)
    r[top+1]=0
    return [len(bydim[d])-r[d]-r[d+1] for d in range(top+1)]

def fixed_orbit_faces(n,m):
    q=n*m
    out=[]
    for s in range(1,1<<q):
        vals=[i for i in range(q) if (s>>i)&1]
        if len({i//m for i in vals})==1 or len({i%m for i in vals})==1:out.append(s)
    return out

def checks():
    num=0
    for n,m in ((2,2),(2,3),(3,2),(2,4),(3,3)):
        faces=build_faces(n,m);q=n*m
        fixed_faces=[f for f in faces if (f&((1<<q)-1))==(f>>q)]
        base=fixed_orbit_faces(n,m)
        assert {f & ((1<<q)-1) for f in fixed_faces}==set(base)
        # An invariant face has k flipped pairs and contributes (-1)^(k+1) to Lefschetz.
        Lef=sum((-1)**(s.bit_count()+1) for s in base)
        b=(n-1)*(m-1)
        B=b*(n*m-2)//2
        assert Lef==1-b and (1-Lef)==b
        assert (B+b)%2==0 and (B-b)%2==0
        plus,minus=(B+b)//2,(B-b)//2
        assert plus==b*n*m//4 and minus==b*(n*m-4)//4
        if n*m<=9:
            bettis=betti_mod2(faces)
            assert bettis==[1,0,0,B]+[0]*(len(bettis)-4),(n,m,bettis,B)
        print('n,m',n,m,'faces',len(faces),'fixed_faces',len(fixed_faces),'H3_rank',B,'trace',b,'eigenspaces',plus,minus)
        num+=1
    print('LAYER_SWAP_FIXED_SPACE_AND_TRACE_CHECKS_PASSED',num)
if __name__=='__main__':checks()
