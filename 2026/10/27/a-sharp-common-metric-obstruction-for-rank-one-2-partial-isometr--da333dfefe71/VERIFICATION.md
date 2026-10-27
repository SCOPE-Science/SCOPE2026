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

Run `python3 checker.py`. The script uses only Python's standard library and performs exact \(\mathbb Q(\sqrt7)\) matrix arithmetic on the two-dimensional witness, checking \(T\beta_2(T)=0\), the formula for \(S_T\), both generalized-inverse relations, the complementary idempotents, and their off-diagonal sign obstruction. It additionally samples fourteen values of \(x=\|T\|^2\) across the sharp threshold, including both degenerate endpoints, to check the constructed positive metric or the sign obstruction.

The proof in `RESULT.md` supplies the universal reduction \(x^2c^2=2x-1\), the common-metric criterion and the best condition-number argument in arbitrary Hilbert dimension. Numerical samples do not establish an infinite-dimensional theorem and are not presented as exhaustive. All mathematical objects used by the checker are defined within its source. Historical originality has not been independently established.
