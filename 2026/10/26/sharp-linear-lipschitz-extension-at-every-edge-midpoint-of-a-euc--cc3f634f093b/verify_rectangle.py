"""Reproduce finite Lipschitz-potential checks for rectangular midpoint extensions.

No third-party packages.  For each rectangle, enumerate vertices of the
3-dimensional dual unit ball of Lipschitz functions on its four corners.
This is a finite numerical check, not a substitute for the analytic proof.
"""
import itertools,math

def lin3(A,b):
    M=[list(row)+[y] for row,y in zip(A,b)]
    for k in range(3):
        p=max(range(k,3),key=lambda i:abs(M[i][k]))
        if abs(M[p][k])<1e-10: return None
        M[k],M[p]=M[p],M[k]
        z=M[k][k]; M[k]=[v/z for v in M[k]]
        for j in range(3):
            if j!=k:
                z=M[j][k]; M[j]=[u-z*v for u,v in zip(M[j],M[k])]
    return tuple(row[3] for row in M)

def distance(x,y):return math.dist(x,y)

def dual_vertices(V):
    eq=[]
    for i,j in itertools.combinations(range(4),2):
        row=[float(int(i==k)-int(j==k)) for k in range(1,4)]
        for sign in (-1,1):eq.append((tuple(sign*z for z in row),distance(V[i],V[j])))
    sols=[]
    for trio in itertools.combinations(eq,3):
        v=lin3([a for a,_ in trio],[b for _,b in trio])
        if v is None:continue
        if any(sum(x*y for x,y in zip(a,v))>b+1e-8 for a,b in eq):continue
        if not any(max(abs(x-y) for x,y in zip(v,old))<1e-8 for old in sols):sols.append(v)
    return [(0.0,)+z for z in sols]

def values(a,b):
    assert a>0 and b>0
    c=math.hypot(a,b)
    dA=math.hypot(a,2*b)
    dB=math.hypot(2*a,b)
    L_A=(a+b+c)/(a+dA)
    L_B=(a+b+c)/(b+dB)
    beta=(L_A-1)*a/(2*(b+c-a))
    delta=(L_B-1)*b/(2*(a+c-b))
    assert 0<beta<.25 and 0<delta<.25
    mu=[tuple(1.0 if i==k else 0.0 for i in range(4)) for k in range(4)]
    mu += [(beta,.5-beta,beta,.5-beta),(.5-beta,beta,.5-beta,beta),
           (delta,delta,.5-delta,.5-delta),(.5-delta,.5-delta,delta,delta)]
    pts=[(-a,-b),(-a,b),(a,-b),(a,b),(0,b),(0,-b),(a,0),(-a,0)]
    dual=dual_vertices(pts[:4]); assert len(dual)>=8
    worst=0.0; worstpair=None; centermax=0.
    for i,j in itertools.combinations(range(8),2):
        if j<4:continue
        norm=max(sum((mu[i][k]-mu[j][k])*f[k] for k in range(4)) for f in dual)
        ratio=norm/distance(pts[i],pts[j])
        if ratio>worst:worst=ratio;worstpair=(i,j)
        if i>=4:centermax=max(centermax,ratio)
    predicted=(a+b+c)/(max(a,b)+math.hypot(max(a,b),2*min(a,b)))
    assert abs(worst-predicted)<1e-9,(a,b,worst,predicted,worstpair)
    assert centermax<=1+1e-9,(a,b,centermax)
    return len(dual),worst,predicted,centermax,worstpair

if __name__=='__main__':
    ratios=(.02,.1,.2,.25,.3,.4,.411594753826,.45,.5,.65,.75,.9,1,1.1,1.5,2,5,10,50)
    n_pairs=0
    for t in ratios:
        nd,w,p,m,pair=values(t,1)
        n_pairs+=22
        print(f't={t:.12f}; extreme_potentials={nd}; norm={w:.12f}; predicted={p:.12f}; midpoint_pair_bound={m:.12f}; tight={pair}')
    print(f'VERIFIED aspect_ratios={len(ratios)} target_pairs={n_pairs} analytical_formula_matches=yes')
