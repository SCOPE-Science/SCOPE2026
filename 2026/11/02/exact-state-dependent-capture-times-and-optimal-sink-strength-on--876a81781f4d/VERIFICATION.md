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

# Reproducibility
Execute `python check_endpoint_path_capture.py` in an environment with NumPy and SciPy installed. It independently verifies the finite-dimensional Lyapunov solution, the four structural commutator identities, definiteness of the two real kernels, and random pure-state expectations.

Observed output: 29 structural dimensions, 180 independently solved numerical Lyapunov equations, 900 coherent-state comparisons and maximum absolute matrix/equation error about \(6.1\times10^{-10}\); all assertions passed.

These are finite numerical tests. The general result relies on the stability recurrence, entrywise identities and Brownian-bridge kernel positivity proved in RESULT.md. Neither independent audit nor historical-priority certification has been performed.
