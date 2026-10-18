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
# Mathematical verification

The theorem is proved analytically from forward invariance of the occupancy simplex, a strict logistic lower comparison, the exact weighted-logarithm ratio identity, induction on each initially occupied consecutive run, a forced linear equation for the total occupancy error, and a strictly monotone limiting composition equation. The proof applies to every finite number of species and all allowed positive parameter choices; it does not extrapolate a finite census to an infinite claim.

The accompanying standard-library Python program `verify_selection.py` evaluates 420 exact rational instances of the model identities, then integrates four distinct heterogeneous directed chains with a fourth-order Runge–Kutta solver. All four produce the support sets predicted by the run-parity theorem and the prescribed final total occupancy. The five-species example converges numerically to approximately `(0.3439589521,0,0.1957654675,0,0.1269422471)`.

Execute `python3 verify_selection.py` after extracting the standalone file. The exact tests verify algebraic identities on selected rational points, not the full proof; the numerical trajectories illustrate representative initial conditions, not global convergence. Independent audit and external validation have not been performed.
