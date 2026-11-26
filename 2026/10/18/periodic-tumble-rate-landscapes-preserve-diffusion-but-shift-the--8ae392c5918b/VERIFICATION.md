---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The additive functional is the unwrapped displacement, so the tilt adds the bounded multiplication kv*sigma. A fixed-time Doeblin minorization on the circle follows from paths making exactly one or two flips: with one flip the opposite terminal direction has an endpoint sweeping the circle as the flip time varies; for the original terminal direction fix the first flip in a short window and vary the second over a sufficiently long interval. The upper/lower rate bounds give a uniform positive density contribution in both cases. The tilted fixed-time operator is analytic, with a simple isolated leading eigenvalue near k=0. Its iterates and the uniformly bounded residual-time factor give log generating function t*alpha(k)+O(1) analytically on a small complex disk (the coefficient of the leading term is nonzero near zero for any starting law); Cauchy differentiation gives the rates. The periodic tilted equations for sum S and difference D give determinant-one Floquet monodromy and trace 2 cosh(kL), making alpha even on its local analytic branch. An independent coefficient check eliminates D to get alpha S=(partial+k)[a_alpha(partial+k)S], a_alpha=v^2/(2 lambda+alpha), from which alpha=-mu_alpha(-ik) for the lowest divergence-form Bloch band. At fixed alpha, write the normalized periodic eigenfunction as 1+z chi+z^2 rho+... with z=iq and expansion mu=-A z^2+C z^4+.... The order-z flux is A=1/mean(1/a_alpha); chi'=A/a_alpha-1. The order-z^2 flux is zero because chi has mean zero, so rho'=-chi. The order-z^3 flux is -A rho+B, where periodicity and mean(rho)=0 imply B=A mean(rho chi')=A mean(chi^2). The next averaged equation gives C=-B. Thus A(0)=v^2/(2 ell), A'(0)=-A(0)/(2 ell), and C(0)=-A(0)E/ell^2; solving the last implicit dispersion relation gives alpha_2=A(0), alpha_4=-v^4/(8 ell^3)+v^2 E/(2 ell^3). Multiplying by 2! and 4! recovers both cumulant rates. Parseval for the centered primitive weights the rate coefficients by L^2/(4 pi^2 q^2), so the sharp equality class excludes every mode |q|>=2 and E=0 holds only for a constant rate. For the cosine E=(ell epsilon L)^2/(8 pi^2), yielding the stated sign and feasibility thresholds. These analytic checks apply to bounded positive profiles, with weak derivatives and absolutely continuous fluxes, not just the finite examples in the package.

## originality

PASS

Credit previous Bloch coefficient methods and the known constant-rate or diffusion results. The supported distinct claim is the exact arbitrary-profile decomposition of the fourth cumulant into the negative constant-rate term and a nonnegative centered-primitive energy, including the sharp frequency optimizer and resulting sign boundary. The strongest indexed exact overlap is a two-zone special case. The strongest accessible general spectral comparator supplies an elliptic cell-problem algorithm for the quartic band coefficient, but not the closed profile identity or the nonlinear telegraph dispersion relation and its two competing contributions. The possible overlap with the closer 2001 damped-wave expansion remains explicitly unresolved on the available material.

## value

PASS

The second and fourth cumulants distinguish physically meaningful properties of the same one-dimensional process: all allowed profiles with fixed mean rate are indistinguishable by long-time diffusivity, but heterogeneity gives a rigid upward shift of the fourth cumulant and can reverse its sign. The explicit primitive energy makes that sensitivity measurable and gives a sharp first-harmonic design rule at fixed rate variance. This is more informative than a generic higher-order cell solve or a table for any one profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
