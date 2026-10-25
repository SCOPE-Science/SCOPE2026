---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For 2<=m<=n the independent empty-label set in K_m square K_n is a nonattacking-rook placement of size <=m. Exact weight is mn-|Z|+|D|, with D doubly colored cells, and the diagonal-hole triangular singleton coloring attains mn-m. Every minimizer therefore has m injection-placed holes and no double labels. Fixing holes, each failed constraint E_i forces monochromatic color on the m+n-2 neighbors; for any nonempty k-row subset of constraints their neighborhoods overlap pairwise and have union size u_k=k(m+n-k-1), yielding 2^(mn-m-u_k+1) solutions. Inclusion-exclusion over k gives stated finite closed formula for all m,n. Its fixed-m k=1 leading term is -m*2^-(n+m-3), higher k terms O_m(2^-2n). New independent singleton-color enumeration matches (2,2)=4,(2,3)=60,(2,5)=4520,(3,3)=264,(3,4)=10224,(4,4)=87024. Enumeration supports, not replaces, the inclusion-exclusion proof.

## originality

PASS

The new all-(m,n) enumeration of labeled minimum outer-independent 2-rainbow functions is not supplied by existing scalar domination bounds, by enumerators for complete multipartite graphs, or by Roman-labeling variants. Its exact pattern of neighborhood intersections matters. Best-of-knowledge PASS, retaining unindexed-result risk.

## value

PASS

The optimal solution count is a natural robustness and degeneracy statistic for rainbow domination on standard rook/Hamming graphs. Unlike scalar optimum weight, it tracks many competing labeled two-color assignments, and nontrivial k-fold neighborhood overlaps require a genuine enumeration. The expression works for every rectangular size, including asymptotic proportion for fixed m; it is more than a small known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
