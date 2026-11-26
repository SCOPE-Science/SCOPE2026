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

Hermite–Genocchi with probability measure on the simplex gives F_(n,0)=1/P for P=∏(z−a_j); m differentiations multiply the spline integral by (−1)^m(n+m)!/n!. The numerator (−1)^mP^(m+1)(1/P)^(m derivative)/m! has degree nm by its nonzero leading term at infinity and value P'(a_j)^m at knot a_j, so the only candidates for zeros are its roots, with no canceled poles. On the real pole complement the normalized derivative ratio is the complete homogeneous polynomial in (x−a_j)^(-1); its even degrees are strictly positive by the nondegenerate even moment of a linear combination of independent exponentials. An odd derivative is then strictly monotone in each gap, and its endpoint divergences are opposite because adjacent P'(a_j) have opposite signs and m+1 is even. The derivative of the odd derivative is nonzero there, making the gap zero simple. Outside the knots the reciprocal variables share a sign, so the homogeneous sum does not vanish. Conjugation now gives n floor(m/2) with multiplicity. The proof includes m=0 and m=1 and imposes no simplicity assumption on nonreal roots. Independent rational Sturm checks of 21 cases, n=1,2,3 and m=0 through 6, also checked the numerator degree, noncancellation and odd-order gap counts.

## originality

PASS

The normalized spline identity and even homogeneous-polynomial positivity are prior results. The supported distinct claim is the full finite real/nonreal census of all derivatives in the simple-real-pole reciprocal-polynomial class, expressed also as the two-parameter spline transform theorem. The strongest inspected reciprocal-derivative theorems treat different hypotheses and asymptotic questions. In particular, the exact odd-order gap and multiplicity argument is not provided by positivity alone or by the previous phase retrieval results. No statement-level coverage of this census was found in the inspected sources.

## value

PASS

These are natural positive compactly supported windows, and the count is a useful exact invariant of their analytic Cauchy transforms. The result gives the zero-free orders, the exact number of upper-half-plane Blaschke zeros at all higher orders, and the real-boundary gap pattern without solving for the roots. Knot invariance is a substantive feature of the result rather than a fixed-configuration computation or just the rational representation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
