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

For each block its row and column intervals have the same length; ordinary matrix multiplication is nonzero exactly when the first column interval and second row interval meet. The zero-product gap count has two left/right orders, three slack gaps, and independent unused interval starts. The resulting sum is polynomial of degree at most six by expansion into monomials and summation in s, so the seven exact values in RESULT.md really prove the identity. Independently, classify nonempty intersections by their first position i. The weighted count of intervals starting at i is A=(n-i+1)(n+i)/2; the weighted count containing i is C=(n+1)i(n-i+1)/2, since the free other start contributes n+start-end and averaging over the rectangle of endpoints gives (n+1)/2. At least one interval starts at i, so sum A(2C-A) over i=1..n. Expanding and using power sums gives n(n+1)(7n^4+14n^3+21n^2+14n+4)/120, the claimed expression. Subtracting 2Q_n-1 removes identity pairs exactly; leading terms (7/120)n^6 and (1/9)n^6 give 21/40. The n=1 extension also gives 1 for the product count, without asserting a ratio on an empty nonzero set. Independent replay `python3 /workspace/reproductions/review_2.py` checks explicit interval sets and first overlaps at n=1..10 (17, 118, 514 for n=2,3,4). This finite run supports, not replaces, the symbolic count.

## originality

PASS

The polynomial and its monoid interpretation as a conjecture are prior. The supported distinct contribution is the all-size proof of their equality, not the sequence or the statement of the conjecture. No equivalent proof was found in the matched statements inspected. The exact conjecture is §7 in the early record reference and §8 in the inspected later author version.

## value

PASS

Settles a stated all-size enumeration conjecture for a natural inverse monoid. The interval count explains the algebraic obstruction and turns a conditional proportion into an exact one, rather than improving a finite test cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
