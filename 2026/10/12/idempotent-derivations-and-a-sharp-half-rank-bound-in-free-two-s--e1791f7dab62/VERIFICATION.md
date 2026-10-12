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

The general claim is proved in `RESULT.md` from the Leibniz-rule block decomposition, exact tensor-block eigenspaces, finite-field subspace and complement counts, and the integer half-rank identity.

The independent-of-proof finite arithmetic checker is `checker.py`, executable with `python3 checker.py` using only the Python standard library. It exhausts every candidate matrix A on one or two generators over GF(2), GF(3), GF(4), and GF(5), plus three generators over GF(2), computes its Leibniz-induced quadratic matrix B, solves all lift constraints by Gaussian elimination, and compares exact rank multiplicities with the theorem. A second route exhaustively builds every full map for two generators over GF(2), checks composition-idempotency, and verifies the derivation rule on every ordered pair of basis vectors. The resulting rank polynomial is `1+256*T^2+96*T^3` with exactly 353 maps. The checker returns `VERIFY_OK`.

These enumerations are finite checks, not exhaustive coverage of all fields and generator counts. The arbitrary-field proof is algebraic; no external or independent audit is asserted.
