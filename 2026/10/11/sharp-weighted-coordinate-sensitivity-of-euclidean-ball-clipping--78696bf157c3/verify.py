"""Independent finite checks of the analytic weighted-coordinate radial clipping theorem."""
import math, random

def clip(x):
    r=math.sqrt(sum(t*t for t in x))
    return [t/max(1,r) for t in x]

def norm_inf(x,w): return max(abs(a)/b for a,b in zip(x,w))
def norm_one(x,w): return sum(abs(a)*b for a,b in zip(x,w))
def jac(u):
    n=len(u)
    return [[(1.0 if i==j else 0.0)-u[i]*u[j] for j in range(n)] for i in range(n)]

def matrix_inf(A,w):
    return max(sum(abs(v)*w[j]/w[i] for j,v in enumerate(row)) for i,row in enumerate(A))
def matrix_one(A,w):
    return max(sum(w[i]*abs(A[i][j])/w[j] for i in range(len(A))) for j in range(len(A)))

def extremal_u(w):
    i=min(range(len(w)),key=w.__getitem__)
    W2=sum(z*z for z in w)
    t=(1-w[i]/math.sqrt(W2))/2
    U=math.sqrt(t)
    rest=math.sqrt(W2-w[i]**2)
    u=[math.sqrt(1-t)*z/rest if j!=i else U for j,z in enumerate(w)]
    return i,u

rng=random.Random(1019)
checks=0
for n in range(2,13):
    for _ in range(50):
        w=[math.exp(rng.uniform(-2,2)) for _ in range(n)]
        opt=(1+math.sqrt(sum(z*z for z in w))/min(w))/2
        i,u=extremal_u(w)
        assert abs(sum(t*t for t in u)-1)<1e-12
        A=jac(u)
        assert abs(matrix_inf(A,w)-opt)<2e-12,(n,w,opt,matrix_inf(A,w))
        assert abs(matrix_one(A,w)-opt)<2e-12
        checks+=3
        for _ in range(10):
            vec=[rng.gauss(0,1) for _ in range(n)]
            den=math.sqrt(sum(t*t for t in vec))
            uu=[t/den for t in vec]
            J=jac(uu)
            assert matrix_inf(J,w)<=opt+1e-12
            assert matrix_one(J,w)<=opt+1e-12
            checks+=2
        # Outside point in the exact maximizing boundary direction, test local quotient.
        x=[(1+1e-4)*k for k in u]
        # row-optimizing input direction h: h_i=+w_i, h_j=-w_j when u_j>=0 and u_i>=0
        h=[(-ww if j!=i else ww) for j,ww in enumerate(w)]
        eps=1e-7/max(w)
        y=[xx+eps*hh for xx,hh in zip(x,h)]
        Q=norm_inf([a-b for a,b in zip(clip(y),clip(x))],w)/(eps*norm_inf(h,w))
        assert Q>=opt/(1+1e-4)-1e-5,(Q,opt)
        checks+=1
print('PASS',checks,'weighted Jacobian and local sharpness checks')
