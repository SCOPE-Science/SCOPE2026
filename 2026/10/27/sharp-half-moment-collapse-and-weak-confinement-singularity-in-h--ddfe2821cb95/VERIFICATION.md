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

# Reproduction notes
Run `python verify.py` in the directory containing this file (NumPy and SciPy required). It discretizes the killed OU resolvent on \([-12,1]\) with a uniform step, checks the discounted Dynkin identity, and integrates the return OU first-exit means to compare \(\sqrt\kappa\,\mathbb E T_{r,\kappa}\) against its predicted limit. It also checks positivity and finiteness of the one-cycle success probability.

The left truncation and mesh size incur finite numerical error; the driver checks several strictly positive search stiffnesses and finite \(\kappa\), not the infinite-time tail. The proof of the infinite-time asymptotic uses Laplace-transform expansion and a monotone Tauberian theorem, and the small-stiffness asymptotic uses dominated convergence. No independent audit was performed.
