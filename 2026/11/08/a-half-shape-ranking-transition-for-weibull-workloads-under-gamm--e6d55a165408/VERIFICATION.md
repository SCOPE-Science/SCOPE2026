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

# Reproduction and verification

The standalone Python 3 standard-library file `verify_transition.py` is included with the scientific result. From a directory containing it, execute:

```bash
python3 verify_transition.py
```

The deterministic verifier completed successfully in the original package preparation, printing `FINITE_CHECKS_OK=3009 integral_p=0.744414082925 PPP_sim=0.74156`. It uses seven independent numerical evaluations of the exact integral identity for \(A(g)\), 3000 Chernoff-rate inequality cases, numerical quadrature for the critical probability, and a separately coded finite-window simulation of the limiting marked Poisson process. The simulation uses a fixed random seed and finite numerical truncation.

The exact claim is proved in `RESULT.md` by analytic extremal-Poisson convergence, an explicit Gamma tail cutoff when \(\beta\le1/2\), a critical Gaussian-mark void-probability calculation, and an independent-many-competitor argument when \(\beta>1/2\). The numerical script is neither an exhaustive asymptotic proof nor a historical-priority certificate. Independent mathematical validation has not been performed.
