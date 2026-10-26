"""Exact reproducibility checks for classical RK4 positivity on strongly regular graphs.

Requires Python 3 and sympy. Contains only symbolic and rational finite checks;
the arbitrary-size assertions are proved algebraically in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations
import sympy as sp

k, la, mu, h, n = sp.symbols('k la mu h n')
I, A, J = sp.symbols('I A J')

def by_L(triple):
    a, b, c = triple
    # Multiplication by k I - A in the SRG adjacency algebra.
    return tuple(map(sp.expand, (
        k*a-(k-mu)*b,
        -a+(k-la+mu)*b,
        -mu*b,
    )))

# Derive the polynomial in the adjacency algebra, not via a graph-specific formula.
power = (sp.Integer(1), sp.Integer(0), sp.Integer(0))
coeff = list(power)
for order in range(1, 5):
    power = by_L(power)
    for i in range(3):
        coeff[i] += (-h)**order * power[i]/sp.factorial(order)
coeff = [sp.factor(f) for f in coeff]

adj = sp.factor(coeff[1] + coeff[2])
non = sp.factor(coeff[2])
H2 = 3*k*(k-la+mu)+(k-mu)+(la-mu)**2
N_expected = mu*h**2*(12-4*(2*k-la+mu)*h+H2*h**2)/24
assert sp.simplify(non-N_expected)==0
W=5*k*(k-la+mu)+3*(k-mu)+2*(la-mu)**2
Q=12-4*(2*k-la+mu)*h+H2*h*h
assert sp.factor(sp.discriminant(Q,h)+16*W)==0
m2=2*k-la
m3=3*k*k-3*k*la+k*mu+k+la*la-la*mu-mu
m4=sp.factor(-sp.diff(adj,h,4).subs(h,0))
# Adjacent-entry series h(1-M2 h/2+M3 h^2/6-M4 h^3/24).
A_expected=h*(1-m2*h/2+m3*h*h/6-m4*h**3/24)
assert sp.simplify(adj-A_expected)==0

# Strict negative derivative of the root cubic from the two positive spectra:
z,t=sp.symbols('z t',positive=True)
R=(1-t*z*z)**2/((1-t*z)*(1-t*z**3))
assert sp.factor(sp.diff(R,t)-z*(1-z)**2*(1-t**2*z**4)/((1-t*z)**2*(1-t*z**3)**2))==0
assert sp.factor(R.subs(t,1)-(1+z)**2/(1+z+z*z))==0
assert sp.factor(sp.Rational(4,3)-(1+z)**2/(1+z+z*z)-(z-1)**2/(3*(z*z+z+1)))==0

# Johnson J(n,2) / triangular graph specialization.
tri={k:2*(n-2),la:n-2,mu:4}
tri_adj=sp.factor(adj.subs(tri, simultaneous=True))
tri_non=sp.factor(non.subs(tri, simultaneous=True))
tri_P=24-(36*n-72)*h+(28*n*n-88*n+48)*h**2-(15*n**3-62*n*n+68*n-24)*h**3
tri_Q=12-(12*n-8)*h+(7*n*n-10*n+4)*h**2
assert sp.simplify(tri_adj-h*tri_P/24)==0
assert sp.simplify(tri_non-h*h*tri_Q/6)==0
assert sp.factor(sp.discriminant(tri_Q,h)+32*(6*n*n-9*n+4))==0
assert sp.factor(tri_P.subs(h,1/(n-2))-(n**3-10*n*n+12*n+24)/(n-2)**3)==0

def make_graph(v, edge_test):
    M=sp.zeros(len(v))
    for i,j in combinations(range(len(v)),2):
        if edge_test(v[i],v[j]):
            M[i,j]=M[j,i]=1
    return M

def families():
    for m in range(4,10):
        v=list(combinations(range(m),2))
        yield ('triangular',m,make_graph(v,lambda x,y:len(set(x)&set(y))==1))
    for m in range(2,6):
        v=list((i,j) for i in range(m) for j in range(m))
        yield ('rook',m,make_graph(v,lambda x,y:(x[0]==y[0]) != (x[1]==y[1])))
    for r in range(2,5):
        for size in range(2,5):
            v=list((part,i) for part in range(r) for i in range(size))
            yield ('multipartite',(r,size),make_graph(v,lambda x,y:x[0]!=y[0]))
    yield ('cycle5',5,make_graph(list(range(5)),lambda i,j:(i-j)%5 in (1,4)))
    # Generalized Petersen G(5,2), standard Petersen graph.
    v=list(range(10))
    yield ('Petersen',5,make_graph(v,lambda i,j:(i<5 and j<5 and (i-j)%5 in(1,4))
                    or (i>=5 and j>=5 and (i-j)%5 in(2,3))
                    or abs(i-j)==5))
    for q in (13,17):
        squares={i*i%q for i in range(1,q)}
        yield ('Paley',q,make_graph(list(range(q)),lambda i,j:(i-j)%q in squares))

cases=0
compared=0
for typ,param,M in families():
    dim=M.rows
    degs=[sum(M[i,j] for j in range(dim)) for i in range(dim)]
    assert len(set(degs))==1, (typ,param,'not regular')
    kk=degs[0]
    adj_count=[]; non_count=[]
    for i,j in combinations(range(dim),2):
        common=sum(M[i,z]*M[z,j] for z in range(dim))
        (adj_count if M[i,j] else non_count).append(common)
    assert adj_count and non_count
    assert len(set(adj_count))==1 and len(set(non_count))==1,(typ,param,'not SRG')
    ll=adj_count[0];mm=non_count[0]
    lap=kk*sp.eye(dim)-M
    adj_formula=sp.factor(adj.subs({k:kk,la:ll,mu:mm}))
    non_formula=sp.factor(non.subs({k:kk,la:ll,mu:mm}))
    for hh in map(sp.Rational,['1/10','1/4','1/2','3/4']):
        mat=sp.eye(dim); T=sp.eye(dim)
        for j in range(1,5):
            mat=mat*(-hh*lap)/j
            T+=mat
        assert all(sum(T[i,j] for j in range(dim))==1 for i in range(dim))
        for i,j in combinations(range(dim),2):
            f=(adj_formula if M[i,j] else non_formula).subs(h,hh)
            assert T[i,j]==f,(typ,param,i,j,hh,T[i,j],f)
            compared+=1
    cases+=1

print(f'VERIFY_OK: 5 symbolic RK4 algebra/positivity identities; universal cubic ratio certificate; '
      f'{cases} exact SRG examples and {compared} rational off-diagonal comparisons; '
      'triangular-family cubic and doubled-Euler boundary identities')
