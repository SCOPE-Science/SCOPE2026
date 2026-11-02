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

The standalone Python 3 script `verify.py`, requiring only the standard library, independently implements the stated deletion map as preservation of input position zero and all later input positions equal to their immediate predecessor in the *original* word. This exactly deletes the first letter of every noninitial run.

Executed checks: exhaustive enumeration of every input at \(q=2,\ n\le12\), \(q=3,\ n\le8\) and \(q=4,\ n\le7\); exact image-set comparisons with the binomial count and independent recurrence; canonical preimage recovery; uniqueness of minimal-length preimages; the Fibonacci identity through \(n=149\); and integer recurrence-vs-count comparisons for \(2\le q\le19\), \(1\le n\le150\). The recorded stdout is `verification_output.txt`; a new execution should end in `VERIFY_OK`.

These checks are finite. They do not establish all-length correctness without the separate run-count, inverse-uniqueness, combinatorial enumeration and recurrence proofs supplied in `RESULT.md`. There has been no independent mathematical audit, expert certification or claim of uniqueness in the global literature.
