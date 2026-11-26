---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Debarre–Manivel require δ⁻=min(δ,n−2k−r)>0 for the connected smooth nonempty scheme in expected dimension. Their strict-positivity equivalence away from a single quadric applies here. In the quadric case δ=1 gives (k+1)(2n−3k−2)=2, so k=1,n=3, excluded and correctly known to have two rulings. Hiep's formula, equivalently Grassmannian adjunction, gives g=1+Be/2 with e>0. With q=k+1 and R_i=binom(d_i+k,k), the expected-dimension identity gives qB=Σ(d_i−1)R_i−q²−1. For r≥3 the sum is at least 3q(q+1)/2≥(q+1)², with equality only at q=2, three equations, all quadrics. For r=2, two quadrics give 1+ΣR_i≡1 mod q and are inadmissible. One cubic or larger gives the lower bound q(q+1)(2q+7)/6>(q+1)². A single degree ≥3 for q≥3 gives q(q+1)(q+2)/3>(q+1)². At q=2 a hypersurface has even degree by divisibility, and hence after the quadric exclusion d≥4, giving d²−1>9. Equality therefore forces k=1,n=6 and the three quadrics. Independently, on Gr(2,7) the Plücker degree is the coefficient of x⁶y⁵ in (x−y)(x+y)[4xy(x+y)]³, namely 64(6−4)=128, giving g=129. This also confirms unique distance g−e=1 and no genus-zero or genus-one case in the stated range. The bundled script was inspected, not executed; its finite grid and fixed degree calibrations are not the proof.

## originality

PASS

The geometry theorem, genus–degree identity and numerical equality specimen are known. The distinct claim is universal sharpness and uniqueness over every allowed k, codimension and multidegree, proved by the arithmetic classification under δ=1.

## value

PASS

For naturally polarized moduli curves in Grassmannians, this gives a sharp universal lower bound on the canonical-to-Plücker ratio and locates the only extremal complete-intersection type. It excludes rational and elliptic curves in this family and distinguishes the three-quadric curve from all other admissible families, rather than merely recomputing its known genus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
