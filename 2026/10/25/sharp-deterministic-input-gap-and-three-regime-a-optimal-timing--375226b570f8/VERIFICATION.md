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

Run `python3 check.py` using Python 3 standard library only. The checker compares the explicit formulas with feasible independent-input moment choices, correlated Cauchy-admissible moment choices, and prescribed deterministic inputs on exact-rational parameter grids. It also checks the rational witness \(b=2\), \(s=\eta=1\), \(\beta=3\), whose causal cost is \(4/5\) and deterministic best is \(5/6\), with gap \(1/30\). The standalone program reports its checked case count and raises an assertion if any check fails.

All universal quantifiers, strict-gap regions and asymptotic statements are established in `RESULT.md` by analytical inequalities. A finite checker, regardless of its number of cases, is not a proof of a universal optimization statement. The analysis assumes exact second moments and expected-energy constraints, not an empirical finite-sample design guarantee.
