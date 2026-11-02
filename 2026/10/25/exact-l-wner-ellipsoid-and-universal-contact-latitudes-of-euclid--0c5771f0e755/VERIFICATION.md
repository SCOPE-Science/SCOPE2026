---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For every d>=2 and h>0, capsule K=B_2^d+[-h,h]e_1 has support 1+h|u_1|. The positive root t of d t^2+(d-1)h t=1 lies in (0,1), and proposed A=(1+ht)(1+h/t), B=1+ht yield exact support square slack h/t (|u_1|-t)^2. This proves global inclusion and precisely two latitude orbits of contacts; the tips are not contacts since A-(1+h)^2=(h/t)(1-t)^2>0. Under Löwner normalization contacts have axial ±1/sqrt d and transverse sqrt((d-1)/d), and their symmetric measure satisfies first moment zero and covariance I_d/d. Any enclosing ellipsoid with shape Q and center c then has tr(Q^-1)/d+c^T Q^-1 c<=1; AM–GM gives det Q>=1 with equality only Q=I, c=0. This proves global uniqueness without symmetry assumption. Volume factor (1+ht)^(d/2) sqrt(1+h/t) tends to exp(tau u_tau/2)/u_tau when h sqrt d→tau; when it diverges, ratio/(h sqrt d)→sqrt e. Independent numerics confirmed support and latitudes for d=2,3,8,23 and varied h, not the quantified asymptotic itself.

## originality

PASS

Best-of-knowledge PASS qualified by inaccessible full Yıldırım 2006 text: its accessible abstract solves approximate enclosing ellipsoid of the convex hull of m ellipsoids, which covers this object as an input but does not assert the exact symbolic capsule optimizer or crossover. Güler–Gürtuna list other explicit bodies; Halder 2018 centered ellipsoids do not include separated generating centers.

## value

PASS

A spherocylinder/capsule is the simplest nonellipsoidal convex hull of two balls. Exact enclosing ellipsoid in every dimension and separation, strict tip noncontact, universal normalized contact latitudes and sharp dimension crossover supply a natural geometric invariant not a fixed table or mere general ellipsoid-existence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
