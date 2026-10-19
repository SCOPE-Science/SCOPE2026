"""Symbolic Lyapunov certificate for a two-wall monitored coined walk.
Run: python check_kernel.py   Requires SymPy >= 1.10.
"""
import sympy as S
N,x,k,u=S.symbols('N x k u', real=True)
T=u**2
# Coin numerator M.  K = shifted M / sqrt(1+u^2).
M=[[S.Integer(1),u],[u,S.Integer(-1)]]
v=[-1,1]

def entry(X,Y,i,j,order,phase):
    """Return Q_{X,i;Y,j}; order = sign(Y-X), phase=(-1)^((Y-X)/2)."""
    if order<0:
        return entry(Y,X,j,i,1,phase)
    if order==0:
        if i==j==0: return N+X+T*(N*(N-1)-X*(X+1))
        if i==j==1: return N-X+T*(N*(N-1)-X*(X-1))
        return 2*X*u
    if i==j==0: return phase*T*(N+X)*(N-Y-1)
    if i==j==1: return phase*T*(N+X-1)*(N-Y)
    if i==1 and j==0:return phase*(X+Y)*u
    return S.Integer(0)

def symbolic_case(gap):
    # gap 0,2 or 2k >=4, use x'=x +/- 1; y'=x+gap +/- 1
    Y=x+gap
    for i in range(2):
      for j in range(2):
       if gap==0:phase0=1; order0=0
       elif gap==2:phase0=-1; order0=1
       else:phase0=S.Symbol('eps');order0=1
       result=(1+T)*entry(x,Y,i,j,order0,phase0)
       for a in range(2):
        for b in range(2):
         diff=v[b]-v[a]
         if gap==0:
          ord2=(diff>0)-(diff<0);ph2=(-1 if diff else 1)
         elif gap==2:
          delta=2+diff;ord2=(delta>0)-(delta<0);ph2=(-1 if delta==2 else 1)
          if delta==4:ph2=1
         else:
          ord2=1;ph2=phase0*(-1 if diff else 1)
         result-=M[a][i]*M[b][j]*entry(x+v[a],Y+v[b],a,b,ord2,ph2)
       result-=(1+T)*(1 if gap==0 and i==j else 0)
       ans=S.factor(result)
       if ans!=0:raise AssertionError((gap,i,j,ans))
    print('symbolic interior case', gap, 'PASS')
for gap in [0,2,2*k]:symbolic_case(gap)

# Complete finite-interval exact certificates, including both boundaries.
def finite(N0,u0):
    sites=list(range(-N0+1,N0));L=len(sites)
    q=S.zeros(2*L);D=S.zeros(2*L)
    n_,u_=N0,S.Rational(u0)
    for aa,X in enumerate(sites):
     for bb,Y in enumerate(sites):
      di=Y-X
      if di%2:continue
      if di<0:continue
      phase=(-1)**(di//2)
      for i in range(2):
       for j in range(2):
        val=entry(S.Integer(X),S.Integer(Y),i,j,0 if di==0 else 1,phase).subs({N:n_,u:u_})
        q[2*aa+i,2*bb+j]=val
        q[2*bb+j,2*aa+i]=val
     if aa>0:D[2*(aa-1),2*aa:2*aa+2]=S.Matrix([[1,u_]])
     if aa<L-1:D[2*(aa+1)+1,2*aa:2*aa+2]=S.Matrix([[u_,-1]])
    error=S.expand((1+u_**2)*q-D.T*q*D-(1+u_**2)*S.eye(2*L))
    assert error==S.zeros(2*L),(N0,u0,error)
    return 1
checks=0
for n in range(2,11):
 for p in [S.Rational(1,5),S.Rational(2,3),S.Rational(3,2)]:
  checks+=finite(n,p)
print('exact finite boundary certificates',checks,'PASS')
