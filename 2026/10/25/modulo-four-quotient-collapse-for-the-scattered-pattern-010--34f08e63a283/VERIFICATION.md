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

# Reproducible finite verification

Run `python3 verify.py` in the directory containing this file. The program is independent of the proof narrative: it breadth-first enumerates reachable states, minimizes the resulting finite DFA by output-partition refinement separately for every residue, and independently counts subsequence index triples for all binary words up to length eleven.

Expected completion line: `VERIFY_OK moduli= 13 residues= 104 words= 4095 largest_reachable= 2197`.

This finite check validates its enumerated cases only. The universal quantifier over integers and the exact equivalence-class argument rely on the proof in RESULT.md. No independent mathematical audit has been performed.
