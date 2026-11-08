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

The projected full/target-avoiding Markov transition kernel is exact: for J=H∩U, pure-death comparison has eigenvalues 1-|A|/r on incidence-zeta basis. Uniform finite-dimensional resolvent isolation works because r/n->0. Stationary entrance flux for one fixed s-set is exactly binom(r-1,s-1)/binom(n,s); overlapping targets produce relative O(r/n) loss. Excursions from the empty projected state and first-return transform yield 1-rho=d beta/M [1+O_{s,d}(r/n)], for any fixed d uniformly over target intersections. The condition (r/n) log M->0 and t/r sufficiently large give fixed factorial moments, then Poisson/Gumbel; union-bound geometric tails give E[T]. I reconstructed the rate/scaling and regenerative steps, and independently matched 30 exact full-versus-killed-projection probabilities on n=9,r=4,s=2 with two overlapping targets. Finite checks do not prove the uniform triangular-array estimates.

## originality

PASS

Compared actual quantified final claim, its hypotheses and all four possible prior-implication routes against named published research and relevant primary texts. Related results do not establish the entire result on inspected evidence; inaccessible or potential aliases are kept as explicit residual risks. The foundational 2025 paper explicitly leaves the Markovian sparse growing-block Gumbel law unproved; fixed-parameter and independent-draw limits do not dominate.

## value

PASS

This gives a precise distributional and mean cover-time law for fixed-order subset shadows when successive retained blocks grow without becoming macroscopic. It resolves an explicit growing-block Markovian gap not addressed by independent block draws or fixed-parameter limits, with a quantitatively meaningful uniformity threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
