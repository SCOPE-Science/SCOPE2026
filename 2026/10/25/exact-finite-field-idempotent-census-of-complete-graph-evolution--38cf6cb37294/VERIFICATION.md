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

The proof is self-contained in `RESULT.md` and rests on the exact common-quadratic reduction, exhaustive two-value parametrisation, odd-characteristic discriminant counting including coincident-root adjustment, singular-matrix linear reduction, and characteristic-two absolute-trace argument. `verify.py` recomputes the original multiplication law over explicit finite fields rather than relying on the classification to enumerate idempotents.

Run `python3 verify.py` from this directory. The observed result was `VERIFY_OK cases= 18`, including the following checks: \((n,q)=(4,2),(4,4),(4,8)\) give \(8,16,8\), and \((3,3),(3,9)\) give \(2,8\). Other checks cover the singular odd-characteristic branch and the exceptional coincident-root branch.

The program is finite exhaustive evidence only at the specified small cases; the proof, not the experiments, establishes the theorem for all dimensions and finite fields. Algebra-isomorphism classification, other graphs and random-walk normalisations are not considered. Independent audit has not been performed.
