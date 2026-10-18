"""Exact checks for two equal-gain noisy leaders on K_{r+1} with two leaves at one hub.
Requires SymPy. This checks representative finite orders and does not replace the all-order proof.
"""
import sympy as sp
from itertools import combinations

R, g = sp.symbols('r g', positive=True)
h = 2/(R+1)
n = R+3
S={'H':2*(2*R+1)/(R+1),'L':(R**2+6*R+3)/(R+1),'C':2*(2*R+3)/(R+1)}
res={'HL':1,'HC':h,'LL':2,'LC':1+h,'CC':h}
T={'HL':R+3,'HC':16/(R+1)**2,'LL':8,'LC':(R**3+5*R**2+7*R+19)/(R+1)**2,'CC':8/(R+1)**2}

def formula(orbit):
    u,v=orbit
    dist=res[orbit]
    return n/(2*g)+(S[u]+S[v])/2-n*dist/4-g*T[orbit]/(4*(2+g*dist))
J={x:formula(x) for x in res}
assert sp.simplify((J['HL']-J['HC'])-(R-1)*(R+1-g)*(g+R+3)/(2*(g+2)*(R+1)*(g+R+1)))==0
F1=(R-1)*(R+1)**2-4*(R+1)*g-(R-1)*g**2
assert sp.simplify((J['LC']-J['HC'])-F1/(2*(g+R+1)*(g*(R+3)+2*(R+1))))==0
F2=-(R-1)*g**2+2*(R**2+R+2)*g+2*(R**2-1)
assert sp.simplify((J['HL']-J['LC'])-F2/((g+2)*(R+1)*(g*(R+3)+2*(R+1))))==0
assert sp.simplify((J['LL']-J['HL'])-((R-1)*g**2+2*(R-2)*g+R-1)/(2*(g+1)*(g+2)))==0
assert sp.simplify((J['CC']-J['HC'])-(3*g+2*R+2)/((R+1)*(g+R+1)))==0
print('Five universal symbolic pairwise identities: passed.')

for r in range(2,10):
    N=r+3
    L=sp.zeros(N)
    def edge(u,v):
        L[u,u]+=1;L[v,v]+=1;L[u,v]-=1;L[v,u]-=1
    for i in range(1,N): edge(0,i)
    for i in range(3,N):
        for j in range(i+1,N): edge(i,j)
    for gain in [sp.Rational(1,8),sp.Rational(1,2),sp.Rational(1),sp.Rational(3),sp.Rational(10),sp.Rational(23)]:
        for pair in combinations(range(N),2):
            types=['H' if i==0 else 'L' if i in [1,2] else 'C' for i in pair]
            orbit=''.join(sorted(types,key=lambda x:'HLC'.index(x)))
            M=L.copy()
            for i in pair: M[i,i]+=gain
            actual=sp.trace(M.inv())
            expected=J[orbit].subs({R:r,g:gain})
            assert sp.simplify(actual-expected)==0, (r,gain,pair,orbit)
    print(f'r={r}: complete five-orbit exact checks passed')
print('All finite exact matrix checks: passed')
