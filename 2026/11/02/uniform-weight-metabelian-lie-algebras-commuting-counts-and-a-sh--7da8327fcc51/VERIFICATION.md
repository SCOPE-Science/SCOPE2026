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

Run `python3 verify.py` with the Python standard library. It enumerates all toral vectors and, independently, all radical rows satisfying the actual pairwise-minor equations over the indicated prime fields, and compares the total with the binomial/matroid expression. The check is exhaustive for the test configurations only. Expected final output: `UNIFORM_METABELIAN_COMMUTING_OK 19`.

The uniformity precondition is independently tested by Gaussian elimination on every subset of the stated field-valued weights. Test cases include diagonal rank \(d=1\), ranges \(m<2d\), \(m=2d\), \(m>2d\), and tuple arities one through three. No finite experiment is treated as an infinite proof; the proof of the geometric component classification is presented separately in `RESULT.md`.
