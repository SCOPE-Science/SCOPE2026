"""Independent finite-group checks for the rotation-angle negative-type threshold.
Only standard-library Python and NumPy; all outputs are deterministic.
"""
import itertools, math
import numpy as np

def sign_of_perm(p):
    inversions=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return (-1)**inversions

def compose(p,q): return tuple(p[q[i]] for i in range(5))
def inverse(p): return tuple(p.index(i) for i in range(5))
def order(p):
    e=tuple(range(5)); q=e
    for i in range(1,61):
        q=compose(p,q)
        if q==e: return i
    raise AssertionError('nonfinite permutation order')
G=[p for p in itertools.permutations(range(5)) if sign_of_perm(p)==1]
assert len(G)==60
identity=tuple(range(5)); index={g:i for i,g in enumerate(G)}
rep=(1,2,3,4,0)
C5A={compose(compose(h,rep),inverse(h)) for h in G}
assert len(C5A)==12
assert sum(order(g)==5 for g in G)==24
angles={}
for g in G:
    o=order(g)
    angles[g]= {1:0.,2:math.pi,3:2*math.pi/3}.get(o)
    if o==5: angles[g]=(2 if g in C5A else 4)*math.pi/5
assert sorted(set(round(x,10) for x in angles.values()))==sorted(set(round(x,10) for x in [0,math.pi,2*math.pi/3,2*math.pi/5,4*math.pi/5]))
phi=(1+math.sqrt(5))/2; other=(1-math.sqrt(5))/2
sizes=np.array([15,20,12,12]); rr=np.array([1.,2/3,2/5,4/5])
chars=np.array([[-1,0,phi,other],[-1,0,other,phi],[0,1,-1,-1],[1,-1,0,0]])
dims=np.array([3,3,4,5]);
critical=math.log(4/3)/math.log(3/2)
assert critical<.75
print('critical_exponent',format(critical,'.16g'))
for exponent in [0.10,0.50,critical,0.73,1.0,1.5]:
    spec=(chars@(sizes*rr**exponent))*math.pi**exponent/dims
    print('exponent',format(exponent,'.12g'),'character_eigenvalues',list(np.round(spec,10)))
    mat=np.empty((60,60));
    for i,g in enumerate(G):
        ig=inverse(g)
        for j,h in enumerate(G): mat[i,j]=angles[compose(ig,h)]**exponent
    es=np.linalg.eigvalsh(mat)
    expected=[sum(sizes*rr**exponent)*math.pi**exponent]
    for val,d in zip(spec,dims): expected.extend([val]*(d*d))
    err=np.max(np.abs(np.sort(expected)-es))
    print('  spectral_reconstruction_error',err,'max_centered_eigenvalue',max(spec))
    assert err<1e-9
    if exponent<=critical-1e-8: assert max(spec)<0
    if exponent>=critical+1e-8: assert spec[-1]>0
    if abs(exponent-critical)<1e-12: assert abs(spec[-1])<1e-11 and all(x<-1e-8 for x in spec[:-1])
    for t in [.005,.1,2.]:
        gram=np.exp(-t*mat)
        gs=np.linalg.eigvalsh(gram)
        print('   t',t,'min_eig',format(gs[0],'.8g'))
        if exponent<=critical+1e-10: assert gs[0]>-1e-10
        if exponent>=critical+1e-8 and t==.005: assert gs[0]<-1e-7
print('PROOF-SUPPLEMENT CHECKS PASSED')
