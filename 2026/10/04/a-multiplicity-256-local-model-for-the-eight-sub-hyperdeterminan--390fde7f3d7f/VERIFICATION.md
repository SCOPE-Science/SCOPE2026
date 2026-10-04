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
Run `python3 artifacts/verify.py`. The script uses exact integer sparse-polynomial arithmetic and no numerical approximation. It reconstructs Cayley's quartic in each of the eight coordinate \(2\times2\times2\) slices after the local substitution at \(T\), checks that the first nonzero homogeneous degree is \(2\), and checks that each degree-\(2\) part is exactly the expected square in a distinct Hamming-weight \(1\) or \(3\) coordinate. It then checks that there are eight independent square initial forms in fifteen variables, giving codimension \(8\), local dimension \(7\), and multiplicity \(2^8=256\). Successful replay ends with `VERIFY_OK`.

The script verifies the nonstandard symbolic input to the proof. The implication from a regular sequence of initial forms to the associated graded quotient is proved in RESULT.md rather than delegated to the script. No statement is made about the reduced structure of the underlying zero set, and no independent audit has been performed.
