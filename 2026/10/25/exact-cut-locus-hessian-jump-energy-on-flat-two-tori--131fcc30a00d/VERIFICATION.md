---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For a full-rank Euclidean lattice in dimension two, a regular cut-locus Voronoi facet F_v identifies two closest lifts 0 and v. Their unit-distance gradients jump by j(x)=|v|/|x|; since F_v is centrally symmetric about v/2, parameter t along its length ell_v gives j²=|v|²/(|v|²/4+t²). Integrating from -ell_v/2 to ell_v/2 yields 4|v| atan(ell_v/|v|). Count only one facet from each opposite pair; triple intersections are H¹-null. For rectangular 2a by 2b torus, J_2=8a atan(b/a)+8b atan(a/b). At area A=4ab, writing r=b/a the normalized function is symmetric under r<->1/r, and its derivative strictly negative for r>1, so unique square maximum 2πsqrt(A).

## originality

PASS

Best-of-knowledge new quantity is the explicitly defined squared cut-locus gradient-jump aggregate and its sharp rectangular fixed-area maximum. Prior general Hessian formulas already identify the local jump and are not claimed new.

## value

PASS

J2 measures concentration of the singular Hessian jump on a cut locus and is a natural scalar geometric functional on flat tori. The exact facet-sum and sharp square extremizer under fixed rectangular area provide a reusable quantitative shape benchmark beyond merely displaying the local distributional Hessian tensor.

The dated certificate retains the supplied scientific assessment, sources and limitations.
