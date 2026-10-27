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

# Verification and limits

Execute `python3 verify.py` from the directory containing this file. The script uses only the Python standard library and requires no external datasets.

The program enumerates finite minima subsets and direct ideal/common-neighborhood counts for all chord locations at sizes \(5\le n\le13\), comparing against the closed formulas. For \(n=5,6\) and the eight-point witness it additionally enumerates all three-way new-element comparability assignments and checks pair constraints independently. It checks reflection symmetry, strict recovery, both infinite-family formulas over the tested sizes, and the small collision; `checks.txt` contains its reference output.

The general statements are proved in `RESULT.md`. Exhaustive finite tests do not establish claims for unbounded \(n\), publication originality, or independent verification. Formal proof-assistant certification was not performed.
