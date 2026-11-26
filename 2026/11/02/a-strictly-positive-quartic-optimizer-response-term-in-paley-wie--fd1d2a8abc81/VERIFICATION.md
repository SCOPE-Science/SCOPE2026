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

For fixed s, the bandwidth bounds control all evaluation derivatives and yield the exchange expansion m^2 Q_s+m^4 U_s+O(m^6) in operator norm, with the fourth-order endpoint derivative factor 1/12. With the leading simple eigenvalue isolated, the complementary part of the first eigenvector correction in parameter m^2 is R_s Pi Q_s psi. The scalar equation therefore adds W_s to the fourth-order Rayleigh term. For the weighted problem at m=0, the Rayleigh principle gives the global maximum at zero; equality for a nonzero shift would force a translate to be collinear with psi by simplicity, incompatible with nonzero square-integrable periodic modulus. The translated integrals vanish at infinity; uniform C^2 convergence localizes all maxima near zero, where Phi_0''(0)=2u'(a)<0 and evenness forces the unique maximizer to be zero. The slope and positive boundary value hold for the first prolate. To check nonvanishing, on the Fourier band Q_s psi is the Fourier transform of psi'(a)(delta_a+delta_-a)-psi(a)(delta'_a-delta'_-a). If proportional to psi, the eigenvalue equation would equate it on that band to the transform of an absolutely continuous compactly supported density. Both transforms extend entire, and distributional Fourier injectivity contradicts the nonzero boundary Dirac derivatives. The reduced resolvent is positive on the complement, so W_s>0. Resolvent boundedness and parity give convergence and the even-mode series. In the ratio, the denominator has leading coefficient 4u'(a)^2 m^4, which is nonzero.

## originality

PASS

The supported claim is the exact positive quartic response for the specified symmetric endpoint exchange, after optimizing the prolate translation, and the resulting sharpness of the squared-discrepancy order. Compared sources supply the upper order, the interval optimizer and related one-sided loss examples, not the positive response. No absolute priority claim is made.

## value

PASS

The natural equal-measure exchange tests a specific open sharpness issue of the existing discrepancy estimate. The theorem both rules out a uniform little-oh improvement and explains the obstruction as a strictly nonzero eigenfunction response transverse to the baseline eigenvector, rather than as a center displacement or the leading loss alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
