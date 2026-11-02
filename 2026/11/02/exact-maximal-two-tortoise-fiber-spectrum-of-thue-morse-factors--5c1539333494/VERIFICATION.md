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

# Reproducibility and boundaries

Run `python3 verify.py` with standard Python 3; no external dependency. The recorded run terminates with `VERIFY_OK`. The script enumerates all length-\(n\) Thue–Morse factors for \(1\le n\le10\) using four iterated two-letter substitution blocks, then compares their exact image-fiber maxima. It cross-checks factor sets against a separate length-16384 fixed-point prefix construction, verifies that each length-ten factor contains at least four ones, and verifies the formula for all length-ten sources. Further exploratory length checks support, but do not prove, the infinite statement.

The mathematical proof of the infinite upper bound is the third-one fiber-injection lemma in RESULT.md. The matching lower bound depends on Campbell–Rampersad, arXiv:2604.25811v2, Theorem 6. This is a self-review only; no independent audit, external certificate or priority guarantee is claimed.
