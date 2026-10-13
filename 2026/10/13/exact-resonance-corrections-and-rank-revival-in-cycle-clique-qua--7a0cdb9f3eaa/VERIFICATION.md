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

# Verification of the cycle–clique average-mixing theorem

The proof in `RESULT.md` is analytic, covering all integers \(n\ge5\), \(q\ge3\). It uses the full Fourier eigendecomposition and the algebraic-integer norm argument to exhaust the cross-band cosine gaps. Numerical calculations serve solely as corroboration.

Run `OPENBLAS_NUM_THREADS=1 python3 verify.py`, requiring Python 3 and NumPy. The checker constructs the adjacency from graph edges rather than importing the predicted spectral projectors. It independently diagonalizes each graph, builds the sum of entrywise squared spectral projectors and compares its complete matrix and Fourier eigenvalues with the rational closed formulas; it also checks stochastic row sums, rank, correction presence and exceptional examples.

Executed result: `VERIFY_OK graphs=84 Fourier_modes=4389 matrix_entries=296709 correction_cases=12 worst_abs=1.110e-15 C6_K4_rank=15/24 C10_K4_rank=23/40`.

Additionally, a separate independent graph diagonalization sweep of \(3\le n\le25\), \(3\le q\le8\), examined 138 instances and 10,626 Fourier modes, with maximal absolute spectral discrepancy about \(3.11\times10^{-15}\). The packaged checker is the self-contained reproducible program; the wider sweep is a recorded corroboration rather than an undeclared package dependency.

The finite checks do not prove that no untested cosine gaps exist. The decisive unconditional classification follows from the algebraic-integer conjugate bound in the written proof. No independent validation or external certification is asserted.
