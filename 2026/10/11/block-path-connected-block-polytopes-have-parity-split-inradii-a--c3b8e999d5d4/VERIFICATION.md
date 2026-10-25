---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For n>=2, the zero-inclusive interval-indicator hull has exactly the nonnegative-coordinate facets and upper facets indexed by odd-support alternating-sign vectors. Two maximal upper normals a,b satisfy a+b=e1+en, and normalized ball-facet clearances therefore bound rho by 2/(2+||a||+||b||). Their norms give the displayed even/odd formulas. The even uniform center and odd two-level center satisfy every upper and lower clearance and attain equality. At radius rho, endpoint equations and the a-equation are three independent equalities (n>=3). A small parity-appropriate interior perturbation preserves the forced contacts while making all other facets strict, showing the affine incenter dimension is n-3. The n=2 square and n=3 unique-center cases are included. The finite LP and hull comparisons are corroboration, not proof of all dimensions.

## originality

PASS

The exact zero-inclusive connected-block path polytope has been studied for facets and Narayana/Ehrhart data by Bruckamp--Chimani--Juhnke. The published complete facet list is a critical mathematical input, but its theorems do not compute the Euclidean inball or dimension of the locus of optimal centers. Beck--De Silva--Dorfsman-Hopkins--Pruitt--Ruiz explicitly use a nonzero-only interval hull and study volume, Ehrhart and face data. The earlier connected-subgraph tree-polytope descriptions do not themselves give a Euclidean clearance optimum. Theorem-specific and alias searches did not find independently prior formulas; this is a best-of-knowledge assessment, not proof of historical novelty, and Geir Dahl 2011 remains an inaccessible full-text risk.

## value

PASS

The zero-inclusive interval-incidence body is a canonical block-path connected-subgraph polytope with a substantial combinatorial literature. Its Euclidean inradius is a natural exact invariant not preserved by its familiar unimodular root-polytope equivalence. A uniform all-dimensional radius formula with a nontrivial parity split and an (n-3)-dimensional incenter family answers a meaningful, intrinsic metric question; the double-facet tangency certificate and relative-interior analysis reveal the geometry beyond tabulating small cases. No new facet-classification theorem, weighted-generalization, or combinatorial type of the incenter polytope is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
