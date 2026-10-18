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

# Reproduction and limits

The mathematical claim is proved in `RESULT.md` by an arbitrary-size incoming-probability partition and an irreducibility argument. The two scripts here provide checks of the kernel and stationary solution, not an infinite proof.

Run from the unpacked artifact root:

```
python verification/symbolic_stationarity.py
python verification/independent_markov_solve.py
```

The first program uses SymPy to symbolically verify, without floating-point approximations, every balance equation, the normalization and the signed-current numerator for all \(3\leq L\leq20\). The second independently constructs the stochastic transition matrix and solves its stationary linear system using NumPy, comparing all state probabilities and signed currents at \(z=0.13,0.37,0.8\) for \(3\leq L\leq11\). Both programs completed with PASS. The source code is supplied to reproduce those computations.

**Scope of checking.** Symbolic finite enumeration through \(L=20\) is not a certificate for larger \(L\); the proof of all-size balance is the seven-case analytic argument in `RESULT.md`. Numerical linear solves establish neither unique asymptotic behavior nor mathematical novelty. The parameter endpoints \(p=0\), \(v=0\), or infinite \(v\) are excluded from the strict negativity and uniqueness statement, although limiting formulas at positive parameters are established.
