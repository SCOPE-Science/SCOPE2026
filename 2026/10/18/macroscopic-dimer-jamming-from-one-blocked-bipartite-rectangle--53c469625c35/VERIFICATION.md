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

The theorem has an analytic proof. Each allowed edge is assigned an independent exponential priority, so the four-group counts form an exact density-dependent Markov process with rates \(n ad\), \(n bc\), and \(n bd\). Doob and Grönwall bounds give fixed-horizon fluid convergence. The exact identity \(a+b=c+d\) integrates the fluid equations and gives the positive root of the scalar auxiliary function. Every later dimer necessarily consumes at least one still-free vertex outside the two blocked groups, so a deterministic tail inequality extends fluid convergence to terminal jamming.

The standalone file `verify.py` contains independent reproducibility checks using only Python's standard library. It verifies the exact terminal distribution by rational finite-state recursion, enumerates every allowed-edge priority order for a two-by-two graph, checks class-swap symmetry and normalization for numerous finite sizes, and compares exact asymptotic values with deterministic-seed stochastic simulations. On the completed package, the program reported:

```
(alpha,beta)=(0.4,0.4) predicted=0.0892520641 simulated=0.0892480000
(alpha,beta)=(0.3,0.4) predicted=0.0533935547 simulated=0.0534197500
(alpha,beta)=(0.2,0.6) predicted=0.0666666667 simulated=0.0667977500
Exact rational recurrences, literal edge-order comparison, and simulations: PASS
```

Run `python verify.py` in the directory containing the file. These checks cover finite cases and numerical consistency only; no finite enumeration proves the infinite-volume limit. The full generality and convergence in probability rest on the martingale and deterministic tail argument in `RESULT.md`. The theorem does not assert finite-size error rates, Gaussian fluctuations, or a vanishing-rectangle limit.
