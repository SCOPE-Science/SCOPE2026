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

# Reproducibility and scope

Execute `python3 checker.py` using Python 3 standard library. It independently compares the complex Zak formula with the positive real-algebraic expression, verifies positive-residue lower bounds by sampling, checks attained endpoint values, tests reciprocity and the scale-invariant optimum, and compares an explicit cosecant identity to truncated conditional Fourier sums. The checker prints `PASS 14508 supplementary checks; finite checks do not prove the theorem` on success.

The exact claims are proved in `RESULT.md`, through the critical Zak multiplier, a derivative-sign lemma, endpoint optimization and an analytic energy calculation. The numerical script is a finite sanity check, not an infinite-dimensional certification. Independent audit has not been performed.
