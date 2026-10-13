import sympy as sp
u,v=sp.symbols('u v')

def std_dim(d,k):
    f=sp.expand(u*v*(u**k-v**d))
    fu=sp.diff(f,u); fv=sp.diff(f,v)
    N=d*k+d+k
    assert sp.expand(N*f - (d*u*fu+k*v*fv))==0
    G=sp.groebner([fu,fv],u,v,order='grevlex')
    assert G.is_zero_dimensional
    lms=[]
    for p in G.polys:
        lm=p.LM(order=G.order)
        # Monomial repr exponents tuple accessible .exponents
        lms.append(tuple(lm.exponents))
    # Standard monomials. A safe finite box: one more than max pure powers from LMs.
    pure_u=[a for a,b in lms if b==0]
    pure_v=[b for a,b in lms if a==0]
    assert pure_u and pure_v, (d,k,lms)
    au=min(pure_u); bv=min(pure_v)
    count=0
    for a in range(au):
      for b in range(bv):
        if not any(a>=i and b>=j for i,j in lms):
          count += 1
    expected=(d+1)*(k+1)
    assert count==expected,(d,k,count,expected,lms)
    return count,lms

for d in range(2,9):
    for k in range(1,d+1):
        std_dim(d,k)

D,K,M=sp.symbols('D K M', positive=True, integer=True)
N=D*K+D+K
mu=sp.factor((N-D)*(N-K)/(D*K))
assert sp.expand(mu-(D+1)*(K+1))==0

tau=sp.expand((M-1)**2+(D+1)*(D+M))
free_tau=sp.expand((D+M)**2-(M-1)*(D+1))
assert sp.expand(tau-free_tau)==0
phi=(D+K)/(D*K+D+K)
assert sp.factor(sp.diff(phi,K)) == -D**2/(D*K+D+K)**2

# Same degree/exponents but different lct: d=6,m=3, partitions (2,2,2) and (4,1,1).
def phi_num(d,k):
    return sp.Rational(d+k,d*k+d+k)
assert min(sp.Rational(2,3),phi_num(6,2))==sp.Rational(2,5)
assert min(sp.Rational(2,3),phi_num(6,4),phi_num(6,1))==sp.Rational(5,17)

print('VERIFY_OK')
print('checked_local_jacobian_dims=2<=d<=8,1<=k<=d')
print('local_tau_formula=(d+1)(k+1)')
print('global_tau_identity=PASS')
print('lct_monotonicity_derivative=-d^2/(dk+d+k)^2')
print('example_d6_m3_lct_222=2/5_lct_411=5/17')
