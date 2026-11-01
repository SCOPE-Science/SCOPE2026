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

The `verify.py` program enumerates all matching faces on the 15 edges, computes all four exact rational simplicial boundary ranks and every chain equation, constructs quotient homology in degree three, and evaluates the full action for all 120 permutations of the five underlying symbols. Degree-two characters are reconstructed using the signed simplicial Lefschetz trace. Recorded stdout is embedded as `verify_output.txt`.

Execute `python verify.py` using Python 3 with SymPy. Success prints `VERIFY_OK`. These finite computations are exhaustive for the exact Petersen graph; no statement is made about other graphs or integral torsion. Independent audit has not been performed.
