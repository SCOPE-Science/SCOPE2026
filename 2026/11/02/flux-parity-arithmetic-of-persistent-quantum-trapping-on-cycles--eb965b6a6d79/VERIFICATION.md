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

# Reproducibility and limits

The mathematical claim concerns the nondecaying subspace of a finite, single-particle, non-Hermitian Hamiltonian. Its proof is analytical and appears in `RESULT.md`; no inference from finite samples to arbitrarily large rings is made.

Run `python verify.py` with NumPy and SciPy installed. The code constructs actual complex hopping matrices with a uniform Peierls phase, diagonalizes their Hermitian part, computes the kernel of the two-site evaluation map in every degenerate eigenspace, and independently counts the real eigenvalues of the lossy matrix. It compares the resulting projection probabilities with the closed trigonometric formulas at each initial vertex. All \(825\) combinations \(3\le n\le24\), \(1\le d<n\), and three fluxes pass the locally executed checks; the check includes two strictly positive loss rates varying with the ring size and trap position. Counts and probabilities at other rates follow analytically from the nodal criterion, not numerically.

The checker uses floating-point tolerances and does not certify exact spectra, asymptotic rates, publication priority, or independent mathematical review. The proof explicitly requires \(J>0\), both trap rates positive, and flux held fixed while time tends to infinity. A different flux/time order of limits is not analyzed.
