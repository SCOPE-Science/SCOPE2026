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

The positive ideal has dimension 31, with 15 even and 16 odd dimensions. Each principal unit factors uniquely as (1+c)(1+s), using its even part c and dividing its odd part by the central unit 1+c. Odd factors commute iff st=0 since the characteristic is not two. A rank r odd multiplication map therefore gives a centralizer of size q^(31−r) and class size q^r. Independently of the filtration automorphism in the proof, write s=a+b+c₅ by degrees 1,3,5. When a≠0, the degree-two image of t↦st is a∧V of rank four. On the kernel of this degree-two projection, the degree-one input is a multiple of a, so the degree-four outputs from both this input and the arbitrary degree-three input lie in and span a∧Λ³V, another four dimensions. Degree-five inputs contribute nothing. If a=0, the map is v↦b∧v; after a volume identification its rank is the rank of the alternating bilinear form (v,w)↦b∧v∧w. Besides zero, the ranks are two and four. Rank two gives a 3-dimensional radical and q−1 nonzero alternating forms on the 2-dimensional quotient for each radical, equivalently one nonzero top wedge on each 3-space. Rank four exists, e.g. two symplectic blocks; its count is q^10−1−D_q. The top-degree odd coordinate is arbitrary. Multiplying the stratum sizes in odd coordinates by q^15 and dividing by q^r gives exactly the four counts including their positive values and weighted sum q^31. Summing gives k(U), hence k(U)/|U| by the commuting-pairs identity. A nonzero scalar splits off centrally in the full unit group. The argument uses odd characteristic throughout, not prime cardinality.

## originality

PASS

Bounded pass for the frozen exact principal-unit class-size census. A distinct later-dated Resultary census is demonstrably equivalent, not merely similar; no inspected evidence dates that equivalent result before this frozen finding. No claim of exhaustive priority is made, and the central-even and odd wedge structural ingredients are not new.

## value

PASS

Class sizes are a natural invariant of the principal-unit group; their full distribution is strictly more informative than the group order, center or aggregate commuting probability. Five generators make a natural low-dimensional case in which the pure degree-three stratum splits into two nonzero ranks by alternating duality, independently of the degree-one stratum. The exact all-q multiplicities expose this split and supply benchmarks for larger unit-group and commuting-law classifications, not merely a sample field calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
