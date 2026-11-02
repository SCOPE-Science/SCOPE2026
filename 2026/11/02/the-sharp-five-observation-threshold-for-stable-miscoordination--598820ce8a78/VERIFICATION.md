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

Run `python check.py` in a working directory containing the accompanying standalone script. Its only third-party dependency is `sympy`; Python 3.10 or newer is suitable.

The checker constructs each binomial response polynomial directly, compares normalized drift factors for three representative no-tie payoff regions, symbolically proves the factorization of the two/five-sampling flow, reconstructs the exact saddle-node threshold and the critical points of its cubic, and independently tests exact sign values at 999 rational points. On execution it reported `PASS 1021 symbolic/finite sign checks`, the explicit radical critical fraction, and both numerical interior roots for the rational case \(u=6/5\), \(q=101/200\).

The finite sign grid is not a proof over a continuum; the proof in `RESULT.md` establishes the all-parameter statements by concavity and exact polynomial critical-point analysis. The verification does not demonstrate uniqueness of this result in all published literature or constitute an independent audit.
