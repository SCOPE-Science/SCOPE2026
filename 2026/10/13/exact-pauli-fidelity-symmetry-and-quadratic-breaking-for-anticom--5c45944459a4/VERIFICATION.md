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

# Reproduction checks

Run `python -m pip install -r artifacts/requirements.txt`, then `python artifacts/verify.py`.

The verifier generates Hermitian Pauli matrices for one- and two-qubit test systems, constructs independent matrix exponentials via `scipy.linalg.expm`, computes Pauli-twirl amplitudes from direct traces, and compares the complete probability weights, conjugate-fidelity differences, and aggregate squared-defect formula. It uses a fixed random seed for 100 parameter draws and six additional edge/structure configurations, and reports `VERIFY_OK 106 matrix experiments`. The tested maximum tolerance is \(3\times10^{-10}\).

The all-\(n\) result depends on the symbolic anticommuting-Hamiltonian exponential and orthogonality of Pauli characters, proved in `RESULT.md`, not on finite sampling. An arXiv full-text comparison for the motivating 2026 publication was inaccessible; only the publicly available abstract and scientific descriptions were read. The independent-audit field above is unperformed, not a negative finding.
