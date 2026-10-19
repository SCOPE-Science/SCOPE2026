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

# Reproducible finite checks

Run `python3 verify_generalized_petersen.py` and `python3 verify_cover_independent.py` with Python 3.9+ from the extracted file directory. Both use only Python standard libraries, print the same sorted JSON (recorded in their corresponding `.out` files), and finish `VERIFY_OK`. The former explores all matching edge subsets and tests every replacement and graph distance; the latter resolves uncovered vertices, tests unmatched-vertex independence, and constructs exchanges from common retained partial matchings. Exact output gives size counts 5, 120, 1620, 1120, 60; layer-edge counts 0, 120, 3360, 2160, 0; component-size distributions 5 singletons, 30 four-vertex components, one 1620-vertex component, one 1120-vertex component, and 60 singletons. Exact connected-component diameters are 2 for the thirty 4-cycles, 14 at size eight, and 12 at size nine. Independent enumerators use structurally different encodings of the Desargues graph.

This verifies a finite exact statement only. Termination and exhaustive search logic, rather than statistical samples or a timed cutoff, establish completeness. Originality is assessed against inspected literature and indexed results and does not constitute independent certification.
