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

# Reproducibility and verification

The mathematical domain is the fixed real two-mode diagonal dissipative system and independent reciprocal-probability exact-subflow sampling defined in RESULT.md, for every \(a>b>0\), \(h>0\), \(p\in(0,1)\), integer \(n\ge1\), and, for the asymptotics, \(T>0\).

Run `python3 verify.py` using Python 3 and the standard library. The program independently enumerates all \(2^n\) switching words for sampled small horizons; evaluates binomial moments; tests optimizer crossing and sides of \(1/2\); checks variance-proxy comparisons; checks small-step and large-step limiting profiles; and tests the positive limiting mean-square deviation. The packaged verifier reports `PASS: 819 independent finite comparisons; no external dependencies` and prints two reference examples.

Exact algebraic proof steps are the binomial generating function, monotonicity of \(u(1-e^{-c/u})\), the crossing characterization, asymptotic inversion of its monotone scaling profile, binomial-to-Poisson convergence, and the boundedness argument permitting moment convergence. The numerical verifier does **not** certify a continuum of parameters or any limit by enumeration. No independent scientific or external formal proof audit has been performed.
