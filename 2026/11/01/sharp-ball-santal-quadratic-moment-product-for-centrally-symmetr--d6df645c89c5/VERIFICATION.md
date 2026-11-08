---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Affine normalize a centered three-zonotope to generators (1,0),(0,1),(p,q), p,q>0. Independently reconstruct the six vertices, six polar support vertices, and unnormalized tensor moments from exact polygon determinant formulas: their trace product reproduces 8N/(9D) for x,y,z pairwise absolute generator determinants. The algebraic upper gap 75D-64N expands at x=W+U+V,y=W+U,z=W to exactly 46 positive integer monomials, including 1024 W^7(U^2+UV+V^2): it vanishes only at U=V=0. The lower gap factors as 8pq H(p,q)/(9(1+p)^3(p+q)^3(1+q)^3), with all 19 coefficients of H positive, and tends to 0 as one positive generator shrinks. At p=q=1 the exact moment gives 25/24; limiting parallelograms have 8/9. Hence no extrapolation from finite tests is required.

## originality

PASS

The earlier Ball/Santaló general inequality caps this quadratic moment by the disk value pi^2/8, which is larger than 25/24, and does not determine the sharp affine-regular hexagon subclass. Directly related Resultary hexagon findings concern enclosing-parallelogram area and other invariants; the l_p moment-product work is only a one-parameter family. No matched full all-hexagon polar moment result in the actual searches; best-of-knowledge PASS, not priority certification.

## value

PASS

The quadratic Ball–Santaló polar moment is a classical affine invariant. Determining its *sharp* global range, unique affinely regular optimizer, and nonattained parallelogram boundary in the complete natural centrally symmetric six-gon moduli gives a nontrivial structural polygon extremal theorem. The 46-monomial certificate is materially stronger than quoting the general ellipsoid inequality; its exact constant is not a routine substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
