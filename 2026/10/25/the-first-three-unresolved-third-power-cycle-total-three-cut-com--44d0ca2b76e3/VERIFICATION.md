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

The executable certificates use only the Python standard library. Running `python verify_morse.py morse_certificate.json` constructs all faces of the total three-cut complexes of the third powers of the cycles with 13, 14 and 15 vertices; repeats their stagewise element matchings; checks exact critical faces and pairs; and checks acyclicity by an exhaustive topological sort of all face-poset covering relations. The expected counts and chosen vertex orders are recorded in `morse_certificate.json`, while `verify_morse_output.txt` records the actual successful execution.

An independent computation, `python verify_mod2.py`, enumerates the faces afresh as vertex tuples and calculates all simplicial boundary ranks over the field with two elements. Results and complete face vectors are in `verify_mod2_output.txt`. This second computation does not prove integral homotopy on its own; the discrete-Morse proof supplies that conclusion.

The strongest claim is restricted to the three graph orders 13, 14, and 15 and depends on the complete, finite certificate reconstruction. No generalization to other orders is inferred from finite experiments. Independent scientific audit has not been performed.
