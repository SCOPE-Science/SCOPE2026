---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In exact row-pivoted GEPP, a natural prefix preserves the leading Wilkinson block and doubles the constant last column at each step. After a first lower-row choice, any nonsingular k-row leading minor excluding the original first row consists of rows 2 through k and one row s>k, since two rows beyond k agree in the first k columns. Replacing row 1 of the leading triangular matrix with an all-minus-one row gives determinant magnitude 2^(k-1): its inverse has strict-lower entries 2^(i-j-1). Adjoining an eligible lower row gives pivot magnitude 2 and at least one such row exists until the lower rows are exhausted; adjoining original row 1 gives 2^(1-k). In the Schur complement, any remaining lower row is reduced by the selected row s and so has last component zero and other entries bounded by 2. The coefficients expressing row 1 on the pivot columns sum to -1 (first column), with coefficient -2^(1-k) on s (triangular elimination), so it retains last component 2q and other entries bounded by 1. Therefore a first lower pivot at stage j gives exactly 2^j, and either choice at the last two-row stage gives the same maximum. Multiplying conditional probabilities 1/m gives the stated tails and point masses, including n=2; tail increments give the exact mean and the k>=3 terms have successive ratios at most 2/3 over their range, yielding O(n^-3). The supplied exact DP retains the peak in its state as needed; the reported finite check is auxiliary, not used for the theorem.

## originality

PASS

The supported distinct result is the closed finite-size distribution (and consequences) on one fixed input, under uniform exact tie resolution. Neither the deterministic extremes nor the generic random-pivot model supplies the support/stopping event and its factorial masses. The closest same-matrix essay actually states a cyclic low-growth ordering and an enumerated minimum, not the law across all legal paths. This is a best-of-knowledge determination.

## value

PASS

The classical extremizer makes the question of how much its exponential growth depends on exact tie order natural. The distribution measures a structural distinction between admissible elimination paths: one departure from the natural prefix fixes all subsequent attainable growth for that path, giving a factorial worst-case probability and a bounded mean. Deterministic endpoints alone do not quantify that contrast.

The dated certificate retains the supplied scientific assessment, sources and limitations.
