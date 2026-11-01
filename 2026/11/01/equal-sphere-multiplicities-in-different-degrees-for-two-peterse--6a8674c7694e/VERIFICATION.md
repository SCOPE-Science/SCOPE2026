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

# Finite verification

Run `python3 verify.py` from the directory containing this file. Python 3's standard library suffices; no installed mathematical packages and no network connection are required. The edge and vertex labeling, both complete pivot orders, and the finite assertions are embedded in the script. Successful output must reproduce `verification_output.txt` exactly and conclude `VERIFY_OK`.

The program performs independent hereditary insertion and exhaustive cardinality-bounded subset tests for the induced-matching condition, confirms that no seven-edge induced matching exists, verifies the antipodal Petersen quotients including multiplicities, and checks complete directed-Hasse acyclicity for the stated sequential-toggling pairs. It computes independent mod-two simplicial boundary ranks. Counts of faces, matched pairs, remaining critical-cell sizes, Hasse incidences and mod-two Betti vectors are checked by explicit assertions. These computations are exact and exhaustive for the two graphs; the integral homotopy statement uses the mathematical discrete-Morse collapse-to-CW argument rather than a mod-two calculation. The work makes no general inference about all generalized Petersen graphs or arbitrary double covers.
