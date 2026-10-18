---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For all star sizes m>=2 and w_i>0, the symmetric weighted Laplacian has simple eigenvalues when w_i distinct: the eigenvector leaf-to-hub ratio is w_i/(w_i-lambda). Evaluating its characteristic polynomial at w_i yields the exact horizon-free determinant ratio d_i², d_i=w_i^{m-1}/prod_{k!=i}|w_i-w_k|. Independent exact rational Krylov determinants confirm |det O_0|=(prod w_i)prod_{a<b}|w_a-w_b| and |det O_j|=(prod w_i)w_j^{m-1}prod_{a<b,a,b!=j}|w_a-w_b|. These polynomial formulas extend to coincident weights and prove only duplicated-pair leaves stay observable in exactly-one-pair case, while any triple or two-pairs make every Gramian singular. Strict factor comparisons exclude hub and lowest leaf; perturbing the pair at ranks r-1 and r yields positive log-ratio derivative and realizes each rank r>=2 as uniquely optimal. Symbolic construction, not finite random tests, supports all m and T.

## originality

PASS

The general eigenvector-coordinate product criterion is already in Fitch-Leonard 2016 and the spectral Gramian method is known. The inspected primary material does not state the exact all-m weighted-star Vandermonde conductance ratio, complete repeated-weight singularity strata or attainability of each nonminimum conductance rank as unique maximizer. Related Resultary normalized-path result is not a star theorem. These graph-specific all-parameter conclusions survive a best-of-knowledge check.

## value

PASS

Conductance-only D-optimal scores for arbitrary size weighted stars, exact observability bifurcation at repeated weights, and realization of every nonminimum leaf rank provide a natural complete single-sensor classification. These are practical network-design invariants not arbitrary finite parameter slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
