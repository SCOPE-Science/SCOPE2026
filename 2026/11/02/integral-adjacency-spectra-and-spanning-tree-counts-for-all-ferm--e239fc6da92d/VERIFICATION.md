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

# Reproducibility and verification limits

Run `python3 verify_fermat_spectrum.py` with Python 3; no third-party packages are needed. Its expected terminal line is `VERIFY_OK`, and the checked output from the executed script is provided as `verify_output.txt`.

For \(d=3,4,5,6,7,8,9\), the program constructs a binary symmetric \(3d^2\)-vertex graph directly from the three projective-line incidence congruences. It checks every vertex degree and edge symmetry; the candidate eigenvalue multiplicities sum to the graph order; the adjacency matrix satisfies the product of distinct predicted linear factors; and the first \(r\) power traces determine the proposed multiplicities uniquely by Vandermonde invertibility. It checks the Gram-rank consequence. Computations use exact arbitrary-precision integers throughout.

The finite checks are not a proof for all integers \(d\). The published `RESULT.md` gives the all-degree proof using discrete Fourier decomposition, an explicit treatment of the even-degree signed three-mode block, and Kirchhoff's matrix-tree theorem. The claimed new fact is the full parity-sensitive spectrum and tree count, not the classical intersection congruences or line-lattice rank. Historical priority and the source literature comparison require independent review. No independent scientific audit has been performed.
