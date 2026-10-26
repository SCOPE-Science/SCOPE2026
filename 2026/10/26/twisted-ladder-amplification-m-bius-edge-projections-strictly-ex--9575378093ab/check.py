"""Exact rational finite checks for sharp gradient-projection norms on Moebius ladders.
This code supplements, but does not replace, the all-size analytic proof.
Requires sympy, standard library.
"""
import sympy as sp

ASSERTIONS = 0

def check(a, b):
    global ASSERTIONS
    assert a == b, (a, b)
    ASSERTIONS += 1

def incidence(edges, nodes):
    B = sp.zeros(len(edges), nodes)
    for i, (u, v) in enumerate(edges):
        B[i, u] = 1
        B[i, v] = -1
    return B

def mobius_edges(m):
    n = 2*m
    return [(i,(i+1)%n) for i in range(n)] + [(i,i+m) for i in range(m)]

def prism_edges(m):
    return [(layer*m+i, layer*m+(i+1)%m) for layer in (0,1) for i in range(m)] + [(i,i+m) for i in range(m)]

def projection(edges, n):
    B = incidence(edges,n)
    L = B.T*B
    H = (L + sp.ones(n,n)/n).inv() - sp.ones(n,n)/n
    return B*H*B.T

def antiperiodic_green(m):
    T=sp.zeros(m,m)
    for i in range(m):
        T[i,i]=4
        if i<m-1:
            T[i,i+1]=T[i+1,i]=-1
    T[0,m-1]=T[m-1,0]=1
    return [x for x in T.inv().col(0)]

def periodic_green(m):
    T=sp.zeros(m,m)
    for i in range(m):
        T[i,i]=4
        T[i,(i+1)%m]=-1
        T[i,(i-1)%m]=-1
    return [x for x in T.inv().col(0)]

def row_sum(P, i):
    return sum(abs(x) for x in P.row(i))

for m in range(3,13):
    b=antiperiodic_green(m)
    p=periodic_green(m)
    check(b[0]>0, True)
    check(sum(p),sp.Rational(1,2))
    for j in range(1,m):
        check(b[j],-b[m-j])
        check(p[j]>abs(b[j]), True)
    B_m=incidence(mobius_edges(m),2*m)
    P_m=projection(mobius_edges(m),2*m)
    check(P_m*P_m,P_m)
    check(P_m.T,P_m)
    check(P_m*B_m,B_m)
    S=1-sp.Rational(1,m)+sum(max(sp.Rational(1,m),2*abs(b[j])) for j in range(1,m))+2*b[0]
    R=4*b[0]+2*sum(abs(x) for x in b)
    for i in range(2*m):
        check(row_sum(P_m,i),S)
    for i in range(2*m,3*m):
        check(row_sum(P_m,i),R)
    check(max(row_sum(P_m,i) for i in range(3*m)),max(S,R))
    check(S>=R, True)
    if m==3:
        check(S,sp.Rational(17,9));check(R,S);check(S<2,True)
    if m==4:
        check(S,sp.Rational(29,14));check(R,sp.Integer(2))
    if m>=4:
        check(S>R,True);check(S>2,True)
    check(S<3,True)
    P_p=projection(prism_edges(m),2*m)
    Sp=1-sp.Rational(1,m)+sum(max(sp.Rational(1,m),2*p[j]) for j in range(1,m))+2*(p[0]-min(p))
    for i in range(2*m):
        check(row_sum(P_p,i),Sp)
    Rp=1+4*(p[0]-min(p))
    for i in range(2*m,3*m):
        check(row_sum(P_p,i),Rp)
    check(S>max(Sp,Rp),True)
    # Symmetric threshold set consists of two initial segments.
    A=[j for j in range(1,m) if 2*abs(b[j])>sp.Rational(1,m)]
    k=sum(int(bool(2*b[j]>sp.Rational(1,m))) for j in range(1,(m-1)//2+1))
    check(A,list(range(1,k+1))+list(range(m-k,m)))
    check(S,2-sp.Rational(2*(k+1),m)+2*b[0]+4*sum(b[j] for j in range(1,k+1)))
    print(m, 'Mobius', S, 'prism', max(Sp,Rp), 'cutoff', k)

print('PASS', ASSERTIONS, 'exact assertions')
