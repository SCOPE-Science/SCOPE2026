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

# Reproducibility and checks

Run `python verification.py` with NumPy installed. The program independently forms the Hermitian hopping matrix, partitions eigenspaces by eigenvalue, computes the common nullspace of sink evaluations using SVD, and sums the sitewise norms of resulting dark eigenvectors. It compares against the exact analytic dimension and localized survival distributions for every nonempty proper trap subset on cycle lengths \(3\) through \(10\), 70 deterministic pseudorandom subsets per cycle length \(11\) through \(28\), and fluxes \(0\), \(\pi\), and \(0.31\). It checks \(9{,}852\) configurations and \(128{,}670\) sitewise entries. Separate diagonalizations of all two-sink subproblems and the three-sink configurations \(\{0,3,5\}\) at length \(60\), and \(\{0,3,10\}\) at length \(105\), confirm the sharp examples at both special fluxes and a generic flux.

The script also exhaustively enumerates candidate triples at smaller lengths for the two cutoffs; this is finite corroboration only. The proof of universality, positivity for any nonzero rates, and sharpness at arbitrarily large lengths is entirely analytical. No calculation of finite-time survival, disordered hopping, non-Markovian loss, or projective measurement dynamics is represented.
