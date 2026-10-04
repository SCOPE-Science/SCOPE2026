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

The verifier checks the algebra used in the proof for every sampled even \(n\) from \(2\) through \(100\). It verifies the weight coprimality, the kernel-basis cross product, the formula
\[
M=(n+1)(n^3-1)=n^4+n^3-n-1,
\]
the two adjacent-level optimization values, and
\[
2(n^4-1)>M.
\]

It also exhaustively enumerates degree fibers for
\[
n=2,4,6,8,10,12
\]
and confirms that the first noncollinear fiber occurs at \(M\). At that degree, the three displayed monomial exponent vectors occur and their two differences have primitive cross product equal to the weight vector.

The finite enumeration does not prove the all-\(n\) theorem. The infinite lower bound is the symbolic \(D\)-level argument in `RESULT.md`; the finite checks guard the arithmetic and boundary cases.

The saved replay output ends in `VERIFY_OK`.
