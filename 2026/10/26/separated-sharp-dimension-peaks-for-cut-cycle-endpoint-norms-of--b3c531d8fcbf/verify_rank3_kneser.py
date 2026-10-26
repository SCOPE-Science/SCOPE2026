#!/usr/bin/env python3
"""Exact checks of the rank-three Kneser cut/cycle projection identities.
Uses only the Python standard library. Scientific scope is stated in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb

def potential(n,a,b):
    if a==b:return F(0)
    if a<b:return -potential(n,b,a)
    if n==7:
        return {(3,0):F(17,70),(2,1):F(1,70),(2,0):F(-1,14)}[(a,b)]
    h=n*(n-5)*(n-4)*(n-2)*(n-1)
    w=n*n-10*n+27
    return {
      (3,0): F(6*(n*n+2),h),
      (2,1): F(108,h*w),
      (2,0): F(-36*(n*n-10*n+36),h*(n-6)*w),
      (1,0): F(-36*(n*n-7*n+18),h*(n-6)*w),
    }[(a,b)]

def q_formula(n):
    poly=n**7-13*n**6-74*n**5+2810*n**4-26525*n**3+122879*n**2-275982*n+224208
    return F(2*poly,n*(n-5)*(n-4)*(n-2)*(n-1)*(n*n-10*n+27))

def p_formula(n):
    poly=n**6-11*n**5-39*n**4+1373*n**3-10024*n*n+30732*n-29808
    return F(3*poly,n*(n-4)*(n-2)*(n-1)*(n*n-10*n+27))

def coef_poly(coeffs,t):
    result=0
    for c in coeffs:result=result*t+c
    return result

R_Q=[18,576,9396,110088,961470,5787648,22279356,51060888,62130240,30373056]
R_P=[18,504,7308,77616,589590,2793168,7206300,8019000,1399680]

def diff_q_den(n):
    return n*(n-5)*(n-4)*(n-3)*(n-2)*(n-1)*(n+1)*(n*n-10*n+27)*(n*n-8*n+18)
def diff_p_den(n):
    return n*(n-4)*(n-3)*(n-2)*(n-1)*(n+1)*(n*n-10*n+27)*(n*n-8*n+18)

def assert_formula_identities():
    # Equal rational functions: differences have numerator degree <= 25.
    # The degree bound follows from the displayed rational formulas and
    # multiplying their explicit polynomial denominators.
    for n in range(9,40):
        assert q_formula(n)-q_formula(n+1)==F(coef_poly(R_Q,n-9),diff_q_den(n))
        assert p_formula(n)-p_formula(n+1)==F(coef_poly(R_P,n-9),diff_p_den(n))
    assert q_formula(8)-q_formula(7)==F(9,385)
    assert q_formula(9)-q_formula(8)==-F(251,4620)
    assert p_formula(8)-p_formula(7)==F(927,1540)
    assert p_formula(9)-p_formula(8)==F(31,220)
    assert q_formula(8)==F(257,77)
    assert p_formula(9)==F(143,35)
    # A separate exact trace diagonal identity for all parameters.
    for n in range(7,42):
        N=comb(n,3);degree=comb(n-3,3)
        assert p_formula(n)==q_formula(n)+1-F(4*(N-1),N*degree)
        assert 2*potential(n,3,0)==F(2*(N-1),N*degree)

def check_orbit_equations():
    # Verify every orbit Laplacian equation at enough integer parameters
    # to force polynomial identities after clearing the eight-degree
    # common potential denominator (entries of the orbit matrix <=degree 3).
    count=0
    for n in range(8,26):
        orbit_types={(a,b) for a in range(4) for b in range(4-a)
                   if 3-a-b<=n-6}
        for a,b in orbit_types:
            c=3-a-b
            lhs=comb(n-3,3)*potential(n,a,b)
            for aa,bb in orbit_types:
                cc=3-aa-bb
                if aa<=3-a and bb<=3-b and cc<=n-6-c:
                    lhs-=comb(3-a,aa)*comb(3-b,bb)*comb(n-6-c,cc)*potential(n,aa,bb)
            assert lhs==(1 if (a,b)==(3,0) else -1 if (a,b)==(0,3) else 0),(n,a,b,lhs)
            count+=1
    return count

def check_cut_thresholds():
    sets=[{(3,0),(0,1),(0,2),(2,1)},
          {(3,0),(0,1),(0,2)},
          {(3,0),(0,1)}, {(3,0)}]
    def cap_formula(n,j):
        polynomials=(
          3*n**5-87*n**4+1151*n**3-8577*n*n+34582*n-57792,
          3*n**5-87*n**4+1133*n**3-8145*n*n+31144*n-48936,
          3*n**5-93*n**4+1277*n**3-9615*n*n+38524*n-63624,
          2*(n-5)*(n-4)*(n-3))
        return F(polynomials[j],12)
    result=0
    for n in range(8,40):
        cells={(a,b) for a in range(4) for b in range(4-a) if 3-a-b<=n-6}
        capacities=[]
        for j,SS in enumerate(sets):
            total=0
            for a,b in SS:
                c=3-a-b
                multiplicity=comb(3,a)*comb(3,b)*comb(n-6,c)
                for aa,bb in cells-SS:
                    cc=3-aa-bb
                    if aa<=3-a and bb<=3-b and cc<=n-6-c:
                        total+=multiplicity*comb(3-a,aa)*comb(3-b,bb)*comb(n-6-c,cc)
            assert total==cap_formula(n,j),(n,j,total,cap_formula(n,j))
            capacities.append(total)
            result+=1
        u21=potential(n,2,1)
        u20=potential(n,2,0)
        u10=potential(n,1,0)
        u30=potential(n,3,0)
        assert u30>-u10>-u20>u21>0
        tv=2*(u21*capacities[0]+(-u20-u21)*capacities[1]
             +(u20-u10)*capacities[2]+(u30+u10)*capacities[3])
        assert tv==q_formula(n)
    return result

def check_whole_graph(n):
    verts=[sum(1<<i for i in t) for t in combinations(range(n),3)]
    A=7;B=56;idx={v:i for i,v in enumerate(verts)}
    edges=[(i,j) for i,v in enumerate(verts) for j in range(i+1,len(verts)) if v&verts[j]==0]
    def vpot(mask):return potential(n,(mask&A).bit_count(),(mask&B).bit_count())
    f=[vpot(v) for v in verts]
    lap=[F(0) for _ in verts]
    total=F(0)
    for i,j in edges:
        val=f[i]-f[j]
        lap[i]+=val;lap[j]-=val
        total+=abs(val)
    for i,val in enumerate(lap):
        assert val == (1 if verts[i]==A else -1 if verts[i]==B else 0),(n,i,val)
    assert total==q_formula(n),(n,total,q_formula(n))
    diag=f[idx[A]]-f[idx[B]]
    assert total+1-2*diag==p_formula(n)
    return len(verts),len(edges)

if __name__=='__main__':
    assert_formula_identities()
    orbit=check_orbit_equations()
    thresholds=check_cut_thresholds()
    graphs=[]
    for n in range(7,14):
        graphs.append((n,*check_whole_graph(n)))
    print('RANK3_KNESER_EXACT_OK', 'orbit_equations='+str(orbit),
          'threshold_counts='+str(thresholds), 'full_graphs='+str(len(graphs)),
          'vertices='+str(sum(x[1] for x in graphs)),
          'edges='+str(sum(x[2] for x in graphs)),
          'rational_identities=PASS', 'peak_certificates=PASS')
