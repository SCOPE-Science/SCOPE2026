---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For finite simple unweighted two-terminal internally disjoint paths, edge gradients are exactly edge vectors whose path sums agree. Orthogonal least squares forces a common corrected path sum weighted by 1/ell_i; the explicitly derived matrix has negative same-path off-diagonal entries and positive cross-path entries. Its maximal absolute row sum is max_i[2-2/ell_i +(2+(r-2)ell_i)/(ell_i^2 sum_j 1/ell_j)], attained by the signs of a row. Cauchy--Schwarz sum_{j != i}1/ell_j >= (r-1)^2/(N-ell_i) gives an all-profile upper bound 3+0.5 sqrt(N/s); one path of length s plus balanced long paths gives 1/(2sqrt(s)) in the limit for every sufficiently large edge count. Independently reconstructed exact rational incidence-Gram projections for (1,2),(1,2,3),(2,2,3),(1,3,4,5),(2,4,5), agreeing with the formula. Code and finite samples corroborate; they are not the proof of the asymptotic quantifier.

## originality

PASS

The known general square-root electrical routing bound and shortcut example establish growth order but do not imply the complete rational profile formula nor the sharp coefficient for every fixed minimum path length s. A different transfer-current average or spectral bound does not determine the maximum absolute row sum exactly. The mathematical statement is a new sharp, natural restriction-family classification on the sources inspected.

## value

PASS

The maximum-row transfer-current amplification is a natural and previously studied electrical routing invariant; exactly optimizing it over parallel-path profiles separates a direct shortcut s=1 from every s>=2 and gives sharp constants, not a mere reproduction of the already known sqrt(N) order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
