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

# Verification notes

Running `python checker.py` with Python 3.10 or newer and no external libraries prints the exact-test result and four finite-truncation diagnostics. The exact part enumerates 8, 64, and 1,024 graphs (1,096 total) over rational score vectors in dimensions three through five and verifies the conditional Bernoulli-tail identity by analytic interval integration using fractions. For every enumerated graph, it directly checks the maximum edge-root support loss; the weighted distribution gives the exact probability that the deleted-support loss is zero, \(p=2/5\). The independent limiting-model diagnostic generates the inhomogeneous Poisson extreme points by exponentiating the arrival times of a homogeneous Poisson process, then independently marks potential edges. It compares the observed zero mass with the exact \(p\) value and checks a conservative mean upper envelope. The numerical diagnostics are seeded and reproducible; neither their sample sizes nor a finite truncation certifies the infinite result.

Actual successful run:

```
EXACT_PASS: 3 score sets, 1096 edge-labeled graphs; conditional tail, zero atom, and rational conditional means
PPP_DIAGNOSTIC: p=0.2, trials=6000, truncation=45, mean_gap=0.95360, mass_at_zero=0.20383 (target=0.2)
PPP_DIAGNOSTIC: p=0.5, trials=6000, truncation=45, mean_gap=0.36386, mass_at_zero=0.50833 (target=0.5)
PPP_DIAGNOSTIC: p=0.8, trials=6000, truncation=45, mean_gap=0.12017, mass_at_zero=0.79600 (target=0.8)
PPP_DIAGNOSTIC: p=0.95, trials=6000, truncation=45, mean_gap=0.02239, mass_at_zero=0.95500 (target=0.95)
```

The analytic proof independently supplies the joint Gaussian extreme-value Poisson limit, the locally finite extreme-pair count, the exact expectation \((1+t)e^t\), and a uniform square-integrability bound for the scaled finite support losses. Radial Gaussian normalization yields intrinsic Euclidean mean width. The endpoint asymptotics follow by dominated convergence near full density and a first-moment lower bound at sparse density. No externally performed independent mathematical audit is claimed.
