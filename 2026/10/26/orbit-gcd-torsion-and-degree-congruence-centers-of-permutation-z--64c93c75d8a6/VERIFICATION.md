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
# Computational reproducibility

Run `python verify.py` in an environment with Python 3.10 or later and the external `sympy` package specified in `requirements.txt`. No network access is used by the script.

The checker constructs, from the defining quadratic relations and each permutation, a full integer relation matrix with one row for every ordered generator pair. It computes the Smith normal form independently of the symbolic cyclic argument and checks that the free rank is exactly the number of permutation cycles, with nontrivial Smith factors equal to a single factor consisting of the gcd of their lengths. Every permutation in dimensions one through six is tested (\(873\) total).

For every permutation in dimensions one through four, every integral coordinate vector with entries in \(\{-1,0,1\}\) is multiplied directly by every basic generator in both orders, and the observed centrality condition is compared with permutation invariance plus total-degree divisibility. The test prints `VERIFY_OK 873` when all assertions pass.

No finite computation can establish the all-degree theorem. The general assertions follow from the explicit relation derivation, lattice presentation, and generator-commutator proof in `RESULT.md`. The finite script requires Sympy's integer Smith normal form and supplies checks rather than a formal proof certificate.
