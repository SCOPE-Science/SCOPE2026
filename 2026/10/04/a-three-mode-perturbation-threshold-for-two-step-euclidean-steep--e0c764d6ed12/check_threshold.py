import sympy as sp

K,S,E=sp.symbols('K S E', positive=True)
P=(2*K**2-4*K+2)*S**3 + (-K**3+3*K**2+3*K-1)*S**2 + (-2*K**3-4*K**2-2*K)*S + (K**4+K**3+K**2+K)
F=K**8-16*K**7+44*K**6-96*K**5+118*K**4-96*K**3+44*K**2-16*K+1
assert sp.factor(sp.discriminant(P,S)) == 4*K*(K-1)**2*(K+1)**2*F
assert sp.factor(P.subs(S,1)) == (K-1)**2*(K**2+1)
assert sp.factor(P.subs(S,K)) == K*(K-1)**2*(K**2+1)
assert P.subs({K:14,S:5}) == -755
assert F.subs(K,13) == -8343568
assert F.subs(K,14) == 73119537

y=sp.symbols('y', positive=True)
z=sp.symbols('z', positive=True)
Q=y**4-16*y**3+40*y**2-48*y+32
assert sp.expand(Q.subs(y,z+2)) == z**4-8*z**3-32*z**2-48*z-16
# One positive z-root by Descartes' rule; hence one K>1 root of F.
qroots=[r for r in sp.nroots(Q, n=40, maxsteps=200) if abs(sp.im(r))<sp.Rational(1,10)**20 and sp.re(r)>2]
assert len(qroots)==1
y0=sp.re(qroots[0])
k0=(y0+sp.sqrt(y0**2-4))/2
assert 13 < k0 < 14

# Reconstruct perturbation derivative directly from exact-line-search moments.
def moment(j):
    return (1-E)*K**2/(1+K**2) + E*S**j + (1-E)*K**j/(1+K**2)
a=sp.factor(moment(2)/moment(3))
ndef=lambda j: sp.factor(moment(j)-2*a*moment(j+1)+a**2*moment(j+2))
b=sp.factor(ndef(2)/ndef(3))
R=sp.factor(ndef(0)-2*b*ndef(1)+b**2*ndef(2))
dR=sp.factor(sp.diff(R,E).subs(E,0))
expected=-8*(K-S)*(S-1)*P/(K*(K+1)**5)
assert sp.factor(dR-expected)==0
assert sp.factor(R.subs(E,0)-((K-1)/(K+1))**4)==0

# Exact finite witness at K=14, S=5, epsilon=1/2000.
Rw=sp.factor(R.subs({K:14,S:5,E:sp.Rational(1,2000)}))
base=sp.Rational(13,15)**4
diff=sp.factor(Rw-base)
assert diff>0
print('kappa0 =', sp.N(k0,20))
print('P(14,5) =', P.subs({K:14,S:5}))
print('witness squared-ratio difference =', diff)
print('witness norm ratio =', sp.N(sp.sqrt(Rw),20))
print('two-mode norm factor =', sp.N(sp.Rational(13,15)**2,20))
print('PASS')
