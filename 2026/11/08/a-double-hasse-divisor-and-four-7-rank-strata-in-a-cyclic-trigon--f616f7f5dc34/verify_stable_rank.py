"""Independent GF(7)[a] computation of Frobenius-stable rank.
No third-party packages. Run: python verify_stable_rank.py.
The Cartier coefficients are represented after seventh powers; products
M^(7^(n-1)) ... M give the n-fold Cartier rank over the perfect closure.
"""
p = 7

def norm(v):
    q = [int(z) % p for z in v]
    while len(q)>1 and q[-1] == 0:
        q.pop()
    return q or [0]

def add(u,v):
    return norm([(u[i] if i<len(u) else 0)+(v[i] if i<len(v) else 0)
                 for i in range(max(len(u),len(v)))])

def neg(v): return norm([-z for z in v])
def sub(u,v): return add(u,neg(v))

def mul(u,v):
    out = [0]*(len(u)+len(v)-1)
    for i,c in enumerate(u):
        for j,d in enumerate(v): out[i+j] += c*d
    return norm(out)

def power(u,n):
    out=[1]
    while n:
        if n&1:out=mul(out,u)
        u=mul(u,u); n//=2
    return out

def rem(u,v):
    u=norm(u[:]);v=norm(v)
    assert v != [0]
    while u != [0] and len(u)>=len(v):
        c = u[-1]*pow(v[-1],-1,p)%p
        shift=len(u)-len(v)
        for i,z in enumerate(v):u[i+shift]=(u[i+shift]-c*z)%p
        u=norm(u)
    return u

def gcd(u,v):
    while v != [0]:u,v=v,rem(u,v)
    return norm([z*pow(u[-1],-1,p) for z in u])

def twist(u,k):
    out=[0]*((len(u)-1)*7**k+1)
    for i,z in enumerate(u):out[i*7**k]=z
    return norm(out)

def matrix_mul(A,B):
    return [[sum_polys([mul(A[i][k],B[k][j]) for k in range(len(B))])
             for j in range(len(B[0]))] for i in range(len(A))]

def sum_polys(qs):
    o=[0]
    for z in qs:o=add(o,z)
    return o

def rank_mod(M, a):
    q=[[sum(z*pow(a,i,p) for i,z in enumerate(e))%p for e in row] for row in M]
    r=0
    for col in range(len(q[0])):
        piv=next((i for i in range(r,len(q)) if q[i][col]),None)
        if piv is None:continue
        q[r],q[piv]=q[piv],q[r]
        z=pow(q[r][col],-1,p)
        q[r]=[(v*z)%p for v in q[r]]
        for i in range(len(q)):
            if i != r:
                z=q[i][col]
                q[i]=[(v-z*w)%p for v,w in zip(q[i],q[r])]
        r+=1
    return r

# The 3-by-3 (j=2) Cartier coefficient matrix specialized at b=0.
# Polynomials in a are in ascending order.
M = [
    [[0,0,0,-3],[-3], [0,0,-1]],
    [[0],[0,-2],[0,0,0,-3]],
    [[1],[0],[0]],
]
M=[list(map(norm,row)) for row in M]
P1=M
P2=matrix_mul([[twist(x,1) for x in row] for row in M],P1)
P3=matrix_mul([[twist(x,2) for x in row] for row in M],P2)

minors=[]
for i in range(3):
    for j in range(i+1,3):
        for k in range(3):
            for ell in range(k+1,3):
                minors.append(sub(mul(P2[i][k],P2[j][ell]),mul(P2[i][ell],P2[j][k])))
g=[0]
for q in minors:g=gcd(g,q)
a=[0,1]
expected=mul(power(a,4),sub(power(a,10),[1]))
assert g == expected, (g,expected)
# One explicit minor identifies the support and shows rank 2 off it.
assert norm(sub(mul(P2[0][0],P2[2][1]),mul(P2[0][1],P2[2][0]))) == norm(mul([3],expected))
assert P2[2][1] == [-3%7]  # Never zero, so rank(P2)>=1.

h=[0]
for row in P3:
    for q in row:h=gcd(h,q)
assert h == a             # P3 is zero precisely at a=0.
# Uniformly prove nonzero P3 on all five geometric roots of a^5=1.
assert rem(P3[1][0], sub(power(a,5), [1])) == [1]
assert rank_mod(P1,0)==2 and rank_mod(P2,0)==1 and rank_mod(P3,0)==0
for a0 in range(7):
    if a0==6:continue  # discriminant zero on the b=0 line
    exp = 0 if a0==0 else 1 if a0==1 else 2
    assert rank_mod(P3,a0) == exp, (a0,exp,rank_mod(P3,a0))
print('FROBENIUS_STABLE_RANK_OK')
print('gcd of all 2x2 minors of M^(7)M: a^4*(a^10-1)')
print('gcd of entries of M^(49)M^(7)M: a')
print('smooth b=0: rank 0 at a=0, rank 1 at a^5=1, rank 2 otherwise')
