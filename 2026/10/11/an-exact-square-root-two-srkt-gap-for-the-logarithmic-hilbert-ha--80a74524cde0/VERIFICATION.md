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

# Verification record
The Hilbert-matrix Schur estimate is proved by a strictly convex midpoint quadrature argument with the exact beta integral. The matching lower bound is a positive Rayleigh quotient whose double integral has a convolution kernel with total mass \(\pi\). Thus the infinite operator norm is \(\pi\).

The exact Garsia variance follows from the disk automorphism coefficient expansion, Parseval, and angular monotonicity of the dilogarithm. Equality at positive real radii tends to the limiting variance \(\pi^2/2\), and the global inequality is pointwise at every complex point. The precise Bonsall identity converts the variance into kernel-testing norm.

Reproduce additional finite checks with `python3 check_hilbert_garsia.py`. The code tests 5 disk points, a real-ray identity, and 3 finite Rayleigh ratios. These are finite consistency checks, not substitutes for the infinite Hilbert or Garsia proofs. No independent audit was performed.
