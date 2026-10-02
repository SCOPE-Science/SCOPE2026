#!/usr/bin/env python3
"""Finite all-grades certificate for K(G2,2) sector tops and Zhu dimension.

Exact Freudenthal-Kac arithmetic is confined to grade <=2 for all 48 tops.
Dong-Ren's lattice-theta decomposition maps any later state in a sector to
one of these low grades at a shortest class representative. This script
verifies the finite data and the grade bound; see RESULT.md for the theorem.
"""
from fractions import Fraction

POS = ((1,0),(1,3),(2,3),(0,1),(1,1),(1,2))
ROOTS = POS + tuple((-a,-b) for a,b in POS)
RHO = (3,5)
LAMS = {"0":(0,0), "w1":(2,3), "w2":(1,2), "2w2":(2,4)}
CLASSES = tuple((i,j) for i in range(2) for j in range(6))
EXPECT = {
    "0":   ((0,1),(30,1),(48,3),(18,1),(48,3),(30,1),(18,1),(30,1),(30,1),(18,1),(30,1),(30,1)),
    "w1":  ((0,2),(-6,1),(12,3),(-18,1),(12,3),(-6,1),(-18,1),(-6,1),(-6,1),(-18,1),(-6,1),(-6,1)),
    "w2":  ((0,1),(-6,1),(12,3),(18,3),(12,3),(-6,1),(18,3),(-6,1),(-6,1),(18,3),(-6,1),(-6,1)),
    "2w2":((0,3),(-6,2),(-24,1),(-18,1),(-24,1),(-6,2),(-18,1),(-6,2),(-6,2),(-18,1),(-6,2),(-6,2)),
}
EMIN = (0,6,24,18,24,6,18,6,6,18,6,6)


def dot3(u,v):
    return 6*u[0]*v[0]-3*u[0]*v[1]-3*u[1]*v[0]+2*u[1]*v[1]


def e36(w):
    a,b=w
    return 18*a*a-18*a*b+6*b*b


def mults(lam, nmax, box):
    """Freudenthal-Kac recursion, exact rational and root-height ordered."""
    m={(0,lam):Fraction(1)}
    base=dot3((lam[0]+3,lam[1]+5),(lam[0]+3,lam[1]+5))
    keys=((n,(a,b)) for n in range(nmax+1) for a in range(-box,box+1) for b in range(-box,box+1))
    for n,w in sorted(keys,key=lambda t:(t[0],lam[0]+lam[1]-t[1][0]-t[1][1])):
        if (n,w)==(0,lam):
            continue
        wr=(w[0]+3,w[1]+5)
        den=base-dot3(wr,wr)+36*n
        if den==0:
            m[(n,w)]=Fraction(0)
            continue
        val=Fraction(0)
        for a,b in POS:
            j=1
            while abs(w[0]+j*a)<=box and abs(w[1]+j*b)<=box:
                ww=(w[0]+j*a,w[1]+j*b)
                val+=dot3(ww,(a,b))*m.get((n,ww),0)
                j+=1
        for np in range(1,n+1):
            for a,b in ROOTS:
                j=1
                while j*np<=n:
                    ww=(w[0]+j*a,w[1]+j*b)
                    if abs(ww[0])<=box and abs(ww[1])<=box:
                        val+=(dot3(ww,(a,b))+6*np)*m.get((n-j*np,ww),0)
                    j+=1
            j=1
            while j*np<=n:
                val+=12*np*m.get((n-j*np,w),0)
                j+=1
        m[(n,w)]=2*val/den
    return m


def shortest(cl):
    # E36 = 6(b-3a/2)^2 + 9a^2/2 = 18(a-b/2)^2 + 3b^2/2.
    # Outside |a|<=2 or |b|<=4 it exceeds 24, the largest class candidate.
    candidates=[(e36((a,b)),(a,b)) for a in range(-2,3) for b in range(-4,5)
                if a%2==cl[0] and b%6==cl[1]]
    return min(candidates)


def vacuum_character(m):
    exact=[m.get((n,(0,0)),Fraction(0)) for n in range(7)]
    assert all(v.denominator==1 and v>=0 for v in exact)
    string=[int(v) for v in exact]
    assert string==[1,2,11,35,114,317,847]
    eta=[1]+[0]*6
    for power in range(1,7):
        for _ in range(2):
            nxt=eta[:]
            for n in range(power,7):
                nxt[n]-=eta[n-power]
            eta=nxt
    character=[sum(eta[k]*string[n-k] for k in range(n+1)) for n in range(7)]
    assert character==[1,0,6,13,38,80,182]
    return string,character


def main():
    shortest_data=[shortest(cl) for cl in CLASSES]
    assert tuple(e for e,w in shortest_data)==EMIN
    zhu=0
    for name,lam in LAMS.items():
        m=mults(lam,2,14)
        found={}
        for (n,w),v in m.items():
            if not v:
                continue
            assert v.denominator==1 and v>=0, (name,n,w,v)
            cl=(w[0]%2,w[1]%6)
            f=36*n-e36(w)
            if cl not in found or f<found[cl][0]:
                found[cl]=(f,int(v))
        assert len(found)==12
        row=tuple(found[cl] for cl in CLASSES)
        assert row==EXPECT[name], (name,row)
        for cl,(f,t) in zip(CLASSES,row):
            emin,w0=shortest_data[CLASSES.index(cl)]
            assert (f+emin)%36==0
            n0=(f+emin)//36
            assert 0<=n0<=2
            assert all(m.get((n,w0),0)==0 for n in range(n0))
            assert m[(n0,w0)]==t, (name,cl,n0,w0,t,m.get((n0,w0)))
            zhu+=t*t
        print(name,"12 sectors, all shortest-representative top grades <=2")
    assert zhu==149
    vac=mults((0,0),6,20)
    string,character=vacuum_character(vac)
    print("ZHU_DIM",zhu,"VAC_STRING",string,"VAC_CHARACTER",character)
    print("VERIFY_OK: all 48 sectors and finite lattice-translation cutoff")


if __name__=="__main__":
    main()

