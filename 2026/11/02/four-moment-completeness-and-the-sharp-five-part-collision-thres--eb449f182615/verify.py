#!/usr/bin/env python3
"""Exact-rational spot checks of a complete-multipartite continuous-distance theorem.
Finite checks corroborate, but do not replace, the analytic proof.
"""
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement, product


def model(parts):
    N = sum(parts)
    P = {j: sum(a**j for a in parts) for j in range(1, 5)}
    p2, p3, p4 = P[2], P[3], P[4]
    m = (N*N-p2)//2
    O = (N+1)*p2-p3-N*N
    T = N**3-3*N*p2+2*p3
    A = O+T
    B = (p2*p2-p4)//2-N*p2+p3+m
    C = (N*N-p2)*(p2-N)-2*N*(p3-p2)+2*(p4-p3)
    F = m*m-m-A-B-C
    H = Q(2*B+C,2)
    assert min(m,O,T,B,C,F)>=0
    assert H == Q(sum(a*(a-1)*(N-a)*(N-a-1) for a in parts),2)
    assert N == 2 + Q(2*A-T,2*m)
    assert p3 == A+N**3-4*m*N+2*m
    assert p4 == 2*H-N*(N+1)*p2+N**3+2*N*p3-2*m
    return dict(N=N,P=P,m=m,S=m,O=O,T=T,A=A,B=B,C=C,F=F,H=H)


def graph(parts):
    labels = [i for i,a in enumerate(parts) for j in range(a)]
    edges = list((i,j) for i in range(len(labels)) for j in range(i+1,len(labels)) if labels[i]!=labels[j])
    return labels,edges


def category(a,b,labels):
    if a==b: return 'S'
    inter = set(a)&set(b)
    if inter:
        c=(set(a)|set(b))-inter
        j,k=tuple(c)
        return 'O' if labels[j]==labels[k] else 'T'
    z=len(set(labels[j] for j in a)&set(labels[j] for j in b))
    return ('F','C','B')[z]


def shortest(points,edge_a,edge_b,labels):
    x,y=points
    if edge_a==edge_b:
        return abs(x-y)
    d=lambda i,j: 0 if i==j else (2 if labels[i]==labels[j] else 1)
    u,v=edge_a; w,z=edge_b
    return min(x+y+d(u,w),x+(1-y)+d(u,z), (1-x)+y+d(v,w),(1-x)+(1-y)+d(v,z))


def kernel(t,x,y):
    if t=='S': return abs(x-y)
    if t=='O': return x+y
    if t=='T': return min(x+y,3-x-y)
    if t=='B': return 2-abs(x-y)
    if t=='C': return min(2-abs(x-y),3-x-y)
    if t=='F': return 1+min(x,1-x)+min(y,1-y)
    raise AssertionError(t)


def density_coeffs(P):
    m,O,T,B,C,F=(P[k] for k in ('m','O','T','B','C','F'))
    # Coefficients (constant, slope) on 0<t<1, 1<t<3/2, 3/2<t<2.
    return ((Q(2*m,m*m),Q(-2*m+O+T,m*m)),
            (Q(2*O+T-2*B-3*C-4*F,m*m),Q(-O+2*B+3*C+4*F,m*m)),
            (Q(2*O-2*B+3*C+8*F,m*m),Q(-O+2*B-C-4*F,m*m)))


def integral(P):
    co=density_coeffs(P)
    return sum(c*(hi-lo)+s*(hi*hi-lo*lo)/2 for (c,s),(lo,hi) in zip(co,((Q(0),Q(1)),(Q(1),Q(3,2)),(Q(3,2),Q(2)))))


def verify_one(parts):
    P=model(parts)
    lab,edges=graph(parts)
    counts={k:0 for k in ('S','O','T','B','C','F')}
    checks=0
    # Ignore graph vertices of zero arclength measure; all sampled points are interior.
    values=(Q(1,7),Q(3,7),Q(5,7))
    for e,f in product(edges,repeat=2):
        typ=category(e,f,lab)
        counts[typ]+=1
        # Orient the common-part endpoints consistently for class C and class B.
        for x,y in product(values,repeat=2):
            xx,yy=x,y
            if typ=='C':
                shared=(set(lab[k] for k in e)&set(lab[k] for k in f)).pop()
                xx=x if lab[e[0]]==shared else 1-x
                yy=y if lab[f[0]]==shared else 1-y
            if typ=='B':
                xx=x
                yy=y if lab[f[0]]==lab[e[0]] else 1-y
            if typ=='T' or typ=='O':
                shared=(set(e)&set(f)).pop()
                xx=x if e[0]==shared else 1-x
                yy=y if f[0]==shared else 1-y
            assert shortest((x,y),e,f,lab)==kernel(typ,xx,yy),(parts,e,f,typ,x,y)
            checks+=1
    assert all(counts[k]==P[k] for k in counts),(parts,counts,P)
    assert integral(P)==1,(parts,integral(P))
    co=density_coeffs(P)
    assert 2/co[0][0]==P['m']
    assert P['m']**2*co[0][1]+2*P['m']==P['A']
    left=co[1][0]+co[1][1]*Q(3,2)
    right=co[2][0]+co[2][1]*Q(3,2)
    assert P['m']**2*(left-right)==P['T']
    assert P['m']**2*(co[2][0]+2*co[2][1])/2==P['H']
    return checks


def main():
    configurations=0; pointchecks=0
    for r in range(2,6):
        for parts in combinations_with_replacement(range(1,4),r):
            if sum(parts)>11: continue
            pointchecks+=verify_one(parts)
            configurations+=1
    a=(1,5,9,17,18)
    b=(2,3,11,15,19)
    A,B=model(a),model(b)
    assert a!=b and len(a)==len(b)==5
    assert A['P']==B['P'] and density_coeffs(A)==density_coeffs(B)
    assert A['N']==B['N']==50 and A['m']==B['m']==890
    assert sum(x**5 for x in a)!=sum(y**5 for y in b)
    print('PASS: ordered-edge classification, exact shortest paths, density normalization,')
    print('      four-observable inversion, and nonisomorphic 5-part collision.')
    print('configurations=',configurations,'point-pair checks=',pointchecks)
    print('collision parts=',a,b,'power sums=',A['P'])
    print('edge count=',A['m'],'density coefficients=',density_coeffs(A))

if __name__=='__main__':main()
