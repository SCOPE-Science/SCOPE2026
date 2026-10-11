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

Run `python3 verify.py` in a directory containing that file. The standard-library-only program checks \(30{,}001\) parameter values, computes all ten distances directly, computes every supporting-edge direction's width directly, and compares both to the closed formulas in RESULT.md. It also tests \(200\) exact rational instances of the convexity identity and checks the limiting trapezoid's values.

Observed output: `VERIFY_OK sampled_pentagons=30001 exact_rational_identities=200 sharp_ratio=14.392304845413`.

The verifier is diagnostic, not a proof by finite enumeration. The universal bound, strict inequalities, equality uniqueness, and limiting behavior are derived in the analytic proof in RESULT.md. The calculation tests no asymmetric pentagons; the theorem does not address that class. Independent audit has not been performed.
