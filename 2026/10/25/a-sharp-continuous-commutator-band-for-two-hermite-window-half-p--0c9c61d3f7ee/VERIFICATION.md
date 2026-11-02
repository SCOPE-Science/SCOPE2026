---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Plancherel and normalized Hermite orthogonality identify each T_s as multiplication by G(s-u) with G(a)=[[F(a),-phi(a)/sqrt2],[-phi(a)/sqrt2,F(a)-a phi(a)]], phi(a)=exp(-a^2)/sqrt(pi). Direct 2x2 multiplication gives skew commutator amplitude (s-t)/(sqrt2 pi) exp(-((s-u)^2+(t-u)^2)); completing square gives kappa_d exp(-2(u-m)^2), kappa_d=d exp(-d^2/2)/(sqrt2 pi). Multiplication-operator spectral theorem yields full imaginary band, entirely essential and absolutely continuous, multiplicity two on each sign and no eigenvalues. Nonzero scalar Gaussian multiplier noncompact on nonatomic measure space; peak measure zero gives nonattained norm; scalar derivative maximizes at d=1. Independently checked numeric values for d=.4,1,2, not substituted for proof.

## originality

PASS

Existing polyanalytic/Hermite horizontal Toeplitz theory provides a general matrix-valued fiber representation, but the inspected primary statements do not evaluate this two-threshold commutator Gaussian, its full spectrum or sharp d=1 norm. General symbolic calculus for smooth masks and Gabor sampling do not imply the specified discontinuous half-plane exact quantitative formula without additional evaluation. Best-of-knowledge PASS with acknowledged risk of a precomputed 2-window specialization.

## value

PASS

The first genuinely coupled Hermite-packet concentration operators do not commute although each single-window fiber is scalar. The theorem quantifies their sharp pairwise incompatibility and complete infinite-dimensional essential/absolutely-continuous spectral structure, including multiplicity and lack of norm attainment. The selected normalized model is canonical and physically interpretable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
