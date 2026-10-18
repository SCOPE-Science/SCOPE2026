"""Numerical and algebraic diagnostics for a critical hybrid opinion dyad.
This script is a reproducibility aid, not a proof of infinite-time limits.
"""
import math

def theory(d,alpha,gr,h,gain):
    L=alpha+gr; a=d*gr/L; K=d*L*L/3.0
    q=math.exp(-a*h)
    D=1-q+gain*q
    C=K/a*gain*(1-q)/D
    return q,D,C,(2*C)**-.5

def step(z,v,d,alpha,gr,h,gain):
    # Explicit RK4, variable number of flow subdivisions.
    nsub=max(4,math.ceil(h/.22)); dt=h/nsub
    def f(w): return -d*w+d/(alpha+gr)*math.tanh(alpha*w+gr*v)
    for _ in range(nsub):
        k1=f(z); k2=f(z+dt*k1/2)
        k3=f(z+dt*k2/2); k4=f(z+dt*k3)
        z+=dt*(k1+2*k2+2*k3+k4)/6
    return z,v+gain*(z-v)

def main():
    cases=[(1.0,0.7,1.1,1.6,0.55),(1.0,0.0,1.3,0.5,1.0),
           (0.8,0.5,0.8,2.0,0.25),(1.3,1.4,0.3,3.0,0.75),
           (0.9,1.7,0.9,1.0,0.4)]
    for d,alpha,gr,h,gain in cases:
        q,D,C,A=theory(d,alpha,gr,h,gain)
        assert 0<q<1 and 0<D<1.001 and C>0
        left_z=gain*q/D; left_v=(1-q)/D
        J=[[q,1-q],[gain*q,1-gain*q]]
        assert abs(left_z+left_v-1)<1e-13
        assert all(abs(left_z*J[0][j]+left_v*J[1][j]-[left_z,left_v][j])<1e-13 for j in (0,1))
        z,v=0.6,0.2
        vals={}
        for k in range(1,60001):
            nz,nv=step(z,v,d,alpha,gr,h,gain)
            assert nz>0 and nv>0
            assert max(nz,nv)<max(z,v)+1e-13
            z,v=nz,nv
            if k in (5000,20000,60000): vals[k]=(z*math.sqrt(k),v*math.sqrt(k))
        err=max(abs(z*math.sqrt(60000)/A-1),abs(v*math.sqrt(60000)/A-1))
        assert err<.018,(cases.index((d,alpha,gr,h,gain)),err)
        print('PARAM',d,alpha,gr,h,gain,'C=',format(C,'.10g'), 'limit=',format(A,'.10g'),'scaled=',vals, 'relerr=',format(err,'.6g'))
        # For fixed d, alpha, gr, gain, h -> C increases, C/h strictly decreases.
        _,_,Cshort,_=theory(d,alpha,gr,h/2,gain)
        _,_,Clong,_=theory(d,alpha,gr,h*2,gain)
        assert Cshort<C<Clong
        assert Cshort/(h/2)>C/h>Clong/(h*2)
    print('All algebraic checks, asymptotic diagnostics and time-step comparisons passed.')
if __name__=='__main__': main()
