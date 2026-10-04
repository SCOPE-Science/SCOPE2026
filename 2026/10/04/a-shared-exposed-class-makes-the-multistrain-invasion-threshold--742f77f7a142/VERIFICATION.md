---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The source equations were checked at the disease-free equilibrium, where \(N^0=S^0+D^0\). The critical distinction is that only the incidence term entering \(E\) creates newly infected people; the terms moving \(E\) into \(I_j\) or \(C\) are transfers among infected states.

With \(a_E=\mu+\phi\), \(a_j=\mu+\mu_j+\gamma_j\), and \(b=\mu+\delta_1+\gamma\), direct inversion of the lower-triangular transfer matrix gives
\[
\mathcal R_*=
\frac{\beta}{a_E}
\left(
\alpha\sum_{j=1}^n\frac{\varphi_j}{a_j}
+\frac{(1-\alpha)\phi}{b}
\right).
\]
The real infected characteristic equation satisfies \(g'(z)>0\) on the domain containing the spectral bound and \(g(0)=a_E(1-\mathcal R_*)\), so its sign at zero gives the local threshold.

`verify.py` checks the exact witness
\[
n=2,\quad \alpha=1/2,\quad \mu=1,\quad
\varphi_1=\varphi_2=1,\quad
\mu_j=\gamma_j=1,\quad
\delta_1=\gamma=1,\quad \beta=5.
\]
It confirms
\[
A=5/9,\qquad B_1=B_2=5/18,\qquad
\mathcal R_*=10/9,
\]
while \(\mathcal R_{\mathrm{print}}^2=5/6<1\), and checks the nontrivial characteristic factor \((z+3)^2-10\), which yields the positive eigenvalue \(-3+\sqrt{10}\).

A successful replay prints `VERIFY_OK`. The script is a finite exact check of the witness only; the general formula is established by the symbolic matrix argument, not by enumeration or numerical evidence.
