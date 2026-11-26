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

After a rotation and translation, the first two coefficients of P(x+ih) are a_d and a_{d-1}+idh a_d. In its squared modulus the extra height term in the coefficient of x^(2d-1) is purely imaginary before taking the real part, so both leading intensity coefficients are shared, including when a_d=0. The first row determines a degree-at-most-2d real trace, and after subtracting the two known leading terms the second row determines a degree-at-most-(2d-2) trace. This covers d=1, when the second residual is constant. If either polynomial vanishes identically the first trace forces both to vanish. Otherwise the quotient R=P/Q satisfies R(z)overline(R(conj(z)+2ih))=1 as a rational identity for each height, by equality off the finitely many excluded points on the line. The two reflections imply a nonzero translation period. Any finite pole would have an infinite orbit under that translation, and a nonconstant polynomial cannot be periodic by comparing leading terms of its difference. Thus R is a constant of modulus one. For reconstruction, for a nonzero first trace its reflected-product factorization gives finitely many root allocations, with the leading-coefficient modulus fixed; the second trace selects the unique phase class. The two shared-coefficient constraints are independent in the formal trace-pair space, and the interpolation establishes the claimed dimension-4d isomorphism, not a lower bound on nonlinear retrieval.

## originality

PASS

The checked sources cover prior whole-curve uniqueness and several 4d-scale designs, not the combination of arbitrary parallel lines, arbitrary distinct nodes in a 2d+1/2d-1 allocation, value-only data, and a linear recovery theorem for the full formal trace-pair space. The distinct claim is this finite sampling and interpolation result, not whole-line uniqueness or the generic measurement count.

## value

PASS

Gives a finite value-only design with no within-row placement restriction, using fewer observations than separate interpolation on each line. The useful structural point is that two intensity traces share exactly the two leading constraints needed for invertibility on the stated linear ambient space; this turns known continuous uniqueness into a concrete sampling guarantee and provides an explicit noiseless route from the observations to the polynomial's phase class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
