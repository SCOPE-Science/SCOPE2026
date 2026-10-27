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

# Verification and reproducibility

Run `python3 check_matrix_idempotent_annihilation.py` with ordinary Python 3. This uses neither network nor third-party libraries and prints deterministic case-by-case checks. Its companion `.out` file contains the actual saved output.

The checker exhaustively enumerates all \(q^{n^2}\) matrices and identifies all idempotents by directly multiplying their rows, independently eliminates to compute ranks, and tests all ordered vertex pairs for both zero-product orientations. Checked parameters: \((n,q)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2)\), encompassing 699,372 ordered vertex pairs. Field order four uses polynomial arithmetic modulo \(z^2+z+1\). Each rank-to-rank adjacency count is compared against the closed formula and multiplicities against Gaussian counts. Auxiliary reverse-product-rank counts serve as an independent consistency check, not an additional claimed discovery.

The abstract graph reconstruction is proved symbolically using \(\delta=2q^{n-1}-1\), \(M=q^{n-1}(q^n-1)/(q-1)\), \(Q=(\delta+1)/2\) and \(q=(M/Q-1)/(M/Q-Q)\). The finite program does not constitute an exhaustive test for all prime powers or unbounded dimensions, and no external mathematical audit has occurred.
