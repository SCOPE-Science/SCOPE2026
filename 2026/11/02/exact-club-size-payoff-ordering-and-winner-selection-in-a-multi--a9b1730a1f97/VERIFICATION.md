---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Conditioning on the tagged restaurant, each independent club sends one other diner with probability g_j/N (none from the tagged club), and each other free diner arrives independently with probability 1/N. The reciprocal occupancy integral factors. In a club comparison only the two differing club factors remain after common factors are removed, producing g_i−g_j; in the free comparison the differing factors are the one club factor versus an extra free Bernoulli, producing g_i−1. The remaining integrals are strictly positive. With fixed K the binomial factor converges uniformly to exp(−f(1−t)) and unoccupied types have the stated smooth extension. Each limiting gap kernel is at least exp(−1) times the integral of (1−t)t^(K−1), namely exp(−1)/(K(K+1)). Summing the club equations shows total club mass B is nondecreasing, so a maximal initially occupied club remains at least B(0)/K. Its log ratio against a positive free fraction grows uniformly, and its log ratio against a smaller club grows uniformly because the smaller-to-larger ratio never exceeds its strict initial value below one. These give the claimed exponential loss and exact tied limits by conservation; zero coordinates remain zero. Equilibrium requires equal payoffs on support, hence no coexistence with the free type and only uniform positive club supports. At such a state the active contrast subspace has the positive eigenvalue in RESULT.md:95 by differentiating the log ratios; absent-type rows are diagonal with the negative invasion gap in line 101. This block structure counts every eigenvalue on the simplex, including the K=1 sink; at the free vertex the linear part is zero. Independent exact check `python3 -B /workspace/review_checks.py 1` enumerated restaurant allocations in N=2–4 with one to three club labels (including empty labels) and checked 126 rankings. The global claims are analytic, not consequences of the packaged trajectory tests.

## originality

PASS

The evidence supports a distinct all-finite-K payoff order and complete ordinary-replicator classification, not novelty for the one-club result, the two-club payoff model, or qualitative monoculture. A named 2025 supplement is a substantive unresolved comparison, especially for the replicator part; the accessible evidence does not demonstrate equivalent coverage of the theorem with the stated quantifiers.

## value

PASS

The theorem addresses the natural multi-club extension raised by the model's founders. It separates the exact finite payoff order from the ordinary mean-field selection rule, and gives a complete assignment of limits, tie faces and local stability indices rather than repeating a one-club advantage or simulation. This value is within independent coordination and fixed finite K; it is not a claim about finite stochastic absorption or tolerance switching.

The dated certificate retains the supplied scientific assessment, sources and limitations.
