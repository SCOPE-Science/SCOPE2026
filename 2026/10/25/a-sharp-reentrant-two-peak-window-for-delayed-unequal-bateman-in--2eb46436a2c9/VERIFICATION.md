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

# Verification record

The closed-form proof in `RESULT.md` is the justification for all parameter ranges; `verify.py` is a finite reproducibility and implementation check. Run `python verify.py` with Python 3.10 or later; only the standard library is required. The executed program printed:

```
deterministic boundary and reentrance checks: PASS
randomized direct finite-difference and peak-sign checks: PASS (2200)
```

The deterministic test locates the two roots of \(Q(d)=1/20\) for \(\lambda=1,\kappa=3\), tests the predicted two/one/two sequence and checks coincident-rate constants. Seeded randomized cases include both coincident and different rates. The tests compare an analytic derivative with finite-difference changes to the superposed concentration at interior points and compare the derivative jump with its closed corner criterion.

Finite tests cannot exclude a counterexample at an untested parameter or certify the general theorem. The proof uses exact signs and differentiability on the two open time intervals to cover all positive rates, amounts and delays. Equality at \(m=Q(d)\), at \(d=t_0\), and at \(m=m_*\) is addressed analytically. No external experiment, clinical safety assessment, or independent mathematical audit has been performed.
