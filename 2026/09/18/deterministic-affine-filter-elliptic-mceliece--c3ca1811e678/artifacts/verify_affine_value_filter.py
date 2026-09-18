import math


def inv(a,p):
    return pow(a,p-2,p)

def chi(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def curve_points(p,A,B):
    pts=[None]
    squares={y*y%p: [] for y in range(p)}
    # rebuild values with actual roots
    roots={}
    for y in range(p): roots.setdefault(y*y%p,[]).append(y)
    for x in range(p):
        rhs=(x*x*x+A*x+B)%p
        for y in roots.get(rhs,[]): pts.append((x,y))
    return pts

def f2_data(p,A,B):
    assert (4*A**3+27*B**2)%p != 0
    pts=curve_points(p,A,B)
    R=next(P for P in pts if P is not None and P[1] != 0)
    alpha,beta=R
    bp=(-beta)%p
    gamma=((3*alpha*alpha+A)*inv(2*bp,p))%p
    def H(z):
        return (1-4*gamma*z+12*alpha*z*z-8*bp*z*z*z)%p
    def f2(P):
        if P is None:
            return 0
        if P==R:
            return None
        x,y=P
        d=(x-alpha)%p
        if d:
            return ((y-bp-gamma*d)%p)*inv(d*d%p,p)%p
        # P=-R, removable value from the second-order local term
        return ((3*alpha-gamma*gamma)%p)*inv(2*bp,p)%p
    V_direct={f2(P) for P in pts if P!=R}
    V_char={z for z in range(p) if chi(H(z),p)>=0}
    return pts,R,H,V_direct,V_char

def candidate_counts(p,V,gs):
    alive=[(a,b) for a in range(1,p) for b in range(p)]
    prefix=[len(alive)]
    for g in gs:
        alive=[(a,b) for (a,b) in alive if (a*g+b)%p in V]
        prefix.append(len(alive))
    return prefix

def bound(p,m):
    if m==0:
        return p*(p-1)
    return p*p/(2**m) + 1.5*m*(p**1.5) + 3*m*m*p

def run_case(p,A,B):
    pts,R,H,Vd,Vc=f2_data(p,A,B)
    assert Vd==Vc
    L=math.ceil(0.5*math.log2(p))
    gs=sorted(Vd)[:L]
    assert len(gs)==L and len(gs)==len(set(gs))
    pref=candidate_counts(p,Vd,gs)
    for m,c in enumerate(pref):
        assert c <= math.ceil(bound(p,m)+1e-9)
    actual_tests=sum(pref[:-1])
    summed_bound=sum(bound(p,m) for m in range(L))
    assert actual_tests <= summed_bound+1e-9
    return {
        'q':p,'curve':f'y^2=x^3+{A}x+{B}','points':len(pts),'R0':R,
        'V_size':len(Vd),'L':L,'survivors':pref[-1],
        'survivor_bound':bound(p,L),'sequential_tests':actual_tests,
        'sequential_bound':summed_bound
    }

if __name__=='__main__':
    cases=[(101,2,3),(251,2,3),(509,2,3)]
    print('Affine value-set filter verification')
    for c in cases:
        r=run_case(*c)
        print(r)
    print('PASS')
