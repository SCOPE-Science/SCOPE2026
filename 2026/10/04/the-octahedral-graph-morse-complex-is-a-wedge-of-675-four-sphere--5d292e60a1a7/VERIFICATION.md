---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

`verify_octahedral_morse.py` reconstructs the octahedral graph \(O=K_{2,2,2}\) from the missing perfect matching \(\{01,23,45\}\). It enumerates every possible graph discrete vector field by choosing at most one outgoing edge at each vertex, rejects repeated underlying edges and directed cycles, and therefore reconstructs the full ordinary Morse complex from its definition.

The replay requires the nonempty face vector \((24,228,1072,2496,2304)\). It then builds the deterministic face-poset matching, reconstructs every Hasse cover relation, reverses exactly the matched edges, and topologically sorts the resulting directed graph. The sort must visit every nonempty face; this is the exhaustive certificate that the matching is acyclic. The unmatched cells must consist of one \(0\)-simplex and \(675\) \(4\)-simplices.

As an independent consistency check, the script constructs all simplicial boundary matrices over \(\mathbb F_2\) and requires ranks \((23,205,867,1629)\), giving Betti vector \((1,0,0,0,675)\). It also checks Euler characteristic \(676\).

A successful run ends with `VERIFY_OK`. The finite replay establishes the complete combinatorial matching certificate for this graph; the final homotopy inference uses the standard discrete-Morse theorem stated in the cited literature.
