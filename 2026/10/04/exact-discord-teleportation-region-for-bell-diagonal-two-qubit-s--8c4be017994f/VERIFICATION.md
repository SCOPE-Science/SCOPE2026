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

With ordered magnitudes s1>=s2>=s3 and q=s1+s2+s3, positivity reduces up to Bell symmetry to s1+s2-s3<=1. Writing y=s2,z=s3 yields exactly (q-1)/2<=z<=q/3 and z<=y<=(q-z)/2. D_G=(y^2+z^2)/3. The minimum occurs at y=z and smallest z; for the maximum y=(q-z)/2 and convexity leaves endpoint z values. Their difference crosses at q=15/13, i.e. F=9/13. Connectedness and continuity give every intermediate value. The exact-rational verifier independently checks a Bell-probability grid and both extremal families.

## originality

PASS

Checked Bell-diagonal literature supplies the tetrahedral state geometry, geometric-discord formula and broad teleportation/discord inequalities, but no inspected source gives the exact fixed-average-fidelity attainable interval or the 9/13 upper-extremizer crossover. Roszak--Cywinski use a different best/worst-case fidelity functional. Resultary did not surface a covering same-statement theorem.

## value

PASS

This is a complete sharp tradeoff region between two standard quantum-information quantities on a canonical state family, not merely a new inequality. The upper-extremizer phase change at F=9/13 is structurally informative.

The dated certificate retains the supplied scientific assessment, sources and limitations.
