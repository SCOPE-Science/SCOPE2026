---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The displayed integral cubics were reconstructed independently and their critical system recomputed. Exact elimination gives a squarefree base resultant of degree nine with nine real roots and a squarefree critical resultant of degree twenty-one with twenty-one real roots. Exact division leaves a monic degree-twelve quotient, coprime to the base resultant, squarefree, with twelve real roots. Lexicographic Groebner bases place both zero-dimensional ideals in shape position; the base Jacobian ideal is the unit ideal, so the nine base points are transverse. On the critical quotient, \(F_2\) is nonzero. The determinant of the Hessian of the corresponding pencil member reduces to a polynomial coprime with the degree-twelve quotient, proving all twelve extra singularities are ordinary nodes. Eliminating the pencil parameter gives a squarefree degree-twelve polynomial with twelve real roots, hence distinct real critical values. Independent projective Groebner checks rule out singular pencil points at infinity and verify smooth affine generators. These computations reproduce the claimed \(\#S=12\) and the genericity boundaries exactly; no floating-point root sampling is used.

## originality

PASS

The initiating Newton-homotopy paper proves \(\#S\le3(d-1)^2\) for equal degrees and then gives sharp examples only for \((2,1),(2,2),(3,1),(3,2)\), explicitly leaving existence of sharp examples for all degree pairs open. Classical real cubic-pencil theory is broader in a different direction: a generic cubic pencil has twelve nodal singular members, and real pencils can have all twelve singular members real. That prior theory covers the geometric possibility of twelve and is therefore excluded from the novelty claim. Fresh exact-coefficient searches found no scientific source containing the submitted pair. The surviving claim is coefficient-specific: this exact integral pair satisfies the Newton-homotopy genericity conditions, has nine transverse real base points and twelve non-base real singular starts with distinct real values.

## value

PASS

The initiating 2026 paper explicitly leaves sharpness beyond its four examples open, making the omitted equal cubic case a natural benchmark. An integral pair with an exact all-real, all-simple, nodal, distinct-critical-value certificate is a reproducible test instance in that framework. Although classical theory already guarantees broad twelve-fiber phenomena, the precise certified witness has concrete computational-algebra value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
