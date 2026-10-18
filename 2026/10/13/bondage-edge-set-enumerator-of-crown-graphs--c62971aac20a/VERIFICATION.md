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

For Cr_n=K_{n,n} minus perfect matching, n≥3, the only dominating two-sets are D_i={a_i,b_i}. Edge deletion cannot create new dominating pairs. D_i survives exactly when F contains no crown edge incident to index i (in either orientation); equivalently auxiliary H_F on [n] has isolated vertex i. Thus γ(Cr_n-F)>2 iff H_F has no isolated vertex. Inclusion–exclusion over isolated indices gives B_n(x)=∑_{j=0}^n (-1)^j binom(n,j)(1+x)^{(n-j)(n-j-1)}. Its min degree is ceil(n/2), with oriented perfect matching count 2^{n/2}(n-1)!! even n, and oriented three-vertex path plus matching count 2^{(n+1)/2} n(n-1)(n-2)!!/2 odd n. Independent direct graph-deletion subset enumeration checked all 2^6,2^12,2^20 subsets for n=3,4,5 against surviving dominating pairs and every inclusion-exclusion coefficient; valid sets 54,3861,1028700 and minimum multiplicities 12,12,240.

## originality

PASS

The general bondage definition and some graph families are known (Fink et al., Xu survey); standard K_n bondage ceil(n/2) is a different graph family. The directly inspected Xu 2013 full OA survey discusses some perfect-matching removal on complete graphs, not matching-deleted K_{n,n}; it has no crown entry. Published related crown-graph papers enumerate restrained/roman dominating vertex subsets or edge metric bases rather than complete *edge deletions raising ordinary domination*. No exact no-isolate edge-set polynomial is implied by those results.

## value

PASS

Bondage measures vulnerability of dominating sets to edge failure. A complete all-edge-set enumerator strengthens one threshold into the whole deletion reliability profile, with a natural auxiliary edge-cover correspondence and closed minimum-witness counts. It is an independently useful graph-family robustness invariant, not a redundant scalar computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
