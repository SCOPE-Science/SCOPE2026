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

The proof relies on the positive rank-one resolvent identity for \(A+tP_v\), the scalar fractional-power integral, monotone convergence, the Loewner–Heinz inequality, the equality of square-root ranges under two-sided operator comparability, and equality of closed quadratic forms on a common form core. All constants and the form domain are recorded in `RESULT.md`.

Run `python check_profile.py` with NumPy installed. The checker diagonalizes independently constructed strictly positive finite matrices, probes many normalized vectors, evaluates \(\max\{\|A+tP_v\|_p^p,\|A-tP_v\|_p^p\}\), and compares finite-difference slopes against \(p\langle v,A^{p-1}v\rangle\). It also tests noncommuting positive comparable pairs and the positive-branch selection. It passed 1,332 finite assertions on the recorded deterministic inputs.

The checker is finite-dimensional. Numerical agreement cannot certify uniqueness in infinite dimensions, control unbounded domains, or establish historical priority. Those require respectively the analytical proof and further independent literature scrutiny. No independent audit was performed.
