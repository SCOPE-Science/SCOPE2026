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

# Exact verification record

Run `python verify_lattice.py` after installing the requirement in `requirements.txt`. It uses exact integer Smith decomposition, verifies unimodularity and kernel primitivity, and recomputes full discriminant invariant factors for both twisted Frobenius actions. It also checks the orthogonal eigenspace discriminant/index relation.

Run `python verify_points.py` to exhaust all 256 coefficient quadruples over \(\mathbb F_5\) and independently enumerate selected \(\mathbb F_{25}\) points. Verified output contains `CHECK_OK` and `VERIFY_OK`. The extension-field finite checks are illustrative; all-field point-count formulas follow from the cohomological proof and the known geometric Picard basis.

The input arrays are published arithmetic geometry data (Shimada; Katsura–Kondō–Shimada), not newly authored mathematical source results. The new computations use their integral pairing and two explicit commuting actions. No independent scientific audit or mathematical priority certification has occurred.
