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
Run `python3 verify.py` from this package. Its exact success terminal marker is `VERIFY_OK`. The script independently enumerates cyclic consecutive partitions, reduced-row-echelon rank-two ternary planes and their zero-one maximal minors, supports and ranks. It checks the sample dimension polynomials and the combinatorial binomial identities, including support-by-support integral Plücker consistency. Python 3 standard library only; no external datasets or network access required.

The finite checks establish the stated finite instances only. The infinite-domain theorem follows from the geometric and combinatorial proof in RESULT.md; experimental enumeration is not substituted for proof. The integer count at \(z=1\) was known previously, and no independent audit has been performed.
