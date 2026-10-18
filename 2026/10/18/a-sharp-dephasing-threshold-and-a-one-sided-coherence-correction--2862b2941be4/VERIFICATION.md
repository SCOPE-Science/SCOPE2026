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
# Verification of the four-site dephasing theorem

Run `python reproduce.py` after extracting the standalone program. Its proof-related exact assertions reconstruct the four-site Hermitian stationary covariance equations directly from the model, check the determinant and rational current, derive the tridiagonal-closure current from retained equations, and verify the exact positive correction. The derivative polynomial is obtained from the rational current rather than trusted as a transcription. Its high-degree coefficients are confirmed negative for every nonnegative squared tilt; the four remaining coefficients are proven to have one positive zero each in four pairwise-disjoint rational intervals, which supplies the sign-order certificate used with Descartes' rule.

With SymPy, NumPy, and SciPy installed, the program completed both the symbolic certificate and five independent original Lindblad density-matrix calculations on the sixteen-dimensional fermionic Fock space. These agree to better than \(10^{-11}\) in current and include zero and nonzero tilt and dephasing. The proof covers the full stated real/nonnegative parameter domain; these discrete comparisons are not an exhaustive parameter scan.

The claim does not treat unequal reservoirs, additional interactions, other chain lengths, nor independent priority validation. The exact lattice-current normalization follows the stated fermionic jump operators and must be converted before comparison with alternative Pauli-operator conventions.
