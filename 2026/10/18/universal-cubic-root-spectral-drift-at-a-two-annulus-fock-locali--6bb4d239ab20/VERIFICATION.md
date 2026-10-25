---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Monomial diagonalization converts eigenvalues exactly to Gamma(shape k+1) mass in two intervals centered at squared radius N. Standard uniform Stirling/Edgeworth expansion for k=N+x√N gives λ_{N,k}=g(x)+N^{-1/2}[g′+(x/2)g′′+(1/3)g′′′]+O(N^{-1}) on compact x. Differentiating the even Gaussian annulus profile gives g′(x)=2φ(x)[e^{-b²/2}sinh(bx)−e^{-c²/2}sinh(cx)]. Strict increase of sinh(cx)/sinh(bx) makes a unique pitchfork at log(c/b)=2aδ; in supercritical case strict h(x_*)<0 selects −x_* at order N^{-1/2}. At criticality b e^{-b²/2}=c e^{-c²/2}=q, g′′(0)=0, g⁽⁴⁾(0)=−24γδ and h′(0)=−8γδ; optimizing −γδ(y⁴+8y) at y=(k−N)/N^{1/3} yields unique −2^{1/3}, value 6·2^{1/3}γδ. Tightness via Gamma tails and quartic bound plus lattice spacing establishes every maximizing sequence. Read the bundled standard-library verify.py and independently evaluated exact Gamma-CDF shell masses at N=200000 for critical δ=0.5 and 1.0; respective maximizing displacements (k−N)/N^(1/3) were −1.26538 and −1.28248 versus predicted −1.25992. The analytic expansion, not finite checks, proves the limit. Scope: fixed δ>0,a>δ,N>c², squared-radius normalization.

## originality

PASS

Esmeral–Maximenko Proposition 6.5 provides leading Gaussian smoothing of radial Fock Toeplitz eigenvalue sequences. Oldfield Theorem 2.4 is a two-term Szegő trace/counting theorem for anti-Wick operators under fixed-shape rescaling. Neither examined theorem determines the precise moving-annulus critical quartic mode, finite-size Gamma skewness selection or universal -2^{1/3} maximizer offset. Classical radial diagonalization of Grudsky–Vasilevski is credited, not claimed new.

## value

PASS

A coalescing pair of natural spectral localization peaks has a genuinely nonstandard quartic-to-cubic-root finite-size regime: exact universal signed displacement, N^{-2/3} norm correction, and symmetry-breaking sign choice. This is a structural stability/bifurcation law for a canonical Toeplitz operator family and supplies precise data where leading symmetric Gaussian limit is insufficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
