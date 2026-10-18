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

# Reproducibility and scientific limitations

Execute `python verify_flux.py` in a Python environment with NumPy and SciPy. The script constructs the magnetic hopping matrix with explicit Peierls phases, the non-Hermitian no-jump generator, numerical Lyapunov Gramians, and the time-scaled survival probability. It compares the resulting quantities to independently evaluated Fourier-mode formulas.

The implemented deterministic checks pass for sizes 3 through 9 and positive detector strengths 0.7, 2 and 5, including 63 Gramians, 63 detector-start trace identities, 126 weak-flux coefficient checks, 126 dark-mode projection checks, 48 slow complex-mode widths, and 28 rescaled survival values. The test's tolerances and worst observed errors are printed on execution. They are *finite numerical corroboration*, not a substitute for the analytical argument in `RESULT.md` or an independent audit. In particular, the weak-flux coefficient is justified by the perturbative resolvent identity and Fourier Parseval summation, not by these tested system sizes.

The theorem holds for a fixed finite nearest-neighbor cycle, one irreversible detector, and any fixed positive detection rate as total flux approaches zero. Its statements do not cover joint large-size limits, other monitoring protocols, or nonhomogeneous hoppings.
