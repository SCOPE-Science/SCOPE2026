---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Starting empty at d=0, the complement-even-sites transformation maps pair 00↔11 updates to exclusion exchanges and proves irreducibility in equal U/V count class; for d>0 physical exchanges and pair removal make all even-total parity configurations accessible. Detailed balance yields Bernoulli(p) conditioned on the relevant class. U and V are conditionally independent given shared count K at d=0, so I=H(K), with probability proportional to binom(m,j)^2 z^(2j). With d>0 they are conditionally independent given shared parity and I=h(q_m), q_m=(1+t^m)^2/(2(1+t^(2m))). Standard local CLT yields H(K)=0.5 log(pi e m p(1-p))+o(1) at fixed p, versus log2 as m→∞ for d>0; mp→λ gives the Bessel count limit. Independently enumerated m=2..4 microstate distributions and computed MI at three densities.

## originality

PASS

Mercado et al. establish and enumerate the relevant stationary configuration classes and hopping singularity, so the ensemble is not new. The assessed information-theoretic consequence is the exact mutual-information reduction to a count or a parity bit, its growing-vs-one-bit scaling and Bessel dilute crossover. These statements are absent from the inspected model results; the logical derivation from published ensemble weights is explicitly acknowledged.

## value

PASS

Reveals that arbitrarily weak diffusion opens an accessible configuration class that collapses global information between interlaced physical halves from order log m to one parity bit; the exact sparse-density Bessel crossover and proper-subset independence show local diagnostics cannot see this global structure. It is a natural invariant of a previously studied solvable stochastic adsorption model, despite reusing known equilibrium weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
