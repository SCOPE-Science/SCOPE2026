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

Execute `python verify.py` using Python with NumPy and SciPy installed. The program constructs the full four-state GKLS superoperator from the detuned three-site Hamiltonian, injection and extraction jumps, and local dephasing; it obtains a trace-one stationary density matrix by linear solve, checks Hermiticity, positivity, trace and residual, and computes passive work using all density-matrix eigenvalues.

At the specified numerical parameters the verifier checks the limiting population ratios and their normalization, both chemical-potential branches, the exact equality at the boundary, the one-sided slope, and convergence of normalized energy and ergotropy between detunings 300 and 900. It varies contact, dephasing, chemical potential and positive temperature independently, and tests the near-saturation limit. The executed program produced `PASS: 231 deterministic analytic, normalization, positivity, and GKLS checks`.

The parameter-universal stationary limits and the nonanalytic limiting threshold are established by the analytical population-balance and passive-spectrum proof in `RESULT.md`, not by finite-dimensional numerical sampling. The checker has no claim to verify untested parameter values or independently certify publication priority.
