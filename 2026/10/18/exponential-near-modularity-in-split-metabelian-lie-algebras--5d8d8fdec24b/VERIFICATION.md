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

Both accompanying Python 3 files can be run from the same directory (`python verify.py` and `python independent.py`). The former constructs all RREF subspaces in several small prime-field vector spaces, tests the Lie bracket, exhaustively compares all ordered subalgebra pairs with the formula, and checks larger Gaussian-sum examples. The latter independently enumerates the split invariant-subspace lattices and recalculates the pair-sum formula for blocks \((2,2,2)\) over \(\mathbb F_3\) and \((2,2)\) over \(\mathbb F_2\).

Observed outcomes: six complete subalgebra-pair enumerations, six larger formula cases, two independent invariant-lattice pair-sum comparisons; both scripts finished without assertion errors. The complete enumeration for \((2,2)\) over \(\mathbb F_2\) has 188 subalgebras and 6,204 nonpermuting ordered pairs. The example with three distinct scalar eigenvalues and three two-dimensional blocks over \(\mathbb F_3\) has 67,280 subalgebras and 911,952,000 nonpermuting ordered pairs by the exact sum.

These finite computations do not certify the claimed infinite-family bounds. The analytic bounds use uniform Gaussian-binomial estimates and an explicit family of noninvariant-hyperplane witnesses as proved in `RESULT.md`. Extension-field cases rely on the field-uniform algebraic argument; the executable tests use prime fields only.
