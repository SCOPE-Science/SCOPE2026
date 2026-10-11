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

# Verification of the Airy-edge asymptotic

The attached `VERIFY.py` is executable with `python3 VERIFY.py` using only the Python standard library. Successful execution prints `GEOMETRIC_FOUR_PERIODIC_AIRY_EDGE_EXACT_IDENTITIES_OK`.

It verifies the following **exact rational** identities at several rational periodic profiles and damping parameters, including the undamped boundary and nontrivial modulated cases: \(2Lm_n=c_{n-1}+c_n\); the Bloch eigenvector equation; \(2/(S\bar m)=2st/[L(s+t)D]\); the entire finite-support ground-state form, including its endpoint term; and equality for inverse-conductance cell interpolation. In particular, the program checks \(\alpha=1/2\) for \(s=t=1\) and \(\alpha=8/21\) for \(s=5/2,t=1\).

The claimed limit concerns infinite-dimensional compact operators and all positive real \(s,t\). Its proof relies on analytical rescaling, tightness, weak lower semicontinuity, matching cellwise recovery, and the ordinary half-line Airy eigenvalue. The finite exact checks do **not** certify those infinite steps; they only guard their algebraic premises and normalizations. The preprint family and mathematical comparisons are cited in `RESULT.md`. The source's open finite-parameter polynomial-root questions remain outside this theorem.

Same-model review: passed. Independent audit: not yet performed.
