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

The count is indexed by increasing start positions i<j, so each candidate is counted once. Substituting j'=j−(m+g−1) gives 1≤i<j'≤n−2m−g+2 and hence the stated binomial count, also zero when no pair fits. Each event imposes a matching of m complement constraints, so has probability q^(−m). At different endpoint sums c and c' the matchings have no common edge. A cycle would have to alternate colors; every two successive reflection steps would advance by the same nonzero translation c'−c (with a fixed choice of first color), which cannot close. Each edge of the resulting forest costs one factor q^(−1), by rooting each component, proving pairwise independence even with intersecting supports. At one endpoint sum the starts are (i,j) and (i+d,j−d); all constraints belong to one matching. The left intervals overlap in max(m−d,0) sites, which is exactly their number of shared edges, since all left endpoints lie strictly below the common geometric center. There are B(n−2m−g−2d+2) unordered pairs of this type at shift d, from the stricter inner-stem separation. Summation of the diagonal and twice these unordered-pair covariances gives the displayed variance including empty and m=1 cases. For fixed m,g each shifted binomial count is asymptotic to the first; the geometric sum then yields the successive limit (q+1)/(q−1). Substitution for q=4,m=2,g=0 gives (15B(n−2)+6B(n−4))/256 and ratio 21/16.

## originality

PASS

Supported distinction: exact covariance support and finite variance for disjoint reverse-complement factor pairs within one iid uniform word. The stem predicate, counting means, and covariance methods for random word matching are not credited as new in themselves. The older Fitch comparison is explicitly access-limited.

## value

PASS

The reflection-center description gives an exact second-moment baseline for a natural random-word statistic. Position overlap alone could suggest widespread covariance; the proof identifies precisely why most such pairs are independent and gives a correction for the rest. The successive Fano ratio (q+1)/(q−1) remains above the independent-event limit even for long rare stems, so the correction is quantitatively relevant rather than a boundary-only effect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
