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
`artifacts/verify.py` uses only the Python standard library and exact integer arithmetic modulo \(23\).

It constructs \(\mathbb F_{23^2}=\mathbb F_{23}(u)\) with \(u^2=5\), verifies that \(\beta=4+7u\) has order \(24\), and rebuilds the minimal polynomials \(M_i\) for \(1\le i\le11\). For each pair \(I=\{1,2\},\{1,3\},\{2,3\}\), it multiplies the prescribed factors, verifies the degree-\(20\) generator and divisibility by \(x^{24}-1\), and forms the four cyclic generator shifts.

The verifier exhausts all \(23^4\) messages for each code, so the weight distributions are complete finite enumerations rather than samples. It separately normalizes all generator columns in projective space, counts point multiplicities, enumerates all projective lines determined by column points, and derives the generalized Hamming weights from the exact column-subspace formula. Successful replay prints `VERIFY_OK`.

The computation does not classify other \([24,4,12]_{23}\) codes and does not infer anything from unsuccessful searches.
