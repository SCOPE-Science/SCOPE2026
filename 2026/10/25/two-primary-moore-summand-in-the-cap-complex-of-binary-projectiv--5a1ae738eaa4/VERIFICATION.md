---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Independently enumerated all 35 XOR-line triples on labels 1..15 and every one of 32767 nonempty subsets: exactly 3048 permitted faces and f-vector (15,105,420,945,1008,420,120,15), with 168 maximal 5-caps and 15 maximal 8-caps in the source. Reconstructed the full greedy coordinate-toggle matching of 1484 incidence pairs and topologically sorted all 13770 incidence arcs on 3048 cells (acyclic). Critical cells are one 0-cell, one 3-cell (mask 534) and 78 4-cells. Computed signed gradient-path projection to the unique critical 3-cell independently: the integer Morse attaching row has 15 entries -2, 44 zeros and 19 entries +2, gcd 2. A CW complex with those critical cells is a 3-sphere plus 78 4-cells attached by integer degrees; unimodular column reduction leaves degree-2 Moore attachment and 77 null attaching maps. Therefore the claimed integral homotopy type follows, not just its mod-two Betti numbers. This finite calculation is exhaustive by bounded 15-point domain.

## originality

PASS

Qualified PASS: the earliest known binary-projective cap studies address admissible sets, cap sizes and saturating geometry, while a highly relevant 2017 thesis computes topology of complexes Cp(2,2), Cp(2,3), and Cp(3,3), not the 15-point Cp(3,2) integral Moore homotopy type. Its framework defines precisely the same type of complex but does not state a theorem covering the precise result; non-indexed equivalent computations remain possible.

## value

PASS

PASS: the line-free-subset complex of the smallest nontrivial binary projective three-space is a canonical combinatorial-topology object. Its complete integral homotopy type separates genuine degree-two Moore torsion from a wedge-of-spheres guess, a precise non-routine invariant relevant to cap-complex/Steiner-system topology; the certificate is finite and self-contained and needs no speculative infinite-family claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
