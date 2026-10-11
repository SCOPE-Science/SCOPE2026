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

The proof has a symbolic lower-bound part and an exact finite sharpness part.

For product framing, the published presentation gives
\[
H_1(Z;\mathbb Z)\cong\operatorname{coker}A_S\oplus\mathbb Z/d,
\qquad d=\gcd(p,q).
\]
The adapted covering maps have cokernels \(\mathbb Z/p\) and \(\mathbb Z/q\). Projection to the two factor cokernels gives a surjection from \(\operatorname{coker}A_S\) onto \(\mathbb Z/p\oplus\mathbb Z/q\). This proves the universal product-framed divisor \(pq\,d\) without computation.

For sharpness, `artifacts/certificates.json` contains three products of integral symplectic transvections in the adapted surface bases. `artifacts/verify_minimal_h1.py` reconstructs every matrix from definitions, checks every transvection and its product against \(S^\top J S=J\), builds the two covering maps from the formula in Lemma 11.2 of the source, and exhaustively evaluates every maximal minor by exact Bareiss elimination.

The replay returns surface-cokernel orders \(16\), \(9\), and \(12\). They equal \(pq\) in the three cases, so the natural quotient map onto \(\mathbb Z/p\oplus\mathbb Z/q\) is an isomorphism. Adding the split meridional \(\mathbb Z/d\) gives the claimed three groups and orders.

The finite replay is a certificate for the three explicit witnesses only. The lower bound for all product-framed full-rank gluings is the symbolic quotient argument above. No claim is made for nonzero framing terms or for a complete classification of all possible first-homology groups.

No independent audit has been performed.
