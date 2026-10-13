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

The proof is analytic and has four independently checkable steps.

1. Flat configurations on the tetrahedral sphere are exactly the edge differences of vertex potentials \(e_{ij}=q_j-q_i\) after fixing \(q_0=0\).
2. For one elementary type-I or type-II cocycle factor, the vertex-\(0\) star ratio restricts at \(q_1=0\) to a nonzero signed scalar multiple of \(C(q_2,q_3-q_2)\). This is insensitive to the three face-orientation signs because the first two carry terms vanish on the slice.
3. The anchor source proves that the carry function has exact reduced polynomial degree \(p\), and that invertible affine changes preserve exact diagonal hierarchy level. Therefore the restricted ratio has exact level \(p\).
4. The anchor's stabilizer-state classification and finite-difference formula imply that an \(X\mathcal C_d^{(k)}\) presentation of the same affine-support state would force every support-displacement amplitude ratio to lie at level at most \(k\). Hence \(k<p\) is impossible, while the anchor construction gives \(k=p\).

The included `artifacts/verify.py` was executed successfully and returned `VERIFY_OK`. It checks all eight sign patterns for \(p=3,5,7,11\), confirms the slice identity, interpolates the reduced carry polynomial, and verifies degree \(p\) in those representative cases.

The finite script is not an exhaustive proof over primes, cocycle gauges, triangulations, or mixed cocycle products. The theorem's all-prime content rests on the exact symbolic carry-degree and affine-invariance results cited from the anchor source.
