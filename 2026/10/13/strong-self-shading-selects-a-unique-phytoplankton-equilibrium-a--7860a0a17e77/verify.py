"""Numerical stress test of the strong self-shading equilibrium limit.
Uses scipy; checks the complete full stationary BVP against its unique scalar limit.
"""
import numpy as np
from scipy.integrate import solve_bvp
P={'d':1.0,'w':0.2,'dn':2.,'r':4.,'mu':0.8,'eta':0.4,'c':0.5,'gamma':1.,'N0':2.,'L0':8.,'h':1.,'l0':0.3,'alpha':1.5}
def light(x,H): return P['L0']*np.exp(-P['l0']*x-H)
def f(l):return l/(P['h']+l)
def g(N):return N/(P['gamma']+N)
x=np.linspace(0,1,600)
# limit u,u',H (scalar) at N=N0
def eq0(x,y):
 u,v,H=y; growth=P['r']*g(P['N0'])*f(light(x,H)); return np.vstack((v, P['w']/P['d']*v+(P['mu']-growth)*u/P['d'],u))
def bc0(a,b):return np.array([P['d']*a[1]-P['w']*a[0],P['d']*b[1]-P['w']*b[0],a[2]])
y0=np.vstack((3*np.ones_like(x),0.2*3*np.ones_like(x),3*x))
sol0=solve_bvp(eq0,bc0,x,y0,tol=1e-10,max_nodes=10000)
assert sol0.success,sol0.message
assert sol0.sol(x)[0].min()>0.05
u0=sol0.sol(x)[0]; U0=np.trapezoid(u0,x); light0=light(x,sol0.sol(x)[2]); uptake0=P['r']*g(P['N0'])*f(light0)*u0
# exact limiting nutrient deficit via nested numerical quadrature
from scipy.integrate import cumulative_trapezoid
J=cumulative_trapezoid(uptake0,x,initial=0.)
# n'(x)=-c/dn * J(x), n(L)= c/alpha *J(L)
nstar=(P['c']/P['alpha'])*J[-1]+(P['c']/P['dn'])*np.array([np.trapezoid(J[i:],x[i:]) for i in range(len(x))])
print('limiting total mass',U0,'nutrient limit surface depletion',nstar[0], 'bottom depletion',nstar[-1])
for kappa in [5,20,100,500,2000]:
 eps=1./kappa
 def eq(x,y):
  u,v,N,Z,H=y; p=P; growth=p['r']*g(N)*f(light(x,H));return np.vstack((v,p['w']/p['d']*v+(p['mu']+p['eta']*eps*u-growth)*u/p['d'],Z,p['c']*eps*growth*u/p['dn'],u))
 def bc(a,b):
  return np.array([P['d']*a[1]-P['w']*a[0],P['d']*b[1]-P['w']*b[0],a[3],P['dn']*b[3]-P['alpha']*(P['N0']-b[2]),a[4]])
 prev=sol0.sol(x); init=np.vstack((prev[0],prev[1],P['N0']-eps*nstar,-eps*P['c']/P['dn']*J,prev[2]))
 sol=solve_bvp(eq,bc,x,init,tol=5e-9,max_nodes=10000)
 assert sol.success,(kappa,sol.message)
 y=sol.sol(x);assert y[0].min()>0 and 0<y[2].min()<P['N0']
 photon=np.log(P['h']+P['L0'])-np.log(P['h']+light(np.array([1.]),np.array([y[4,-1]])))[0]
 uptake=np.trapezoid(f(light(x,y[4]))*y[0],x)
 rhs=P['l0']*np.trapezoid(f(light(x,y[4])),x)+uptake
 print("photon_err",abs(photon-rhs)); assert abs(photon-rhs)<4e-5
 nu=kappa*(P['N0']-y[2]);nerr=np.max(abs(nu-nstar));uerr=np.max(abs(y[0]-u0));
 print(f'kappa={kappa} mass rescaled={np.trapezoid(y[0],x):.9f} sup_uerr={uerr:.5g} sup_nerr={nerr:.5g}')
 assert uerr<max(0.5,25/kappa) and nerr<max(.5,25/kappa)
print('VERIFY_OK')
