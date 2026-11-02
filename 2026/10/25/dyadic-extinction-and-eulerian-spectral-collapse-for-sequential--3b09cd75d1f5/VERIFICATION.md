---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

In any sequential Rule90 permutation sweep, the updated-neighbor dependence satisfies (I−L)y=Ux over F2 with L strictly lower triangular in time order. The determinant expansion of z(I−L)−U permits exactly disjoint transpositions of cycle edges and two Hamiltonian orientations, yielding H_n(z)+z^a+z^(n−a). The matching polynomial trace recurrence is monomial z^n precisely at n powers of two; terms of degree below n/2 prevent nilpotency unless a=n/2. Eulerian ascents count cyclic update permutations. Independently constructed all 5910 sweep maps n=3..7; checked char polynomials by an unrelated permutation determinant algorithm through n=5 and nilpotence of every n<=7 schedule; n=4 has exactly 16 nilpotent orders. Exact 0011->0101->0000 under pi=(0,2,1,3) and the n=16 five-sweep adjacent-pair extinction under even-then-odd order check the contrary-literature boundary.

## originality

PASS

Qualified best-of-knowledge PASS for the all-schedule Rule-90 characteristic polynomial, Eulerian ascent distribution and dyadic nilpotency cutoff. Closest primary 2026 paper in fact asserts a contrary universal obstruction, contradicted by a completely explicit direct 4-ring example.

## value

PASS

The all-size Rule90 sweep classification connects update-order ascents, the graph matching polynomial and nilpotence, giving a sharp dyadic boundary and exact schedule frequencies. The small explicit counterexample also corrects a materially misleading published universal obstruction. This is more than a computational census or routine renaming, even though underlying polynomial and Eulerian tools are standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
