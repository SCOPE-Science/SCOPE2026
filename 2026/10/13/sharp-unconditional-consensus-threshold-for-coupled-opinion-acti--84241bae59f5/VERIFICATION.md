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

# Mathematical verification

The undelayed update on the \(2n\)-coordinate vector \((x,y)\) is reconstructed directly from the equations, rather than borrowing the delayed augmented representation. Each row is stochastic and every positive coefficient is at least \(\eta=\min\{\phi,1-\phi\}/n\). Every action row of any two-step product is componentwise at least \(\eta^2\), which is the essential persistent-envelope lemma. The extreme-leader argument and strict cross-confidence inequality are analytic and hold for every finite \(n\ge2\).

Run `python verify.py` with Python 3. The verifier exhausts the \(2^2\) possible directed neighbor masks for \(n=2\) and the \(2^6\) masks for \(n=3\), as well as all ordered two-step mask pairs, using `fractions.Fraction`. It independently checks the two-agent fixed configuration for \(\phi=2/5\) below and at \(\varepsilon=7/10\), verifies complete-neighborhood two-step positivity, and conducts 100 randomized convergence diagnostics for \(n\in\{2,3,5,10\}\). Expected terminal output: `VERIFY_OK: rational two-step action mixing, sharp two-agent obstruction, 100 dynamical checks`.

The finite matrix calculations are not a substitute for the all-\(n\), all-real-parameter proof. They do not provide a quantitative pre-asymptotic entrance time, validate heterogeneous parameters, or address noncomplete social contact graphs. A separate independent scientific audit has not been performed.
