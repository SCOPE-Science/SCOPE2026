---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Centrality and W=[L,L] force B(W,W)=0. On V the trilinear B([x,y],z) is cyclic and vanishes on repeated arguments by the alternating bracket; this also proves alternation in characteristic two. A missing edge in any of the three pairs kills its coefficient. Assigning triangle coefficients independently and assigning arbitrary symmetric A gives the converse. Testing with only one triangle coefficient detects each of its edge coordinates separately, while the arbitrary A detects all vertex components, proving the common radical. Split off the 2r block on perfectly paired complements for the mixed pairing of rank r. Its inverse has zero vertex-vertex corner, so the remaining Schur complement is exactly A restricted to the kernel of the transpose mixed pairing. Each active windmill triangle contributes the two private dual coordinates and the shared hub dual coordinate, giving cross rank 2k+1 for k>0. Restriction of A is surjective with the stated constant-size fibers; choosing the radical and a nonsingular symmetric form on the quotient counts every restriction once. Independently, bordered matrices give ν_j=q^(j−1)(q−1)(ν_(j−1)+[j−1 choose 1]_q ν_(j−2)) for j≥2, starting with 1 and q−1: an invertible leading block permits q−1 last diagonal choices for every border, and a one-null-direction block needs a border nonzero on its radical but any last diagonal. Larger nullity cannot give invertibility. The recurrence yields the two stated products in every characteristic. All active triangles give rank 2n; with one inactive triangle the upper bound is 2n−2 and equality requires a nonsingular binary-dimensional restriction, counted by ν_2=q²(q−1). With two or more inactive triangles the upper bound is smaller for t≥2. The t=1 exception and the corank conclusions follow. Frozen small-field verification was inspected, not executed.

## originality

PASS

The known three-form framework, graph construction and real metric-existence criterion are not the novelty. Even the complete single-triangle form space in characteristic zero appears explicitly in prior work. The all-graph forced-radical description and, chiefly, the uniform all-finite-field windmill census and missing rank are supported distinct content: none of the inspected strong matches computes the interacting triangle mixed ranks and ensuing distribution. The assessment is bounded to inspected evidence, not absolute priority.

## value

PASS

The dimension of the parameter space alone does not tell how much degeneracy is unavoidable or how common each radical dimension is. The windmill is a natural connected test family where each edge belongs to a triangle but a full metric is impossible once t≥2. The census quantifies that contrast for every finite field, with a sharp smallest radical and a missing next radical dimension. Independent triangle coefficients for general graphs and the explicit all-rank distribution are useful beyond the known real existence criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
