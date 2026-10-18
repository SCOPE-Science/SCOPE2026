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

For α,θ>0,0<p<1, setting λ=θ/p in EPQL(y)=p^y θ[α(θ+p)+θ(y+1)]/[(α+1)(θ+p)^{y+2}] cancels p^{y+2} and yields exact PQL(y;α,λ) at every y≥0. For any positive λ choose p=1/2, θ=λ/2, so families have identical images. The PQL PGF λ α/[(α+1)(λ+1−s)] + λ²/[(α+1)(λ+1−s)²] has a genuine unique double pole at s=λ+1; pole and leading coefficient identify λ and α uniquely. Thus full triple equivalence classes are exactly constant α and θ/p. An iid univariate likelihood depends on θ,p only through θ/p; its score in direction (0,θ,p) vanishes pointwise, making Fisher information singular when defined. SymPy algebra independently verified full-parameter PMF ratio 1; inspected exact-rational checker supports but does not prove the infinite identity.

## originality

PASS

Best-of-knowledge PASS for a source-specific full parameter quotient and statistical non-identifiability correction: the source only calls p=1 a PQL reduction and assigns additional flexibility to p. General Poisson thinning/scale reduction and 2017 PQL law are correctly treated as prior, but neither inspected article states that all 0<p<1 EPQL marginals coincide with PQL including exact equivalence fibers and null Fisher direction. More limited 2022 binomial-discrete Poisson-Lindley antecedent was only partially accessible.

## value

PASS

The exact collapse shows that published three-parameter univariate likelihood fitting is structurally nonidentifiable irrespective of sample size. This changes inferential degrees of freedom, confidence intervals and model-comparison interpretation; it is not an arbitrary renaming, though restrictions or bivariate observations may restore identification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
