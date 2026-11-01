"""Exact symbolic and independent binary-word checks for fan two-cycle counts.
Requires Python 3 and sympy. No numerical fitting is used in the proof.
"""
import itertools
import sympy as sp
z,t=sp.symbols('z t')
pairs=[(0,0),(0,1),(1,0),(1,1)]
T=sp.zeros(4,4)
for i,(a,b) in enumerate(pairs):
    for c in (0,1):
        T[i,pairs.index((b,c))]=z**b*(b+(a!=b)+(b!=c))
E=sp.Matrix([[z**a*(a+(a!=b)) for a,b in pairs]])
L=sp.Matrix([z**b*(b+(a!=b)) for a,b in pairs])
P=sp.factor(t**2*(E*(sp.eye(4)-t*T).inv()*L)[0])
Pg=-t**2*z*(t**3*z**2+2*t**2*z**2+5*t**2*z+8*t*z+3*t+z+4)/(t**4*z**2+2*t**3*z**2+3*t**3*z+6*t**2*z+t*z-1)
assert sp.factor(P-Pg)==0
N=sp.factor((z*sp.diff(P,z)).subs(z,1))
Ng=t**2*(6-16*t**2-7*t**3-t**4)/((1+t)*(1-3*t-t**2)**2)
assert sp.factor(N-Ng)==0
# Independent direct word count (no transfer matrix involved).
def direct_word(n):
    v=0
    for bits in itertools.product((0,1),repeat=n):
        total=sum(bits)
        weight=total
        for i,x in enumerate(bits):
            weight*=x+(i>0 and bits[i-1]!=x)+(i<n-1 and bits[i+1]!=x)
        v+=weight
    return v
for n in range(2,16):
    transfer=sp.diff((E*T**(n-2)*L)[0],z).subs(z,1)
    assert transfer==direct_word(n),(n,transfer,direct_word(n))
    print('fan',n,transfer)
# Independent wheel partition function for comparing edge deletion.
Pw=sp.factor(-z*sp.diff(sp.det(sp.eye(4)-t*T),z)/sp.det(sp.eye(4)-t*T)).subs(z,1)
W_expected=t*(1+5*t+2*t*t)/((1+t)*(1-3*t-t*t))
assert sp.factor(Pw-W_expected)==0
rho=(sp.sqrt(13)-3)/2
Bw=sp.simplify((1+5*rho+2*rho*rho)/((1+rho)*sp.sqrt(13)))
Bf=sp.simplify((6-16*rho**2-7*rho**3-rho**4)/(13*(1+rho)))
assert sp.simplify(Bf/Bw-(1-2/sp.sqrt(13)))==0
print('rational_GF_OK')
print('wheel_boundary_ratio=',sp.simplify(Bf/Bw))
