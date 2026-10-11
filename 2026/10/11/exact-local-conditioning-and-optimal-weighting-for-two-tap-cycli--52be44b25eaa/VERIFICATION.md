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
# Verification notes

The real Jacobian was constructed from the original nonlinear intensity expression, not from the claimed eigenvalue bands. For every integer \(3\le N\le24\), all \(2N\) squared real singular values of the normalized Gram operator were compared against the two analytic bands, for four choices of \(t\) (two fixed interior values, the derived optimum, and the balanced boundary). The discrepancy was below \(3\times10^{-12}\). Independently, centered intensity differences were compared with Jacobian actions for seven dimensions, using nontrivial complex window phases and nonconstant perturbations; errors were below \(2\times10^{-8}\). The provided checker uses `numpy.linalg.eigvalsh` and fixed-seed random vectors.

The proof itself is algebraic: spectral orthogonality of the three independent Fourier characters and cyclic shift diagonalization. These numerical tests are not an exhaustive computation or proof over all dimensions. A potential duplicate in unindexed ptychographic conditioning calculations remains an originality risk. Independent audit is not performed.

Reproduction: `python verify_local_two_tap.py` (Python 3, NumPy dependency).
