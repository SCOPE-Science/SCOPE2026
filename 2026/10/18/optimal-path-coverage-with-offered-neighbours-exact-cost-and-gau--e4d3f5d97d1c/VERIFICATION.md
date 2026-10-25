---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Reconstructed two-stage dynamic programming: full path is covered iff both boundaries have been visited; after the first hit the minimum crossing expectation C_n is independent of which endpoint. For target-right hitting, Bellman H_x=1+p H_(x+1)+q H_(x-1) (H_0=1+H_1, H_n=0), with q=2^-c and p=1-q; H decreases so selecting best offered target-neighbor minimizes the full Bellman equation. For first endpoint, nearest-end distance d has reflected/holding midpoint recurrence, value E_d increasing; exact even/odd formulas solve respective recurrences and satisfy Bellman inequalities. Independent exact rational checks for all c=1..5 and n=1..17 independently enumerated two-outcome offer probabilities and confirmed target and first-exit recurrences; source verify.py evaluates larger finite samples. The strong Markov property extends stagewise optimality to randomized history-dependent policies; c=1 gambler-ruin gives n^2+i(n-i). For fixed c>=2, positive drift delta=p-q, bounded reflection visits O_P(1), martingale functional CLT for hitting distance L_n~ell n gives variance 4pq ell/delta^3; first stage ell=eta and opposite crossing ell=1 are conditionally independent, hence total variance 4pq(1+eta)/delta^3, especially 9 for c=2, eta=1/2. Finite checks do not prove infinite CLT; the stopped-walk coupling does.

## originality

PASS

Best-of-knowledge after two real Resultary searches, public-primary reading and comparison of mathematical implications, not merely titles. General O(n) adaptive-walk bounds imply only a rate and do not identify the optimal feedback or explicit Gaussian law. Standard biased-walk hitting-time CLT is an ingredient but optimal two-stage decomposition and midpoint boundary recurrences require proof.

## value

PASS

A natural adaptive-cover stochastic control model on the elementary path acquires an exact finite-horizon optimal strategy and value for any offer count, including the transition from quadratic to linear worst-start cover cost and full centered fluctuation theorem. This materially refines existing general linear bounds for bounded-degree trees and provides a precise benchmark for choice random walks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
