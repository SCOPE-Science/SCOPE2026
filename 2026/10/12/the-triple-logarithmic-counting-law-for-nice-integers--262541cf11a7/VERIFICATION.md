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

The analytical proof is equations (1)–(7) in RESULT.md. The published nice-integer prime-factor criterion is taken from the cited primary research; second-moment concentration, elementary inclusion–exclusion, and Mertens' prime-product law are reconstructed there.

`nice_integers_verifier.py` runs with the Python 3 standard library. Its output (`nice_integers_verification_output.txt`) records independent prime-factorization checks through 2000, exact congruence-assignment decision by backtracking for 2 through 36, and exact counts through 2,000,000. No independent external review, proof certification, or formal verification has been conducted. Finite experiments alone do not establish the asymptotic.
