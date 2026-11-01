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

Every site-subset state with k vacancies admits pair intensity binom(k,2) and triple intensity λ binom(k,3); conditioning on the next accepted event yields u_k=[3/(3+λ(k-2))]u_(k-2)+[λ(k-2)/(3+λ(k-2))]u_(k-3), with u_0=0,u_1=1,u_2=0. The three-consecutive-coordinate stochastic transfer matrices have three-step products whose pairwise row overlap is at least min(q_j,q_(j+1),q_(j+2))/2 once q≤1/2. The harmonic divergent sum of q_k gives Dobrushin contraction and a common full-sequence limit, not just a subsequence limit. Exact coefficient summation yields λ z(1-z³)Fʹ+(3-2λ-3z²-λz³)F=(3-λ)z. The integrating factor z^(3/λ-2)(1-z³)e^(-3K(z)/λ), after subtracting z^a, gives an integrable lower-end regularization for a=3/λ-1>-1. Abel convergence evaluates the limit; λ=3 produces the closed form. Dominated convergence (α→0) and one-sided Laplace asymptotics (α→∞, φʹ(1)=2/3) establish endpoint-rate limits. Independent exact-rational checks verified 796 generating-equation coefficient cases and the transfer product; finite numerics are corroboration only.

## originality

PASS

The object is terminal one-vacancy probability in a complete mixed 2-/3-hyperedge adsorption process with fixed per-edge rates, not spatial nearest-neighbor RSA coverage or dimer-only graph blocking. Full accessible primary studies of one-dimensional polydisperse RSA and graph dimer RSA do not state the exact full-sequence Bernoulli limit, regularized λ-integral and noncommuting pure-species limits. This is a best-of-knowledge positive comparison, not a novelty proof by failed search.

## value

PASS

Terminal Bernoulli jamming count on a completely interacting mixed-species substrate is a motivated exact observable; the full analytic rate-dependent law, elementary λ=3 value and disappearance of parity/mod-three size memory at every fixed positive minority rate describe genuine structural effects. An entire infinite substrate-size limit is proved analytically, not inferred from a few enumerated sizes. Scope is an idealized complete hypergraph and does not claim physical Euclidean adsorption predictions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
