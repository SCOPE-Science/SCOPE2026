"""Reproducibility checks for quadratic-polynomial two-channel three-point phase retrieval.
The analytical proof in RESULT.md is independent of this finite test.
"""
import cmath, math, random
from fractions import Fraction

W=complex(-0.5,math.sqrt(3)/2)

def moments(a,b,c):
    return (abs(a)**2+abs(b)**2+abs(c)**2,
            b*a.conjugate()+c*b.conjugate()+a*c.conjugate(),
            abs(b)**2+4*abs(c)**2,
            2*c*b.conjugate())

def samples(a,b,c):
    return [(abs(a+b*W**j+c*W**(2*j))**2,
             abs(b+2*c*W**j)**2) for j in range(3)]

def recovered_moments(s):
    I=[v[0] for v in s]; J=[v[1] for v in s]
    return (sum(I)/3,sum(I[j]*W**(-j) for j in range(3))/3,
            sum(J)/3,sum(J[j]*W**(-j) for j in range(3))/3)

def reconstruct(s,tol=1.e-8):
    h0,h1,j0,j1=recovered_moments(s)
    discr=j0*j0-4*abs(j1)**2
    if discr<-tol: return []
    tvals=[(j0+math.sqrt(max(0.,discr)))/8,(j0-math.sqrt(max(0.,discr)))/8]
    results=[]
    for t in tvals:
        if t<=tol: continue
        c=math.sqrt(t); b=j1.conjugate()/(2*c)
        den=c*c-abs(b)**2
        if abs(den)<tol:continue
        v=h1-c*b.conjugate()
        a=(c*v-b*v.conjugate())/den
        if abs((abs(a)**2+abs(b)**2+c*c)-h0)<tol*max(1,h0):
            results.append((a,b,c))
    return results

# Exact integer equality of the three Fourier intensities: the first and the
# remaining two values follow from the constant/first cyclic autocorrelation.
P=(7,6,2); Q=(8,4,3)
def exact_invariants(a,b,c):
    return (a*a+b*b+c*c, a*b+b*c+c*a, b*b+4*c*c, 2*b*c)
assert exact_invariants(*P)==exact_invariants(*Q)
assert P!=Q
print('exact witness:', exact_invariants(*P), 'I=(225,21,21) J=(100,28,28)')
for a,b,c in (P,Q):
    s=samples(a,b,c)
    assert all(abs(s[j][0]-v)<1e-10 for j,v in enumerate((225,21,21)))
    assert all(abs(s[j][1]-v)<1e-10 for j,v in enumerate((100,28,28)))

# Exact branch-structure check for a=0,b=3,c=1: the alternative branch has
# c'=3/2,b'=2,a'=0, but differs in the zeroth P intensity moment.
assert exact_invariants(0,3,1)[0]==10
assert exact_invariants(Fraction(0),Fraction(2),Fraction(3,2))[0]==Fraction(25,4)
print('analytic nonidentity witness: branch energies 10 and 25/4')

# Finitely sampled stress test; it supports but never substitutes for the proof.
rng=random.Random(20261013)
checked=0
for k in range(1000):
    a=complex(rng.uniform(-4,4),rng.uniform(-4,4))
    b=complex(rng.uniform(-4,4),rng.uniform(-4,4))
    c=complex(rng.uniform(0.5,3),rng.uniform(-3,3))
    ss=samples(a,b,c)
    h=moments(a,b,c)
    dh=recovered_moments(ss)
    assert max(abs(h[j]-dh[j]) for j in range(4))<1e-10
    sols=reconstruct(ss,tol=1e-7)
    # Normalize original to gauge c>0.
    phase=abs(c)/c
    a0,b0,c0=a*phase,b*phase,abs(c)
    assert any(max(abs(v[0]-a0),abs(v[1]-b0),abs(v[2]-c0))<1e-5 for v in sols)
    assert len(sols)==1, (k,sols)
    checked+=1
print('randomized branch checks:',checked,'all uniquely recovered within tolerance')
