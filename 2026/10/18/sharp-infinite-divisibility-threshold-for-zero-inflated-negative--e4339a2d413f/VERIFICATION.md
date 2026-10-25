---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For positive integer shape m and 0<q,w<1, factoring the zero-inflated negative-binomial PGF gives G(z)=w[(1−qz)^m+c^m]/(1−qz)^m, with c=(1−q)((1−w)/w)^(1/m). The exact log-PGF coefficients are ν_k=[m q^k−Σ_j(q/(1−c e^{i(2j+1)π/m}))^k]/k. If c≥2cos(π/m), all root ratios have modulus ≤q<1, so ν_k≥0 and summable and G is explicitly compound Poisson. If m≥3 and c<2cos(π/m), numerator has nearest nonreal zero at modulus R<1/q; if coefficients ν_k were all nonnegative, Pringsheim forces a singularity of log G on the positive real axis at R, contradicting local analyticity of log G there. Therefore some coefficient is negative and no lattice compound-Poisson/infinitely divisible representation exists. Boundary equality and shapes m=1,2 are covered; c threshold translates to exact w threshold for m≥3. Independent rational recurrence checks up to coefficient 110 included examples inside/outside m=3,4 thresholds. Initially choosing outside w=1/64 near m=4 threshold did not find a negative within 110; no improper conclusion was drawn from that finite cutoff, and a farther outside w=1/16 exhibited a negative coefficient at k=5. Finite tests support but do not replace Pringsheim.

## originality

PASS

Best-of-knowledge originality of the actual final claim, with explicit antecedent coverage and residual risk. The theorem makes a natural statistically motivated restriction of a general criterion but computes a non-obvious and sharp parameter boundary. The possibility that Puri–Goldie’s broader theory implies it cannot be excluded without full text; retain this explicit priority risk.

## value

PASS

A closed sharp if-and-only-if phase boundary for infinite divisibility of a widely used structural-zero count family is a meaningful distribution-theoretic invariant, with a constructive compound-Poisson Lévy measure on one side and a root/Pringsheim obstruction on the other. It shows a qualitative transition at shape 3 and explicit weights such as w*=1/9 (m=3,q=1/2) and 1/65 (m=4,q=1/2). This is a genuinely informative model classification rather than recomputation of a general CP criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
