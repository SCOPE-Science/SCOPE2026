---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Represent the centered simplex vertices by coordinate differences. Two faces I,J have trivial direction-space intersection exactly if |I∩J|≤1 (by affine independence); disjoint face spaces are orthogonal. For |I∩J|=1 their basis Gram blocks, after common scaling, equal I_r+J_r, I_s+J_s and cross block all ones. Since (I_r+J_r)^−1=I_r−J_r/(r+1), the largest cosine is √[r/(r+1)]√[s/(s+1)]. The permissible r+s≤n maximizes at r+s=n; balancing the positive integers uniquely maximizes rs/((r+1)(s+1)), proving all n≥2 and equality cases. Algebra gives 1−c²=(n+1)/((r+1)(s+1)), and insertion into the source M formula yields the stated radius. Inspected all actual proof and verifier code, including finite exact rank n≤6 and dimension comparisons n≤100, auxiliary only.

## originality

PASS

The original far-observer theorem defines an abstract angular maximum for polytopes; it does not compute the all-dimensional regular-simplex value or classify its balanced-face maximizers. Standard facet dihedral-angle formula is a different optimization.

## value

PASS

Turns the naturally required but implicit worst-face-angle constant in a general geometric theorem into a closed all-dimensional simplex benchmark and identifies its exact extremal face type. The explicit sufficient radius is motivated by the parent observer theorem, not an arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
