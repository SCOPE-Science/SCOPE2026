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

The supplied `verify.py` is a standalone Python standard-library program. It constructs the precise 5-regular Clebsch graph and its neighborhood complex, checks the face vector, derives rational boundary ranks by combinatorial block splitting and exact mod-two elimination, and verifies all 1920 homology character values by three combinatorially independent formulas. It checks the Fourier multiplicities and quotient invariants. The recorded deterministic output is `verify_output.txt`.

All computations are exact finite computations; the assertions about all group elements hold because every element of the specified finite group is enumerated, not sampled. The proof does not establish the integral representation lattice or any generalization to other graphs. No independent mathematical audit has been performed.
