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
# Verification of the exact quadratic noise ceiling

The complete algebraic and interval proof is in `RESULT.md`. Its essential identity is the factorization of \(p_{\varepsilon_c}\), with nonnegative quadratic residual on \([0,1]\), and its essential comparison is \(u\ge g_\varepsilon(u)\) for **any** separated two-band interval trap containing the deterministic orbit.

Run the included independent diagnostics by executing `python3 verify.py` in this directory. The numerical program uses only the Python 3 standard library. Run `python3 symbolic_check.py` as a separate exact-algebra check (requires SymPy); it returned `PASS 4 exact polynomial certificates` for the resultant, double root and factorization. It tests numerical double-root identities, 23 subcritical saturated interval pairs against direct image endpoints, stability and repulsion of the two branches, sampled polynomial factorization and above-threshold inequalities, fold coefficient and slow critical endpoint convergence. The diagnostic run performed before acceptance returned `PASS 2232 diagnostics; epsilon_crit=0.046270003904528; u_crit=0.286885943875667; gap=0.584540507426373; fold_coefficient=1.392938820312`.

Floating-point equality tests are subject to usual rounding and **do not prove** positivity on continua or exhaust all noise histories. The proof of those universal claims consists of the endpoint inequalities and algebraic elimination in `RESULT.md`. The critical convergence asymptotic is one-sided and counts two-step returns. The code does not check publication priority, random-measure properties, or arbitrary maps.
