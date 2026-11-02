"""Exact integer verification of the stated harmonic sampling theorem.
No third-party dependencies. Run: python3 check.py
"""
from fractions import Fraction
from itertools import product
from math import isqrt

def points():
    ans=[]
    for i in range(3):
        jj=[j for j in range(3) if j!=i]
        for a,b in product((-1,1),repeat=2):
            v=[0,0,0]
            v[i]=3*a*b; v[jj[0]]=a;v[jj[1]]=b
            ans.append(tuple(v))
    assert len(ans)==12 and len(set(ans))==12
    return ans
V=points()
T=[[sum(a*b for a,b in zip(v,w)) for w in V] for v in V]
assert all(T[i][i]==11 for i in range(12))
assert set(t for row in T for t in row)=={-9,-5,-1,7,11}
assert all({t:row.count(t) for t in (-9,-5,-1,7,11)}=={-9:2,-5:2,-1:4,7:3,11:1} for row in T)

def scaled_legendre(N):
    # Evaluates the integer 22^N P_N(t/11), via standard three-term recurrence.
    output={}
    for t in (-9,-5,-1,7,11):
        a=1;b=2*t
        if N==0: output[t]=a;continue
        for n in range(1,N):
            z=(2*n+1)*(2*t)*b-484*n*a
            assert z%(n+1)==0
            a,b=b,z//(n+1)
        output[t]=b
    assert output[11]==22**N
    return output

def rank_int(matrix):
    # Gaussian elimination with exact rationals, only small N (0 to 6).
    a=[[Fraction(v) for v in row] for row in matrix]
    r=0
    for c in range(len(a[0])):
        p=next((j for j in range(r,len(a)) if a[j][c]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r]
        for j in range(r+1,len(a)):
            if a[j][c]:
                q=a[j][c]/a[r][c]
                for h in range(c+1,len(a[0])):a[j][h]-=q*a[r][h]
                a[j][c]=0
        r+=1
        if r==len(a):break
    return r

def is_spd_integer(m):
    # Fraction-free symmetric elimination; positive consecutive principal
    # minors are precisely the Sylvester criterion.
    a=[row[:] for row in m]
    prev=1
    for k in range(len(a)):
        p=a[k][k]
        if p<=0:return False
        for i in range(k+1,len(a)):
            for j in range(i,len(a)):
                num=p*a[i][j]-a[i][k]*a[k][j]
                assert num%prev==0
                a[j][i]=a[i][j]=num//prev
        for i in range(k+1,len(a)):
            a[i][k]=a[k][i]=0
        prev=p
    return True

def gram_scaled(n):
    f=scaled_legendre(n)
    return [[f[t] for t in row] for row in T]

# Exact small-degree ranks.
ranks=[rank_int(gram_scaled(k)) for k in range(7)]
assert ranks==[1,3,5,7,9,11,9],ranks
print('LOW_RANKS_OK',ranks,flush=True)

# The row-sum sector of K_17 gives an almost-vanishing harmonic moment.
k=17; f=scaled_legendre(k); S=22**k
row_sum=sum(f[t] for t in T[0]); assert all(sum(f[t] for t in row)==row_sum for row in T)
lam=Fraction(row_sum,S)
assert 0<lam<Fraction(1,1000000),lam
print('DEGREE17_CONSTANT_EIGENVALUE',str(lam),float(lam),flush=True)

# The orthogonal complement to the constants at degree 17 has
# eigenvalues above 1/10000. Add +J/12 to remove the constant's nullity.
# K17 - (1/10000)(I-J/12) + J/12 is strictly PD, since its
# constant eigenvalue is lam+1 and its other eigenvalues are shifted.
M=[]
for i in range(12):
    row=[]
    for j in range(12):
        # common integer scaling 120000*S
        value=120000*f[T[i][j]]
        if i==j:value-=12*S
        value+=10001*S
        row.append(value)
    M.append(row)
assert is_spd_integer(M)
print('DEGREE17_COMPLEMENT_GAP_OK',flush=True)

# All other degrees 7..100 are separated from zero by at least 1/10000.
for n in range(7,101):
    if n==17:continue
    S=22**n; F=gram_scaled(n)
    M=[[10000*F[i][j]-(S if i==j else 0) for j in range(12)] for i in range(12)]
    assert is_spd_integer(M),n
print('FINITE_POSITIVITY_OK',93,'degrees in 7..100 excluding 17',flush=True)

# Tail: Bernstein bound |P_k(t)| <= sqrt(2/(pi*(k+1/2)*sqrt(1-t^2))).
# Since pi>3 and sin(theta)=sqrt(121-t^2)/11, each coefficient is
# < rational u_t / sqrt(k+1/2), with the rational u_t below.
upper={9:Fraction(1079,1000),5:Fraction(866,1000),1:Fraction(820,1000),7:Fraction(932,1000)}
for t,u in upper.items():
    # u^2 > 22 / (3 sqrt(121-t*t)); square both sides (all positive)
    assert (u*u*3)**2 * (121-t*t) > 22**2
C=2*upper[9]+2*upper[5]+4*upper[1]+3*upper[7]
assert C<10
# In particular k>=101: sum |offdiag| < 10/sqrt(101.5) < 1-1/10000.
assert Fraction(100,1) < (Fraction(203,2))*(1-Fraction(1,10000))**2
print('TAIL_BOUND_OK',str(C),flush=True)

# Whole theorem: rank 12 for all k>=7; degree 17 unique global
# maximizer of condition number, since k !=17 has λ_min > 1/10000
# and λ_max <= trace=12, so κ<120000. Meanwhile degree 17
# has λ_max >= trace/12=1 and λ_min <1/1000000,
# hence κ>1000000.
print('TRUNCATED_TETRAHEDRON_HARMONIC_CERTIFICATE_OK',flush=True)
