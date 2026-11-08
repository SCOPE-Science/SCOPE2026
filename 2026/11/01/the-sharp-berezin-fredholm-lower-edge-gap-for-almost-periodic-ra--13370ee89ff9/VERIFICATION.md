---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For real continuous Bohr almost-periodic p with ||p||∞≤1 on Gaussian Fock C^d, radial monomials of total degree m have eigenvalue E p(sqrt(Gamma(m+d,1))), whose Gaussian delta limit is (H_{1/8}p)(sqrt(m+d))+o(1), uniformly in d fixed via finite Fourier sums and sup approximation. The coherent Berezin transform is E p(|se1+W|)=(H_{1/4}p)(s)+o(1). Compact almost-periodic translation hull, relatively dense almost-periods and vanishing mesh sqrt(m+d+1)-sqrt(m+d) establish min sigma_ess=inf H1/8p and liminf Berezin=inf H1/4p, not pointwise finite-n bounds. Gaussian semigroup ordering gives nonnegative Delta; choosing near-minimizers of H1/8p gives Delta≤||G1/4-G1/8||_1, which was independently integrated using their crossing at |x|=sqrt(log2/2)≈0.5887050113 to 2[erf(sqrt(log2))-erf(sqrt(log2/2))]≈0.3321281499670257. Widely spaced periodic sign profiles -1 on intervals of half-width a* and +1 elsewhere attain this signed-kernel bound asymptotically; uniform Gaussian tails plus mollification produce admissible smooth periodic profiles. Nonattainment follows from AP hull uniform compactness and the equality condition q=sgn(G1/4-G1/8) almost everywhere, impossible for a continuous hull limit at ±a*. Strict positivity for nonconstant p follows injectivity of Gaussian heat on Bohr spectrum and strict positive-kernel averaging. Source check.py numerical diagnostics were inspected, not treated as proofs of analytic limits.

## originality

PASS

Esmeral–Maximenko (2015) Proposition 6.5 already supplies the time-1/8 eigenvalue heat approximation (a critical premise, not a new theorem). Looi (2026) independently gives explicit cosine radial symbols showing Berezin positivity need not imply Fredholm essential positivity in all d, including unequal heat attenuation scales; it does not establish a sharp normalized supremum over all Bohr AP profiles, strict nonattainment, or smooth periodic optimizing sequences. Bdarneh (2026) develops radial-weighted Fock Toeplitz spectral representations for a broader class of weights, with no matching two-heat sharp gap in the inspected relevant theorem material. The exact L1 total-variation of Gaussians is classical; originality is attributed to the Fock spectral–Berezin variational classification, not the standalone integration identity. A potential prior semigroup-minimum defect theorem remains residual risk.

## value

PASS

The maximal additive difference between two natural asymptotic Fock operator lower edges measures the worst false-positive margin of Berezin essential-positivity tests under the natural ||p||∞≤1 normalization, for every finite complex dimension. It is a sharp variational invariant over a nontrivial infinite-dimensional almost-periodic profile space, with rigorous nonattainment and explicit smooth periodic approximants. These consequences exceed a mere one-frequency example or numerically re-evaluating the known Gaussian L1 distance. The theorem makes no assertion about arbitrary measurable radial symbols or multiplicative ratios.

The dated certificate retains the supplied scientific assessment, sources and limitations.
