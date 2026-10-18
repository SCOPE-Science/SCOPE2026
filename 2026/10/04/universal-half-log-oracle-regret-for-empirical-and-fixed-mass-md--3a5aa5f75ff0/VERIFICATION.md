---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In the pinned proof, with nondegenerate P supported in [0,1], µ,c interior and oracle bet λ* interior of [-c/(1−µ),c/µ], hλ(x)=(x−µ)/(1+λ(x−µ)). Uniform positivity 1+λ(x−µ)≥1−c yields bounded scores/derivatives. The stationarity identity P hλ*=0 implies score variance =P hλ*²=J=−M″(λ*)>0. Fixed score separation and Hoeffding concentration exclude boundary optimizer with exponentially small probability. Local score expansion gives n E(λhat_{n+1}−λ*)²→J^(−1) and n E|λhat−λ*|³→0; Taylor expansion gives nE[M(λ*)−M(λhat)]→1/2. For arbitrary predictable H on [0,1] and fixed κ, the mixture score differs uniformly by O(1/n), so same local limits. Summing one-step deficits by harmonic summation gives (1/2)log N+o(log N). The argument is valid subject to its stated interior/fixed-mass hypotheses; finite Bernoulli examples do not prove it. The public RESULT.md has an unexpanded literal {claim} under its ## Finding header, although its assumptions and proof state the theorem; scientific proof can be assessed but publication must not proceed without a verified full replacement.

## originality

PASS

Kilian–Cortinovis–Caron prove first-order log-optimality and an O(n^-1/2) Wasserstein predictive rate, not the exact half-log expected gap. Grünwald publicly anticipated a half-log GRAPA benchmark but describes it as an open/conjectural comparison, not a proved bound for this betting rule. Classical prequential MLE/one-parameter AIC/M-estimation half-log penalties motivate but do not directly state this distribution-free bounded-mean growth objective with arbitrary predictable fixed-mass MDP perturbation. Potential general M-estimation corollaries remain a residual originality risk.

## value

PASS

The leading expected oracle-regret constant identifies the exact second-order price of empirical optimization in bounded-mean betting and shows resilience under a natural Bayesian predictive perturbation. This improves a first-order result for a practically defined strategy and quantifies the conjectured logarithmic regime, without falsely claiming pathwise or constant-order regret.

The dated certificate retains the supplied scientific assessment, sources and limitations.
