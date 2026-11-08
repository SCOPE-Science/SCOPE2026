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

The strip removes two congruent triangular caps of Euclidean area (1-h)^2 cot(pi/n) each. The polar is conv(P_n^circ,(±1/h,0)), replacing two polar edges by triangles of area (1/h-1)tan(pi/n), yielding A_n=n sin(pi/n)cos(pi/n)-2(1-h)^2 cot(pi/n) and B_n=(n-2+2/h)tan(pi/n), hence the claimed product. Differentiation gives M_n′(h)=2 G_n(h)/h², with G_n(h)=2+(2n-6)h²+(4-2n)h³-nq and G_n′(h)=-2h[3(n-2)h-2(n-3)]. For even n>=6, G is strictly decreasing on [cos(2pi/n),1], with positive lower endpoint and negative upper endpoint; n=4 has direct quadratic M_4=8+4h-4h². Thus a unique interior maximum follows. Inserting w=1-h_n=q/2+O(q²) into the exact difference yields gain pi^4/(2n³)+O(n^-5); the regular polygon benchmark increment is 4pi^4/(3n³)+O(n^-4), giving 3/8. Independent geometric polygon/polar area and root checks corroborate several even n. No finite check is substituted for the general polar and derivative proof.

## originality

PASS

Meyer–Reisner’s optimal-volume-product regular polygon result provides the external at-most-(n+2)-vertices benchmark, and shadow-system theory gives qualitative deformation framework, but neither readily supplies this exact one-strip polar-area profile and unique interior maximizer. Lin–Leng studies product-reducing vertex removal in a planar symmetric minimum setting, not the strict interior max along a prescribed clipping family. Related published 3D cube–cross-polytope Mahler interpolation and simplex difference-body profiles use other bodies. The constrained even-polygon formula and 3/8 efficiency limit remain original by checked statements, with a direct 2011 source full-text access risk.

## value

PASS

The two-corner clipping deformation is canonical, low-dimensional and motivated by known polygonal upper extremals and symmetric Mahler volume products. An exact optimum shows maximal Mahler gain is achieved by partial rather than complete corner deletion and quantifies its share of the ideal extra-vertices gain. This is not an arbitrary slice of a table or a mere endpoint computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
