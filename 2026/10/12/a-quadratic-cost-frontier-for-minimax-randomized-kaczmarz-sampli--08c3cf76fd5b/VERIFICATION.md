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

# Mathematical reproducibility

Run `python3 check.py` in the directory containing the delivered files. The checker uses Python 3's standard library only, including exact `fractions.Fraction` arithmetic.

The deterministic result is `VERIFY_OK 56 exact simplex primal-dual cases; all principal minors checked`.

The checker constructs each regular-simplex dyad exactly in the rational ambient sum-zero hyperplane of dimension \(d+1\). For each integer \(2\le d\le8\) and eight positive rational exceptional prices, it verifies unit norms, pairwise regular-simplex Gram values, the tight-frame identity, the candidate expected-cost budget, the analytic optimal objective, dual matrix constraints, equality of primal and dual prices, and nonnegativity of every principal minor of the exact matrix slacks. At the transition it additionally verifies four members of the complete feasible optimum family.

The universal positivity, uniqueness, and complete equality classification rest on the analytic dual and complementary-slackness arguments in `RESULT.md`; finite rational cases do **not** prove a continuum of prices or arbitrarily large dimensions. The theorem optimizes exactly the one-step worst-case mean-squared error decrement per *expected* projection cost. It does not optimize all definitions of long-run rate per unit time or establish exact realized-runtime performance.
