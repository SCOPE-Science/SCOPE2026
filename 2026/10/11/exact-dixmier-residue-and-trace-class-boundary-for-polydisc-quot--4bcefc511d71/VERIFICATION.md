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
The accompanying `verify_endpoint.py` checks rational equalities for the rank-two block trace, determinant, Hilbert–Schmidt energy, and the exact finite telescoping sum at the trace-class endpoint. It computes finite reordered singular-value lists across several dimensions, transverse multiplicities and rational squared overlaps. The invocation `python3 verify_endpoint.py` completed successfully and printed `QUOTIENT_ENDPOINT_BLOCK_CHECK_OK`.

The infinite-dimensional theorem follows instead from the proof in `RESULT.md`: unitary layer construction, exact rank-two eigenvalues, counting-function inversion, logarithmic summation, and Schwarz's equality case. Finite spectral probes are not proofs of limiting statements. The supported sources identify the base quotient model; this computation is a new endpoint analysis of that model. No independent audit has been performed.
