---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The set of points below the new point is a downset L, the set above an upset U; they must be disjoint and every member of L must be strictly below every member of U. These conditions also suffice by transitivity. Universality and homogeneity realize every such finite diagram over the fixed parameters and identify its realizations; arbitrarily many incomparable copies of the new point give nonalgebraicity. A fixed downset under σ is a union of cycles on the lower level, all of the lower level plus a nonempty union on the upper level, or all but one lower point together with its paired upper point at a fixed index. These contribute 2^c, 2^c−1 and f. Mixed diagrams are two nonempty disjoint unions of index cycles. There are 3^c−2^(c+1)+1 of these; after adding the one-sided diagrams and counting the empty pair once the result is 3^c+2^(c+1)+2f−2. Under στ a mixed diagram must swap its two index colors along each cycle; each odd cycle is therefore unused, each even cycle is unused or alternates in one of two phases. Including the empty diagram gives 3^e. As a separate orbit check, permutation averages of q^c and f are binomial(n+q−1,q−1) and 1; the average of 3^e is the coefficient of z^n in exp(sum_{k≥1} z^k/k + 2 sum_{k even} z^k/k)=1/[(1−z)(1−z²)], namely floor(n/2)+1. Burnside gives the two claimed orbit counts. At n=2 the counts are 19, 12 and 7, with no equality types included.

## originality

PASS

The scalar count already follows from a more general height-two identity and is not credited as new. The distinct contribution is the equivariant character, especially the signed even-cycle dependence, and the resulting orbit comparison. A later same-object record shares the scalar and ordinary orbit counts, and has stronger ordinary profile data; the mathematical overlap is real. No earlier equivalent signed or full character was established from the inspected evidence.

## value

PASS

Standard-example posets are a canonical family. Their one-point extensions give a natural permutation representation, and its fixed characters distinguish what is invisible in a scalar count: only even cycles support nontrivial duality-twisted diagrams, with two alternating choices each. The two orbit counts quantify the additional effect of order-dual equivalence and give exact benchmarks for comparisons with other height-two examples. Value is in this equivariance, not recomputing the known scalar specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
