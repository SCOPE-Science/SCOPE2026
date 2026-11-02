---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The k-fold signed-vertex sum set is exactly {z in Z^5: ||z||_1<=k and ||z||_1 ≡ k mod 2}: constructive proof adds cancelling signed unit pairs after generating coordinate masses. Reflect to nonnegative orthant, write each y_i=floor(y_i)+fraction f_i, set integer slack t=k-sum floor(y_i), satisfying sum f_i<=t. Rounding up r largest fractions, for 0<=r<=min(5,t) with r≡t mod2, produces feasible sites with squared error E_r=sum f_i^2+r-2 sum_top_r f_i. Cases t=0,1,2 yield max squared error<=1 by explicit bounding E1 and min(E0,E2). For t>=4, Boolean parity-constrained rounding gives error<=5/4 (flipping minimum bias cost 2delta_min bounded by total squared-distance deficit), with all needed parity weights admissible. For t=3, if the full Boolean-parity minimizer is of forbidden weight5, optimality implies f_(4)+f_(5)>=1, and the split u∈[1/2,3/5] or [3/5,2/3] bounds admissible E3<=5/4; otherwise the minimizer itself is admissible. Explicit sites show equality: y=0 for k1, y=e1 for k2, half-integer five-vector for k>=3. Independently enumerated 12890 feasible quarter-grid cases and six full parity-lattice sharp witnesses; proof holds beyond finite tests.

## originality

PASS

Compared equivalent mathematical formulations, stronger coverage, exact-data overlap, and logical prior implication using primary material and actual Resultary searches. No materially inspected theorem was found to imply the complete final claim; this is a best-of-knowledge, not an exhaustive novelty certificate. All unread relevant material and other risks are recorded.

## value

PASS

The first finite clipping threshold in a canonical root-lattice approximation problem is a natural precise geometric invariant for Minkowski convexification of a regular cross-polytope. The D5 infinite-space covering constant is old, but it does not determine that the bounded parity site set attains that constant already at k=3 or the two exceptional resolutions. The boundary-aware rounding argument adds nontrivial structure to the classical covering result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
