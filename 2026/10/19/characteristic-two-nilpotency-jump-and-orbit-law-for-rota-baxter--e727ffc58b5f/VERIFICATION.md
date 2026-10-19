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

# Computational checks and limits

Run `python3 artifacts/verify.py` with the Python 3 standard library. Successful execution concludes with `FULL_VERIFY_OK`.

The checker directly enumerates all linear transformations of the ambient algebra, not only maps satisfying the proposed block form, over \(\mathbb F_2\) for radical dimensions \(1,2,3\), over \(\mathbb F_3\) for dimensions \(1,2\), and over \(\mathbb F_5\) for dimension \(1\), and over \(\mathbb F_4\) for dimension \(2\). The corresponding full-map spaces have sizes \(16,512,65536,81,19683,625,262144\), respectively. It tests the defining Rota–Baxter identity on basis pairs and compares every accepted map with the proposed classification and exact rank frequencies.

The resulting operator counts are \(2,16,176,3,33,5,256\), respectively; in the three binary cases, exactly \(0,6,84\) operators have nonzero square. In the quaternary radical-dimension-two case, exactly \(180\) operators have nonzero square. Explicit automorphism conjugation independently enumerates \(2,5,6\) orbits for the binary radical dimensions \(1,2,3\), and \(2,4\) orbits for the ternary dimensions \(1,2\).

Exact integer counting formulas evaluated at radical dimensions \(80\) and \(81\) agree with the parity-dependent limiting constants to within the programmed relative tolerance of \(10^{-8}\) for finite field orders \(2\) and \(4\). This is a numerical asymptotic check, not an infinite proof. The general structural classification, all-dimensional count, orbit count and sharp asymptotic are established by the arguments in RESULT.md. Independent auditing has not been performed.
