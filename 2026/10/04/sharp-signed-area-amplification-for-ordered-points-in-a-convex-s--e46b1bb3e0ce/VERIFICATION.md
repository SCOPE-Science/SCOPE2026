---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For an arbitrary cyclic m-point list in convex H, Keller Lemma 3.3 proves the signed shoelace bound F≤area(H) on every 3–5 point list without simple-polygon assumptions. For m≥6 remove P1,P2,P3 to form (P0,P4,…,P_{m−1}); the exact determinant telescoping identity F(P)−F(Q)=F(P0,P1,P2,P3,P4) yields F(P)≤area(H)+F(Q). Induction gives floor(m/3)area(H); reversing the list obtains |F|. Taking an H-triangle and tracing its A,B,C loop q=floor(m/3) times, inserting r=m−3q repeated vertices, attains q area(H) exactly for every m. This also covers repeated/degenerate locations and area-zero H; the theorem is signed area, not unsigned self-intersecting lobe area. Checked the exact cancellation identity and equality construction directly from determinant algebra, not logs.

## originality

PASS

Keller 2026 §3.3 explicitly proves only factor one for m=3,4,5 and notes its failure at six due to twice traversing a triangle, then pursues geometric fan/chord hypotheses for factor one at longer lengths. The submitted all-m optimal unconstrained factor floor(m/3), with every residue class attained, is not in the inspected source. Fáry–Makai edge-vector convexification does not maintain vertex containment in H and therefore does not yield this area(H) coefficient.

## value

PASS

Keller’s work makes the arbitrary-order longer-polygon failure a concrete gap; the exact all-length best universal constant and its equality mechanism supply a useful baseline separating unconditional shoelace bounds from stricter geometric hypotheses. This solves a natural complete extremal profile rather than an arbitrary numerical sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
