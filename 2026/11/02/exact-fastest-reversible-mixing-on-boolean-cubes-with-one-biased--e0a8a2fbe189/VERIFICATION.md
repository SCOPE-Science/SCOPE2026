---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For reversible full-support product target on Q_{d+1}, conjugating by fair-bit flips and permutations and averaging preserves feasibility and does not increase the centered spectral operator norm. This reduces all feasible kernels to vertical flow c and per-layer fair-bit rates p,q. Walsh characters yield exact symmetric 2x2 H_k with I−H_k=z uu^T+2kD; Loewner order reduces the nontrivial spectral constraints to H_1<=mu I and H_d>=−mu I plus k=0 contrast. The two PSD determinant conditions and Cauchy–Schwarz give F_mu(z)>=0. Its concavity and strict negative derivative beyond z=1−mu at the positive f(mu)=0 root exclude any smaller mu; the explicit reversible kernel saturates both boundary PSD constraints and the k=0 eigenvalue. Algebra establishes strict increase with s=ab and known uniform endpoint. Independently built 12 full transition kernels for d=1..4 and three biases; checked nonnegativity, detailed balance and exact SLEM. This is finite corroboration; not the all-kernel proof.

## originality

PASS

Qualified original one-biased-coordinate solution. Boyd–Diaconis–Parrilo–Xiao 2009 treats the uniform-target hypercube and obtains mu=(D−1)/(D+1), exactly the a=1/2 endpoint for D=d+1; that known result is credited. Boyd–Diaconis–Xiao 2004 states the generic semidefinite formulation including reversible chains and arbitrary stationarity, but provides no examined closed exact biased-cube answer. The new feature is state-dependent fair-bit rates and exact all-bias radical formula, not the convex-averaging/SDP method itself. Potential independent coordinate Gibbs-sampler literature could contain an algebraically equivalent minimax result, a bounded priority risk.

## value

PASS

Fastest reversible spectral mixing on a fixed graph and target law is a natural Markov-chain design problem. Solving the complete one-biased-Bernoulli-bit cube parameter family with sharp transition probabilities, a radical SLEM and strict bias interpolation goes beyond the known uniform cube case and supplies a concrete optimal sampler/benchmark; the new state-dependent fair-bit adjustment is structurally meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
