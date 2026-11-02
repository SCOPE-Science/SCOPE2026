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

# Reproducibility and checked limits

The document `RESULT.md` states the exact real domain, the exhaustive algebraic factorization, the prime-two count and all derivative-based stability inequalities. Run `python3 verify.py` using Python 3's standard library only.

The program checks, as an exact identity of bivariate integer polynomials, the numerator of \(T_h^2(x)-x\) for every formal \(x\) and \(h\). It checks the elementary derivative-product identity symbolically, exact rational examples at several gains, and the proposed asymmetric cycle coordinates and multipliers by floating-point substitution for five gains. The program's success was observed on the included file. The finitely many numeric substitutions are diagnostics, not evidence of exhaustive orbit classification. That exhaustiveness is provided analytically by factoring the exact period-two equation over the reals.

There has been no independent mathematical audit. Possible coverage by unidentified historical results is a residual originality risk. The theorem deliberately leaves all higher minimal periods, nonlinear marginal stability and attraction-basin geometry unresolved.
