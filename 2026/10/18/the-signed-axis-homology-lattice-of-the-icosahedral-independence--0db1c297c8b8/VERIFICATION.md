---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The independent sets split into the clique sphere of the distance-two graph and six antipodal edges: every other vertex is adjacent to one endpoint of each antipodal pair. The distance-two graph is icosahedral, whose cliques are its vertices, edges and facial triangles. Attaching the six one-cells to a connected sphere gives the nonequivariant wedge. The only nonzero relative chain group for (X,S) is the integral oriented-axis group in degree one, and the pair sequence gives the claimed canonical H1 and H2 maps (not merely abstract ranks). I reconstructed the graph separately in exact golden-ratio coordinates, enumerated all independent sets and 120 automorphisms, and checked the signs on the six axes and on a coherent integral sphere cycle; replay python3 -B /workspace/audit_math.py 3. The rotation stabilizer is dihedral of order ten: its five involutions reverse the selected axis, giving the induced lattice and two negative fixed-axis contributions per involution; order three fixes none and order five fixes one positively. Odd-order rotations preserve spherical orientation and generate the rotations; the spherical antipode is free, giving degree -1. The two complex 3-dimensional constituents have conjugate character values and are exchanged by rational Galois action, so their rational six-dimensional form is irreducible. The original script was inspected, not executed.

## originality

PASS

Classical graph data and earlier exact neighborhood-complex results do not supply the natural integral signed-axis H1 lattice of the ordinary independence complex. The closest same-day entry permits selected edges and concerns a different complex. A distinct 2026-10-25 record states the exact equivalent integral result, including identification with the oriented-edge lattice; its later catalogue date is not evidence of earlier coverage, nor do these dates alone establish ultimate priority. The pass concerns the audited claim against verified earlier and same-day evidence, not present-day uniqueness.

## value

PASS

The natural symmetry of a standard polyhedral graph motivates its independence homology, and the canonical integral oriented-axis lattice supplies information not recoverable from a Betti count or abstract rational character. The sphere-relative identification gives a useful symmetry-respecting model without claiming an equivariant wedge splitting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
