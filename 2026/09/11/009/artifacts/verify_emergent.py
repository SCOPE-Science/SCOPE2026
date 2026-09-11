"""Consolidated verification for emergent sign-reversal lemma (lane-691).
Checks, with the FALLBACK'S OWN amplitude a^2=c_cap*lam^{-2/3}r^{4/3} and c1=1e-2:
 (a) transport-source constant S>0; (b) floor-dominance exponent (1-4al)/3<0 on window;
 (c) ratio upper-bound exponent -(1+2al)/3<0 vs claimed lower-bound exponent (4al-3)/3>0;
 (d) ALL-pairs violation of the claimed inequality (58 pairs, dyadic lam=2^12..2^24)."""
import numpy as np
N=801; L=6.0
x=np.linspace(-L,L,N); dx=x[1]-x[0]
S1,S2=np.meshgrid(x,x,indexing='ij')
P=np.exp(-(S1**2+S2**2)); C2=np.sqrt(np.sum(P**2)*dx**2)
Psi=P/C2; D1=np.sum(np.abs(np.gradient(Psi,dx,axis=0)))*dx**2
S=(2/np.pi)*D1
c1=1e-2; C_osc=2.0; c_cap=1.0
print(f"S={S:.6f} (>0: {S>0})")
ok=True
for al in (0.751,0.8,0.9,1.0):
    ef=(1-4*al)/3; er=-(1+2*al)/3; ec=(4*al-3)/3
    print(f"al={al}: floor-dom exp={ef:.4f}<0:{ef<0} ratio exp={er:.4f}<0:{er<0} claimed exp={ec:.4f}>0:{ec>0}")
    ok &= (ef<0 and er<0 and ec>0)
fails=total=0; worst=1e99
for al in (0.751,0.8,0.9,1.0):
    for k in range(12,25):
        lam=2.0**k; r=lam**(-al); a2=c_cap*lam**(-2/3)*r**(4/3); a=np.sqrt(a2)
        ratio=(a*lam**(-1)*S)/(C_osc*a2+lam**(-1)); bound=c1*lam**((4*al-3)/3)
        total+=1; q=ratio/bound; worst=min(worst,q)
        if ratio<bound: fails+=1
print(f"violation: {fails}/{total} pairs; worst ratio/bound={worst:.2e}")
print("VERIFY_OK" if (ok and fails==total) else "VERIFY_FAIL")
