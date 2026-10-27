import sympy as s
import mpmath as mp
mp.mp.dps=42
x=s.symbols('x',real=True)
tests=0
for k in range(1,15):
    H=s.exp(-x)*x**k*(x-k)*(x-k-1)/s.factorial(k+1)
    P=-x**3+(3*k+3)*x**2-(3*k*k+4*k+1)*x+k*k*k+k*k
    assert s.simplify(s.diff(H,x)-s.exp(-x)*x**(k-1)*P/s.factorial(k+1))==0; tests+=1
    roots=sorted(float(s.re(t)) for t in s.nroots(P,maxsteps=100))
    u,v,w=roots
    assert 0<u<k<v<k+1<w;tests+=1
    hf=lambda t: (lambda q: mp.exp(-q)*q**k*(q-k)*(q-k-1)/mp.factorial(k+1))(mp.mpf(t))
    assert hf(w)>hf(u)>0 and hf(v)<0;tests+=1
    lf=lambda z:mp.quad(lambda t:mp.exp(-t)*t**(k-1)*(t-k)**2/mp.factorial(k),[0,z])
    rf=lambda z:mp.quad(lambda t:mp.exp(-t)*t**k*(t-(k+1))**2/mp.factorial(k+1),[0,z])
    for a,b in [(0.25*k, k+2.5),(0.5*k,k+6.3),(k+0.3, k+0.85)]:
        if b<=a:b=a+5
        v1=(lf(b)-lf(a))-(rf(b)-rf(a))
        v2=hf(b)-hf(a)
        
        if abs(v1-v2)>=mp.mpf('1e-13'): print('FAIL',k,a,b,mp.nstr(v1,18),mp.nstr(v2,18),mp.nstr(v1-v2,15));raise SystemExit
        tests+=1
    for a,expected in [(u/2,3),((u+k)/2,2),(float(k),1),((k+v)/2,1),((v+k+1)/2,0),((k+1+w)/2,1),(w+1,0)]:
        z=hf(a)
        points=[a]+[t for t in [u,float(k),v,float(k+1),w] if t>a+1e-10]+[w+250 if w+250>a else a+250]
        counts=0
        for j in range(len(points)-1):
            t0,t1=points[j],points[j+1]
            f0,f1=hf(t0)-z,hf(t1)-z
            if f0*f1<0: counts+=1
            if j<len(points)-2 and abs(f1)<mp.mpf('1e-28'):counts+=1
        assert counts==expected,(k,a,counts,expected);tests+=1
print(f'PASS: {tests} symbolic, root-interval, numerical quadrature and level-crossing checks for k=1,...,14; finite tests are not all-degree proof.')
