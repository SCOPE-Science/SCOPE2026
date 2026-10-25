---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Reconstructed the entire n>=4 proof for the inherited Euclidean zero-sum metric: polar vertices are exactly integer 1-Lipschitz potentials with a connected tight spanning graph; crown diameter 3 bounds translated labels to 0..3. A range-three extremum is necessarily a missing-pair (0,3) labeling with n−1 other 1s and n−1 other 2s, squared centered norm S_n=(n+8)/2, with precisely 2n sign/index choices. Range at most two with no diagonal gap two belongs to the complete-bipartite Lipschitz polar, whose extremal norm is U_n=n−(n mod2)/(2n), achieved at 0/2 splits of one part. Remaining diagonal-gap-two assignments satisfy the explicit J,K incompatibility; norm² <=n/2+2 (or 4), strictly below S_n. Strict convexity restricts maximal polar norm to vertices, polarity gives r=1/sqrt(max(S_n,U_n)), and duality gives all tangent facets. Comparing branches gives the unique n=8 tie, F8=16+2*C(8,4)=156; 4<=n<=7 gives 2n; n>=9 gives central-binomial multiplicities. Central symmetry centers a maximal ball at origin even when arbitrary centers allowed. Independently enumerated ALL integer potentials and tight connected subgraphs for n=3,4,5 in a separately written program, confirming exact maxima/contact counts; symbolic arithmetic checked n=4..60. This FINITE check is corroborative, NOT a replacement for unrestricted proof.

## originality

PASS

Best-of-knowledge original: searched actual Resultary and related published results, and materially read three original primary research papers and three closely related full Resultary theorems. Prior general facet/Lipschitz descriptions supply premises or aliases but not the crown-specific Euclidean maximum, the exact n=8 tie, or the complete nearest-facet count. The exact candidate mirror at Resultary is the SAME finding and is not independent prior coverage. Residual risk of an older graph-spread formulation remains.

## value

PASS

The crown graph K_{n,n} minus a perfect matching is a natural canonical highly symmetric non-complete bipartite family, and its Euclidean symmetric-edge-polytope inradius is an intrinsic geometric invariant in the prescribed root embedding, equivalent to a natural exact maximum-variance graph-spread fact. The deletion creates genuinely new diameter-three extremal potentials competing with balanced complete-bipartite cut potentials; the first and unique sharp switch at n=8, and the complete classification/number of nearest facets for every n>=4, are nonroutine structural results not an arbitrary tiny sample, cosmetic reparametrization or mere recomputation of a prior table. This exact fact could serve later study of graph spread, metric Lipschitz polytopes and symmetric-edge-polytope contact geometry. The claim is mathematically self-contained; no downstream theorem is required for its intrinsic value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
