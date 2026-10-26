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

# Reproducibility and verification limits

In a directory containing `verify.py` and `requirements.txt`, install the dependencies and run:

```sh
python -m pip install -r requirements.txt
python verify.py
```

The program constructs independent \(2m\)-by-\(2m\) stochastic matrices for each \(2\le m\le16\), checks the proposed complete spectrum and optimum, tests several thousand feasible symmetric two-weight competitors and several hundred asymmetric edge allocations, and verifies large-size asymptotic expressions. The exact output of the recorded replay is supplied in `verification_output.txt`.

The proof of global optimality is analytical, using automorphism averaging, the strict lower bound provided by the largest contrast eigenvalue, and a one-dimensional unique minimizer. Finite tests cannot certify that theorem for all graph orders. Independent assessment has not been performed.
