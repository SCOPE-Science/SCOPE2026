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

The exact standard-library checker `verify.py` constructs the graph, the unordered two-particle cubical cells, the signed incidence matrices, every hexagon product torus, and the complete full-automorphism action. It verifies characteristic-three pivot ranks 90 and 154 for the two cubical boundaries, rank 14 for the 42 two-torus cycles, and all exact cellular Lefschetz traces. It computes the complete character pairings for all 336 group elements.

Execute `python3 verify.py`; the recorded completed run is in `verification_output.txt`. The calculations prove ranks over the rationals using lower/upper certificates, but not integral lattice saturation or a canonical representation splitting. Independent external audit has not been performed.
