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

# Reproducibility and verification

The analytic proof is in `RESULT.md`. Execute `python3 verify.py` with Python 3 (no external dependencies). This checks the stated rational constants, the exact square-summable gap-cost series, the strict dual quadratic bound on a rational parameter grid, and a deterministic approximation of the monotone Cantor quantile coupling.

For a dyadic mesh with \(2^{14}\) points the code compares the transport cost with the analytic fair-coin value. The omitted digit tail changes the Cantor quantile by at most \(r^{14}\), and the midpoint Riemann error is bounded conservatively by \(3/2^{14}\). The test does not infer any universal assertion from finite checks. The all-real-parameter conclusions follow from the supplied duality, monotone coupling, nearest-projection and predecessor-support proofs.

The construction requires \(0<r<1/2\). No computation or argument claims behavior for overlapping maps or arbitrary IFS. The theorem has not undergone independent scientific audit.
