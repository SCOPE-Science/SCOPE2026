---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For fixed integer M>=1 and a,b>0, the initial M-window has the stationary beta-binomial exchangeable distribution; the finite binary shift chain is irreducible, aperiodic, and exponentially mixing. Its binary covariance equals v at lag 0, v/(kappa+1) for 1..M, and thereafter satisfies the finite-memory linear recurrence with denominator M+kappa. Absolute summability permits summing the recurrence to integrated variance v*(M+kappa)*(M+kappa+1)/(kappa*(kappa+1)). The functional Markov CLT plus summation by parts yields the n^(-3/2) weighted edge-count CLT with variance one-third this value; dominated covariance summation establishes the separate n^(-3) variance limit. The fixed-M ergodic n^(-2) limit rho/2 differs from Beta-random infinite-memory limit Theta/2. Checked the conditional law, lag normalization, variance weights, terminal universal-vertex O(n) perturbation, and distinction between fixed and growing M. Independent exact SymPy finite-state Poisson checks for M=1..4 and (a,b)=(1,1),(2,3) corroborated the integrated factor, not the infinite CLT.

## originality

PASS

The stationary queue process, its memory recurrence and the general finite-state CLT preexist; the actual proposed addition is the all-M evaluated integrated covariance and its weighted Pólya-threshold-graph edge-count Gaussian limit. Inspected the motivating graph and queue/autocorrelation work and queried published mathematical findings under statistical/urn and graph aliases; no checked source directly states or dominates the full graph-statistic theorem. Priority risk remains for older communication-channel variance identities and related finite-memory urn papers.

## value

PASS

The central statistic of a natural random threshold-graph model receives a sharp all-memory fluctuation coefficient, revealing a quadratic fixed-M memory cost and separating finite from infinite memory behavior. This is an infinite family analytic fluctuation theorem rather than a low-order parameter substitution or finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
