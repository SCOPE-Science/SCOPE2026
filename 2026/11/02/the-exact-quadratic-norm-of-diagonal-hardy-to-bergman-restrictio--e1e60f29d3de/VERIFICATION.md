---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For F(z1,z2)=z1^2 P(z2/z1), normalized H^1 is int_T |P| and normalized A^1 of diagonal P(1)z² is |P(1)|/2. Complex conjugation and reversal preserve the normalization P(1)=1 and L1 norm; their convex average yields real palindromic P_u=u+(1-2u)z+uz² globally without loss for minimization. Then G(u)=average |1-4u sin²(theta/2)| is convex for all real u; its critical point has v=sin(tau), tau=cos(tau), giving min=2tau/pi and exact restricted norm pi/(4tau). Independent high-precision quadrature verified tau root, 2tau/pi integral to <1e-38 and ratio 1.06266264615663 > pi/3; five additional trial polynomials checked. These numerical checks are not the universal argument.

## originality

PASS

Best-of-knowledge qualified: the 2026 exact-diagonal study demonstrates general p>=2 contractivity and a linear p=1 test, while this computes the exact all-complex quadratic restriction. Classical Nikolskii/Arestov general inequalities are related, but the inspected Arestov endpoint concerns a geometric-mean functional rather than this degree-one L∞/L1 trigonometric extremum; no decisive covering exact n=1 theorem was located. Full primary study could not be accessed, and a differently indexed classical evaluation formula is a priority risk.

## value

PASS

The degree-two homogeneous slice is the first natural extension of the known linear H1 diagonal test, and computing its sharp three-complex-coefficient operator norm gives an explicit, strictly stronger lower bound for the unresolved unrestricted H1-to-A1 norm. The transcendental extremal parameter and full optimizer are natural outcomes of the finite-section operator norm rather than an arbitrary parameter choice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
