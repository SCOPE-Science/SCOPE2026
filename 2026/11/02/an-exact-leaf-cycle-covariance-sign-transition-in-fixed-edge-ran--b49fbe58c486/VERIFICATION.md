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

# Reproduction and verification

Run `python3 check.py` using the Python 3 standard library. The final packaged verifier reports:

`PASS: 68 exhaustive graph-ensemble checks; 39329 exact rational formula/sign checks; total 39397`

The verifier enumerates all simple graphs on \(n=4,5,6\) vertices and computes the leaf/triangle and leaf/four-cycle mixed covariances by full exact-edge strata, comparing with the independent conditional-count formula. It also performs a rational parameter sweep over motif classes and integer triangle sign thresholds for \(4\le n\le40\). The exhaustive enumeration applies only to the stated finite values; the proof for arbitrary sizes is the symbolic conditional-expectation identity, monotonic factor and strict threshold inequalities in `RESULT.md`. No external prover or independent scientific audit is asserted.
