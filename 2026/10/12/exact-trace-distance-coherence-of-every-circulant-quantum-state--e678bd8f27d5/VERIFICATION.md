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

The claim is verified analytically.

For an arbitrary incoherent density matrix \(\delta\), the exact cyclic average is
\[
\frac1d\sum_{m=0}^{d-1}S^m\delta S^{-m}=\frac{I_d}{d}.
\]
For a circulant state \(\rho_p\), every conjugate \(S^m\rho_pS^{-m}\) equals \(\rho_p\). Convexity and unitary invariance of the trace norm therefore give
\[
\left\|\rho_p-\frac{I_d}{d}\right\|_1\le\|\rho_p-\delta\|_1
\]
for every feasible \(\delta\). This is a global optimization argument, including boundary points of the incoherent simplex.

Unitary Fourier diagonalization gives the eigenvalues \(p_k-1/d\) of \(\rho_p-I_d/d\), hence
\[
\left\|\rho_p-\frac{I_d}{d}\right\|_1
=
\sum_{k=0}^{d-1}\left|p_k-\frac1d\right|.
\]

For the qutrit corollary the Fourier eigenvalue deviations are
\[
2r\cos\!\left(\theta+\frac{2\pi k}{3}\right),\qquad k=0,1,2.
\]
Their sum is zero, so their absolute-value sum is twice their largest absolute value, yielding the displayed formula.

No finite computation is needed for the proof. The result does not establish uniqueness of the closest incoherent state, strong monotonicity, or a formula outside the circulant family.
