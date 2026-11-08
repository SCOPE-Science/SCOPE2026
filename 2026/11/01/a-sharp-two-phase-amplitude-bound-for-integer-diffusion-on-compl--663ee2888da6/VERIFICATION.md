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

For synchronous sign-comparison diffusion, the signed edge-flow sum across an x→y→x pair is divergence free. Pairing with x+y expresses zero as a sum of nonnegative edge terms, forcing every edge to be tied in both phases or reverse strictly between phases. On K_{a,b}, reversing integer gaps and degree-sum a+b bounds cross-shore gaps by H=a+b−1 at either phase. Normalize minimum over both phases to zero. For a left-shore minimum, its right neighbours and phase changes are bounded by H and b; splitting other left vertices at value H gives all two-phase labels ≤H+b−1; exchanging shores gives H+a−1. Thus maximal span ≤a+b+max(a,b)−2. For a≤b the left labels (0 repeated a−1,H−1) and all right labels H update to left (b repeated a−1,H+b−1) and right (b−1 repeated b), then reverse, attaining upper bound. All sizes ≥2, ties and arbitrary translated labels covered. Independent finite integer-state enumeration for K_2,2 and K_2,3 confirmed widths 4 and 6; not extrapolated to all parameters.

## originality

PASS

Best-of-knowledge original feature is the exact two-phase recurrent amplitude a+b+max(a,b)−2 for complete bipartite graphs with both parts ≥2, not edge sign potentials or period-two classification generally. The same-model Duffy et al theorem establishes eventual periodicity but its width bounds depend on a chosen initial configuration; Long/Narayanan restrict possible periods on all finite graphs; Carlotti/Herrman bound a starting chip floor sufficient for nonnegativity. None of these quantified statements implies a sharp maximum over all primitive two-cycles and both phases after translation. The Resultary same-object query returned integer height-function ranges (different dynamics) and no dominating recurrent-width theorem. Indexed absence is not novelty proof.

## value

PASS

The exact maximum span over two recurrent configurations gives the smallest global translation-normalized integer alphabet needed for the entire period-two recurrent set of K_{a,b}, independent of arbitrary initial chip counts. This is an intrinsically motivated finite cutoff enabling finite classification of recurrent orbits on a canonical dense bipartite network. The sharp attained law is not a table of hand-picked small states, nor a routine consequence of eventual-period ≤2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
