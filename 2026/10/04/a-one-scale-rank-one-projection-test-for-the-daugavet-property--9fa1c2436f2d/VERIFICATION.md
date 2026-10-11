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

For \(0<t\le1\), the identity \(I+\sigma P=(I+\sigma tP)+\sigma(1-t)P\) forces the sharp lower bound, while the triangle inequality gives the matching upper bound. For \(t\ge1\), the decomposition \(I+\sigma P=t^{-1}(I+\sigma tP)+(1-t^{-1})I\) does the same. Every rank-one \(T=f\otimes x\) satisfies \(T^2=f(x)T\); if the scalar is nonzero, \(P=T/f(x)\) is a projection and \(T^2=f(x)^2P\), a positive multiple over the real field. Thus the projection hypothesis yields Langemets’s signed-square property for every rank-one operator, which characterizes Daugavet in real dimension greater than one.

## originality

PASS

Langemets’s primary arXiv record states that either signed square identity for every rank-one operator characterizes the Daugavet property in real dimension greater than one, but the accessible material does not state the one-scale projection-only criterion. The older bad-projection condition is only a lower bound and is explicitly known not to be equivalent to Daugavet. Exact web and Resultary searches for every-rank-one-projection/idempotent formulations found no earlier fixed-scale identity with right side \(1+\|P\|\).

## value

PASS

The theorem isolates a natural exact projection boundary: a single-scale equality on rank-one idempotents suffices, while the classical bad-projection inequality is strictly weaker. This makes the newest square characterization easier to test on a distinguished operator class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
