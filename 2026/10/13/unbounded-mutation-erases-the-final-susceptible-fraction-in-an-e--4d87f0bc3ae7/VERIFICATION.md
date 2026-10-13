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

The theorem is proved by a population-mass identity, parabolic maximum-principle comparison with a positive Dirichlet principal eigenfunction, and a bounded-rate SIR final-size comparison. `verify.py` is self-contained and checks an exact rational positive-growth margin and sample bounded-domain root inequalities. It does not replace the analytic all-time comparison argument.

On the test \(k=2\), \(\mu=1\), \(\mathcal D=1\), candidate terminal susceptible lower level \(a=1/10\), Dirichlet interval \([40,41]\), use \(\pi^2<10\) to verify the eigenvalue gap exceeds \(2\). The exact-rational arithmetic verifies the parameter-side inequality; float bisection checks that the unique sharp bounded-size root lies strictly between zero and \(S_0=99/100\) for \(I_0=1/100\) and \(kL/\mu=2\).

Observed output from `python3 verify.py`:
```
Dirichlet sample: growth > 2
Bounded-domain final-size root: 0.199796032323201
CHECK: sharp-root inequalities and growth witness consistent
VERIFY_OK
```

Scientific limit: no finite calculation can verify universal half-line convergence directly. Independent audit has not been performed.
