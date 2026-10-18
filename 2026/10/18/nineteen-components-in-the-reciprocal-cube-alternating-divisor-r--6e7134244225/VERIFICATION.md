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

Run `python3 verify.py` with Python 3 and the standard library. Expected initial output: `VERIFY_OK`, followed by strict rational enclosures, `distinct_finite_local_products 135`, `components 19`, and an exact 19-row endpoint table. The checker uses `fractions.Fraction`, not floating-point decisions. It explicitly checks finite prime-tail inequalities, a uniform rational bound underlying Nagura's prime-gap application, exponent replacement inequalities, and each overlap/gap using opposing rigorous bounds on the reciprocal-zeta tail. Scientific limits: Nagura's theorem and the elementary subsum-interval lemma are external analytic inputs explained in `RESULT.md`. The reported execution was performed on the supplied checker; the finite calculation alone is not an infinite proof.
