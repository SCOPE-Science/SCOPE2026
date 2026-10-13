---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof was reconstructed from the independent-set lemma and iterative recoloring proof of arXiv:2609.21286v1. The varying-list modification was checked at the two points where it matters: existence of at least \(d+1\) currently available permitted colors and Borel selection of the indexed available color.

For every vertex \(x\), the hypothesis gives \(|L(x)|-d_G^+(x)\ge d+1\). Thus the update is always defined. If a neighboring source recolors, at most one of the \(d+1\) random indices can create a conflict with the old color of \(x\), so the original geometric recurrence remains valid with \(d_G^+(x)\le d\). The series of sadness probabilities is summable, so Borel--Cantelli applies pointwise.

The limit map is Borel because eventual constancy at a natural-number color is a countable Boolean combination of Borel events; a fixed fallback list color is used only on the null nonconvergence fiber for each vertex. Every intermediate and fallback color lies in the assigned list. For each fixed edge, finite out-degree allows simultaneous stabilization of the source and its out-neighbors on a probability-one event, proving the edgewise conclusion.

The proof does not establish a single realization proper on all edges simultaneously, and it does not establish pointwise optimality of the nonuniform threshold. Independent audit has not been performed.
