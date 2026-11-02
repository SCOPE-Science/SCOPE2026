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

# Exact verification of the dodecahedral perfect-matching calculation

Run `python3 verify_dodecahedral_pm.py` in a standard Python 3 interpreter from the package root. No nonstandard Python dependencies, network access or external downloaded input is required. To regenerate the certificate, run `python3 verify_dodecahedral_pm.py --emit-certificate certificates/morse_boundary.json`.

The checker reconstructs the graph and exactly 36 perfect matchings, enumerates 30,503 nonempty faces, verifies the face vector, and creates 15,231 disjoint Morse pairs. It visits all 163,650 nonempty Hasse incidences and all 30,503 vertices of the directed face-poset graph, proving global acyclicity.

It reconstructs the signed integral ten-by-thirty Morse attaching matrix and verifies that it has 69 entries in \(\{-1,1\}\). Bitset elimination gives rank nine modulo two. Bareiss elimination computes the nine-by-nine minor \(-1\) on zero-based rows \((0,2,3,4,5,6,7,8,9)\), columns \((0,2,4,5,6,7,8,11,26)\), and ten-by-ten minor \(2\) on all rows, columns \((0,2,4,5,6,7,8,10,11,26)\). The three facts imply exactly nine Smith units and one factor two; this is an integral certificate, not an inference from modular ranks alone.

Independent elimination of the original simplicial complex over \(\mathbb F_2\) gives boundary ranks in degrees one through nine \((29,346,1833,3936,4416,3024,1296,324,36)\). This yields mod-two homology ranks one in degrees zero and two, twenty-one in degree three, and zero otherwise, consistent with integral \(\mathbb Z/2\) in degree two and free \(\mathbb Z^{20}\) in degree three.

Expected successful marker: `DODECAHEDRON_PERFECT_MATCHING_MOORE_2_TORSION_20_S3_OK`.

**Limits:** The code directly verifies finite combinatorial and integer linear-algebra assertions. The passage to the asserted homotopy equivalence uses Forman's discrete-Morse theorem, Hurewicz for the simply connected two-skeleton, and standard integral basis changes of three-cell attaching maps. Those mathematical steps are stated in `RESULT.md`. No independent scientific audit has yet been performed.
