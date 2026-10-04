#!/usr/bin/env python3
from math import comb

# Truncated Chow ring Z[h,k]/(h^3,k^3), represented by {(i,j): coefficient}.
def add(a,b):
    c=dict(a)
    for m,v in b.items(): c[m]=c.get(m,0)+v
    return {m:v for m,v in c.items() if v}
def scale(a,s): return {m:s*v for m,v in a.items() if s*v}
def mul(a,b):
    c={}
    for (i,j),u in a.items():
        for (r,s),v in b.items():
            if i+r<3 and j+s<3:
                c[(i+r,j+s)]=c.get((i+r,j+s),0)+u*v
    return {m:v for m,v in c.items() if v}
def powp(a,n):
    r={(0,0):1}
    for _ in range(n): r=mul(r,a)
    return r

def fmt(a):
    return dict(sorted(a.items()))

one={(0,0):1}; h={(1,0):1}; k={(0,1):1}
# For U,Z the tautological rank-2 bundles on Gr(2,3)=P^2:
# c(U)=1-h+h^2 and c(Z)=1-k+k^2.
# For F=(U tensor Z)^*, splitting-principle arithmetic gives:
c=[one,
   add(scale(h,2),scale(k,2)),
   {(2,0):3,(1,1):3,(0,2):3},
   {(2,1):3,(1,2):3},
   {}]

# Route A: Segre recursion s(F)c(F)=1 and projective-bundle pushforward
# for X=P(F) in the lines convention: pi_*(xi^(3+i))=s_i(F).
s=[one]
for n in range(1,5):
    acc={}
    for j in range(1,n+1):
        acc=add(acc,mul(c[j],s[n-j]))
    s.append(scale(acc,-1))
expected_s=[
    {(0,0):1},
    {(1,0):-2,(0,1):-2},
    {(2,0):1,(1,1):5,(0,2):1},
    {(2,1):-3,(1,2):-3},
    {(2,2):3},
]
assert s==expected_s, (s,expected_s)
base=add(scale(h,2),scale(k,2))
routeA=0
terms=[]
for i in range(5):
    # H=xi+base, dim X=7; xi exponent 3+i contributes s_i(F).
    coeff=comb(7,3+i)
    bpow=powp(base,4-i)
    integ=mul(bpow,s[i]).get((2,2),0)
    val=coeff*integ
    terms.append(val)
    routeA += val
assert terms==[3360,-3360,1008,-84,3], terms
assert routeA==927, routeA

# Route B: independently expand H^7 in Z[h,k,xi], then reduce by
# xi^4+c1(F)xi^3+c2(F)xi^2+c3(F)xi+c4(F)=0.
# A class is {(i,j,e): coeff}; base powers are truncated at h^3=k^3=0.
def add3(a,b):
    c=dict(a)
    for m,v in b.items(): c[m]=c.get(m,0)+v
    return {m:v for m,v in c.items() if v}
def mul3(a,b):
    c={}
    for (i,j,e),u in a.items():
        for (r,s0,f),v in b.items():
            if i+r<3 and j+s0<3:
                m=(i+r,j+s0,e+f)
                c[m]=c.get(m,0)+u*v
    return {m:v for m,v in c.items() if v}
def pow3(a,n):
    r={(0,0,0):1}
    for _ in range(n): r=mul3(r,a)
    return r

def c_to3(poly, e):
    return {(i,j,e):v for (i,j),v in poly.items()}

H={(1,0,0):2,(0,1,0):2,(0,0,1):1}
P=pow3(H,7)
# Repeatedly replace every term a*h^i k^j xi^e with e>=4 using relation.
changed=True
while changed:
    changed=False
    Q={}
    for (i,j,e),a in P.items():
        if e<4:
            Q[(i,j,e)]=Q.get((i,j,e),0)+a
            continue
        changed=True
        # xi^e = -c1 xi^(e-1)-c2 xi^(e-2)-c3 xi^(e-3)-c4 xi^(e-4)
        for r in range(1,5):
            if not c[r]: continue
            for (u,v),cv in c[r].items():
                if i+u<3 and j+v<3:
                    m=(i+u,j+v,e-r)
                    Q[m]=Q.get(m,0)-a*cv
    P={m:v for m,v in Q.items() if v}
routeB=P.get((2,2,3),0)
assert routeB==927, routeB
# Pushforward kills xi^0,xi^1,xi^2; only xi^3 coefficient contributes.
assert all(e<=3 for (_,_,e) in P)

print('CHERN_F_OK', [fmt(x) for x in c])
print('SEGRE_F_OK', [fmt(x) for x in s])
print('PUSHFORWARD_TERMS', terms)
print('ROUTE_A_DEGREE', routeA)
print('ROUTE_B_DEGREE', routeB)
print('VERIFY_OK')
