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

# Reproduction and finite-computation limits

Use `python verify.py` alongside `witnesses.json` with Python 3, NumPy and SciPy/HiGHS. This verifies each of the eight explicit codebooks against all 64 received words, confirms the incidence matrix from every codeword deletion agrees with the independently generated matrix from receiver insertions, and optimizes each finite 0–1 problem to a proven integer optimum. It also recomputes both list-one and list-two optima for all shorter lengths, tests eight VT syndrome classes, and prints `VERIFY_OK` on success.

Successful local replay was observed with SciPy 1.17.0 and NumPy 2.3.5. The solver is constrained to report completed optimal termination and tight primal/dual bounds; a timed-out feasible incumbent cannot pass. Solver completion verifies these *finite* integer upper bounds assuming the correct operation of the MIP backend. There is no independently machine-checkable MILP search-tree certificate, no proof for arbitrary length, and no external independent audit.
