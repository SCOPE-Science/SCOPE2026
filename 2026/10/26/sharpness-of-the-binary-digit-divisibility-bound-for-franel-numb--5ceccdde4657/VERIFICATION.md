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

# Verification of sharp Franel valuations

Run `python3 verify_franels.py` using standard Python 3. The checker independently computes \(F_n\) through \(n=6000\) via the standard three-term recurrence, verifies congruence modulo \(2^{s_2(n)+1}\) for every index, and compares 101 terms against separate direct binomial-cube and Strehl formulas. It checks each of the 5151 possible terms of these identities through \(n=100\) for the termwise lower bound and precise carry-free/Lucas equality criterion, then tests thirteen complete binary-length Fibonacci censuses. All local checks passed on the packaged source. The infinite statement follows from the symbolic proof in RESULT.md and is not certified by these finite checks.

The 2014 MSRI-UP report's indexed title, abstract and contents were accessible, but the relevant full text was not. The originality conclusion is therefore subject to a meaningful literature risk. An independent mathematical audit has not been performed.
