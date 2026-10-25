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

The standalone `verify.py` reconstructs two-level Latin complexes for cyclic groups and products of cyclic groups. It checks complete colorful edge/face counts, that every full edge has two triangles, separation into exactly the quotient-coset surface pieces, piecewise link cycles, incidence-graph connectivity and cycle rank, and modular boundary ranks over \(\mathbb F_2\) and \(\mathbb F_{1009}\) for groups of order at most ten. The run passed 42 nongenerating-gap instances and all associated generating-gap control instances.

The all-parameter mathematical argument is in RESULT.md: the subgroup-coset decomposition, closed-surface recognition, orientability, and graph-of-spaces homotopy splitting. The finite tests provide independent consistency checks but are not a proof of arbitrary finite group cases. The review is internal same-model only; independent audit is not performed.
