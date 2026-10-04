#!/usr/bin/env python3
import math, random

RNG=random.Random(20261001)

def det(a):
    a=[list(map(float,row)) for row in a]
    n=len(a)
    if n==0: return 1.0
    out=1.0
    for c in range(n):
        p=max(range(c,n), key=lambda r: abs(a[r][c]))
        if abs(a[p][c])<1e-14: return 0.0
        if p!=c:
            a[c],a[p]=a[p],a[c]; out=-out
        piv=a[c][c]; out*=piv
        for r in range(c+1,n):
            q=a[r][c]/piv
            for j in range(c+1,n): a[r][j]-=q*a[c][j]
    return out

def sub(a,b): return [x-y for x,y in zip(a,b)]
def add(a,b): return [x+y for x,y in zip(a,b)]
def scale(c,a): return [c*x for x in a]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm(a): return math.sqrt(dot(a,a))

def simplex_volume(v):
    n=len(v)-1
    M=[[v[i+1][j]-v[0][j] for j in range(n)] for i in range(n)]
    return abs(det(M))/math.factorial(n)

def facet_measure(v,i):
    f=[v[k] for k in range(len(v)) if k!=i]
    m=len(f)-1
    if m==0: return 1.0
    B=[sub(f[k+1],f[0]) for k in range(m)]
    G=[[dot(B[r],B[c]) for c in range(m)] for r in range(m)]
    return math.sqrt(max(0.0,det(G)))/math.factorial(m)

def null_normal(rows):
    # rows is (n-1) x n; cofactor vector lies in its nullspace
    m=len(rows); n=m+1
    z=[]
    for c in range(n):
        minor=[[rows[r][j] for j in range(n) if j!=c] for r in range(m)]
        z.append(((-1.0)**c)*det(minor))
    q=norm(z)
    if q<1e-14: raise ValueError('degenerate facet')
    return [x/q for x in z]

def facet_data(v,i):
    f=[v[k] for k in range(len(v)) if k!=i]
    rows=[sub(f[k+1],f[0]) for k in range(len(f)-1)]
    u=null_normal(rows)
    c=dot(u,f[0])
    if dot(u,v[i])-c<0:
        u=[-x for x in u]; c=-c
    return u,c

def pedal_data(v,p):
    q=[]; ds=[]
    for i in range(len(v)):
        u,c=facet_data(v,i)
        d=dot(u,p)-c
        ds.append(d)
        q.append(sub(p,scale(d,u)))
    return q,ds

def formula(v,p):
    n=len(v)-1
    V=simplex_volume(v)
    S=[facet_measure(v,i) for i in range(n+1)]
    q,d=pedal_data(v,p)
    direct=simplex_volume(q)
    phi=sum(S[i]*math.prod(d[j] for j in range(n+1) if j!=i) for i in range(n+1))
    coeff=(n**n)*(V**(n-1))/((math.factorial(n)**2)*math.prod(S))
    return direct,abs(coeff*phi)

def circumcenter_triangle(v):
    A,B,C=v
    # solve 2(B-A).O=|B|^2-|A|^2 and same for C
    M=[[2*(B[j]-A[j]) for j in range(2)],[2*(C[j]-A[j]) for j in range(2)]]
    b=[dot(B,B)-dot(A,A),dot(C,C)-dot(A,A)]
    D=det(M)
    if abs(D)<1e-14: raise ValueError('degenerate')
    ox=det([[b[0],M[0][1]],[b[1],M[1][1]]])/D
    oy=det([[M[0][0],b[0]],[M[1][0],b[1]]])/D
    return [ox,oy]

worst=0.0
cases=0
for n in range(2,7):
    for t in range(220):
        while True:
            v=[[RNG.uniform(-2,2) for _ in range(n)] for __ in range(n+1)]
            V=simplex_volume(v)
            if V>1e-5: break
        if t%2==0:
            w=[RNG.random() for _ in range(n+1)]; s=sum(w); w=[x/s for x in w]
            p=[sum(w[i]*v[i][j] for i in range(n+1)) for j in range(n)]
        else:
            p=[RNG.uniform(-3,3) for _ in range(n)]
        a,b=formula(v,p)
        err=abs(a-b)/max(1.0,a,b)
        worst=max(worst,err); cases+=1

# planar specialization: pedal-area/original-area = |R^2-OP^2|/(4R^2)
worst_euler=0.0
for t in range(600):
    while True:
        v=[[RNG.uniform(-2,2),RNG.uniform(-2,2)] for _ in range(3)]
        V=simplex_volume(v)
        if V>1e-5: break
    p=[RNG.uniform(-3,3),RNG.uniform(-3,3)]
    q,d=pedal_data(v,p)
    ped=simplex_volume(q)
    O=circumcenter_triangle(v)
    R2=dot(sub(v[0],O),sub(v[0],O))
    rho2=dot(sub(p,O),sub(p,O))
    rhs=V*abs(R2-rho2)/(4*R2)
    err=abs(ped-rhs)/max(1.0,ped,rhs)
    worst_euler=max(worst_euler,err)

print('VERIFY_OK')
print('cases',cases)
print('worst_formula_error',format(worst,'.3e'))
print('worst_planar_euler_error',format(worst_euler,'.3e'))
if worst>2e-9 or worst_euler>2e-9:
    raise SystemExit(1)
