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
# Finite verification and proof dependencies

Run `python verify_ladder.py` with Python 3, NumPy and SymPy (versions given in `requirements.txt`). An actual execution on the embedded program returned `ALL_CHECKS_PASSED 1124`. The program checks exact gcds of the two shifted path characteristic polynomials for 49 sizes, independent adjacency spectral projection calculations for 20 sizes, every vertex, and several strictly positive sink rates. No external files are needed. The finite scope is not confused with an exhaustive proof: the universal result uses the Ramanujan-sum equality case and the dissipative spectral argument written in `RESULT.md`.

The prior-work assessment is bounded by the accessible four full-text primary papers and the listed research-record searches. A broader graph-observability theorem may subsume the special case; independent audit is not claimed.
