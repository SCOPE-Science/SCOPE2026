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

The orthonormal Takenaka–Malmquist basis gives the compressed multiplication operator (aI+J)(I+aJ)^(-1) with J the forward nilpotent shift. For the restricted backward shift X, if g=(I-X)f then g(1)=f(0) and the quotient of g is Xf. This gives Q=A*/(1-a), A=(aI+J)(I-J)^(-1). The shifted Gram identity AA*+aI=(1+a)^2 U, U_ij=min(i,j)+a/(1+a), holds entrywise. Applying the invertible first-difference map to U yields diagonal variances a/(1+a),1,...,1, proving the stated inverse tridiagonal including N=1. The nonzero subdiagonal makes its eigenvalues simple and det(A)=a^N gives strict positivity, the singular-value product and, by triangularity, the stated ordinary spectrum. Embedded in L2 via isometric step functions, A/N converges in Hilbert–Schmidt norm to (1+a) times Volterra, whose squared singular modes satisfy mixed Dirichlet–Neumann conditions. At the other edge the row-reversed and sign-adjusted a^N A^(-1) has geometric entries (1+a)a^(r+t) up to r+t=N-2; the omitted tail and the antidiagonal of norm sqrt(N)a^(N-1) vanish in Hilbert–Schmidt norm. The rank-one limit has norm (1+a)/(1-a^2), giving exactly s_N/a^N→1 and the condition number. The local Douglas identity adds I to the Gram operator for the embedding, so only the quotient seminorm loses coercivity, not the full embedding norm. An independent rational monomial-numerator calculation verified the quotient matrix, Gram identity, tridiagonal inverse and inverse of A for 27 parameter/dimension pairs; the spectral limits are analytic, for fixed real 0<a<1, with the top limit at fixed rank only.

## originality

PASS

Credit the established ordinary spectrum and the materially covered fixed-top-rank leading law. No inspected stronger result gives both the finite fixed-a singular spectrum and the sharp least-singular coefficient in this model operator; those are the supported distinct contribution. The embedding list follows algebraically from the spectrum, not from a separately new embedding criterion.

## value

PASS

In a canonical repeated-zero model space the exact formula solves a finite approximation-number problem, with a simple positive Jacobi matrix and a sharp a^N lower scale that the nonzero ordinary eigenvalue and qualitative embedding results conceal. The contrast with the linear top scale is significant for norm conditioning. The supported value rests on the finite list and sharp lower coefficient, not rediscovery of the leading Volterra law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
