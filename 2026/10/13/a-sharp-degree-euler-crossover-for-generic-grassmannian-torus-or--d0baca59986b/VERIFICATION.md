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

For all nonzero Plücker coordinates the monomial orbit configuration is the hypersimplex. Differences of its vertices generate the full sum-zero integer lattice: realize e_i−e_j by swapping i for j with a common (k−1)-subset disjoint from both. Thus the normalized lattice volume has no extra index factor. The toric degree formula and hypersimplex volume theorem give A(n−1,k−1). Additivity of compactly supported Euler characteristic on torus orbits gives one per vertex and zero for every positive-dimensional torus, and compactness gives ordinary Euler characteristic for the whole closure. The interior row minimum for m≥4 is A(m,1)=2^m−m−1: at an index 2≤j≤m−3 both earlier-row terms are interior and the recurrence has weights summing to m+1; (m+1)A(m−1,1)−A(m,1)=(m−1)(A(m−1,1)−1)>0 for m≥5. The parity class of the central binomial term has total 2^(n−1) and for n≥6 the other terms sum to more than n: when the center index is odd, index 1 and at least one more term suffice; when it is even (then n≥8), indices 0 and 2 suffice. At n=5 the bound is 11>10. The excluded interior case (n,k)=(4,2) gives 4<6, and simplex endpoints give 1<n. The dimension-four statement is read as the first dimension with non-simplex examples having the positive sign, not as a claim that a universal statement over an empty family is false in dimensions one and two. Independent replay `python3 /workspace/checks/frozen_replay.py 2` verified 7140 exact slice-volume comparisons and the numeric row bounds through n=120 via inclusion–exclusion. The supplied verification prose describes, but does not supply, its recurrence checker; neither finite check proves the infinite classification.

## originality

PASS

The two geometric formulas are classical. The distinct claim is their strict comparison across the full hypersimplex family, including the exceptional dimension-three interior and the absence of equality. The closest inspected indexed ordering treats the whole Grassmannian and has a different degree and different signs at common parameters. Direct inspections support the underlying formulas but did not establish prior coverage of the crossover; the judgment is bounded by the search and access limitations below.

## value

PASS

The classification gives the exact dimension threshold at which a generic orbit closure's general Plücker section length exceeds its fixed point count, two natural invariants not inherently ordered. The comparison is uniform, sharp, and has a concrete geometric use: the full Grassmannian and the orbit closure have the same ordinary Euler characteristic and fixed points, yet the signs of the degree comparison can differ even in the first non-simplex cases (for example 5<10<11 at k=2,n=5). This is more than recomputing either classical invariant or providing a finite table, although the proof of the comparison is elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
