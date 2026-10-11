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
# Verification

The elementary Fourier calculation requires the normal-radius coefficients
\[
\rho(\theta)=\frac12+\sum_{\substack{\ell\ge1\\\ell\ \mathrm{odd}}}
\frac{2(-1)^{(\ell-1)/2}}{\pi\ell}\cos(3\ell\theta).
\]
The support coefficients are obtained by dividing the nonconstant coefficient at frequency \(3\ell\) by \(1-9\ell^2\). Rotational Minkowski averaging multiplies its amplitude by \(\cos(3\ell\delta/2)\). The area identity therefore reduces to the explicitly summable series
\[
\frac\pi4-\operatorname{area}(M_{x/3})
=\frac1\pi\sum_{\substack{\ell\ge1\\\ell\ \mathrm{odd}}}
\frac{1+\cos(\ell x)}{\ell^2(9\ell^2-1)}.
\]
Its second derivative is the negative of an odd-harmonic cosine series divided by \(\pi\). The closed elementary cosine-series identity in `RESULT.md` follows from direct Fourier coefficient integration, and the endpoint conditions determine both integration constants.

The standalone checker `verify.py` checks this differential equation, both areas, strict-derivative factorization, and the complementary-angle identity symbolically; also checks cosine-series coefficients by exact integration and evaluates the series numerically.

A separate circle-arc support-point construction computes Minkowski-average areas at five angles, agreeing with the closed formula to polygonal-sampling tolerance. This finite numerical test is not a proof of the identity over the continuum. No external independent audit is claimed.
