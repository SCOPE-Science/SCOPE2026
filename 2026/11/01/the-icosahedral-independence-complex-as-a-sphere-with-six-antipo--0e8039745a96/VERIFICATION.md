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

# Verification scope

Run `python3 verify_icosahedral.py` using the standard Python interpreter. The program reconstructs the graph from the displayed six edge families; enumerates the complete simplicial complex; checks the explicit distance-two graph isomorphism and all twenty spherical triangles; checks each vertex link and an integral orientation cycle; enumerates all graph automorphisms without an external package; and computes their signed actions on the six antipodal chords and the two-sphere fundamental cycle.

It reports \(12,36,20\) nonempty simplices by size; thirty distance-two edges and six antipodal edges; a triangulated sphere with twelve five-cycle links; exactly \(120\) automorphisms. For orientation-preserving elements it gives the order/trace/count triples \((1,6,1)\), \((2,-2,15)\), \((3,0,20)\), \((5,1,24)\). Inversion multiplies the homology trace values by \(-1\). Independent modular calculations of boundary ranks \(11,19\) in characteristics \(2,3,5,101\) provide finite consistency checks.

The proof of integral homology uses an explicit sphere with six one-cells and the long exact sequence, not the modular ranks; a finite list of characters does not by itself certify the homotopy claim. The proof of the fundamental-group outer action uses homotopy uniqueness of connecting paths in the two-sphere. All computations and unproved limitations are given in `RESULT.md`. No independent mathematical audit has been performed.
