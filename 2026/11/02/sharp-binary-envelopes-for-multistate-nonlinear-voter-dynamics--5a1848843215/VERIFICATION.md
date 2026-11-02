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

# Reproduction of finite-state comparisons

Run `python verify.py` with Python, NumPy, SciPy and SymPy. The program constructs the multistate generator with transition rates \(n_\beta(n_\alpha/(N-1))^q\), solves transient absorption linear systems, constructs the binary comparator and evaluates \(\exp(tQ)\) for finite-time event probabilities.

The directly executed program printed:

```
fixation_states_checked= 2540
strict_fixation_cases_checked= 882
finite_time_tail_compared= 19392
four_singleton_opinions_q=0.5 multistate=0.250000000000 binary=0.316987298108
four_singleton_opinions_q=2.0 multistate=0.250000000000 binary=0.125000000000
exact_rational_q2_states_checked= 157
```

Finite model sizes are \(N=3,4,5,6,7,8\), \(M=3,4\), and \(q=1/2,1,2,3\). Time-distribution comparisons use \(N\le6\) and times \(0.1,0.6,1.5\); exact-rational absorption checks use \(q=2\) and \(N=3,4,5\). Numerical tolerances apply to floating-point solves and matrix exponentiation; the exact-rational checks use SymPy rationals. This is not an exhaustive computation over all population sizes or exponents. The theorem's universal assertions rest on the independently readable symbolic coupling and stopped-generator proof in `RESULT.md`.
