---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For each non-induced H embedding, conditioning on the presence of its e prescribed edges forces exactly d_v edges at each internal vertex v; thus its degree distribution becomes d_v+Bin(n−1−d_v,p), whereas external vertices retain Bin(n−1,p). Consequently Cov(D_k,X_H)=((n)_h/a_H)p^e P_{n,k}(p)[Σ_v(k)_{d_v}/((n−1)_{d_v}p^{d_v})−h] for n≥h≥2 and 0<p<1, with H having no isolates. Each nonzero term in the bracket decreases strictly with p. For k<δ it is −h; δ≤k≤n−2 gives a unique root, increasing strictly with k by falling-factorial monotonicity; k=0 negative and k=n−1 positive. Expanding (n−1)_{d}=n^d[1−d(d+1)/(2n)+O(n⁻²)] and applying the simple-root implicit expansion gives exactly the displayed c/n plus second-order term for fixed H,k. The n^{e−h} normalized limit follows from Poisson binomial convergence; no uniformity in growing H,k. All steps follow conditional identities rather than finite enumeration alone.

## originality

PASS

Goldstein–Rinott 1996/full arXiv preprint studies cross-covariances among degree-frequency counts, not against arbitrary non-induced motif copies or the ordered motif–degree critical p roots. General subgraph overlap/U-statistic theory could supply a formal starting point but no inspected published theorem gives the degree-multiset-only normalized formula together with complete sign diagram and second-order roots. k=0 is elementary and not claimed as the main discovery.

## value

PASS

Degree frequencies and motif counts are central observables of G(n,p); their cross-dependence is not given by separate variance/concentration statements. The universal degree-multiset collapse, unique roots indexed by k, and ordered sparse sign changes are natural structural properties over all motifs, not an arbitrarily chosen finite statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
