---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For all n>=2, good positional edges G={i:|sigma(i+1)-sigma(i)|=1}; an admissible permutation has no adjacent edges outside G. A forced set S of good edges separates into r(S) increasing-or-decreasing runs on value intervals, giving exactly 2^{r(S)}(n-|S|)! permutations. Boolean-lattice Mobius inversion and the explicit three-state (S,T) transfer yield P_1=1,P_2=4u-2u^2,P_3=2u+4u^2-2u^3, P_m=uP_{m-1}+(2u-u^2)P_{m-2}. Independent brute permutation counts n=2..8 matched the polynomial recurrence exactly (2,6,18,52,170,550,1972). This independently checked finite domain corroborates but does not replace the unlimited combinatorial proof.

## originality

PASS

The theorem is an exact all-length cardinality generating-function theorem for the full symmetric two-neighbor tolerance-one rank-modulation alphabet, not an asymptotic rate or construction of a subset. The initiating primary preprint fixes the same OR absolute-succession constraint and proves asymptotic capacities/bounds, but does not imply the exact cardinality recurrence; historical exact succession refinements remain a documented risk.

## value

PASS

Exact counts for a natural rank-constrained permutation alphabet refine its known asymptotic capacity and supply a quadratic-arithmetic coefficient algorithm, a structurally motivated complete enumeration not just a small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
