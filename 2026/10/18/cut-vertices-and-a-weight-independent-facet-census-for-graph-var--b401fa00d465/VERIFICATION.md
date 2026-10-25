---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Verified the precise norm N(f)=||f||_infty+sum(w_e|f_i-f_j|), finite simple graph, positive real weights, and path n>=2. The level-set identity f=(1/2)int_{-r}^r s(t)dt and integrated cut weight give an exact convex combination of s/(1+2C_w(s)). The edge-sign linear functional L_s dominates by N(f) with equality only on the positive ray of s, exposing all 2^n vertices even when disconnected. For paths, N is the maximum over j,sigma,epsilon of signed coordinate and edge-difference forms. A unique absolute maximizer with signs forces the two adjacent epsilon constraints. Conversely tiny steps realize an open cone for each such form, hence a true facet. Distinctness of normals and endpoints/interior counting give (n+2)2^(n-2). Retrieved and read verification/verify.py: exact fractions, independent active-vertex rank tests (n<=5 facets, up to n6 vertices) support but do not prove the general result.

## originality

PASS

The exposed-vertex formula uses a standard graph coarea decomposition, duly credited; the original assertion assessed is the fully exposed norm-ball representation together with the complete weight-independent path facet census, not novelty of graph TV or min-cut. Five-source searches in Resultary and targeted literature returned work on graph-TV, weighted graphical zonotopes and Lipschitz-free facets but no implication yielding this additive sup-plus-TV path facet law. Same ambient vertex graph alone does not establish an identical polytope; residual priority risk remains.

## value

PASS

The weighted graph total-variation plus sup norm is a natural regularization norm; its exact dual extreme sign signals and complete combinatorial facet count constrain convex optimization geometry. The formula is uniform over arbitrary strictly positive edge weights and all path lengths, more than a numerical instance or reparameterization of a textbook cube. Min-cut threshold characterization is a useful subsidiary computational description.

The dated certificate retains the supplied scientific assessment, sources and limitations.
