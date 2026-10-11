---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Fourier characters diagonalize both quadratic difference forms. If \(r(k)\) coordinates of a frequency are odd, the long-difference energy is \(4r(k)/n\), while averaging over independent signs gives sign energy \(2(1-\prod_j\cos(\pi k_j/m))\). For \(c=\cos(\pi/m)\), any positive cosine product is at most \(c^{r(k)}\), and \(r/(1-c^r)\) is increasing in positive \(r\); nonpositive products give no larger ratio. Hence the maximum is at \(k=(1,\ldots,1)\) and equals \(2/(1-c^n)\). The conjugate-pair real span attains the same ratio, so the complex Fourier computation is valid over real scalars. Wang's exact quotient duality then transfers this to the adjoint lifting constant; normalization gives the displayed \(L_{n,m}\), and the Taylor expansion of \(\log\cos(\pi/m)\) gives the sharp-scale limit. Independent enumeration for small \(n\) and even \(m\), including \(m=2\), reproduced the maximizing frequency and formula.

## originality

PASS

Wang's primary paper defines exactly these difference and divergence-lifting constants, proves their quotient-duality equality, and computes the optimal regular factorization norm; at the normalized \(p=q=2\) scale this regular norm is \(\sqrt n\). The complete paper does not state the real-scalar Fourier constant \(\sqrt{2/(1-\cos(\pi/m)^n)}\): targeted full-text searches found no Fourier or cosine calculation supplying it. Mendel and Naor provide the metric-cotype discrete-torus framework but not this exact finite scalar extremum. Current Resultary search returned the assigned formula as the exact same-object hit and no stronger scalar theorem.

## value

PASS

The result exactly evaluates the scalar Hilbert benchmark inside a current metric-cotype lifting framework and exposes a sharp qualitative separation: datum-dependent liftings remain bounded at \(m\asymp\sqrt n\) while every regular linear realization has cost \(\sqrt n\). The exact frequency extremizer and limit profile are natural invariants of the canonical torus model and give a meaningful baseline for the Banach-valued theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
