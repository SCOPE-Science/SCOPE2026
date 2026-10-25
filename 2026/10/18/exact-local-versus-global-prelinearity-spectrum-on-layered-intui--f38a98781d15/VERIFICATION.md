---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For ordinal sums of finite nonempty antichains, every upset has exactly one first occupied level and arbitrary nonempty boundary subset, giving N=1+sum_i(2^n_i-1). Incomparability occurs only at a shared first boundary level: ordered pairs of incomparable subsets there number q_i=4^n_i-2*3^n_i+2^n_i. The Kripke implication clause fails both ways exactly at a common lower bound of U\V and V\U; that lower bound exists for such a pair iff its level is at least 2. Thus the three disjoint counts N²−sum q_i, q_1, sum_{i>=2}q_i are correct for all h>=1 and positive n_i. q_i=0 iff n_i=1, yielding the universal-validity boundary. Increasing the bottom layer alone makes prelinearity almost certain while comparability tends to zero, and opposite limits follow from dominant 4^n terms. Independently checked every composition of total 1..8 worlds (255), evaluating upsets and worldwise clauses without trusting closed formulas; example (3,2,1): N=12 and cells (124,18,2).

## originality

PASS

Best-of-knowledge original mathematical contribution after separate comparisons of equivalent formulations, broader known work, exact tables and logical prior implications. Related methods and endpoint results explicitly credited; residual bibliographic uncertainty retained.

## value

PASS

Prelinearity is a canonical nonclassical logical law and uniform distribution on distinct upsets is a natural finite-Heyting satisfiability measure. The exact split of globally comparable, locally but not globally valid, and invalid instances is a genuine full classification for layered weak-order frames; the counterintuitive probability separation gives a reusable benchmark for logic/probabilistic semantics. Not a mere substitution in a chain theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
