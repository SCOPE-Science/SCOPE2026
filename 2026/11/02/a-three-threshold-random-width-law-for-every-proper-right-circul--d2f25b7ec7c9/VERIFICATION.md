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

# Computational and analytical verification

The exact CDF comes from two monotone interval contributions of the uniform absolute axial cosine. The global extrema and contact thresholds follow direct one-dimensional monotonicity and algebraic identities; no numerical optimization is used in the proof.

The embedded `verify.py` evaluates 150 distribution thresholds on a deterministic 300,001-point cosine grid for each of nine geometries across all three regimes. It confirms the CDF within the deterministic sampling error, computes the predicted extrema and checks the integrated expectation. Every sample is finite and therefore only corroborative: it is not a certificate for all possible parameters.

Reproduce with `python3 verify.py` using NumPy. The comparisons do not require access to external documents. Independent validation has not been performed.
