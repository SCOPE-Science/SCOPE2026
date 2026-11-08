---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Reconstructed actual RESULT.md's precise claim for equal-depth icosahedron edge truncations T_t, 0<t<1/2, and the active normal criterion. Independently implemented exact Q(phi) arithmetic and great-circle local-sector traversal (not simply reading verification logs). Enumeration from the twelve base vertices gave 30 edges, 20 triangular facets, 60 oriented-edge truncated vertices and 32 outward normals in 16 antipodal pairs. Enumerated all intersection rays and nested tangent perturbation sign sectors; deduplicated exactly 152 chambers, with strict-illumination counts 132 of 20 and 20 of 21; independent exact witness computations returned 21 for (1,1,1) and 20 for (-2,0,1). Independently tested every active facet inequality at t=1/4,1/3,2/5,49/100 and reconstructed the symbolic argument that equal-depth truncation keeps the same five-vertex cut and six-vertex original-face incidences for all 0<t<1/2. Each great-circle chamber boundary contains an intersection ray; each local sector touches an incident circle half-ray, so the traversal is exhaustive even at multiway intersections. Nongeneric directions cannot improve a strict inequality count because illuminated vertices persist in sufficiently small generic perturbations. Applying the already-known vertex-transitive averaging identity gives lower and upper fractional weight 60/21=20/7. Original verify.py and 152-row cells.csv were read from exact Git blob SHA tree, though the original checker was not locally executed; new independent exact checker printed INDEPENDENT_CERT_OK. Endpoints t=0,1/2 and arbitrary deformations are not claimed.

## originality

PASS

Best-of-knowledge PASS after fresh Resultary searches and full-text comparison of the same truncated solid's 2012 weighted source illumination study, the 2009 fractional foundational theorem and complete published Resultary Platonic-solid theorem. The vertex-transitivity formula i*=f0/alpha is established prior art, but none of the inspected works or their mathematical implications gives alpha=21 for the 60-vertex truncated icosahedral normal fan or the 132/20 split of its 152 open chambers. The nearest same-object 2012 table has a different objective (norm-gauge-weighted finite point sources) and an upper estimate, not this exact unweighted fractional invariant. Gorodzha 2026 global bound is accessible from abstract only and is numerically weaker; inaccessible full text remains a priority risk, not automatic failure. Originality is provisional, not certified exhaustive.

## value

PASS

Regular truncated icosahedron is a canonical sixty-vertex Archimedean solid with a previously studied illumination problem. Exactly identifying its nonintegral fractional illumination invariant 20/7 and a rigid two-level count of illuminated vertices, together with the complete 152-cell direction-spectrum and uniform persistence over the entire natural nondegenerate truncation interval, answers a mathematically motivated sharp normal-fan/covering problem. The finite chamber count has a constructive completeness proof and is not an arbitrary small-instance calculation; prior generic bounds and four-source estimates do not supply the exact invariant. No ordinary-illumination improvement or broad Archimedean classification is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
