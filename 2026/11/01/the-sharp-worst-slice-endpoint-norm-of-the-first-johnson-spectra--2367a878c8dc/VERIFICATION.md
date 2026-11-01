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
# Verification evidence and limits

The bundled `verify.py` is a standalone Python 3 exact-arithmetic checker. It confirms, for every pair \((n,k)\) with \(2\le n\le100\) and \(1\le k<n\), that the one-boundary expression is equal to the direct hypergeometric absolute sum and is unchanged by complementation. Independent full kernel-row calculations are checked up to \(n=9\). The hypergeometric discrete-antiderivative is separately tested at all support atoms up to \(n=100\); the elementary Poisson crossover stationary-point and cusp relations are checked numerically for initial parameter values. Observed output: `PASS 100553 exact-rational or elementary numerical comparisons`.

To reproduce, execute `python3 verify.py` in the directory containing this document. The verification program requires only the Python standard library and prints its test count. The general all-\(n\) exact identity and three-regime asymptotic theorem are established by the proof, not by finite enumeration. Limits: these computational tests do not constitute independent validation, and the recent 2026 hypergeometric-deviation paper was not materially available beyond its abstract.
