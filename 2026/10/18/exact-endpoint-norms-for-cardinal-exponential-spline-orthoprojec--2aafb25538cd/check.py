"""Finite-section consistency checks for cardinal exponential-spline projection.

The analytical proof, not finite tests, establishes the infinite-dimensional theorem.
Requires Python standard library only.
"""
import math

def gram(t):
    if t == 0:
        return 2/3, 1/6
    s, c = math.sinh(t), math.cosh(t)
    return (s*c-t)/(t*s*s), (t*c-s)/(2*t*s*s)

def phase(t):
    a,b=gram(t)
    d=math.sqrt(a*a-4*b*b)
    q=2*b/(a+d)
    return d,q

def closed_norm(t):
    if t==0: return 2.
    d,q=phase(t)
    c,s=math.cosh(t),math.sinh(t)
    J=((1+q)*(c+1)-2*math.sqrt(1+2*q*c+q*q))/(t*s)
    return 2*J/(d*(1-q))

def hat(t,x):
    if abs(x)>=1: return 0.
    return math.sinh(t*(1-abs(x)))/math.sinh(t) if t else 1-abs(x)

def solve_tri(n,a,b):
    # solve Gx = e_{n//2} for constant tridiagonal Gram G
    lower=[0.]*n; diag=[a]*n; rhs=[0.]*n;rhs[n//2]=1.
    for i in range(1,n):
        w=b/diag[i-1]
        diag[i]-=w*b
        rhs[i]-=w*rhs[i-1]
    out=[0.]*n;out[-1]=rhs[-1]/diag[-1]
    for i in range(n-2,-1,-1):out[i]=(rhs[i]-b*out[i+1])/diag[i]
    return out

def cell_integral(t,A,B):
    # integrate |A phi(u)+B phi(1-u)| for 0<=u<=1
    if t==0:
        if A*B>=0:return (abs(A)+abs(B))/2
        u=abs(A)/(abs(A)+abs(B))
        return (abs(A)*u+abs(B)*(1-u))/2
    I=math.tanh(t/2)/t
    if A*B>=0:return (abs(A)+abs(B))*I
    if A==0 or B==0:return (abs(A)+abs(B))*I
    aa,bb=abs(A),abs(B)
    q=bb/aa
    c,s=math.cosh(t),math.sinh(t)
    J=((1+q)*(c+1)-2*math.sqrt(1+2*q*c+q*q))/(t*s)
    return aa*J

def finite_norm(t,m):
    n=2*m+1
    a,b=gram(t)
    col=solve_tri(n,a,b)
    ext=[0.]+col+[0.]
    return sum(cell_integral(t,ext[i],ext[i+1]) for i in range(n+1))

def direct_kernel_integral(t,M,samples=5000):
    d,q=phase(t)
    total=0.
    for j in range(-M,M+1):
        # midpoint quadrature over each unit grid interval
        for h in range(samples):
            u=(h+0.5)/samples
            x=j+u
            k=(((-q)**abs(j))*hat(t,u)+(-q)**abs(j+1)*hat(t,1-u))/d
            total+=abs(k)/samples
    return total

def main():
    assertions=0
    for t in [0.2,0.5,1.0,2.0,3.0,5.0,7.0]:
        a,b=gram(t)
        assert 0<2*b<a;assertions+=1
        d,q=phase(t)
        assert 0<q<1 and abs((a*q-b*(1+q*q)))<1e-10;assertions+=1
        v=closed_norm(t)
        f=finite_norm(t,35)
        assert abs(f-v)<1e-8,(t,v,f);assertions+=1
        z=direct_kernel_integral(t,20,1000)
        assert abs(z-v)<3e-5,(t,v,z);assertions+=1
    for t in [.05,.1,.2]:
        v=closed_norm(t)
        # Taylor's theorem prediction: 2+t²/120+O(t⁴)
        assert abs((v-2)/t**2-1/120)<0.002*t*t;assertions+=1
    assert abs(finite_norm(0,35)-2)<1e-8;assertions+=1
    assert closed_norm(.2)>2 and closed_norm(3)>2 and closed_norm(10)>2;assertions+=1
    assert abs(closed_norm(15)-2)<.00001;assertions+=1
    print(f'PASS: {assertions} analytical-formula and independent finite-section consistency assertions')
if __name__=='__main__':main()
