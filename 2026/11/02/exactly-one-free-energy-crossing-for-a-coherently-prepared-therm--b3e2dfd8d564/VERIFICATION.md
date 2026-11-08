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

For finite positive bath temperature, gamma_+,gamma_->0 satisfying detailed balance and no added pure dephasing, Bloch evolution gives longitudinal p=e^-Gamma t and transverse sqrt(p). The coherent original has radius A(p) and population-inverted isospectral comparator radius B(p); Gibbs-relative entropy difference Delta(p)=(R-z)atanh(b)p-[S(B)-S(A)]. The exact squared radius gap is (R-z)(R+z+2b)p(1-p)>=0. Entropy derivative S(sqrt(q))=-h(q), h(q)=1/2 integral_0^1(1-qs^2)^-1 ds. Quadratic interpolation Q_theta between A^2 and B^2 satisfies Q+(1-p)Q_prime=R^2-a_theta(1-p)^2<=1. This makes the normalized gap Delta(p)/((R-z)p) strictly increase in p, even for pure initial vectors at every finite t. The normalized signs at p=1 and p->0 are positive and -((R+z)/(2b))atanh(b); coherence c>0 means -R<z<R, hence unique finite root. Cases c=0 are treated separately. Independent symbolic verification and direct numerical implicit root at b=.5,R=.8,z=0 gave p*=0.42993172972647203, t*=0.8441288509774865.

## originality

PASS

Moroder et al. 2024 already construct an isospectral population-inverted Davies comparison and exhibit a sample free-energy crossing (Fig. 2 and Appendix A); that example and physical setup are prior. The inspected main paper and appendix do not prove strict global monotonicity of normalized difference for every coherent Bloch vector or uniqueness and if-and-only-if classification. Summer et al 2025 compare divergence-dependent crossover times in a wider resource-theoretic setup, not the same all-state theorem.

## value

PASS

Global uniqueness of a quantum thermodynamic relaxation crossing gives a structurally useful theorem beyond illustrated examples. It identifies exactly when coherence forces an inversion of nonequilibrium free-energy order and provides sharp late-time coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
