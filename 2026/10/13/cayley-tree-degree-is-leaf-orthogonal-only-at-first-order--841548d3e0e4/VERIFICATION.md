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

The Prüfer bijection makes a uniform Cayley tree an iid uniform word W of length m=n−2 on n labels. A fixed vertex degree equals N_v+1, where N_v is its word occupancy, and total leaves L=Σ_j 1{N_j=0}. The distinguished-own term in E[Lz^{N_v}] is ((n−1)/n)^m; every other label contributes ((n−2+z)/n)^m, giving the exact mixed generating function. Differentiating at z=1 and subtracting E[(N_v)_r] E L yields (m)_r n^(−r) a^(m−r)[(n−1)−na^r]. The bracket is exactly zero for r=1, strictly positive for 2≤r≤n−2, and tends to r−1 for fixed r, yielding the (r−1)/e limit. Conditional occupancy on N_v=k gives the stated strict one-step valley. Independent complete Prüfer enumeration through n=7, including all 16,807 length-five words, verified the generating-function factorial moment consequences, degree-order-one cancellation, and all available higher positive factorial covariances. The all-n result is proved by multinomial factorial moments.

## originality

PASS

Best-of-knowledge original after mathematical claim-versus-prior comparison: The submitted formula follows from new explicit marked-label/empty-label mixed Prüfer expectations, not from marginals alone. Given inaccessible plausible original texts, PASS is best-of-knowledge and qualified rather than claiming definitive exclusion. Explicit unexcluded risks and source-access limits are documented without claiming exhaustive novelty proof.

## value

PASS

A fixed degree and global leaf count are canonical random-tree observables; exact uncorrelatedness despite nonindependence is a mathematically motivated statistical phenomenon. The explicit conditional valley, full factorial covariance hierarchy, and nonzero limiting higher-order dependence diagnose precisely why first-order orthogonality is misleading. This is a natural exact invariant and not an arbitrary finite test or only a textbook marginal computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
