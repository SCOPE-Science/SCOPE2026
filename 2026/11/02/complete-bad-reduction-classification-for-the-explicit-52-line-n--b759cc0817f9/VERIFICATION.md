---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For the literal integral 52-line quartic equation in Veniani Example 5.5, independently checked 8F=-Q under the invertible odd-characteristic coordinate change. The fifteen integer principal minors are -4,0,4,0;-4,-25,-1,-1,-1,-4;-24,8,24,-8;64, so nonzero determinant primes are only 2,3,5. Kernel-support analysis over algebraic closures gives exactly two axis singularities in odd characteristics other than 3/5, eight extra points in characteristic 3 and two extra in 5. Independently evaluated local affine Hessian determinants at all five singularity types (nonzero mod p), hence A1 nodes. In characteristic 2 F=H^2(x0*x3+x1*x2), all four partials generate H^2 times the irrelevant coordinate ideal, and projective saturation yields (H^2); G is smooth with two-line intersection with H=0. The determinant argument, not finite enumeration of primes, establishes the all-prime claim. No line-count statement beyond prior work.

## originality

PASS

Veniani already printed the exact integral equation, 52 complex lines, two complex nodes, ten characteristic-3 nodes, four characteristic-5 nodes, and noted a characteristic-2 singular line. This audit credits those results and regards only the complete absence of exceptional odd primes outside 3/5 plus the entire characteristic-2 doubled-plane Jacobian scheme and uniform minor proof as candidate novel. Primary Example 5.5 read directly; specialized unindexed modular analyses remain a priority risk.

## value

PASS

An exact reduction-type boundary and nonreduced Jacobian scheme for an extremal nodal quartic are natural arithmetic-geometric invariants. A uniform support/minor certificate distinguishes all good odd reductions from bad reductions, rather than re-tabulating known small-prime point counts. Applies only to the published integral presentation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
