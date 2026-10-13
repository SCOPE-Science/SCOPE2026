#!/usr/bin/env python3
# Finite anchor for p=5,m=3. F_125 = F_5[u]/(u^3+u^2+2).
p=5; n=124; h=31
# tuples low-to-high; u^3 = -u^2-2 = 4u^2+3
def add(a,b): return tuple((a[i]+b[i])%p for i in range(3))
def mul(a,b):
    c=[0]*5
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%p
    # reduce u^4 then u^3 using u^3=4u^2+4
    for d in (4,3):
        q=c[d]%p
        if q:
            c[d]=0
            c[d-3]=(c[d-3]+3*q)%p
            c[d-1]=(c[d-1]+4*q)%p
    return tuple(c[:3])
one=(1,0,0); alpha=(0,1,0)
def pw(a,e):
    r=one
    while e:
        if e&1:r=mul(r,a)
        a=mul(a,a); e//=2
    return r
assert pw(alpha,124)==one and all(pw(alpha,d)!=one for d in (1,2,4,31,62))
pows=[pw(alpha,i) for i in range(n)]
def smul(k,a): return tuple((k*x)%p for x in a)
sol=[]
for i in range(1,n):
    for j in range(i+1,n):
        ai=pows[i]; aj=pows[j]; ai2=pows[(2*i)%n]; aj2=pows[(2*j)%n]
        for a in range(1,p):
            for b in range(1,p):
                e1=add(one,add(smul(a,ai),smul(b,aj)))
                e2=add(one,add(smul(a,ai2),smul(b,aj2)))
                if e1==(0,0,0) and e2==(0,0,0): sol.append((i,j,a,b))
assert sol and all(i%h==0 and j%h==0 for i,j,a,b in sol)
# beta=alpha^h lies in prime field and has order 4
beta=pows[h]; assert beta[1:]==(0,0) and beta[0] in (2,3)
b=beta[0]
# g=(x^h-beta)(x^h-beta^2): coefficients [beta^3, -(beta+beta^2), 1]
gcoef=[pow(b,3,p), (-(b+pow(b,2,p)))%p, 1]
assert all(gcoef)
# Show every normalized solution polynomial in y is divisible by quadratic g_y by checking roots beta,beta^2.
def peval(coeffs,x):
    z=0
    for c in reversed(coeffs): z=(z*x+c)%p
    return z
for i,j,a,c in sol:
    r=i//h; s=j//h
    co=[0]*(max(r,s)+1); co[0]=1; co[r]=a; co[s]=c
    assert peval(co,b)==0 and peval(co,pow(b,2,p))==0
# g itself is a normalized weight-3 BCH word after constant scaling; direct field checks.
vec=[0]*n; vec[0]=gcoef[0]; vec[h]=gcoef[1]; vec[2*h]=1
assert sum(x!=0 for x in vec)==3
def eval_vec(exp):
    out=(0,0,0)
    for k,c in enumerate(vec):
        if c: out=add(out,smul(c,pows[(exp*k)%n]))
    return out
assert eval_vec(1)==(0,0,0) and eval_vec(2)==(0,0,0)
# Rank over F5 of all cyclic shifts of g; should be n-deg(g)=62.
def rank_mod(mat):
    A=[row[:] for row in mat]; R=0
    for col in range(len(A[0])):
        piv=next((r for r in range(R,len(A)) if A[r][col]%p),None)
        if piv is None: continue
        A[R],A[piv]=A[piv],A[R]
        inv=pow(A[R][col],-1,p); A[R]=[(v*inv)%p for v in A[R]]
        for r in range(len(A)):
            if r!=R and A[r][col]%p:
                q=A[r][col]%p; A[r]=[(A[r][c]-q*A[R][c])%p for c in range(n)]
        R+=1
        if R==len(A): break
    return R
shifts=[]
for s in range(n): shifts.append(vec[-s:]+vec[:-s] if s else vec[:])
r=rank_mod(shifts)
assert r==62
print('primitive_beta',b)
print('normalized_weight3_solutions',len(sol),sol)
print('generator_coefficients_at_0_h_2h',gcoef)
print('cyclic_shift_rank',r)
print('C_dimension',n-2*3,'component_exponent',(n-2*3)-r)
print('VERIFY_OK')
