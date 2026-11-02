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

Given source recovery lifetimes, receiver states solve q′=h(1-q)-mu q independently. Linearization q0=(lambda/m)exp(-mu t)sum_i int_0^(L_i wedge t)exp(mu s)ds has n E q0->lambda Phi(theta)exp(-x) at t=log n+loglog n+x, and variance O(1/log n) from independent source lifetimes. The difference q0-q is nonnegative and has expectation at scale n bounded O(1/log n) via the explicit two-source covariance. Conditional binomial n,q then converges to Poisson; surviving source probability ≤m exp(-t)=O(1/log n), and zero infected is absorbing, giving the Gumbel zero-atom. The detuning theta=0 follows from continuous exponential quotient. Independent finite formula computations support normalization, albeit slow convergence at finite n when theta<0.

## originality

PASS

Heinzmann (2009) proves extinction asymptotics for irreducible subcritical multitype branching with simple leading eigenvalue; that hypothesis fails at resonance in this reducible one-way two-class model. Windridge (2014) treats exponential-tail multitype branching SIR, not receiver SIS reinfection or Jordan resonance. The new claim has an explicit log-log delay and 1/log n detuning crossover with a conditional Poisson proof. Closest 2015 general SIS article was only abstract-accessible and remains priority risk; no assertive whole-document noncoverage.

## value

PASS

Identifies a natural critical-resonance extinction scale, including explicit crossover between nearly equal recovery modes, for a finite susceptible-infected process beyond irreducible branching theory. A sharp log-log delay and whole distribution are meaningful asymptotic structure rather than a small finite example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
