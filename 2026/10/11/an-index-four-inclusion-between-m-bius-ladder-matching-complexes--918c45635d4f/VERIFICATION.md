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
# Finite certificate and reproduction

Execute `python3 verify.py` with standard Python 3.10+. The script constructs the fifteen edges of the ten-vertex Möbius ladder, enumerates all 344 faces of its ordinary matching complex and the 284 extendible-to-perfect-matching faces, and verifies there are exactly thirteen perfect matchings.

For each complex it constructs a deterministic edge-toggle discrete-Morse matching and verifies its acyclicity over every Hasse incidence (1045 for the ordinary complex and 835 for the perfect subcomplex). Removing the augmented pair containing the empty face leaves the appropriate single critical vertex. The perfect complex has two additional critical two-cells; the ordinary complex has six critical two-cells and four critical three-cells. The latter Morse boundary is explicitly recomputed and has a unit four-by-four minor.

The script then enumerates the relative signed boundary among the thirty nonextendible triangles and thirty nonextendible tetrahedra. It checks the signed incidence decomposition into ten unit blocks and two ten-by-ten signed cycles, computes their determinants exactly (each cycle has determinant -2), and verifies a unit nine-by-nine minor in each cycle. These assertions prove the two order-two relative homology summands and, with the two homotopy classifications, the index-four inclusion.

All integers and incidence signs are exact. No random trials, timeouts, external libraries or unverifiable computational oracle are used. The claim does not extend to larger Möbius ladders. An independent audit has not been performed.
