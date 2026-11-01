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

The mathematical verification is finite and exhaustive for exactly the stated parameters \(3\le n\le7\). The standalone `verify.py` generates the complexes directly from their forbidden triples, verifies all face counts and acyclic gradient matchings, and recomputes all integral signed Morse differentials and Smith forms. It also computes mod-two ranks from the original simplicial boundary operators, independently of the Morse pairing. Python with SymPy (see `requirements.txt`) is required; run `python verify.py` and check the final `ALL_VERIFY_OK` line. The wedge conclusion additionally uses the standard discrete-Morse CW theorem and the fact that attaching maps from a sphere of dimension \(d\ge2\) to a wedge of \(d\)-spheres are classified by degree vectors. No homotopy statement for larger parameters or equivariant splitting is established. Independent mathematical audit has not been performed.
