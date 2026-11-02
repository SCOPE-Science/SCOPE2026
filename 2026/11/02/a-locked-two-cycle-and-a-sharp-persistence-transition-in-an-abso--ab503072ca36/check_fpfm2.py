"""Standalone high-precision checks for the FPFM2 prime-two classification.

Requires mpmath. Mathematical identities and exhaustive implications are proved
analytically in RESULT.md; finite parameter checks do not replace those proofs.
"""
import mpmath as mp
mp.mp.dps = 75
P = mp.pi
BCRIT = 4/(4-P)
checks = 0

def check(cond, message):
    global checks
    if not cond:
        raise AssertionError(message)
    checks += 1

def f(alpha, beta, x, y):
    return alpha*mp.cos(x)+beta*(abs(y)-1)*x, y+x

def root_bisect(fun, a, b):
    fa, fb = fun(a), fun(b)
    if fa == 0:
        return a
    if fb == 0:
        return b
    check(fa*fb<0, 'Expected strictly bracketing signs')
    for _ in range(310):
        mid=(a+b)/2
        if fun(mid)*fa>0:
            a,fa=mid,fun(mid)
        else:
            b=mid
    return (a+b)/2

def enumerate_cycles(alpha,beta):
    if beta<=1:
        return []
    L=2*(1-1/beta)
    cycles=[]
    U=min(L,P/2)
    if alpha*mp.cos(U)-beta*U*U/2 < -mp.mpf('1e-65'):
        u=root_bisect(lambda u: alpha*mp.cos(u)-beta*u*u/2,mp.mpf('0'),U)
        cycles.append(('positive',u,(L-u)/2))
    if L>P/2 and alpha*mp.cos(L)+beta*L*L/2 < -mp.mpf('1e-65'):
        u=root_bisect(lambda u: alpha*mp.cos(u)+beta*u*u/2,P/2,L)
        cycles.append(('negative',u,-(L+u)/2))
    t=alpha*mp.cos(L)/(beta*L)
    if abs(t)<=L/2+mp.mpf('1e-64'):
        cycles.append(('crossing',L,t-L/2))
    return cycles

def expected(beta,alpha):
    if beta<=1: return 0
    L=2*(1-1/beta)
    if L>=P/2: return 2
    a_star=beta*L*L/(2*mp.cos(L))
    if abs(alpha-a_star)<mp.mpf('1e-55'): return 1
    return 2 if alpha<a_star else 0

betas=[mp.mpf('0.7'),mp.mpf('1'),mp.mpf('1.02'),mp.mpf('1.5'),mp.mpf('1.9'),mp.mpf('2'),mp.mpf('2.3'),mp.mpf('4'),BCRIT,mp.mpf('5'),mp.mpf('10')]
for beta in betas:
    alphas=[mp.mpf('0.01'),mp.mpf('0.05'),mp.mpf('0.2'),mp.mpf('1'),mp.mpf('3'),mp.mpf('10'),mp.mpf('100')]
    if beta>1:
        L=2*(1-1/beta)
        if abs(L-P/2)>mp.mpf('1e-55'):
            astar=beta*L*L/(2*abs(mp.cos(L)))
            alphas += [astar/2,astar,2*astar]
    for alpha in alphas:
        cycles=enumerate_cycles(alpha,beta)
        check(len(cycles)==expected(beta,alpha),('count',str(beta),str(alpha),cycles))
        for kind,u,v in cycles:
            u1,y1=f(alpha,beta,u,v)
            u2,y2=f(alpha,beta,u1,y1)
            check(abs(u1+u)<mp.mpf('1e-55'),('first coordinate',kind,beta,alpha,u))
            check(abs(y1-(v+u))<mp.mpf('1e-55'),('second coordinate',kind,beta,alpha,u))
            check(abs(u2-u)<mp.mpf('1e-55'),('period two',kind,beta,alpha,u))
            check(abs(y2-v)<mp.mpf('1e-55'),('period two y',kind,beta,alpha,u))
            check(u>0,('prime',kind))

# Rigidity of the parameter-independent boundary orbit.
beta=BCRIT
u=P/2
for alpha in [mp.mpf('0.00001'),mp.mpf('1'),mp.mpf('5'),mp.mpf('2000')]:
    x1,y1=f(alpha,beta,u,-u/2)
    x2,y2=f(alpha,beta,x1,y1)
    check(abs(x1+u)<mp.mpf('1e-65') and abs(y1-u/2)<mp.mpf('1e-65'),'locked first step')
    check(abs(x2-u)<mp.mpf('1e-65') and abs(y2+u/2)<mp.mpf('1e-65'),'locked second step')

# Confirm the exact Jacobian algebra and the sink criterion at sample points.
for beta in [mp.mpf('1.1'),mp.mpf('1.5'),mp.mpf('1.8'),mp.mpf('2'),mp.mpf('2.3'),mp.mpf('5')]:
    L=2*(1-1/beta)
    for alpha in [mp.mpf('0.001'),mp.mpf('0.01'),mp.mpf('0.1'),mp.mpf('1')]:
        for kind,u,v in enumerate_cycles(alpha,beta):
            w=v+u
            if min(abs(v),abs(w))<mp.mpf('1e-40'):continue
            def J(x,y):
                return mp.matrix([[-alpha*mp.sin(x)+beta*(abs(y)-1),beta*x*mp.sign(y)],[1,1]])
            mat=J(-u,w)*J(u,v)
            tr=mat[0,0]+mat[1,1]
            det=mp.det(mat)
            if kind=='positive':
                h=beta*u/2+alpha*mp.sin(u)
                B=beta*u
                check(abs((1-tr+det)+B*(B+2*h))<mp.mpf('1e-53'),'positive p(1)')
                check(1-tr+det<0,'positive expanding eigenvalue')
            elif kind=='crossing':
                h=alpha*(mp.cos(L)/L+mp.sin(L))
                B=beta*L
                check(abs(tr-(2-2*B-h*h))<mp.mpf('1e-53'),'crossing trace')
                check(abs(det-((B-1)**2-h*h))<mp.mpf('1e-53'),'crossing determinant')
                check(abs((1-tr+det)-B*B)<mp.mpf('1e-53'),'crossing p(1)')
                if 1<beta<2:
                    sink=(1-det>0 and 1-tr+det>0 and 1+tr+det>0)
                    threshold=(h*h<(2-B)**2/2)
                    check(sink==threshold,'crossing Schur criterion')

print('PASS',checks,'high-precision conditions; critical beta =',mp.nstr(BCRIT,30))
