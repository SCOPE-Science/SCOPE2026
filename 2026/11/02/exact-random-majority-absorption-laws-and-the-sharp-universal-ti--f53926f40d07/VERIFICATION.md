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

# Mathematical verification record

The result uses synchronous independent fair-tie majority updating, on the entire range \(a,b\ge1\). Its proof reduces the full chain to sign persistence at two-step times, derives three exact probability-generating functions from first-step conditioning, solves their expectations, and bounds all even-size cases using central-binomial monotonicity. Only nine unordered even-size pairs remain for exact-rational comparison; the unique maximizer is \(K_{2,6}\) with value \(79/27\). The result explicitly separates entrance into any closed class from eventual consensus.

## Standalone calculation

Run `python3 verify_bipartite_rmm.py` from the directory containing this file and the verifier. No network access or nonstandard Python packages are used. The verifier constructs the count-process transition law independently of the three-state formulas and tests the Bellman equations for expected first entrance and each of three absorbing-class probabilities. It reports 144 graph pairs, 7524 transient states, and 18024 exact-rational transitions; it checks nine finite extremal pairs and central-binomial monotonicity for the first forty steps. All checks passed when executed on the packaged source.

## Scope of verification

These finite exact-arithmetic checks detect algebraic and normalization mistakes within the tested range, but cannot prove universal statements by enumeration. The analytic mathematical proof establishes the all-size bound. Absolute literature priority has not been certified. No independent audit or external mathematical validation has been performed.
