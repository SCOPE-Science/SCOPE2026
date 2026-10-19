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

# Verification notes

Run `python3 check_new.py` from the same directory as this document. The checker uses only the Python standard library. It enumerates all increasing-position embeddings of `0` repeated \(k\) times followed by `1` repeated \(k\) times in the alternating parent, independently generates every proposed canonical output, confirms injectivity and both exact binomial counts, and compares the resulting sets. It also tests an independently defined prefix-peak and ordering characterization for short residuals.

Expected output: `EXACT ENUMERATION, NORMAL FORM, SHAPE AND BINOMIAL CHECKS PASS; parameter pairs: 36`.

This tests \(1\le m\le11\) (all feasible \(k\), and separately rules out infeasible ones). It is not a proof of the infinitely many larger cases. The general proof is in `RESULT.md`; it does not depend on any computational theorem prover, external certificate, or heuristic assumption.
