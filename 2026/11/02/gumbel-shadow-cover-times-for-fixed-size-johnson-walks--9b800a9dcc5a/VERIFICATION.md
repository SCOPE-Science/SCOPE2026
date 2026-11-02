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

## Computational checks
Execute `python verify.py` from this directory, with NumPy available. The checker independently evaluates stationary avoidance of specified target sets by (i) a rational-valued projected chain on selected coordinates, and (ii) the full rational-valued Johnson walk. It compares both paths for up to four transitions for six small configurations and checks large-size normalized killed eigenvalues for several intersecting and disjoint targets. The executed checker returned `PASS: 556 exact and spectral checks; 6 finite-chain cases and 6 asymptotic patterns`.

## Analytical verification and limits
The substantive proof is the finite-state perturbation calculation in RESULT.md: uniform stationary entrance flux, comparison of quasi-stationary and stationary laws on the bounded coordinate chain, spectral separation, and factorial-moment convergence. This is not a machine certificate for all \(n\). The numerical probes do not establish an infinite limit or originality. The work has not undergone an independent mathematical audit.
