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

After specializing the golden-ratio coefficient phi to 3 modulo the ramified prime 5, F=-(X²+Y²)(Y²+Z²)(Z²+X²)-3(X²+Y²+Z²-W²)²W² up to a unit. Independent Gröbner checks on all four projective affine charts show the Jacobian ideal contains each local t^5-t, so no geometric singularities outside F5 and the singular coordinate ring is reduced. Independent exhaustive F5 chart counts [75,13,3,0] for points and 65 singular nodes with nonzero Hessians; independent direct F25 arithmetic (theta²=2) counts [1635,13,3,0] (1651 total). The 65 split A1 exceptional conics add 65q points, giving Y(F5)=416 and Y(F25)=3276. Adjunction/K resolution gives K²=24, chi=11, c2=108, b1=b3=0, b2=106; F25 count saturates 1+25²+106*25, forcing Frobenius squares=25. Trace 390 at F5 gives multiplicities +5=92,-5=14 and exact all-extension zeta. Finite counts are exhaustive only over F5/F25; cohomological rigidity supplies the infinite statement. No claim about Picard rank or other integral models.

## originality

PASS

Classical Barth 65 complex nodes, equation, and Jaffe–Ruberman bound are known and not claimed new. Complex geometry does not force the node scheme to remain split and ordinary under ramified mod-5 specialization, or F25 maximality and all-extension zeta. Actual independent finite-field counts establish new arithmetic assertions not located in targeted sources or indexed research search. The 1996 original full paper was not read, and unindexed characteristic-five computations remain historical priority risks.

## value

PASS

Prime 5 ramifies in the golden-ratio coefficient ring; preserving all 65 rational nodes is a nontrivial special-fiber rigidity fact. Maximality over F25 forces a complete Frobenius spectrum and exact zeta data for a distinguished general-type surface. A natural arithmetic-geometric invariant, not an arbitrary finite-field census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
