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

The complete mathematical proof is in `RESULT.md`. Run `python3 verify.py` using Python 3.9 or newer. The script enumerates all ordered positive parallel-class size vectors of total size at most eleven, forms every base indicator, and checks the precise Minkowski reflection containment with `fractions.Fraction`. Expected output includes 2036 checked profiles and 77808 transformed vertices.

A separate independent numerical linear program, based on all matroid rank inequalities, agreed in 247 profiles through total size eight. This comparison was executed during development; no external solver is needed to replay the included exact-rational verifier. Numerical or finite exact checks do not prove the infinite-family theorem; the complete proof derives the center conditions and feasible interval system for all positive class sizes.
