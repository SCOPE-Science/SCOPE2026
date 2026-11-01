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

# Verification of the powered-distance threshold

The proof is analytic. The standalone `verify_hypercube_line_negative_type.py` checks separate, finite consequences: direct cube-edge incidence construction, all-pairs BFS distances in the line graph, agreement of those distances with the endpoint-Hamming formulas, and complete dense spectral agreement with the Walsh sector formulas. The checker compares five real exponents for every dimension from two through five (twenty matrix spectral tests) and confirms root equations through dimension twelve.

Command executed from a folder containing the standalone script:

`OPENBLAS_NUM_THREADS=1 python3 verify_hypercube_line_negative_type.py`

Observed completion marker:

`CUBE_LINE_POWERED_DISTANCE_OK 20 independent BFS/Gram spectral comparisons; n=2..12 roots`

The checker requires Python 3 and NumPy; it does not require a separate external dataset. Its numerical tolerances cannot prove an infinite family or historical originality. Those conclusions rest on the explicit Walsh-block identity, Bernstein integral inequality, strict eigenmode comparison and binomial concentration proof in RESULT.md. Independent external validation was not performed.
