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
# Verification of the prevalence-control theorem

The full mathematical derivation is given in `RESULT.md`. The executable `verification/verify.py` uses **only Python's standard library** and exact rational fractions; run it with:

```bash
python verification/verify.py
```

The checker must print `VERIFY_OK`. Its computations reconstruct the eight differential-equation right-hand sides from the published model and check an exact nonnegative coexistence equilibrium whose human-to-human reproduction quantity lies below one, while the rodent reproduction quantity lies above one:
\[
\mathcal R_h=\frac{49}{96}<1<2=\mathcal R_r.
\]
At the tested parameter values, the exact endemic human infectious prevalence is
\[
J=\frac4{49},
\]
while the sharp baseline attained at zero human-to-human transmission is
\[
J_{\min}=\frac4{65}.
\]
All eight right-hand sides vanish exactly in the coexistence witness. The checker separately verifies the zero-human-contact boundary state, the disease-free state, and a human-only endemic equilibrium, each with zero residuals, and it checks the inverse-contact identity using rational arithmetic.

The proof that these are the *only* types of equilibria uses the reservoir-force cancellation and human-force monotone bijection, not finite checking. In particular the checker does not establish global stability, nor does it interpret a numerical convergence test as a general proof.
