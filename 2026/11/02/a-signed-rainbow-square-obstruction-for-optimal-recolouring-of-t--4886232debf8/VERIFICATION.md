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

# Reproduction and scope of verification

Run `python3 chvatal_verifier_a.py` and `python3 chvatal_verifier_b.py` on Python 3.9 or later; both use only the Python standard library. They specify the full 24-edge graph from scratch and do not require external data, historical files, any network service, or scientific packages.

The first program enumerates all proper named four-colourings by induction over the vertex order, rejecting every improper partial assignment, and additionally rejects all three-colour assignments. It generates every one-vertex recolouring, verifies that all 64,320 edges preserve the signed 11-cycle invariant and that exactly two connected 9,012-vertex sectors occur. The eight displayed symmetry maps are independently verified, and shortest-path eccentricity calculations from all 108 joint symmetry orbits establish the exact radius, diameter, and eccentricity distribution.

The second program enumerates ordered independent-set partitions (a fundamentally different completion algorithm), assembles legal recolourings via coordinate-deletion buckets rather than neighbour scans, independently finds both sectors, and enumerates all proper Hamming-distance-two crossing pairs. It verifies 11,616 crossing pairs and one explicit proper pair; this proves two-vertex reachability when combined with within-sector connectedness.

The programs were actually executed and all assertions passed in their exact packaged form. This is a finite exhaustive verification, not proof of a universal theorem about all graphs. Five-colour connectivity follows from the cited published theorem, not from an unperformed exhaustive enumeration of five-colour states. Independent scholarly validation has not been performed.
