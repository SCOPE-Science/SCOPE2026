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

# Reproducibility

Run `python verify.py` in this package. It uses only Python's standard library. The checker returned `PASS 9499 exact and numerical tests` in a reproducibility run against this file's contents. Exact rational assertions verify selected affine moment fixed-point identities and sample losses; numerical assertions check the full optimizer root equation, KKT marginal equality, feasibility, strictly better performance than sampled competing feasible allocations, limiting asymptotics, and a concrete heterogeneous-noise example. The proof of the theorem is the analytic argument in `RESULT.md`, not the finite suite. In particular, finite sampling of other probability vectors cannot certify global optimality, and finite asymptotic probes cannot certify limits. No independent audit has been performed.
