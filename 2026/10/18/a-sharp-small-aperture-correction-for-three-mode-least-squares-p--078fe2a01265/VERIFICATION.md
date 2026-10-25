---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS: The normalized reproducing kernel is exactly 1+(cos(hx)-a_h)(cos(hy)-a_h)/(b_h-a_h^2)+sin(hx)sin(hy)/c_h, where a_h=sin(h)/h, b_h=1/2+sin(2h)/(4h), c_h=1/2-sin(2h)/(4h). Its uniform smooth limit is the quadratic Legendre kernel 1+3xy+5(3x²-1)(3y²-1)/4. At x=1 its simple roots (-1±sqrt(6))/5 bound the negative interval, whose exact integral gives L*=1+12sqrt(6)/25. The diagonal Cauchy–Schwarz norm bound is strictly below L* for |x|<=21/25 and the explicitly factored derivative of the Lebesgue function is strictly positive for 21/25<=x<=1; reflection and uniform smooth perturbation preserve exactly the two endpoint maxima at small h. Expanding the true kernel at x=1 gives -(h²/280)(175y⁴+140y³-90y²-28y-5), whose integral over the moving negative interval contributes -387sqrt(6)/21875 h²; moving roots are O(h²) with zero boundary integrand, hence remainder O(h⁴). Symmetry of K and duality give equal L1 and L∞ norms. Independent symbolic integration checked the radical coefficient, separate from claimed packaged 25 assertions.

## originality

PASS

Best of knowledge PASS for the evaluated sharp small-aperture endpoint norm and nonzero second-order correction, not for the known limiting Legendre kernel or Fourier-extension construction.

## value

PASS

PASS: For a natural three-frequency continuous least-squares/Fourier-extension projector, determining the precise leading curvature correction and proving localization of the actual global maximizing evaluation point is a motivated sharp approximation-stability theorem, rather than a table lookup or a numerical limit. The negative second-order term is not already contained in the classical degree-two Legendre limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
