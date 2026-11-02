---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the reset-clock exit theorem

The proof is analytic. The following checks specify the ingredients and their reproducible evaluations; no empirical or computational test is represented as an infinite-limit certificate.

1. **Characteristic exponent to jump tail.** For \(\exp(-t\sigma^\alpha|\xi|^\alpha)\), the symmetric Lévy density is \(\alpha\Gamma(\alpha)\sin(\pi\alpha/2)\sigma^\alpha/(\pi|z|^{1+\alpha})\). Integrating beyond the two endpoints gives the displayed \(k_\pm\), with \(k_+=k_- =\sigma/\pi\) when \(\alpha=1\), \(\Lambda=0\).
2. **Published centered coefficient.** Euler's reflection formula yields \(1/(2\eta_\alpha)=\Gamma(1-\alpha)\cos(\pi\alpha/2)\); the continuous value at \(\alpha=1\) is \(\pi/2\). This equals the centered Poisson-reset mean coefficient in arXiv:2610.20410.
3. **Geometric renewal transform.** Conditional on \(N=n\) failed cycles before a successful exit, the marked transform is \(b_K(s)^n a_{\pm,K}(s)\). Summation over \(n\ge0\) gives \(a_{\pm,K}(s)/(1-b_K(s))\). Differentiation at zero or a renewal-reward argument yields the exact mean ratio in the proof.
4. **Dominated convergence.** The stable exit functions satisfy \(F_\pm(u)\le Cu\), which bounds scaled finite-mean success probabilities by \(CR\). For \(0<\delta<1\), the subcritical reset-time integral is dominated by \(\min(su,1)u^{-1-\delta}\), integrable at both endpoints.
5. **Critical logarithm.** With Lomax shape one, the scale range \(1\ll R\ll K\) makes \(\int (sR/K)(1+R)^{-2}\,dR\sim s\log K/K\); the same logarithm appears in successful attempts, with coefficient \(k_\pm\). Thus the ratio has denominator \(k+s\) and numerator \(k_\pm\).
6. **Mean comparison at the boundary.** For \(\alpha=1\) and \(\Lambda=0\), the known unreset mean \(\mathbb ET=1/\sigma\) differs from \(1/k=\pi/(2\sigma)\); the result therefore distinguishes the subcritical and critical clock families.

All limits concern fixed flight parameters and fixed reset laws. The directional small-time first-exit estimate is an externally established mathematical premise, inspected in Figueroa-López and Tankov (2014); it has not been numerically certified here. Independent audit is not performed.
