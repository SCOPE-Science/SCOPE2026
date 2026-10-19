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

# Verification

The theorem, hypotheses, boundary conventions and proof appear in `RESULT.md`. With Python 3 standard library, run `python3 verify.py` in the directory containing that document and script. The script was executed successfully and reported `PASS: 945 reproducibility assertions; exact identities plus finite examples.`

The check includes exact-rational verification of all two-step Jacobian matrix identities at 81 slope/kick combinations; boundary-inclusive finite root-census and floor-formula comparisons for rational parameter families; exact rational inequalities separating the outer elliptic and hyperbolic resonances of a sample map; and sample two-step evaluations. Floating calculations are labeled as supplementary finite checks and use explicit tolerances. The infinite cardinality, all-cutoff formula and asymptotic exponent depend on the analytical argument, not on finite experiments. Results for nonconstant-action orbits, nonlinear KAM stability and physical applicability at very large actions are not established. No independent audit has been performed.
