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

The analytic proof identifies
\[
H_{k-1}(t)=E[D\mathbf 1_{\{D>t\}}]
=\sum_{j=1}^{k-1}(-1)^{j+1}\binom{k-1}{j}\frac{(jt+1)e^{-jt}}{j(j+1)}.
\]
With \(K=k(n-1)\), \(c_U=1/(nK)\), \(c_B=1/[n(K+1)]\), and \(E[A]=(1+H_{k-1}(t))/n\), the risk difference simplifies to
\[
\frac{1-2KH_{k-1}(t)}{n^2K(K+1)}.
\]

The standalone `verify.py` checks \(H_{k-1}\) against direct two-dimensional quadrature, compares the simplified and unsimplified risk differences, and solves the threshold equation by bisection.

Expected terminal line:
`VERIFY_OK k3n3=4.111450606420 k3n5=4.961181135319 k3n10=5.923005815333 k3n15=6.436753036096`.

Finite computations are reproducibility checks only.
