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

## Reproducibility

Run `python3 verify_sierpinski.py` under Python 3.8 or later, using only its standard library. The script checks direct first-difference adjacency against a separately generated adjacency representation, the proposed minimum sets against the literal domination and capacity definitions, the structure of quotient cliques and linking edges, and selected small cases by exhaustive subset enumeration. The recorded output is in `verification_output.txt`.

Checks: 16 graph-adjacency comparisons; 75 construction/capacity parameter cases; 12 quotient/link comparisons; and 22 exhaustive minimizations examining 198,420 subset masks. All assertions passed. Finite verification cannot establish the universal theorem; the proof in `RESULT.md` is required for that conclusion. All file-local dependencies of the verifier are standard library imports. No independent audit has been performed.
