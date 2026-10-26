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

Run `python3 verify.py` from the directory containing `verify.py`. The program uses only Python's standard library. It independently generates every vertex subset of each crown graph for the six integer parameters \(3\le n\le8\), computes distances using breadth-first search, and directly tests all vertex triples. It also enumerates the inclusion-maximal sets and verifies the exact polynomial coefficients. The standard output is provided in `verify_output.txt`. The program checks the cubic and quartic excess in the formula printed in the 2024 article as a separate arithmetic comparison.

All listed finite checks passed on the packaged executable. The unrestricted proof is deductive and does not rely on these finite experiments; no claim of independent or formal certification is made.
