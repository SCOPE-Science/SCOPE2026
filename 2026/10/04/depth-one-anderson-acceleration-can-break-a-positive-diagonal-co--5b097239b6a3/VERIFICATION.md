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

The depth-one least-squares coefficient was re-derived and the exact rational recurrence independently replayed. At \(\varepsilon=1/200\), iterates one through five have both coordinates positive, while the sixth has second coordinate \(-4801559852330482770906299820259/349417867959904066964567555052100\), with positive first coordinate. The scaled limiting recurrence has nonzero least-squares denominators and a strictly negative limiting sixth second coordinate, so rational dependence gives an open small-\(\varepsilon\) family. In one dimension the first accelerated residual can be annihilated exactly and the iterate lands at the positive fixed point.

## originality

PASS

Qualitative loss of nonnegativity under Anderson acceleration is prior: Walker--Ni explicitly warn that AA may create negative entries. The audited claim is substantially narrower and stronger: a two-dimensional diagonal positive strict contraction, an open parameter family, five positive accelerated iterates before a certified sign crossing, and a proof that the analogous scalar affine class cannot fail. Fresh Resultary and web searches found safeguarding and nonnegativity-preserving variants but no implication-equivalent minimal-dimensional theorem or exact family.

## value

PASS

This is a motivated boundary result for an accelerator routinely applied to positive variables. It isolates a genuine multivariate cone-invariance failure even for a decoupled positive strict contraction, proves dimension two is minimal in the stated affine class, and provides an exact regression witness for safeguard design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
