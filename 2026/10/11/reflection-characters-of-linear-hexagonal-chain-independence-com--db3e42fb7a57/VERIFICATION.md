---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

PASS: The graph G_n is explicitly two rails j=1..2n+1 and rungs at odd columns. Involutions h(row exchange), v(end reversal), hv commute and preserve edges. For each automorphism, reject vertex orbits containing an edge, then graph Q_g connects conflicting orbits. Fixed independent faces correspond exactly to independent orbit sets, and orientation parity of 2-cycles yields reduced Lefschetz trace -I(Q_g;-1); with Chandrakar-Singh full Theorem 3.1 non-equivariant Ind(G_n)≃S^n∨S^n, the top trace is (-1)^(n+1) I(Q_g;-1). h quotient has n isolated vertices =>0. Even n=2k: v quotient G_k =>2(-1)^k, while hv has an adjacent-supported leaf pair =>0. Odd n=2k+1: v has leaf-pair cancellation =>0, hv quotient G_k plus triangular cap =>2(-1)^(k+1), with n=1 triangle explicitly checked. Character decomposition gives two one-dimensional rational sign reps. Independently built orbit graphs for n=1..12 and directly orientation-signed enumerated original fixed faces for n=1..4; all 64 targeted checks matched, but finite checks are not the all-n proof.

## originality

PASS

PASS, best of knowledge: Chandrakar-Singh arXiv:2512.21318v1 proves only Ind(H_1x1xn)≃S^n∨S^n and computes no automorphism characters. Same 2D homology size permits multiple inequivalent Klein-four representations, so the source does not imply these trace signs. Jonsson 2010 treats cross-cycles in periodic quotient hex grids, not these finite linear chains; Moci-Pezzoli treats matroid rather than graph independent-set complexes. Resultary top self-hit excluded as prior and other equivariant examples concern different graphs. Accessible Jonsson abstract only, explicit residual risk retained.

## value

PASS

PASS: Exact all-n rational reflection character refines a non-equivariant wedge decomposition by distinguishing which reflection fixes the two homology generators depending on n mod 4. This is a motivated structural representation invariant of the natural geometric symmetries, not a pure rephrasing of rank two homology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
