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

# Reproduction of mathematical checks

Run `python3 verify_tetra.py` with Python 3 and SymPy. The script constructs the four tetrahedral sign vectors and two independent tangent vectors at each vertex, builds the exact differentiated Legendre-kernel Gram matrix and symbolically factors its determinant over the rational function field. It computes exact ranks for all degrees zero through twelve using rational Legendre polynomial derivatives and separately computes harmonic homogeneous-polynomial tangent-derivative ranks for degrees one through six. It checks by exact integer and rational inequalities the numerical comparisons required to apply the analytic Bernstein bound from degree thirteen upward.

The checker was run successfully from its current package path. Expected terminal output is:

`VERIFY_OK determinant_factor=exact rank_0_to_12=[0, 3, 5, 6, 8, 5, 8, 8, 8, 8, 8, 8, 8] direct_harmonics_1_to_6=exact Bernstein_tail_13_plus=certified`

The infinite-range argument additionally invokes the published classical Bernstein bound for Legendre polynomials at interior points, DLMF equation 18.14.3. The checker validates its required rational consequences; it does not purport to reprove this external classical inequality. The argument is exact, not floating-point extrapolation. Independent mathematical audit has not been performed.
