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

The proof uses exact polynomial identities, the fundamental theorem of algebra, and a zero-on-an-arc contradiction. No finite search is used to infer an infinite-support statement or to prove the all-degree equivalence.

Reproducible command: `python3 check.py` (standard library only). The checker verifies exact rational arithmetic for the ordinary-versus-strong three-atom separation, the zero of the tilted generating polynomial in the quadratic field with \(i\sqrt{15}\), and a Bernoulli-product illustration. Its checks do not replace the general symbolic proof.

Scientific boundary: only finitely supported integer-valued laws are classified. The independently supplied audit status above indicates that no independent validation has yet been performed.
