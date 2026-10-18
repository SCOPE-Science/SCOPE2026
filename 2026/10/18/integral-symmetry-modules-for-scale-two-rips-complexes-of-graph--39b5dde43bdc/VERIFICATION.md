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

Two Python 3 standard-library programs are included. `verify_total_graph.py` enumerates 856 connected graph instances, and checks exact graph-square distances, maximal exceptional edge-only triangles, the contractible-link core deletion formula, integral octahedral cycle boundaries, unique exceptional coordinates, and reduced mod-two homology. `verify_equivariant.py` recomputes all simplicial chain Lefschetz traces for the full symmetric groups of orders 6, 24, 120, and 720 and checks them against the signed oriented-three-subset character, independently of the cycle construction. Output files are `verification_output.txt` and `equivariant_output.txt`. A reproducible run is `python3 verify_total_graph.py` and `python3 verify_equivariant.py` from the directory containing both programs. No third-party packages are needed.

These checks are finite; they do not prove any universal quantifier. The general proof is the explicit relative cellular decomposition and canonical signed integral cycle section in `RESULT.md`. Independently reviewed or machine-formally certified proof is not claimed.
