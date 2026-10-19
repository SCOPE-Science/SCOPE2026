"""Finite Fourier checks for box-supported positive-definite extremizers.
Science/reproducibility only. Uses Python standard library.
"""
import cmath
import itertools
import math

TOL = 3e-9

def one_dim(n, t=0.0):
    if n < 3:
        raise ValueError('n>=3 required')
    a = 1/(2*math.cos(math.pi/n)) if n % 2 else 0.5
    w = [complex(0.0) for _ in range(n)]
    w[0] = complex(1.0)
    w[1] = a + 1j*t
    w[-1] = a - 1j*t
    return w

def dft_1(w):
    n = len(w)
    return [sum(w[x]*cmath.exp(-2j*math.pi*k*x/n) for x in range(n))
            for k in range(n)]

def direct_dft(vals, sizes):
    out = {}
    for k in itertools.product(*(range(n) for n in sizes)):
        v = 0j
        for x in itertools.product(*(range(n) for n in sizes)):
            v += vals[x]*cmath.exp(-2j*math.pi*sum(k[j]*x[j]/sizes[j] for j in range(len(sizes))))
        out[k] = v
    return out

def run():
    tests=0
    for n in range(3,24):
        f=one_dim(n)
        F=dft_1(f)
        assert max(abs(z.imag) for z in F)<TOL
        assert min(z.real for z in F)>-TOL
        val=1+(1/math.cos(math.pi/n) if n%2 else 1)
        assert abs(sum(f).real-val)<TOL
        if n%2:
            zeros={k for k,z in enumerate(F) if abs(z)<TOL}
            assert zeros=={(n-1)//2,(n+1)//2}
        else:
            endpoint=0.5*math.tan(math.pi/n)
            for t in (-endpoint, -endpoint/2, 0, endpoint/2, endpoint):
                p=dft_1(one_dim(n,t))
                assert min(z.real for z in p)>-TOL
                assert max(abs(z.imag) for z in p)<TOL
                assert abs(sum(one_dim(n,t)).real-2)<TOL
                tests+=1
            p=dft_1(one_dim(n,1.1*endpoint))
            assert min(z.real for z in p)<-1e-6
        tests+=1
    for sizes in ((3,3),(3,5),(5,5),(5,7),(7,7),(3,5,7),(4,5),(6,6),(6,5),(8,3)):
        f=[one_dim(n, (0.125*math.tan(math.pi/n)) if n%2==0 else 0) for n in sizes]
        vals={x:math.prod(f[j][x[j]] for j in range(len(sizes)))
              for x in itertools.product(*(range(n) for n in sizes))}
        F=direct_dft(vals,sizes)
        assert max(abs(z.imag) for z in F.values())<5e-8
        assert min(z.real for z in F.values())>-5e-8
        v=math.prod(1+(1/math.cos(math.pi/n) if n%2 else 1) for n in sizes)
        assert abs(sum(vals.values()).real-v)<5e-8
        if all(n%2 for n in sizes):
            nonzero={k for k,z in F.items() if z.real>5e-8}
            assert len(nonzero)==math.prod(n-2 for n in sizes)
            assert all(all(k[j] not in ((n-1)//2,(n+1)//2) for j,n in enumerate(sizes)) for k in nonzero)
        tests+=1
    print('PASS',tests,'Fourier-positivity, sharp-mass, odd-grid-zero-mask, and even-phase checks')

if __name__=='__main__':
    run()
