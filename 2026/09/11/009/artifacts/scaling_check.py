import numpy as np

# Explicit 2D-concentrated Mikado-like tube along e3, cross-section profile psi
# psi(s) = exp(-|s|^2) normalized in L^2; W = r^{-1} psi(x_perp / r) e3, periodized (single tube per T^3 cell, r<<1)
# L^p norm over T^3: ||W||_p^p = r^{-p} * r^2 * ||psi||_p^p = r^{2-p} ||psi||_p^p
# so ||W||_p = r^{2/p - 1} C_p.
# Gradient: transverse grad ~ r^{-1}; axial fast oscillation at lambda (phase along tube) multiplies by e^{i lambda x3}?
# Consider W_{lam,r} = r^{-1} psi(x_perp/r) e^{i lam x3} e3 (complexified for scaling; L^p unaffected).
# Then (v0 . grad)W with v0=(sin x3,0,0): v0·∇W = sin x3 * d1 W ~ sin x3 r^{-2} (d1 psi)(./r) e^{ilam x3}.
# L^1 norm: ||(v0·∇)W||_1 = <|sin x3|> * r^{-2} * r^2 ||d1 psi||_1 = c_shear * ||d1psi||_1 = O(1) const in (lam,r)!
# R_trans = R[(v0·∇)w], w = a W: model ||R_trans||_1 ~ lam^{-1} * a * C_trans (gain lam^{-1} from inverse div at freq lam).
# Oscillation: div(W⊗W)= div(|W|^2 e3⊗e3) = d3(|W|^2) = i lam |W|^2 (fast axial). For exact steady Mikado (no axial oscillation) this is 0.
# With axial oscillation e^{ilam x3}, W⊗W oscillates at 2lam; R_osc = R[div(a^2 (W⊗W - avg))].
#   ||div(W⊗W)||_1 ~ lam ||W||_2^2 = lam*1 = lam. Gain lam^{-1} => ||R_osc||_1 ~ a^2 * C_osc = O(a^2) const.
# Ratio at fixed a: R_trans/R_osc ~ (a lam^{-1})/(a^2) = 1/(a lam) DECAYING. With cap-saturating a, 1/a ~ B ~ lam^{(1+al)/3} => ratio ~ lam^{(1+al)/3 - 1} = lam^{(al-2)/3} DECAYING on window (al<=1 => exponent<0).
# This direct axial-oscillation model REFUTES growth. Log it.
# Alternative: no axial oscillation (pure shear-transverse Mikado): div(W⊗W)=0 exactly => R_osc=0 (a const) => denom floor lam^{-1}.
#   ratio = ||R_trans||/lam^{-1} = lam * a lam^{-1} C = a C const; with cap a ~ lam^{-(1+al)/3}?? DECAYS.
#   Hmm with transverse-derivative-dominated transport: ||(v·∇)W||_1 = O(1) as above, gain r (freq r^{-1}) => ||R_trans|| ~ a r; ratio vs floor lam^{-1}: lam a r = a lam^{1-al}; cap => lam^{1-al-(1+al)/3} = lam^{(2-4al)/3}, decaying for al>1/2.
# So naive models all DECAY. The claimed GROWTH lam^{(4al-3)/3} requires different mechanism (temporal corrector mu, or Nash, or Besov-costly amplitude shaping).
# Let's numerically verify the O(1) transport-source scaling by quadrature on one cell.

def psi(s1,s2): return np.exp(-(s1**2+s2**2))
# normalization constants via quadrature on R^2
N=801
L=6.0
x=np.linspace(-L,L,N); dx=x[1]-x[0]
S1,S2=np.meshgrid(x,x,indexing='ij')
P=psi(S1,S2)
C2=np.sqrt(np.sum(P**2)*dx**2)  # ||psi||_2
print("||psi||_2 =",C2)
# normalized psi2 = psi/C2 => W L^2 =1
Psi=P/C2
C1=np.sum(np.abs(Psi))*dx**2  # ||psi_n||_1
C3=(np.sum(np.abs(Psi)**3)*dx**2)**(1/3)
dPsi=np.gradient(Psi,dx,axis=0)  # d1 psi_n
D1=np.sum(np.abs(dPsi))*dx**2
print(f"C1={C1:.6f} C3={C3:.6f} D1={D1:.6f}")
# Transport source L^1 prefactor: <|sin|> over x3 in [0,2pi] = 2/pi
c_shear=2/np.pi
# ||(v0·∇)W||_1 = c_shear * D1 * r^{-2} * r^2 = c_shear*D1 (independent of r) -- verify scaling across r
for al in [0.76, 0.9, 1.0]:
    for k in [12,16,20]:
        lam=2.0**k; r=lam**(-al)
        src=c_shear*D1  # analytic
        W3=r**(2/3-1)*C3
        Besov_proxy=(lam**(1/3))*W3  # lam^{1/3}||W||_3
        a_cap=1.0/Besov_proxy  # M=1
        Rtrans_model=a_cap*(1.0/lam)*src  # gain lam^{-1}
        Rosc_model=a_cap**2*1.0  # O(a^2) const (axial-osc model, C_osc=1)
        ratio=Rtrans_model/(Rosc_model+1.0/lam)
        e_claim=(4*al-3)/3
        print(f"al={al} k={k} lam=2^{k} r={r:.2e} B={Besov_proxy:.2e} a_cap={a_cap:.2e} Rtr={Rtrans_model:.2e} Ros={Rosc_model:.2e} ratio={ratio:.2e} lam^e={lam**e_claim:.2e}")
