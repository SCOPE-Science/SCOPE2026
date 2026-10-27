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
# Reproducible mathematical checks

Execute `python3 verify.py` with the Python standard library. The verifier constructs the partial-bijection generator on two disjoint sets and builds its closure under the generator and inverse using breadth-first enumeration. For every enumerated element, it substitutes that element into a recorded word for each monoid element, forming the entire candidate endomorphism image.

For all \(n\in\{2,3,4,5,6\}\) and \(k\in\{1,2,3,4,6\}\), it checks the monoid size, the full endomorphism image-size histogram, the number of idempotent endomorphisms and the number of automorphisms. For \(n\le4\), every candidate endomorphism is also verified by all ordered multiplication pairs, without relying on the abstract presentation for that finite check. The terminal success line is `VERIFY_OK 25 exact configurations`.

The executable verifies finite instances only. The proof of all dimensions rests on the presentation, the interval/rotation normal forms, the longest-link characterization and the criterion for a substitution endomorphism to be idempotent. In particular, no finite enumeration certifies that all larger instances obey the formulas.
