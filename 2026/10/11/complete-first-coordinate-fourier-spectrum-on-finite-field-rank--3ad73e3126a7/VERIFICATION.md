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

# Verification

The algebraic proof establishes the complete multiset of eigenvalues and all equality spaces for every prime power and \(m,n\ge2\). In particular, it independently derives the rank-one Fourier kernel, diagonalizes all rook subspaces, checks that dimensions sum to \(1+mn(q-1)\), and proves the remaining two-dimensional block is positive through a nonzero variance. The asymptotic uses exact trace and determinant identities and is limited to fixed field order with both square dimensions tending to infinity.

To repeat finite experiments, run `python checker.py` in a Python 3 environment with NumPy. The checker independently enumerates the rank-one matrices, constructs the Gram matrix from field-additive characters, and compares every entry and every eigenvalue (with multiplicities) to the claimed formulas. It tests twelve cases using field orders \(2,3,4,5,7\); nonprime \(\mathbb F_4\) uses an explicit irreducible polynomial and trace character. Passing finite checks is not evidence of a proof for arbitrary dimensions or field orders.

Limitations: no independent scientific audit has yet occurred; higher-degree Fourier bands and non-rank-one shells are outside scope. The precise historical novelty of this selected-band specialization remains subject to expert literature review.
