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

# Verification and limits
The proof in `RESULT.md` verifies surjectivity and inverse-fiber cardinalities pointwise, determines fixed points without omissions, proves both necessity and sufficiency of the polynomial invariant for unrestricted topological conjugacy, and computes all period sums symbolically. The natural extension equivalence follows from a continuous explicit recovery of each bilateral source coordinate as coordinate zero along its corresponding inverse-limit orbit; both entropy inequalities follow from factor maps.

Standalone command: `python CHECKS.py`. Observed output: `CHECKS_PASS 5316 surjective maps; N=1..6; periodic n=1..3 for N<=4; weighted r=0..2`. This checks finite instances only. The infinite assertions depend on the elementary analytic and combinatorial arguments, not the checker. The classification does not cover higher-block, constrained or sofic zip shifts, and priority remains subject to independent review.
