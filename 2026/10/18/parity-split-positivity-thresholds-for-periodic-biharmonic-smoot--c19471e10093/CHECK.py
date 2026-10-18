"""Reproducible finite checks for periodic biharmonic smoothing.

Uses only Python's standard library. This does not certify limits in n.
Run: python3 CHECK.py
"""
import math


def root_bisect(f, lo, hi, steps=80):
    f_lo = f(lo)
    assert f_lo * f(hi) < 0
    for _ in range(steps):
        mid = (lo + hi) / 2
        if f_lo * f(mid) <= 0:
            hi = mid
        else:
            lo, f_lo = mid, f(mid)
    return (lo + hi) / 2


def constants(mmax=70000):
    a = root_bisect(lambda z: math.sin(z)*math.cosh(z)+math.cos(z)*math.sinh(z),2.2,2.5)
    c = 1/(64*a**4)
    gamma = 0.0
    h = 0.0
    gxx = 0.0
    for m in range(1,mmax+1):
        lam = (2*math.pi*m)**4
        fac = 1 + c*lam
        sg = -1 if m%2 else 1
        gamma += -2*sg*lam/fac**2
        h += 2*sg*(32/3)*c*math.pi**6*m**6/fac**2
        gxx += -2*sg*(2*math.pi*m)**2/fac
    return a,c,gamma,h,gxx,-h/gamma,-(h+gxx/8)/gamma


def closed_green(c, x):
    s = 1/(math.sqrt(2)*c**.25)
    a = s/2
    U = lambda z: math.sinh(z)*math.cos(z)-math.cosh(z)*math.sin(z)
    V = lambda z: math.sinh(z)*math.cos(z)+math.cosh(z)*math.sin(z)
    z=s*(.5-min(x%1,1-x%1))
    den=U(a)**2+V(a)**2
    return s*(V(a)*math.cosh(z)*math.cos(z)-U(a)*math.sinh(z)*math.sin(z))/den


def fourier_kernel(n, t, j):
    return sum(math.cos(2*math.pi*m*j/n)/(1+t*(4*math.sin(math.pi*m/n)**2)**2)
               for m in range(n))/n


def full_matrix_inverse(n, t):
    L = [[(2 if i == j else 0) - (1 if (j-i)%n in (1,n-1) else 0) for j in range(n)] for i in range(n)]
    L2 = [[sum(L[i][k]*L[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    B = [[(1.0 if i==j else 0.0)+t*L2[i][j] for j in range(n)] for i in range(n)]
    augmented = [B[i]+[float(i==j) for j in range(n)] for i in range(n)]
    for i in range(n):
        p=max(range(i,n), key=lambda k:abs(augmented[k][i]))
        augmented[i],augmented[p]=augmented[p],augmented[i]
        d=augmented[i][i]
        assert abs(d)>1e-13
        augmented[i]=[v/d for v in augmented[i]]
        for k in range(n):
            if k!=i:
                d=augmented[k][i]
                augmented[k]=[augmented[k][j]-d*augmented[i][j] for j in range(2*n)]
    return [row[n:] for row in augmented]


def main():
    a,c,gamma,h,gxx,e,o = constants()
    assert 2.36501<a<2.36503
    assert .00049943<c<.00049945
    assert gamma>0 and gxx>0
    assert .00104<e<.00106 and -.00361<o<-.00358
    checks=5
    for C in (c/1.1,c,c*1.1,c*2,0.02):
        for j in range(41):
            x=j/80
            g=closed_green(C,x)
            approximation=1+sum(2*math.cos(2*math.pi*m*x)/(1+C*(2*math.pi*m)**4) for m in range(1,1400))
            assert abs(g-approximation)<2e-8, (C,x,g,approximation)
            checks+=1
    for n in range(5,21):
        for t in (.001,.04,.5,3,20,150):
            inv=full_matrix_inverse(n,t)
            for j in range(n):
                assert abs(inv[0][j]-fourier_kernel(n,t,j))<5e-10,(n,t,j)
                checks+=1
            assert abs(sum(inv[0])-1)<2e-9
            checks+=1
    for n in (20,21,30,31,40,41,60,61,80,81,100,101,160,161):
        def center_tau(t):return fourier_kernel(n,t,n//2)
        tcrit=root_bisect(center_tau,c*n**4*.8,c*n**4*1.2)
        scaled=(tcrit/n**4-c)*n**2
        limit=e if n%2==0 else o
        tol = .05 if n<=21 else .015 if n<=31 else .007 if n<=41 else .003 if n<=81 else .0008
        assert abs(scaled-limit)<tol,(n,scaled,limit)
        for tfac in (1.025,1.1,1.35,2.0):
            t=tcrit*tfac
            vals=[fourier_kernel(n,t,j) for j in range(n)]
            assert min(vals)>-2e-12,(n,t,min(vals))
            checks+=1
        for tfac in (.95,.975):
            assert center_tau(tcrit*tfac)<0,(n,tfac)
            checks+=1
        checks+=1
    print('CHECK_OK',checks,'assertions')
    print('critical root = %.15f; critical scale = %.16g' %(a,c))
    print('even correction = %.12g; odd correction = %.12g'%(e,o))
    print('gamma = %.12g; H = %.12g; curvature = %.12g'%(gamma,h,gxx))

if __name__=='__main__':main()
