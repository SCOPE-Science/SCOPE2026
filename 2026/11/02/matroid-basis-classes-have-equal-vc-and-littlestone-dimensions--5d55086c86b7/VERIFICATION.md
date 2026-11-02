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
# Verification of matroid basis learning dimensions

Run `python3 verify_matroid_bases.py` with Python 3 and the standard library. The checker enumerates all rank-uniform nonempty labeled basis families on ground sets up to five and filters exact basis-exchange axioms, then computes for each accepted matroid the VC dimension by all possible traces, the Littlestone dimension by recursive restriction of version spaces, primal/dual common-independence number, and minimum primal/dual rank cut. It checks equality of these four independently computed values. It additionally independently lists complete-graph spanning trees for three, four, and five vertices and checks their dimensions.

Expected decisive terminal line: `ALL_MATROID_BASE_LEARNING_CHECKS_PASS total_matroids=498`.

The all-size claims are proved in `RESULT.md` using elementary matroid extension, duality, a fully shattered tree path bound, and the classical Edmonds intersection theorem. These finite tests are safeguards against small counterexamples, not a replacement for that proof. They do not certify publication priority, independent review, online regret under adversarial labels, or complexity without an independence oracle.
