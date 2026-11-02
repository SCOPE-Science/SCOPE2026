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

The embedded `materializer_distributivity_verify.py` uses only Python standard-library facilities. Running `python3 materializer_distributivity_verify.py` enumerates the distinct naturally labeled finite posets whose underlying labels form a linear extension. Every isomorphism class of finite posets has such a labeling, so the enumeration covers every poset structure through the tested orders.

For each antecedent downset it computes the minimal external-support family, tests the equivalent pairwise union condition, and checks that these agree. For every poset of orders 1–5, it also computes the materializer directly from the Heyting implication formula, reconstructs all intrinsic joins as intersections of common upper bounds, and tests distributivity over every ordered triple. For order six, only the two equivalent structural criteria are compared, not all distributivity triples.

Expected successful output concludes with `ALL_MATERIALIZER_DISTRIBUTIVITY_CHECKS_PASS posets=5231 antecedents=101658`. The script additionally confirms the explicit smallest four-point non-distributive poset witness. These finite tests are supplementary; the proof of the all-size theorem is in `RESULT.md`.

The scientific status is self-reviewed only. No independent audit has been performed.
