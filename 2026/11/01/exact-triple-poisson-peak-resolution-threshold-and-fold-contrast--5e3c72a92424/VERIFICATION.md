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

Setting s=h² and clearing the strictly positive denominator gives V_s′(x)=−2x[3(x²+s)^4+(4s+1)(1−4x²)]/D_s(x). An independent sparse exact bivariate polynomial expansion and threshold factorization confirmed the identity. The polynomial Q_s(y) is strictly convex for y≥0, with global minimum at y0=((4s+1)/3)^(1/3)−s and value 9r^4(r²−1); the sign changes at s=1/2. Its exact factorization at equality has only the positive double root y=1/2. This proves complete critical-point multiplicities for all real h>0. Analytic Taylor expansion around (x,s)=(1/sqrt2,1/2) gives local derivative 2sqrt2 μ−9sqrt2 ξ²+ controlled errors; integration across the two roots and multiplication by h/pi yields the 3/2 contrast coefficient. The checker confirms only algebraic subclaims; continuum root counts and asymptotic remainders follow from the written inequalities.

## originality

PASS

Duan arXiv:2608.28376 and Oliveira arXiv:2609.00336 establish the general upper bound of 2n−1 critical points for n-source line-restricted potentials, hence at most five here. The special exact transition h=1/sqrt2 and fold amplitude do not follow quantitatively from a universal upper count or generic attainment construction. Equivalent three-component equal-scale Cauchy-mixture modality literature was searched; a previously tabulated equal-spacing threshold could still exist and its historical priority is not exhaustively ruled out.

## value

PASS

The minimal symmetric three-source configuration is a canonical resolution benchmark for harmonic/Poisson smoothing. The sharp loss of two side peaks and the exact shrinking peak-to-valley height quantify an authentic modal transition, a natural invariant not determined by generic point-source zero-count results. This is a complete all-height classification, not a numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
