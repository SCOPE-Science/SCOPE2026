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

The standalone `verify.py` computes the exact two-update expectation matrices using rational arithmetic. It checks the difference-matrix factorization, both eigenvector relations, the threshold signs, a fully rational reversal witness, and the endpoint reflection behavior. Execute `python3 verify.py` from the extracted artifact directory. The observed output is:

```
VERIFY_OK 202 exact rational matrix/eigenmode/witness checks
```

The key analytic identity is \(D=\beta[(\beta+\alpha^2\rho^2)(P+Q)-2\alpha(PQ+QP)]/4\) with \(\beta=\alpha(2-\alpha)\). Its proof is a finite matrix expansion written in RESULT.md and does not depend on numerical interpolation or sampling. The verifier tests finitely many exact rational inputs; it does not certify quantified claims by enumeration. The geometric convergence conclusions follow from the nonexpansive-update equality cases and compactness, not from the finite verifier. No independent review has been performed.
