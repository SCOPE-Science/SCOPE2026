---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For generic complex symmetric sparse matrix on a spider T, differentiation in independent diagonal variables makes Sing(det M=0) exactly corank>=2. Path blocks with all nonzero edge parameters have nullity <=1, and if s singular arms attach at center, global nullity=s-1, yielding Z_{ijk} for triples. If some edge parameter vanishes, cut-forest ranks put the point either in Y_e (singular components on opposite sides) or in a centered truncated spider with three singular arms, again Z. Irreducibility follows from leaf expansion and primitive linear-polynomial Gauss; Y_e and Z_{ijk} have disjoint-variable prime complete-intersection defining equations. Their codim3 degrees are |A_e||B_e| and ell_i ell_j ell_k; rank-three restriction to Sym² of the two-dimensional kernel yields generic transverse uv-w² ordinary nodes, and Serre R1/S2 yields normality. Independently checked aggregate degree identity for 5,440 arm-length profiles; source script inspected, its claimed finite ranks are not universal proof.

## originality

PASS

General symmetric corank-two degeneracy and aggregate degree are old; the reviewed result is the explicit irreducible Y_e and arm-triple Z_ijk decomposition, component degrees and generic analytic local models for all genuinely non-star spiders, which inspected general determinantal and Parter-type results do not state as such. Possible older starlike sparse-matrix formulation remains.

## value

PASS

The complete reduced singular-component and generic-transverse classification, with explicit degrees under changing arm lengths, is a natural algebro-geometric invariant of sparse determinant hypersurfaces. It resolves coordinate degenerations and nontrivial branching, exceeding a classical aggregate degree or an arbitrary finite case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
