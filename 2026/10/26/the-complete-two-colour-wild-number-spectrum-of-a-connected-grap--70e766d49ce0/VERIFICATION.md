---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Anders et al established the two-color identity wld=κ(R)+κ(B)-2=2(n-1)-r(R)-r(B). Maximizing r(R)+r(B) over surjective colourings gives the rank r_2(E) of two-union graphic matroid: choose two disjoint maximal forests, then color any extra edges freely without reducing ranks; even if one forest initially empty two independent edges ensure surjectivity. Edmonds matroid union yields min wld=max_(A subset E)[2(κ(A)-1)-|E\A|], equal to D(G) by both directions using component partitions and edge sets internal to a vertex partition. The binary cycle-space identity lambda(S)=dim Z(E)-dim Z(S)-dim Z(E\S) forces lambda=0 iff every simple cycle is monochromatic, equivalent to constant color per cycle-edge-block; the count is 2^b-2 and if b=1 one-edge-red achieves n-2. Surjective hypercube edge subsets are connected by one toggle for m>=3; each toggle changes wld by at most 1, so the set of attainable integers has no gaps. m=2 is the 3-vertex path with value 2. Independent exhaustive checks of connected labelled graphs n=3,4,5 and representative n=6 graphs agreed.

## originality

PASS

Earlier wild-number work supplies the fixed-coloring identity, and complete/bipartite-graph specialists give restricted spectra. Matroid union supplies the lower endpoint mechanically but not the cycle-block upper endpoint, the exact extremal count or gap-free interpolation over arbitrary connected graphs. The combination is assessed as qualified original mathematics.

## value

PASS

Classifying the entire value spectrum, the cycle-block dichotomy of its maximum and the exact multiplicity of extreme colorings for every connected graph constitutes a useful structural invariant and sharp all-graphs extension of prior special families. Minimum deficiency and its tree-packing corollary are acknowledged classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
