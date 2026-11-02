---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For all real cyclic x,y, use the exact continuous piecewise-linear median-selector representation. On strict chambers P1=1; variations of arc indicators are extreme modulo constants because a zero-sum cyclic gradient decomposes into positive linear combinations of e_p-e_q. Thus each selector norm is the maximum number of connected components of its preimage of an arc. A 3-local selector creates at most three such components, at most two for n=4,5, and zero for n=3 because every window equals the whole 3-cycle. Explicit strict-order and arc witnesses realize 2 or 3 for every admissible n (n>=7 uniformly). Separately threshold coarea proves the one-input TV contraction, not the two-input result. Independently reconstructed all strict selectors and cyclic arcs for n=3..7, obtaining max 0,2,2,3,3, and checked unequal-total-variation attaining pairs n=4..7; finite checks do not establish the n>=8 bound.

## originality

PASS

The sharp ratio measures V(Tx-Ty)/V(x-y), not classical V(Tx)/V(x) or pointwise median continuity. No inspected primary result or published semantic-search hit implies this full periodic n-dependent two-input theorem. Novelty is best-of-knowledge and the 1994 smoothing source full text remains unavailable.

## value

PASS

This exact operator norm measures stability of variation under small differences in two filtered signals, a natural robustness invariant despite each individual signal losing variation. It locates first sharp saturation at six samples and explicitly separates nonlinear two-input amplification from one-input smoothing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
