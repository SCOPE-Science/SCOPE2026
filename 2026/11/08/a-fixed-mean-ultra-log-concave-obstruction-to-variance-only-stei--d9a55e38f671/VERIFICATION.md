---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Convolution gives p_n=e^{−ε}ε^{n−1}(ε²+n(1−ε))/n!, mean 1, variance 2ε−ε², and (n!p_n)^2−(n−1)!p_{n−1}(n+1)!p_{n+1}=e^{−2ε}ε^{2n−2}(1−ε)^2>0. Detailed balance telescopes to sharp indicator envelope F_m(1−F_m)/(w p_m). Strict ratio monotonicity and r2<ε,r3<=ε/2 imply all sites j>=2 have envelope <=2/(3w); j=1 has (1−εe^{−ε})/w>2/(3w), so first site is unique maximizer. Hence Γ/(σ/w)~(2ε)^−1/2→∞. Exact algebra proves infinite support; inspected checker is only diagnostic.

## originality

PASS

DeSalvo Open Problem 8.2 explicitly proposes the variance-only sup-norm estimate contradicted by this strictly ultra-log-concave fixed-mean Bernoulli–Poisson family. General tail-covariance Stein envelope is prior; newly identified exact supremum and sharply divergent variance ratio provide a mathematically motivated counterexample, not a new Stein operator.

## value

PASS

A full-support strictly ultra-log-concave counterexample at fixed mean refutes a newly stated universal Stein variance-scaling conjecture, isolates the failing second factor, and gives exact worst-index behavior; meaningful negative structural result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
