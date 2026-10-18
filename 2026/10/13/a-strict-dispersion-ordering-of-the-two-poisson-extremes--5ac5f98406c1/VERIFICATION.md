---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

From T=X+Y and Skellam H=X−Y, E|H|=2λ(a+b) with a=e^(−2λ)I0(2λ), b=e^(−2λ)I1(2λ), c=a+b. Poisson size bias yields E[T|H|]=4λ²c+2λa. Hence means λ(1∓c), variances λ(1∓a−λc²), and exact D_L−D_U=2(b−λc³)/(1−c²). The key strict Bessel inequality is proved for every λ>0: c=E exp(−4λS), S~Beta(1/2,3/2); with G~Gamma(1/2,1),J~Gamma(3/2,1), Jensen conditional on S=G/(G+J) gives c<(1+2λ)^(-1/2). Bessel ODE identities give c′=−b/λ and b′=2c−(4+1/λ)b. F=b−λc³ positive near zero cannot have a first zero because there F′=c[2−(2+4λ)c²+3λc^4]>0 by the strict Laplace bound. Independently checked numerical moment formulas and F at λ=.001,.1,1,10,100,1000 using high-precision special functions; numerical samples are corroboration, not the all-λ proof. Correct variance reversal VarU−VarL=2λa. Leading endpoint rates follow standard Bessel expansions.

## originality

PASS

Best-of-knowledge originality: relevant primary statement/implication comparisons do not cover the precisely stated contribution; no absolute priority certification. The exact moment formulas reduce the claim to a specific strict cubic Bessel inequality, for which the new conditional Jensen/zero-crossing proof supplies an all-positive-λ sign. No same inequality was found in inspected statements.

## value

PASS

The min and max Poisson order statistics are canonical discrete dispersion benchmarks. Strictly ordering their Fano factors across the entire intensity range, while their variances run in the opposite direction, resolves a meaningful contrast not determined by individual underdispersion or large-rate asymptotic equivalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
