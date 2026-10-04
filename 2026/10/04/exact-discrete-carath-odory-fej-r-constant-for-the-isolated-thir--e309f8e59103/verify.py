import math

def t3(x): return 4*x*x*x-3*x

def formula(N):
    a=(5*N)//12
    b=(5*N+11)//12
    v=math.cos(2*math.pi*a/N)
    u=math.cos(2*math.pi*b/N)
    den=u*v*(u+v)
    lam=(0.75-(u*u+u*v+v*v))/den
    c=1.0/(4*den)
    return lam,c,u,v

max_factor=0.0
min_grid=1.0
for N in range(6,5001):
    lam,c,u,v=formula(N)
    for r in range(N):
        x=math.cos(2*math.pi*r/N)
        q=1+lam*x+c*t3(x)
        qf=(x-u)*(x-v)*(x+u+v)/(u*v*(u+v))
        max_factor=max(max_factor,abs(q-qf))
        min_grid=min(min_grid,q)
        assert q > -2e-11
        assert abs(q-qf) < 3e-11
    if N%12==0:
        assert abs(lam-2/math.sqrt(3)) < 2e-12
    else:
        Tu,Tv=t3(u),t3(v)
        assert Tu < 2e-12 and Tv > -2e-12
        alpha=Tv/(Tv-Tu); beta=-Tu/(Tv-Tu)
        dual=-1.0/(alpha*u+beta*v)
        assert abs(lam-dual) < 3e-11

# Independent 2D LP by intersections of sampled constraints.
# Constraints are 1 + lambda*x_i + c*T3(x_i) >= 0.
def lp_enum(N):
    xs=[]
    for r in range(N):
        x=math.cos(2*math.pi*r/N)
        pair=(x,t3(x))
        if not any(abs(pair[0]-y[0])<1e-13 and abs(pair[1]-y[1])<1e-13 for y in xs):
            xs.append(pair)
    best=-1e100
    # all intersections of two boundary lines
    for i in range(len(xs)):
        x1,y1=xs[i]
        for j in range(i+1,len(xs)):
            x2,y2=xs[j]
            det=x1*y2-x2*y1
            if abs(det)<1e-13: continue
            lam=(-y2+y1)/det
            c=(-x1+x2)/det
            if all(1+lam*x+c*y >= -2e-10 for x,y in xs):
                best=max(best,lam)
    # one-dimensional degenerate possibility c=0 at a boundary
    for x,y in xs:
        if abs(x)>1e-13:
            lam=-1/x
            if all(1+lam*xx >= -2e-10 for xx,yy in xs): best=max(best,lam)
    return best

lp_cases=0
for N in range(6,91):
    got=lp_enum(N)
    lam,_,_,_=formula(N)
    assert abs(got-lam) < 2e-8, (N,got,lam)
    lp_cases += 1
print(f'closed_form_meshes={5000-6+1} lp_cases={lp_cases} max_factor_error={max_factor:.3e} min_grid={min_grid:.3e}')
print('VERIFY_OK')
