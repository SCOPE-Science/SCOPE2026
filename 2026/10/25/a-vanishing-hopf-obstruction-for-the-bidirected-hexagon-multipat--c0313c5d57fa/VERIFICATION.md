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

The complete finite certificate is `BP5_MATCHING.json` and its standalone standard-library checker is `verify.py`.

Run `python3 verify.py` in their common directory. Successful execution prints `VERIFY_OK` after regenerating 196 simplices with dimension counts \((12,48,76,48,12)\), validating 96 paired facets and four unmatched critical cells in dimensions \(0,2,4,4\), checking full gradient acyclicity, checking the signed integral two-cocycle and an eight-triangle cycle pairing \(-1\), and verifying that its Alexander--Whitney integral cup square is zero on all twelve four-simplices.

These exact checks establish the finite combinatorial premises. The deduction of the homotopy equivalence separately invokes the standard discrete Morse CW-equivalence theorem and the integral Hopf-invariant classification of maps \(S^3\to S^2\). No infinite-parameter extrapolation, numerical rank approximation, or independent external audit is asserted.
