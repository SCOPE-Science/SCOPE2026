---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

After diagonalizing Z orthogonally, extract the coefficient of t²su in det(tA+sZ+uI). Fixing the two complementary diagonal rows for sZ and uI leaves the two-by-two principal minor of A; the polarization coefficient is 12. With complementary pair sums w_ij this gives the diagonal block W/24, where W has those off-diagonal entries and zero diagonal, and six independent scalar terms −w_ij a_ij²/12. W is nonzero for Z≠0 and has trace zero, so has a strictly positive eigenvalue; a negative w_ij adds a second independent positive direction. For W entrywise nonnegative the largest eigenvalue bounds every eigenvalue in absolute value (apply |xᵀWx|≤|x|ᵀW|x|). Thus if there are two positive eigenvalues, the remaining two are strictly negative by zero trace. The determinant is then positive; with exactly one positive eigenvalue it is nonpositive, including zeros. Independently, set u₁=λ₁λ₂+λ₃λ₄ and take u₂,u₃ from the other two pair partitions. The three complementary products of W-entries are P_i=e₂−u_i, and the determinant expansion is (∑P_i)²−4∑_{i<j}P_iP_j=−4∑_{i<j}u_iu_j using ∑u_i=e₂. The last sum contains exactly the twelve monomials of e₁e₃ other than the four copies of e₄. This proves the determinant criterion including all equalities. Orthogonal decomposition along any vector of strictly positive quadratic value proves the reverse inequality; zero gives it trivially, and PSD arguments have nonnegative value by the weighted principal-minor formula. I checked that (−1,3,4,100) gives e₁e₃−4e₄=56528 outside the weak balance cone, and that (−1,1,2,3) gives −1 and the asserted deficit −5t²/144 for the given positive definite matrices. The frozen symbolic support was inspected, not executed.

## originality

PASS

The principal-minor identity, strict pair-sum positivity test on definite inputs, and strict and weak spectral-balance sufficiency are established antecedents. The distinct contribution is the exact positive-index-one criterion on the full ten-dimensional space, including the polynomial equality boundary and parameters outside weak spectral balance. The comparison in the frozen record would be more complete if it also cited the weak-balance result in Theorem 4.7 and its proof; that result still does not give the necessary-and-sufficient boundary.

## value

PASS

For a natural signed Alexandrov–Fenchel quadratic form this replaces a sufficient cone with a checkable necessary-and-sufficient spectral boundary on the full space, rather than only positive input tests. It handles degenerate forms and exhibits both a signed case that works outside prior balance and a positive-definite inequality failure when only the pair-sum test holds. These distinctions are substantive even though the classification is specific to dimension four and one signed reference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
