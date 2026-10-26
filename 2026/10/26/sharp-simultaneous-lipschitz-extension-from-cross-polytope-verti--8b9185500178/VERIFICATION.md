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
# Reproducibility and scope

The main argument is an exact all-dimension symmetry and transportation proof in RESULT.md. The verifier `verify_crosspolytope.py` is an independent finite check of the extension kernels using a direct Lipschitz dual linear program, rather than the orbit ratios employed in the proof.

Environment: Python 3 with NumPy and SciPy installed. From a directory containing the checker, run `python verify_crosspolytope.py`.

Observed checks: dimension three, 153 pairs; dimension four, 496 pairs; dimension five, 1225 pairs; dimension six, 2556 pairs. Total: 4430 pair LPs, with tolerance \(2\times10^{-8}\). All measured operator norms equalled the corresponding theoretical constants within this tolerance.

Limits: a floating-point linear program is neither an exact proof nor an exhaustive check over unbounded dimensions or arbitrary extension operators. The global-minimality certificate and exact radical identities are analytic. No independent mathematical audit has been performed.
