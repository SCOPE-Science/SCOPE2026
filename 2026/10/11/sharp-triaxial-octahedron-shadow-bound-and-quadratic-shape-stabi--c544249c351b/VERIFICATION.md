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
# Reproducibility and verification

Run `python verify.py` in an environment with NumPy and SciPy. The program directly counts vertices of planar convex hulls, independently classifies Gaussian directions through strict triangle inequalities, and compares empirical frequencies with the exact analytical expression for five anisotropic octahedra. It also checks randomly sampled shape parameters against the proven bound and checks the local quadratic coefficient along two inequivalent centered logarithmic directions.

The completed package was executed with `VERIFY_OK 1527004`. The exact regular reference value was \(0.350959312184\ldots\). A symbolic computation independently expanded \(D/(abc)\) for the centered log-shape path \((t,-t,0)\) to second order and recovered \(5\sqrt2+(27\sqrt2/4)t^2+O(t^4)\).

The proof, not random simulation, covers all positive side lengths and all isotropic plane directions. Monte Carlo error, including the loose numerical tolerance in the supplied program, means finite diagnostics are not a proof of the exact event measure, uniqueness or infinite-parameter sharp inequality. The standard trihedral solid-angle identity is the nontrivial exact geometric ingredient and is stated with a branch and denominator check in `RESULT.md`. Independent audit has not been performed.
