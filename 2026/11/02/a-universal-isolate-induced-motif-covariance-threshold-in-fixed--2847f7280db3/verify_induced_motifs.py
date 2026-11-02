"""Independent finite exact enumerations for induced-motif/isolate covariance.
Standard-library only. All probability calculations use fractions.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


def falling(x, k):
    if x < k:
        return 0
    z = 1
    for j in range(k):
        z *= x-j
    return z


def theoretical(n, m, h, e, aut):
    N = comb(n, 2)
    B = comb(n-1, 2)
    r = comb(h, 2)-e
    EI = Fraction(n*comb(B,m), comb(N,m)) if m <= B else Fraction(0)
    EX = Fraction(falling(n,h)*falling(m,e)*falling(N-m,r),
                  aut*falling(N,comb(h,2)))
    if m<=B and B>=comb(h,2):
        EX_given_isolate = Fraction(falling(n-1,h)*falling(m,e)*falling(B-m,r),
                                   aut*falling(B,comb(h,2)))
    else:
        EX_given_isolate = Fraction(0)
    return EI, EX, EI*(EX_given_isolate-EX)


def census(n, motifs):
    edges = list(combinations(range(n), 2))
    edge_index = {e:i for i,e in enumerate(edges)}
    vertex_masks = [sum(1<<j for j,(a,b) in enumerate(edges) if i in (a,b)) for i in range(n)]
    triples = [(1<<edge_index[e0],1<<edge_index[e1],1<<edge_index[e2])
               for a,b,c in combinations(range(n),3)
               for e0,e1,e2 in [[(a,b),(a,c),(b,c)]]]
    quartets = [tuple(edge_index[e] for e in combinations(q,2)) for q in combinations(range(n),4)]
    sums = [{k:[0,0,0] for k in motifs} for _ in range(len(edges)+1)]
    counts = [0]*(len(edges)+1)
    for mask in range(1<<len(edges)):
        m=mask.bit_count(); counts[m]+=1
        iso=sum((mask & vmask)==0 for vmask in vertex_masks)
        xvals={}
        if 'P3' in motifs:
            xvals['P3']=sum(bool(mask&a)+bool(mask&b)+bool(mask&c)==2 for a,b,c in triples)
        if 'C4' in motifs or 'P4' in motifs:
            count4={'C4':0,'P4':0}
            for q in quartets:
                loc=[int(bool(mask>>i&1)) for i in q]
                k=sum(loc)
                if k!=3 and k!=4: continue
                # six ordered pairs (01,02,03,12,13,23)
                deg=[loc[0]+loc[1]+loc[2], loc[0]+loc[3]+loc[4],
                     loc[1]+loc[3]+loc[5],loc[2]+loc[4]+loc[5]]
                if k==4 and all(d==2 for d in deg):count4['C4']+=1
                if k==3 and sorted(deg)==[1,1,2,2]:count4['P4']+=1
            for k in ['C4','P4']:
                if k in motifs:xvals[k]=count4[k]
        for kind,x in xvals.items():
            z=sums[m][kind];z[0]+=iso;z[1]+=x;z[2]+=iso*x
    checked=0
    for m, total in enumerate(counts):
        assert total==comb(len(edges),m)
        for kind,(h,e,aut) in motifs.items():
            ei,ex,eix=sums[m][kind]
            formula=theoretical(n,m,h,e,aut)
            assert Fraction(ei,total)==formula[0],(n,m,kind,'EI')
            assert Fraction(ex,total)==formula[1],(n,m,kind,'EX')
            assert Fraction(eix,total)-Fraction(ei*ex,total*total)==formula[2],(n,m,kind,'COV')
            checked+=3
    return checked,sum(counts)

if __name__=='__main__':
    checks=0;graphs=0
    for n in (4,5,6):
        c,g=census(n,{'P3':(3,2,2)})
        checks+=c;graphs+=g
    c,g=census(5,{'C4':(4,4,8),'P4':(4,3,2)})
    checks+=c;graphs+=g
    print(f'PASS exact identities: {checks}; independently enumerated labeled graphs (counting test families separately): {graphs}')
