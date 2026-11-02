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

# Verification of mathematical result

`python3 checker.py` is a standalone Python 3 checker with only standard-library imports. Its tested output is:

```
PASS 17603 exact, algebraic, and seeded simulation assertions
Monte Carlo means D,E,Y 0.9432 2.91 196.7588
```

For \(n=4,5,6\) with two roots, it exhaustively enumerates ordered parent-pair choices and computes the exact joint distribution of frontier size, internal redundant hits, root duplicates, and unique ancestors. An independently implemented rational frontier Markov recurrence followed by Stirling-number occupancy probabilities yields the same full distribution. Every direct sample and Markov state obeys \(X=2Y_m-1+D-E\). Critical-window Riemann sums check the analytic rate constants \(1/6\) and \(1/2\). Seeded Monte Carlo at \(n=10^6,m=10^4\) gives means close to the asymptotic mixed-Poisson expectations \(1\) and \(3\); sampling is not used to infer infinity.

The analytically relevant proof steps and cited premises are included in RESULT.md, especially Gamma frontier convergence and flatness (Janson Sections 3–4), the conditional Bernoulli thinning and root-birthday coupling, and the exact 2-to-1 red-vertex counting identity. The checker does not independently establish Gamma convergence, uniqueness in literature, or a formal infinite-domain certificate.
