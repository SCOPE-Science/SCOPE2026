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

The file `verify.py` uses only Python standard-library modules. It reconstructs the exact factorization of the finite covariance with fractions on several grids for \(3\le n\le11\). It also evaluates the corresponding uniform-grid positive-integer-composition model at increasingly fine resolution, tests the critical mean-one plateau for a range of sample sizes, samples normalized exponentials, and compares the proposed fixed-scale limit and crossover location numerically. The script prints `PASS 7763 exact, lattice-limit, asymptotic and simulation assertions` on successful completion.

The analytical proof does not rely on these checks: the Dirichlet simplex shift gives the exact moment identity, and a monotone one-dimensional quotient establishes all finite sign transitions. Numerical root locations and simulations do not establish infinite-range claims. The source comparison establishes only best-knowledge originality, not exhaustive priority or independent verification; full historical access to some earlier circle-covering literature was unavailable.
