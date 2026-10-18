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

Chefles gives the exact LOCC detection condition: product state in W_k=orthogonal to the other two but not psi_k. Independent triple makes W_k dim2, while psi_k functional has one-dimensional kernel spanned by nonzero C. With independent D, all candidates sC+tD detect iff t!=0, and are product iff det(sC+tD)=s²det C+st tr(adj(C)D)+t²detD=0. Over complex numbers this homogeneous quadratic has a projective zero at t!=0 unless its sole double root is t=0; that exceptional case is exactly det C=0, mixed term zero and detD nonzero. A line with this intersection is tangent to the smooth Segre quadric; the condition is invariant under changing adapted bases. Independent explicit C=[[1,0],[0,0]], D=[[0,1],[1,0]] gives determinant -t²; source Bell-pair example supplies a physical witness. This is exact algebra; random triples are not an infinite proof.

## originality

PASS

Chefles 2004 establishes product-detector necessity/sufficiency, and Niu–Griffiths describes product states in two-dimensional two-qubit subspaces using quadratic geometry. Yang et al. 2015 identify triple-state counterexamples. Neither inspected relevant primary theorem states the explicit iff triple scalar tangency test. The result is a synthesis/specialization of known detector and Segre concepts; equivalent matrix-pencil tangency formulation could preexist and is a clear residual risk.

## value

PASS

Three pure two-qubit states are the smallest nontrivial case where LOCC unambiguous identification can fail despite linear independence. Converting an existential product-state search into an exact projective tangency condition and three explicit determinant tests is a motivated classification/decision procedure in this boundary case; it distinguishes tangent, secant and contained-line cases. No optimization of success probabilities is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
