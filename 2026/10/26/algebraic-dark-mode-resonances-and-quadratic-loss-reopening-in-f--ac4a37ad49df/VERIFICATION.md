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

# Verification of the finite SSH loss-resonance theorem

The main result is proved analytically in `RESULT.md`. The bundled standalone Python program `verification/check.py` performs a separate construction of the finite Hermitian and lossy matrices using alternating tridiagonal bonds. It directly diagonalizes them and compares with the sine boundary quantization and exact site-node formulas.

Run `python verification/check.py` after installing the packages named in `verification/requirements.txt`. The actual packaged program was executed with NumPy and SciPy and printed `SSH_DARK_MODE_CHECKS_PASSED 4237`.

Checks include every positive ratio appearing in the finite formula for \(2\le N\le23\), all site positions, normalized sublattice weight balance, eigenvector residuals, dark-mode multiplicities, reflection to the second sublattice, and the uniform-chain greatest-common-divisor special case. At \(N=14,m=3,r=\sqrt2\), both direct Hermitian and non-Hermitian spectra exhibit exactly four undamped orbitals for three nonzero loss rates. The predicted positive quadratic coefficient is compared against nearby eigenvector amplitudes for selected finite sizes.

The checks use floating-point diagonalization and numerical tolerances. They do not themselves prove the complete all-size theorem, uniqueness of the vacuum for every admissible initial state, or the ordered weak-loss asymptotic. These claims rest on the recurrences, eigenvalue identities and perturbative argument given in `RESULT.md`. Literature-wide priority has not been independently certified.
