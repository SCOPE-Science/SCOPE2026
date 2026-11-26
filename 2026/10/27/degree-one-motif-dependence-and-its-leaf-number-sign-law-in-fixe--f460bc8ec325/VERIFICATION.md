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

Independently conditioned in the reverse order from RESULT.md: fix an injection and condition on all h motif edges being present. The remaining m−h edges are uniform on N−h choices. For a test vertex outside the image, the degree-one probability is (n−1) C(U−h,m−h−1)/C(N−h,m−h); at a motif leaf it is C(U−h+1,m−h)/C(N−h,m−h); at an image of a motif vertex of degree at least two it is zero. Weight by (n−k)/n and ℓ/n, and divide by the positive marginal (n−1)C(U,m−1)/C(N,m). Cancellation gives the stated normalized mixed moment and the covariance factor. The zero binomial convention covers m=h, including k=n; h≤m≤U also keeps all claimed denominators nonzero. The slope in ℓ is positive and the function of 1/m is affine, proving the stated strict sign comparisons. The sign parameters are n,m,k,h,ℓ, not a list omitting m. Exact integer replay: multiply (N)_h/(U)_h by [(n−k)(m−h)(n−1)+ℓ(U−h+1)]/[n(n−1)m], cancelling by gcd before multiplication; n=12,m=10,k=6,h=5 gives 41664/49555 and 11284/9911 for ℓ=2,5. For H=P3 at n=5 the ratios at m=2 and 6 are 3/4 and 21/20. Read the frozen verification notes and verifier source; did not run it. Its selected finite checks are corroboration, not a full-order proof.

## originality

PASS

Credit is for the extension to leaf-bearing motifs, the exact ℓ term and the matched-size opposite-sign witness, not for the already stated minimum-degree-two formula or its single-crossing consequence. The earlier no-leaf law excludes the additional overlap case v=an image of a leaf, and does not give its contribution. No inspected source establishes the full leaf-bearing statement.

## value

PASS

The extension identifies precisely which motif feature enters a natural mixed observable after size and edge count have been fixed. The path and star show that ignoring that feature can reverse the prediction at the same graph and motif sizes. This is stronger than repeating the no-leaf formula or recomputing one isolated example, while still restricted to noninduced embeddings with no isolated motif vertices and the stated edge range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
