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

The exact replay script `verify.py` reconstructs \(T(1)\), \(T(1/2)\), and \(T(2/5)\) as rational finite distributions. It checks normalization, means, variances \(0\), \(1\), and \(2\), performs both convolutions, and computes the length-two concentration directly from the finite support.

Expected exact outputs are \(2/5\) for the proposed triple, \(3/8\) for the variance-equalized triple, and violation gap \(1/40\). The replay is supplemental: the proof in `RESULT.md` establishes the claim analytically, including uniqueness of the variance-matching parameter through strict monotonicity of the piecewise variance formula.

No claim is made about the maximal possible violation or a classification of all counterexamples.
