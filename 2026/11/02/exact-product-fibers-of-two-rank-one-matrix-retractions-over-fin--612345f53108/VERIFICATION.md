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
Run `python verify.py` using Python 3 standard library. The script independently generates every rank-one idempotent \(E=u\phi\) using a normalized projective image vector and all normalized covectors, computes every ordered product, accumulates a dictionary keyed by exact matrix bytes/entries, and compares each full fiber with the stated formula. It generates all possible rank-one matrices separately and checks that all such targets occur. Tested fields are \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\) and \(\mathbb F_5\), at the eight parameter pairs listed in RESULT.md. All checks printed `VERIFY_OK`, ending with `ALL_VERIFY_OK`.

The checker contains an explicit multiplication reduction modulo \(X^2+X+1\) for \(\mathbb F_4\). No third-party package is needed. Enumeration is exhaustive only for the eight listed instances. Arbitrary field orders and dimensions are covered by the proof, not the finite experiments. No independent audit has been performed.
