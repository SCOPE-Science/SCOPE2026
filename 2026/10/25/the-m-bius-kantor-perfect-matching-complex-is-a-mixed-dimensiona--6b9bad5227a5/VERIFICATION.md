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

# Verification of the Möbius–Kantor perfect-matching homotopy type

Run `python3 verify_mobius_kantor_perfect_matching.py`, requiring only Python 3.9 or later, beside the supplied verifier. The finite computation reconstructs all graph edges and perfect matchings, all 6051 nonempty simplices, and their 27192 face incidences. It checks the 3019-pair discrete-Morse matching and a complete acyclic topological sort. The exact integral signed projection computes a zero four-by-eight Morse differential, establishing all eight nullhomotopic three-cell attachments once the missing critical one-cells establish simple connectivity.

The checker independently computes mod-two simplicial boundary ranks `(23,205,775,1059,693,231,33)`, and independently enumerates ordinary matchings to verify that 5016 are nonextendible with 112 minimal three-edge and 120 minimal four-edge obstructions. The executed output is retained in `verification_output.txt` and terminates with `VERIFY_OK`.

These exhaustive checks constitute a finite proof for the specified 16-vertex graph, not a claim about general graph families. Mod-two ranks alone would not certify integral torsion or attaching maps; the integral gradient-path computation supplies the necessary homotopy certificate. Independent scientific audit has not been performed.
