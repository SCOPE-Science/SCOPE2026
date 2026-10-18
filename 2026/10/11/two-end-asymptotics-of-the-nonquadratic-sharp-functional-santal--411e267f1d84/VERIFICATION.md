---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

Using the claimed sharp-slab canonical radial equality profile, reconstruct the left-end profile ODE: with a=k_n^{-1/n}, s=t+1, r=as-a^(2n+1)s^(n+1)/(n(n+1))+o(s^(n+1)). The projective sublevel-radius transform R(z)=(1+z)r((z-1)/(z+1))/sqrt(2) gives the small-radius inverse with coefficient 1/[n(n+1)c_0^(n-1)]. At t=1 put q=-r'; q'/q^(n+2)->b^(n-1) with b=k_n^(1/n). Integrating and inverting gives the claimed large-radius exponent 1/(n+1), negative correction and stated coefficient. Direct algebra checks c_0*c_infinity=1. Convex radiality makes the limiting slope the global Lipschitz constant; if slopes were equal the profile would be affine, contradicting r'(1-)=-infinity. Conjugate zero ball is the origin subgradient and the open effective-domain ball follows from the negative unbounded sublinear correction on its boundary. These are analytic deductions, not inferred from the n=2..40 verifier. Caveat: exact ODE and endpoint data are source-dependent premises not independently cross-checked against primary full text during this run because primary extraction was unavailable.

## originality

PASS

Best-of-knowledge comparison of mathematical statements and implications against named primary sources, published findings and exact source-object searches. The current Resultary hit for the very assignment under audit is not independent novelty evidence. A mirror of this assigned 2026-10-11 finding returned as the highest-ranked Resultary hit is not counted as independent prior art.

## value

PASS

Exact local and large-radius nonlinear corrections describe a natural implicit nonquadratic extremizer of a sharp functional inequality and determine the dual zero region and its precise open boundary. The dimension-dependent singular exponents and reciprocal cones give mathematical geometry and nontrivial information on the scalar maximizer; not just substituting constants into a known norm bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
