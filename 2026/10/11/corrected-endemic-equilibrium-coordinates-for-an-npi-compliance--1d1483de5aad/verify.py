import sympy as sp
pi,rho,lam,theta,mu,eps=sp.symbols('pi rho lam theta mu eps', positive=True)
sn,sy,E,In,Iy,J,R=sp.symbols('sn sy E In Iy J R')
sig_n,sig_y,eta,gam_n,tau_n,del_n,gam_y,tau_y,del_y,tau_J,del_J=sp.symbols('sig_n sig_y eta gam_n tau_n del_n gam_y tau_y del_y tau_J del_J', positive=True)
A1=sig_n+sig_y+mu
A2=eta+gam_n+tau_n+del_n+mu
A3=gam_y+tau_y+del_y+mu
A4=tau_J+del_J+mu

# Printed first endemic coordinate in Eq. (7)
sn_print=(1-rho)*pi/(lam+mu)
res_print=sp.factor((1-rho)*pi-(lam+theta+mu)*sn_print)
expected=-((1-rho)*pi*theta)/(lam+mu)
assert sp.simplify(res_print-expected)==0

# Corrected equilibrium coordinates conditional on a positive force of infection lam.
sn_c=(1-rho)*pi/(lam+theta+mu)
sy_c=pi*(rho*lam+theta+rho*mu)/((eps*lam+mu)*(lam+theta+mu))
E_c=lam*pi*(eps*lam+eps*theta+mu*(1-rho+eps*rho))/(A1*(lam+theta+mu)*(eps*lam+mu))
In_c=sig_n*E_c/A2
Iy_c=(sig_y*E_c+eta*In_c)/A3
J_c=(gam_n*In_c+gam_y*Iy_c)/A4
R_c=(tau_n*In_c+tau_y*Iy_c+tau_J*J_c)/mu

F1=(1-rho)*pi-lam*sn_c-(theta+mu)*sn_c
F2=rho*pi+theta*sn_c-eps*lam*sy_c-mu*sy_c
F3=lam*(sn_c+eps*sy_c)-A1*E_c
F4=sig_n*E_c-A2*In_c
F5=sig_y*E_c+eta*In_c-A3*Iy_c
F6=gam_n*In_c+gam_y*Iy_c-A4*J_c
F7=tau_n*In_c+tau_y*Iy_c+tau_J*J_c-mu*R_c
for k,F in enumerate([F1,F2,F3,F4,F5,F6,F7],1):
    assert sp.simplify(F)==0, (k, sp.factor(F))

print('VERIFY_OK')
print('printed_Sn_residual =', res_print)
print('corrected_coordinate_residuals = 0,0,0,0,0,0,0')
print('force_consistency = must still impose lam = beta*(In+alpha*Iy)/N')
