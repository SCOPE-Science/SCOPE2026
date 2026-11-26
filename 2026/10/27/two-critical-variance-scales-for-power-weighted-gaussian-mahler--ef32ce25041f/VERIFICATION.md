---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With the specified complex density, |G|² is Exp(1), and log|G| has mean −γ/2. For normalized values of two Gaussian evaluations, put c=|ρ|². The joint Laplace transform of their squared moduli is 1/((1+s)(1+t)−cst). Substituting the Laguerre generating variables gives 1/(1−cuv); also integrating the one-variable generating function against log x times exp(−x) gives −γ+log(1−u), hence the Laguerre coefficients −1/k for log|G|². The square-summable expansion yields Cov(log|G|,log|G'|)=Li₂(c)/4 including c=1. The marginal second moments justify angular integration and give the factor 1/(8π) in the variance. For n=1 this gives π²/24 as it should. Parseval and the nonnegative Li₂ tail bound separate H_n(2α)/(4H_n(α)²) with residual at most a constant times ||F||₄⁴/H_n(α)^4. Splitting the Fourier sum near |t|⁻¹, bounding the head by an integral and the monotone tail by Abel summation gives the claimed power bound; near α=1 use j^(±λ/log n)≤exp(|λ|) for j≤n, including in the logarithmic head, to give uniformly bounded fourth moments. For α<1/2, after t=u/n the normalized sum has the claimed Riemann limit and an integrable squared majorant min(1,|u|^(2α−2)), giving the positive full-chaos constant. At α=1/2 the residual is O(n⁻¹); on 1/2<α<1 it is lower order than the first term, including the log fourth moment at α=3/4. At α=1 the residual is O(log⁻⁴ n); at α>1 uniform convergence of the normalized series gives a positive integral. For λ in a fixed compact, H_n(1/2+λ/log n)~2√n exp(−λ) and H_n(1+κ/log n)/log n→∫_0^1 exp(−κs)ds uniformly for κ=λ or 2λ by integral comparison. In the second window the numerator H_n(2α)→ζ(2) uniformly. These produce both profiles with the stated normalizations and removable λ=0 singularities; higher terms are uniformly negligible (O(n⁻¹) and O(log⁻⁴ n), respectively). The frozen numerical checker was inspected, not executed; its FFT/Jensen-root sample checks are not evidence of uniform error control.

## originality

PASS

The generic Gaussian logarithmic covariance machinery and the explicitly excluded exact unweighted specialization are prior. The distinctive evaluated result is the power-weighted variance profile at positive exponents and, in particular, both compact-uniform moving-exponent crossover functions. Neither a covariance representation nor the inspected prior zero-count or leading unweighted results imply the two evaluated critical profiles without the weighted localization and summability analysis.

## value

PASS

The variance of a natural logarithmic spectral statistic distinguishes collective Fourier peak/chaos effects, an intermediate summability regime and persistent boundary randomness. The two different, sharp compact-uniform transition functions quantitatively connect these behaviors; they are substantial even without a distributional limit or a non-Gaussian extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
