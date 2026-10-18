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

# Verification scope

Execute `python3 theta_general_checker.py` using a standard Python 3 interpreter from a directory containing that standalone file; no external libraries are needed. The program explicitly enumerates all orientations of nine finite generalized-theta graphs, computes acyclicity, checks reachability after directed-edge deletion, and verifies that the coefficient polynomial and smooth-orientation descriptions agree on each instance. A successful run ends in `VERIFY_OK`.

The complete proof of the infinite parameter family is the symbolic argument in `RESULT.md`, not the numerical checks. No independent audit, external proof-assistant certification, or claim of exhaustive testing over all lengths is represented.
