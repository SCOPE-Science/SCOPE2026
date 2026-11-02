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

# Finite certificate and witness checks

Run `python3 check.py` with a standard Python 3 interpreter. The checker uses no external packages. Its recorded output is `check_output.txt`.

The degree-five certificate represents four matrix entries of each of six coefficients as 24 scalar variables modulo four. It constructs the 24 necessary constraints described in `RESULT.md` directly from right evaluation. Exact Bareiss elimination returns determinant 4096; exact binary elimination returns rank 12. Together these values prove, through integer Smith invariant factors, that a degree-at-most-five null polynomial must have entrywise-even coefficients. The proof that all such null polynomials are right-stable is symbolic and independent of the checker.

For the upper bound, the checker constructs the ring's 128 elements, checks closure under multiplication, evaluates the degree-six polynomial on **every** ring element, and separately evaluates its right multiple at the displayed witness matrix. The checker returns `VERIFY_OK` only after all assertions succeed. These checks do not establish a result for any other ring and do not substitute for the proof of the lower bound.

Self-review was performed; independent external audit was not performed.
