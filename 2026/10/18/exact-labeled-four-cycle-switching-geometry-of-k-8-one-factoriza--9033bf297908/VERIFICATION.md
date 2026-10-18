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

# Reproduction of the finite result

Two self-contained standard-library programs are provided: `verify_matchings.py`, enumerating perfect matchings then exact covers, and `verify_coloring.py`, assigning the opponent of team zero to each factor and testing all four-vertex alternating switches. Execute `python3 verify_matchings.py .` in a writable directory and `python3 verify_coloring.py`. Both recompute every edge and shortest-path eccentricity rather than trusting the saved output.

`factorization_states.txt` contains 6240 lines of seven sorted hexadecimal masks; mask bits index the lexicographically ordered 28 unordered edges on teams 0 through 7. `fourcycle_edges.txt` has 17640 sorted distinct pairs of 0-based row indices. The programs independently yield the SHA-256 digests `544c02ebaa1e834f533f4e04aa3b8524b517d46fbc5900c8d72d43e70e36e9f3` and `278543195bffe9e837bb1ed4358cc87cabb4b2ac7929b06a24e6c4bcbc253c4a`, respectively. Their recorded standard outputs agree byte-for-byte, with component sizes and eccentricities as in the theorem.

Both programs were run on the actual supplied source paths and the saved output and certificate files checked. All cases are finite and covered, including the exact enumeration of 105 matchings and all 6240 factorizations. A third-party reproduction and literature priority examination have not occurred. No conclusion about larger complete graphs follows.
