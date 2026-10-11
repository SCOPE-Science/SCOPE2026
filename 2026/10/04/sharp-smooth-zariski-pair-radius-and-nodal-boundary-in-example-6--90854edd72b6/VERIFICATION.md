---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The affine singular locus is exhaustive because the homogeneous cubic part is parameter-independent and splits into three distinct directions at infinity, while fresh exact lexicographic elimination of \(u=u_x=u_t=0\) reproduced the two factors \(s^2(s-84)^2(2s+1)(10s+1)(20s+1)\) and \(s^2(s-14)^2(s+18)(5s+2)(20s+9)\). Fresh substitution at \(s=-1/20\) reproduced the singular point \((31/10,45/4)\) and Hessian determinant \(369/25\). The package then checks the remaining exceptional fibers, line discriminants, square restrictions to both conics, overlap values, and exact Rouché inequalities. Those inequalities exclude every other obstruction in the punctured centered disk, while the boundary node makes the radius sharp.

## originality

PASS

The primary source explicitly says only that some sufficiently small \(\varepsilon>0\) exists for which smoothness, three distinct intersections with \(L_1\), and six distinct tangencies hold. It does not state the exceptional parameter sets, node locations/types, or the maximal centered radius. Fresh Resultary search returned the audited record as the only exact same-family hit, and targeted source/formula searches found no implication-equivalent prior computation.

## value

PASS

The parameter family is not an arbitrary slice: it is the explicit family used to construct degenerating Zariski pairs in the source. Replacing an unspecified small neighborhood by the exact first obstruction, and classifying every singular fiber of both printed families, gives reusable local moduli/degeneration data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
