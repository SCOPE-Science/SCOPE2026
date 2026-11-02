---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Accepted edges are sampled uniformly from vacant edges, so while a,b,c remain, the rare-event chance is bc/[a(b+c)+bc]. Each accepted majority/minority edge lowers s=b+c by one; B-C lowers s by two and increments J, leaving exactly M−S+2J unpaired A. Since a>=M−S and bc<=(b+c)^2/4, each minority-minority event has p<=s/[4(M−S)]; the expected number is O(S²/M)=o(S) and J/S→0. Conditional B fraction has drift only on B-C events, equal p(b−c)/[s(s−2)], and the rest is a bounded-difference martingale, establishing uniform bulk composition. Coupling to Bernoulli intensities (BC/S²)(S−k)/M has total-error o(S²/M); these sum to BC/(2M)(1+O(1/S)). Le Cam proves finite-λ Poisson convergence, while compensator variance and martingale variance O(λ) give the diverging-λ law. An independently coded exact recursive finite-state absorption law was normalized/symmetric in 54 small triples; at (M,B,C)=(100,10,10), E J=0.49767 near the critical prediction 0.5.

## originality

PASS

Closest exact RSA full-text result (Turban 2019) analyzes the Poissonian terminal count of rejected trials on a homogeneous fully connected graph, a different observable from accepted B-C matches on a highly imbalanced tripartite graph. Broader random greedy matching asymptotics do not automatically yield the critical Poisson law with explicit rate BC/(2M) for the specific dominant-class depletion process. Searches did not locate an exact equivalent; possible implicit generalized density-dependent Markov-chain theorem remains a material priority risk.

## value

PASS

The Poisson-to-law-of-large-numbers transition for rare successful minority–minority pairings identifies a natural sharp n² majority-size crossover, and the exact vacancy relation interprets the defect count as the jamming correction. This is a motivated stochastic phase phenomenon, not an artificial finite-parameter count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
