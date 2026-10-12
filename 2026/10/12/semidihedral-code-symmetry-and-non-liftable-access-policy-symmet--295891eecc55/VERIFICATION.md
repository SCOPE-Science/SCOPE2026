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
The standalone verifier `artifacts/verify.py` uses only the Python standard library.

It reconstructs the source's \(4\times8\) ternary generator matrix, enumerates all \(81\) words, and checks the published weight distribution
\[
1+20z^4+32z^5+8z^6+16z^7+4z^8.
\]
It independently applies the definition of a minimal codeword and checks that normalization at dealer coordinate \(0\) gives exactly the \(15\) minimal access sets printed in the source.

It then exhausts every one of the \(40320\) coordinate permutations. Exactly \(16\) preserve the code. The verifier checks the cyclic shift \(r\), the involution \(s\), the relation \(srs=r^3\), equality of the generated subgroup with the entire exhaustive automorphism set, and the element-order census \(1^1,2^5,4^6,8^4\).

Finally it exhausts all \(5040\) participant permutations of the published access hypergraph. Exactly four preserve it; the explicit generators square to the identity and commute, giving \(C_2\times C_2\). The participant orbits and the order-\(2\) image of the code's dealer stabilizer are checked exactly. Successful replay ends with `VERIFY_OK`.

No random sampling is used. The computation proves only coordinate-permutation symmetry; monomial symmetry is outside the claim.
