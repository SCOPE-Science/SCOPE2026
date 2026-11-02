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

## Mathematical checks

The proof in `RESULT.md` reduces the infinite-dimensional eigenvalue equation to a finite resolvent matrix, diagonalizes it by Walsh characters, and uses a positive Bessel heat-kernel formula. Critical-state square summability is determined by the exact local Fourier singularity rather than by finite-volume extrapolation. The adjacent-corner identity is obtained by integration by parts of a modified-Bessel heat-kernel factor.

## Numerical reproduction

Execute `python check.py` with NumPy and SciPy. The checker asserts strict ordering of numerically integrated thresholds for several dimensions and spacings, checks the exact adjacent-corner ratio numerically, compares Bessel integration with separate Brillouin-zone quadrature at energies outside the spectrum, and compares selected above-band counts against direct finite periodic Hamiltonian diagonalization. The completed checker returned `PASS 79 checks`.

Numerical quadrature and finite lattices do not certify the universal claims; the analytic arguments provide those conclusions. For finite-volume comparisons, a positive spectral buffer avoids counting shifts of unbound finite-volume levels. Independent external review has not been performed.
