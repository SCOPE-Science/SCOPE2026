"""Exact arithmetic checks of an RK4 positivity theorem for biregular bipartite graphs.

Requires sympy >= 1.12; no network access. Run: python verify.py
"""
import itertools
from sympy import Matrix, Rational, symbols, expand, factor, simplify

x,y,h=symbols('a b h', positive=True)
S=x+y
c1=1-S*h/2+(x*x+x*y+y*y)*h*h/6-(x**3+x*x*y+x*y*y+y**3)*h**3/24
c3=h**3*(1-S*h/2)/6
c2left=h*h/2-h**3*(2*x+y)/6+h**4*(3*x*x+2*x*y+y*y)/24
c2right=c2left.xreplace({x:y,y:x})

# Independently multiply generic 2x2 block algebra, representing B and B^T
# by a freely noncommuting alternating-walk algebra of length up to four.
# The formulas above can be reproduced by the exact block matrix for 4+5 vertices.
def bipartite_matrix(left, right, edges):
    B=Matrix([[int((i,j) in edges) for j in range(right)] for i in range(left)])
    A=Matrix.zeros(left+right)
    for i,j in edges:
        A[i,left+j]=A[left+j,i]=1
    deg=[len([1 for j in range(right) if (i,j) in edges]) for i in range(left)] + [len([1 for i in range(left) if (i,j) in edges]) for j in range(right)]
    if min(deg)<=0: raise ValueError('isolated vertex')
    L=Matrix.diag(*deg)-A
    return B,A,L,deg

def make_cycle(n):
    assert n>=2
    return n,n,{(i,i) for i in range(n)}|{(i,(i+1)%n) for i in range(n)}

def make_crown(n):
    assert n>=3
    return n,n,{(i,j) for i in range(n) for j in range(n) if i!=j}

def make_complete(p,q):
    return p,q,{(i,j) for i in range(p) for j in range(q)}

def make_incidence(n,k):
    subsets=list(itertools.combinations(range(n),k))
    return len(subsets),n,{(i,j) for i,sub in enumerate(subsets) for j in sub}

def make_circulant(n,shifts):
    return n,n,{(i,(i+s)%n) for i in range(n) for s in shifts}

def rk4(L,t):
    N=L.rows
    I=Matrix.eye(N)
    M=-t*L
    return I+M+M**2/2+M**3/6+M**4/24

cases=[]
for n in range(3,10): cases.append((f'cycle-{2*n}',make_cycle(n)))
for n in range(3,10): cases.append((f'crown-{n}',make_crown(n)))
for n in range(3,10): cases.append((f'complete-{n}-4',make_complete(n,4)))
for n in range(4,7):
  for k in (2,3):
    if k<n: cases.append((f'incidence-{n}-{k}',make_incidence(n,k)))
for n in range(5,9):
  for ss in [(0,1,2),(0,1,3)]: cases.append((f'circulant-{n}-{ss}',make_circulant(n,ss)))

count=0; tested=0; witnesscount=0; complete_brackets=0
for label,(p,q,edges) in cases:
    B,A,L,degs=bipartite_matrix(p,q,edges)
    if len(set(degs[:p]))>1 or len(set(degs[p:]))>1: raise AssertionError(label)
    a,b=degs[0],degs[-1]; full=len(edges)==p*q
    if not full and (a+b)>12: continue
    t=Rational(2,a+b)
    X3=B*B.T*B
    for test in [Rational(1,2)*t,t,Rational(101,100)*t]:
        T=rk4(L,test)
        U=c1.subs({x:a,y:b,h:test})*test
        V=c3.subs({x:a,y:b,h:test})
        C=c2left.subs({x:a,y:b,h:test})
        D=c2right.subs({x:a,y:b,h:test})
        LL=(B*B.T)
        RR=B.T*B
        for i in range(p):
          for j in range(q):
            assert T[i,p+j] == U*B[i,j] + V*X3[i,j],(label,i,j,test)
            count+=1
        for i in range(p):
          for j in range(p):
            if i!=j:
              assert T[i,j] == C*LL[i,j] + test**4/24*(LL*LL)[i,j],(label,i,j,test)
              count+=1
        for i in range(q):
          for j in range(q):
            if i!=j:
              assert T[p+i,p+j] == D*RR[i,j] + test**4/24*(RR*RR)[i,j],(label,i,j,test)
              count+=1
        if test<=t:
            assert all(T[i,j]>=0 for i in range(p+q) for j in range(p+q)),label
        if not full and test>t:
            assert any(T[i,j]<0 for i in range(p) for j in range(p,p+q)),label
            assert all(T[i,j]>=0 for i in range(p) for j in range(p) if i!=j)
            witnesscount +=1
    # For a complete bipartite network, the positive interval exceeds
    # 2/(a+b): rational bracket 11/4 < rho < 14/5 for the RK4 radius.
    if full:
        Tinside=rk4(L,Rational(11,4)/(a+b))
        Toutside=rk4(L,Rational(14,5)/(a+b))
        assert all(Tinside[i,j]>=0 for i in range(p+q) for j in range(p+q)),label
        assert all(Toutside[i,p+j]<0 for i in range(p) for j in range(q)),label
        complete_brackets+=1
    # Exactly reproduce the top-Laplacian eigenmode using only degrees.
    v=Matrix([a]*p+[-b]*q)
    assert L*v == (a+b)*v,label
    tested+=1

# Exact symbolic certificates for the proof inequalities, including no
# assumption that a or b is an integer in their sign arguments.
assert simplify(c2left/h**2*24 - ((3*x*x+2*x*y+y*y)*h*h-4*(2*x+y)*h+12))==0
assert expand(3*(2*x+y)**2-9*(3*x*x+2*x*y+y*y)) == -15*x*x-6*x*y-6*y*y
z=symbols('z', nonnegative=True)
s= symbols('s', positive=True)
Cnorm=1-z+Rational(2,3)*(1-s)*z*z-Rational(1,3)*(1-2*s)*z**3
assert simplify(Cnorm -(1-z+z*z/3) - z*z*(1-z)*(1-2*s)/3) == 0
# x=degree fraction in (0,1) => s=x(1-x) in (0,1/4];
# hence c1/h >= 1-z+z^2/3>0 for 0<=z<=1.
w=symbols('w', real=True)
positive_diag= (w*w-2*w+2)**2+4*((w-2)**2+1)
assert expand(positive_diag-(w**4-4*w**3+12*w*w-24*w+24))==0
assert (24-12*Rational(11,4)+4*Rational(11,4)**2-Rational(11,4)**3)>0
assert (24-12*Rational(14,5)+4*Rational(14,5)**2-Rational(14,5)**3)<0
print('VERIFY_OK',tested,'biregular cases;',count,'exact rational offdiagonal checks;',witnesscount,'strict distance-three failures;',complete_brackets,'complete-graph spectral-bracket tests; symbolic positivity certificates')
