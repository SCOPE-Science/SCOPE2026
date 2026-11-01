---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

PASS: After factoring z^n, the two analytic rescalings are even Gaussian sums with opposite signs (-1)^j. On compacts, diagonal covariance tends by Riemann sum to 4∫cosh(tw)conj(cosh(tv))dt; off-diagonal alternating sum O(1/n) and zero pseudo-covariance establish independence. Uniform Gaussian moment bounds give compact-open tightness, and Hurwitz/argument principle give zero-count convergence. Independently computed K(w,w)=sinh(2x)/x+sin(2y)/y, Δlog K = (16/45)(x²+y²)+O(|w|⁴) and EN(B_r)=(2/45)r⁴+O(r⁶); finite-n exact moment coefficients converge. Conditioning on independent ξ_n shifts a smooth planar curve away from 0 almost surely, proving no finite-degree unit-circle zeros; reciprocity then pairs inside/outside. Limits require fixed compact w sets, not uniform in growing windows.

## originality

PASS

PASS, best of knowledge: the primary 2025 Kabluchko–Khoruzhenko–Marynych paper treats independent-coefficient regular-variation polynomials and self-inversive conjugated-reverse coefficients, with real unit-circle boundary traces; our mirrored half-coefficients are non-conjugated self-reciprocal and yield an even complex Gaussian entire field, with zero-free finite unit circle. Classic Edelman–Kostlan intensity and Hurwitz imply the technique but not this covariance or two-window decorrelation. A general dependent Gaussian analytic field theorem could subsume formulation, so priority is qualified.

## value

PASS

PASS: a natural reciprocal-symmetry random polynomial exhibits exact two-fixed-point decorrelation while having quadratic local intensity depletion and quartic zero-count growth. The exact local exponent and coefficient expose a geometric symmetry obstruction and distinguish self-reciprocal from self-inversive zero laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
