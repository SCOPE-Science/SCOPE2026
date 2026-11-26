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

Under x=(1-cos(theta))/2, the centered integral is -1/4 times the m-th cosine coefficient of a(theta)=g(x(theta)) sin(theta). Since m is even, the boundary contributions alternate in the stated signs; a'(0)=g(0), a'(pi)=-g(1), a'''(0)=3g'(0)/2-g(0), a'''(pi)=3g'(1)/2+g(1). Integrating 2r times gives the claimed remainder by Riemann–Lebesgue; two more derivatives give the stronger bound. Endpoint evaluation has rank two, split into even and odd rank-one blocks, with exact parity cancellation by logistic reflection. For polynomials vanishing at both endpoints, the theta^5 coefficient of a for their product is p'(0)q'(0)/16, with the reflected coefficient at pi. This yields the 15/8 derivative Gram coefficient. On endpoint complements the leading block is T*T/(4m^2) and the coupling is 3T*RJ/(8m^4), with T invertible and R=diag(-1,1). Eliminating the complement subtracts 9/16 J*J, leaving 21/16. To verify multiset convergence even at a zero limiting eigenvalue, apply Schur inertia to H-m^(-6) z I for each real z outside the limiting spectrum: the complement block stays positive and the rescaled Schur block tends to (21/16)J*J-z I. This yields exactly the claimed small-eigenvalue counts and limits. Writing p=x(1-x)s gives the rank and, at d=2, the ratio of squared derivative norm 2 to squared polynomial norm 1/30, hence 315/4. The asserted signs at the two scales are asymptotic, not signs for every n. All matrix estimates are at fixed cutoff; the bundled rational program is finite corroboration only and was inspected, not executed.

## originality

PASS

The exact entries of the same Legendre compression and their O(4^-n) estimate are existing work. The supported distinction is the endpoint-jet expansion and the resulting two-scale spectral law, particularly the cancellation of the would-be m^-4 small-eigenvalue scale and the Schur-corrected m^-6 limit. A separate catalogue result has exact spectra in the arcsine/Chebyshev compression, not the Lebesgue/Legendre compression. Neither inspected statement gives the new spectral assertion as a direct special case.

## value

PASS

For a natural polynomial Galerkin approximation, this identifies how many independent directions see the leading endpoint effect and how coupling changes the first nonzero eigenvalues in the endpoint-null space. An entrywise decay bound cannot answer either question. The explicit loss of an entire scale and the derivative-Gram coefficient are useful fixed-cutoff data, without claims about projected nonlinear dynamics or a growing dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
