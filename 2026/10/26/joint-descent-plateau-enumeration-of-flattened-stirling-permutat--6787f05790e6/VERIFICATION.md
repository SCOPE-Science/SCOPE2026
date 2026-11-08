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

For each n>=1, the Buck–Elder–Figueroa–Harris–Harry–Simpson type-B partition bijection maps a distinguished zero block with z extra labels to a word of (d,p)=(0,1) when z=0, otherwise (1,z), giving Z=u+t(exp(ux)-1). A nonzero block pair of s absolute labels, normalized with its smallest absolute label positive, has q negative and s-q positive entries; its word f(N)g(P) has (d,p)=(0,1) for s=1, and for s>=2 the mutually exhaustive classes q=0, q=s-1 and 1<=q<=s-2 contribute t*u^(s-1), t*u^s and binom(s-1,q)*t^2*u^(s-1), respectively. Counting signs gives the factor 2^(s-1)-2. The canonical order of blocks makes every interblock adjacency a strict ascent; thus no boundary plateau/descent and the labeled SET exponential formula proves Z*exp(W) over Z[t,u][[x]] for all n. The x^(n-1)/(n-1)! index shift and 2n-1 internal comparisons are correct; n=1 gives H1=u. Independent exhaustive insertion enumeration of all (2n-1)!! Stirling permutations for each 1<=n<=8, filtered by weak-run starts, matched the independently derived signed-block polynomial recurrence in every (d,p) cell (totals 1,2,6,24,116,648,4088,28640); at n=4 the five coefficients match RESULT.md. At u=1 algebra yields exactly Shankar Corollary 10; at t=u=1 the total EGF is exp(x+(e^(2x)-1)/2). The infinite proof comes from the bijection plus local weights, not finite checks.

## originality

PASS

Best-of-knowledge originality of the all-order simultaneous internal-descent/internal-plateau enumerator on flattened 2-Stirling permutations. Shankar 2023 gives only the u=1 descent marginal and expressly asks in Section 7 item 4 for the joint ascent/plateau distribution. Buck et al. give the requisite bijection but not the joint marked species. Ma–Ma–Yeh 2019 concerns all Stirling permutations, Ma–Liu–Yeh–Yeh 2025 concerns the distinct singleton-minimum class; Baril–Ramírez 2026 concerns ordinary distinct-letter flattened permutations. Actual Resultary queries found no dominating same-object result, but search noncoverage does not establish priority. The proof refines prior block decomposition with a separate plateau marking; the established bijection, totals, and descent marginal are excluded from the novelty claim.

## value

PASS

A natural and previously explicitly requested joint distribution for flattened 2-Stirling permutations is determined at all sizes, not just another marginal or finite table. It gives every descent–plateau covariance and mixed moment, with equivalent joint ascent–plateau statistics and consistency with the known descent EGF and Dowling totals. This is a specific nonroutine bivariate enumeration motivated by Shankar’s Section 7 question 4. The paper-sized k>2 extension is not proved or required; significance is narrow because the base bijection and univariate EGF are prior art.

The dated certificate retains the supplied scientific assessment, sources and limitations.
