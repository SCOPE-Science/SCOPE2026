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

# Verification

Run `python3 verify_three_sun_morse.py` with standard Python 3. Its exact, exhaustive checks comprise two independent face generators, 1,444-face equality, the entire 708-pair acyclic discrete-Morse matching, the complete 5,388-incidence Hasse DAG, mod-two boundary ranks, and an independent fraction-free determinant of \(I-L\). It verifies the absence of a complete source and of a Jojić dominant pair, and failure of the complete-multipartite hypothesis.

The output file `verification_three_sun_output.txt` records the actual successful execution. The homotopy conclusion uses the acyclic matching and its critical-cell vector; numerical homology calculations alone would not prove a wedge decomposition. This is a finite check for the specified graph only. No external or independent audit is claimed.
