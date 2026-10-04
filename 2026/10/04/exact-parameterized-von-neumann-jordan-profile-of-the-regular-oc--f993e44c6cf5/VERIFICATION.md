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

The theorem was checked from the explicit regular-octagon model using exact arithmetic in \(\mathbb Q(\sqrt2)\). The bundled `verify.py` checks all five vertex separations, the support-facet changes needed for the \(k=2\) and \(k=3\) cases, the exact factor identities controlling the upper envelope, the strict ordering of the relevant breakpoints, continuity at \(m_*=(4-\sqrt2)/7\), and the endpoint value \(4-2\sqrt2\). It prints `VERIFY_OK` on success.

The proof, rather than the execution log, establishes the universal quantifier in \(\lambda\). The checker certifies the algebraic reductions used by that proof. No finite sampling is used as evidence for the continuum statement.

The literature checks establish that the defining source gives only general bounds for this invariant and that the closest exact regular-octagon paper computes a different two-parameter functional. They do not amount to a proof that no equivalent result exists anywhere; that residual bibliographic risk is stated in the review.
