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
# Verification of the Ising susceptibility extremum

The accompanying `verify_ising.py` uses only Python's standard library. Execute `python3 verify_ising.py` from the package directory. The most recent completed invocation printed:

`PASS: 8164 exact layouts, 238 independent exact spin-ensemble checks, 65 distinct (n,m) minima, asymptotic comparisons`

For every composition with 3 through 12 bonds, its exhaustive rational count confirms the mechanical word's closed-form minimum and identifies equality only at rotations. For systems of at most seven spins, an independent sum over all spin configurations checks the derived two-point and susceptibility representation without reusing the cyclic-arc formula. A distinct rational coupling pair provides another algebraic check, and lengths 200, 400 and 800 check the displayed asymptotic formulas. A finite-size comparison to an infinite-volume segregated limit is evaluated with an explicitly relaxed finite-size tolerance; it is not a claim of finite-n exact equality.

The infinite theorem, strict equality classification, zero-field partition identity and thermodynamic formulas require the analytic derivation in `RESULT.md`. These finite tests do not constitute an exhaustive proof for arbitrary n. The finite-volume system requires positive finite inverse temperature and strictly positive unequal ferromagnetic couplings. No assertions are made about nonlinear magnetic response, alternate Hamiltonians or two-block maximality.
