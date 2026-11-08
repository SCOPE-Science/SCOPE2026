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

# Reproducibility

Run `python3 verify.py` in the same directory as this file, using Python 3.9 or later; no nonstandard packages or external network resources are needed. The exact expected stdout is in `verification_output.json` (one JSON object per line, with a final newline). The verifier independently builds the Petersen and line graphs, checks the odd-scale ball-center witness condition, enumerates 2141 simplices, computes the full face vector and simplicial boundary ranks over \(\mathbb F_2\), and executes two complete 1059-pair acyclic discrete-Morse matchings. All 8955 incidence orientations are topologically sorted in each matching. No integer homology is inferred from finite-field ranks: the one-critical-vertex/21-critical-three-cell Morse cell structure supplies the integral homotopy proof. A separate human or external validation is not represented as having occurred.
