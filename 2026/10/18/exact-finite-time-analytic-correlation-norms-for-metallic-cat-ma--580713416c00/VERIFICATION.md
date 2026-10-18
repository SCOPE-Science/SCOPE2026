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
# Reproducible verification

Run `python3 checks.py` using Python 3 without third-party packages. The integer-only code checks the two matrix-power formulas and conjugate frequency cost for \(1\le s\le6\), \(1\le n\le7\), and each nonzero integer \(v\) in the square \([-9,9]^2\), verifying the four equality modes. The completed run reported exactly 15,456 passed assertions. These are finite diagnostics, not an exhaustive check over all integers.

The infinite proof in `RESULT.md` relies instead on unimodular lattice substitution and a three-case sign inequality. The precise analytic domain, normalization, and interpretation as a two-observable operator norm matter. Neither an unweighted \(L^2\) norm nor a single-observable autocorrelation is asserted. Independent mathematical validation has not been carried out.
