---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The complete graph graphic matroid is connected with base-polytope dimension m-1, m=n(n-1)/2. Feichtner–Sturmfels connected restriction/contraction flacet criterion yields x_e>=0 and x(E(S))<=|S|-1 for every proper S of size 2..n-1. At vertex 1_T, the former are tight for e outside T, the latter for T[S] connected. The primitive normal-cone rays comprise -[e_f] for non-tree f and [sum_{e in E(S)}e_e] for each proper connected S. In particular S is each tree edge, so the ray set integrally generates N=Z^E/Z*1; the divisor exact sequence has saturated image and torsion-free cokernel of rank (m-n+1+c)-(m-1)=c-n+2. Connected induced subtrees count tau=c+n+1, yielding rank tau-2n+1. Distinct endpoint paths give tau>=n+binom(n,2), equality only paths; leaf-removal induction gives tau<=2^{n-1}+n-1 with equality only stars. Independent enumeration of all 16/125/1296 labeled K4/K5/K6 trees reconstructed rank ranges 3..4/6..11/10..26. Finite tests support, not prove, all n.

## originality

PASS

PASS limited to explicit integral local class-group computation for the complete-graph graphic matroid toric variety and its tree-type rank range. General matroid flacet theorem, toric divisor exact sequence and tree subtree-count extrema are prior, not new. No exact per-tree class-group statement located, but specialization is short and a higher-priority implicit computation remains possible.

## value

PASS

Local Weil divisor class groups measure local non-Q-factoriality, a standard birational-toric invariant. The all-tree closed formula and sharp path-to-star quadratic/exponential range identify distinct singularity complexities inside one natural toric variety; integral saturation removes torsion ambiguity. This is a coherent complete local classification rather than an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
