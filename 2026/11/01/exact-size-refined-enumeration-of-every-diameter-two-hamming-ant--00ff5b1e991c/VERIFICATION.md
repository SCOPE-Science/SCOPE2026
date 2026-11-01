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

# Reproducibility and limits

Run `python3 verify_diameter2_anticodes.py` with Python 3.10 or newer. The program uses only the standard library. It directly enumerates all cliques of the distance-at-most-two Hamming graph by recursively choosing the smallest remaining vertex and restricting to later adjacent vertices; it does not use the support-classification counting argument. It compares complete cardinality histograms at 17 small parameter pairs, integer coefficient and edge-count identities at 140 parameter pairs, and the already known binary total-count formula at 20 parameters. The exact recorded stdout is `verify_diameter2_anticodes_output.txt`.

The symbolic proof, not these computations, establishes the formula for all integer \(q\ge2\), \(n\ge1\), and the fixed-alphabet asymptotic. The input size makes brute-force enumeration unsuitable for larger parameters; no inference from missing brute-force data is made. The existing OEIS binary count is treated as prior coverage, not an independent discovery. No external independent mathematical audit was performed.
