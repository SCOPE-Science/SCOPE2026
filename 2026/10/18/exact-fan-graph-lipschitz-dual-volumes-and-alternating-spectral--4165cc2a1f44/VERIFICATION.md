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

Run `python3 verify.py` with Python 3 and its standard library. Exact polynomial integration on \([0,1]\) constructs the fan-volume sequence through dimension 16. A separate count of integer lattice points in dilated fan polytopes obtains the leading Ehrhart coefficients, compared at exact rational precision through dimension 12. The computation also checks the strict alternating-ratio inequalities for 14 indexes and numerical spectral sums for 10 dimensions.

The graph-edge inequalities have a rooted, totally unimodular difference-constraint matrix, so Ehrhart's leading coefficient is exactly the anchored volume. This integrality is independently justified by the spanning-tree argument in RESULT.md. The trigonometric generating function, infinite cotangent sum and uniform alternating signs are proved symbolically in RESULT.md; sample calculations alone do not imply them.

Scientific limits: no independent scientific audit has been completed, the numerical series comparison uses finitely many terms, and the spectral remainder estimate is a mathematical proof step rather than a finite numerical certificate.
