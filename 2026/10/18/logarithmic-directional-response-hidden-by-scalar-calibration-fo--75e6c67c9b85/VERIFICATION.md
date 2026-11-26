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

Differentiate the smooth Gaussian convolution via its integrable density derivatives. Writing Q=r^2 U^2+V^2, the score formula gives a=E[U^2/sqrt(Q)], b=E[V^2/sqrt(Q)] with off-diagonals zero by reflection. Swapping U and V, the difference b-a is half the expectation of (V^2-U^2)(Q^(-1/2)-Q_swap^(-1/2)); the two factors have the same sign for r>1 because Q_swap-Q=(r^2-1)(V^2-U^2). In Rayleigh polar coordinates the gains are sqrt(2/pi)/r times the quarter-circle integrals of cos^2 and sin^2 against (1-k^2 sin^2)^(-1/2). The latter integral is (K-E)/k^2; subtracting it from K proves the former and hence both stated exact formulas. At r=1 each gain is sqrt(pi/2)/2. The standard complementary-modulus expansions yield a=sqrt(2/pi)/r times 1+O(r^(-2)log r) and b=sqrt(2/pi)/r times log(4r)-1+O(r^(-2)log r), so division retains the constant -1. For fixed sufficiently large r the response difference in direction (c,1) is epsilon(b-ca)+o(epsilon)>0; there is no uniformity assumption in r. Completing the square in r^2(a-s)^2+(b-s)^2 gives the exact fit. Its minimum is asymptotic to (2/pi)(log r)^2/r^2 and the normalizer tends to 2/pi, giving the stated relative error with coefficient one. The score proof bypasses any need to dominate a family of shifted singular derivatives of P. The frozen numerical assertions are corroborative only and were not rerun.

## originality

PASS

Pass the coupled quantitative planar witness, not the Gaussian score identity, least-squares formula, elliptic reducibility, or qualitative warning about response in low-noise directions. The checked sources give those ingredients, but the strongest matches do not cover the sharp directional-gain asymptotic, strict signal reversal and simultaneously vanishing specific diagnostic as a result about this Gaussian polar family.

## value

PASS

This is a motivated boundary example for an existing scalar diagnostic. It quantifies a simultaneous order reversal and unbounded gain discrepancy that is invisible to the very weighted criterion used for fitting. The rates show exactly how a diagnostic tending to zero coexists with arbitrarily poor directional matching, which supplies a concrete benchmark rather than a generic observation about weighted norms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
