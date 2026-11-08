---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For N>=q+1, q>=2, 0<p<=1, exchangeability yields exact birth/death rates U_k=(N-k)[(k)_q+p((N-1)_q-(k)_q-(N-k-1)_q)]/[N(N-1)_q], D_k=k(N-k)_q/[N(N-1)_q]. Inject exactly-one-plus mixed ordered panels qk(N-k-1)_(q-1) to show U_k>=pq D_k, including small remaining minus panels; equality at k=1. For pq>1, bounded supermartingale (pq)^(-X_t) and optional stopping imply all-N Moran lower bound. The birth-death harmonic product has fixed-k ratio D_k/U_k -> 1/(pq) as N grows. Geometric dominated convergence yields 1-(pq)^(-m) for pq>1; divergent denominator bounds yield 0 at/under pq=1, for each fixed m. Independently checked 2280 exact transition, injection, and fixation identities; finite checks do not prove the N limit.

## originality

PASS

The 2023 source media q-voter paper covers q-panel nonlinear drift and a macroscopic threshold near 1/q and finite-size exit probabilities in a different normalization. Its results do not state the specified focal-first distinct-other-panel exact all-N domination or the fixed-m rare-seed limit. Doniec et al. generalized q-voter finite Markov method and branching theory are relevant but a general algorithm to solve every N does not directly imply the uniform sharp bound plus singular regime. Historical equivalent branching/fixation result under the same sampling convention remains possible.

## value

PASS

Fixed finitely many initial advocates constitute a distinct scaling from a positive fraction. The theorem gives a sharp invasion survival probability and an all-population comparison, showing that even p=1 leaves a single initial plus with limiting failure probability 1/q. This exact finite-size and infinite-limit boundary is natural for biased opinion dynamics and not a routine restatement of mean-field drift.

The dated certificate retains the supplied scientific assessment, sources and limitations.
