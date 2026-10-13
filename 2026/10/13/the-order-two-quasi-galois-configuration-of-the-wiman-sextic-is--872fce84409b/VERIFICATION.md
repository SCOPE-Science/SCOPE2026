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

The exact finite certificate is `artifacts/verify.py`. It uses only Python's standard library and exhaustively enumerates \(A_6\) inside \(S_6\). It checks: \(45\) double transpositions; four commuting neighbors for each; exactly \(30\) Klein four-groups; their two conjugacy orbits of size \(15\); one subgroup of each type through each involution; the bijection with the \(45\) duad-syntheme incidences; the equivalence between commutation and shared incidence endpoint; and that the resulting \(30\)-vertex bipartite graph is connected, cubic, and has girth \(8\).

Fresh package execution output:

`VERIFY_OK involutions=45 degree=4 V4=30 orbits=15+15 each_involution=2 duad_syntheme=TutteCoxeter commuting=line_graph girth=8`

The certificate does not reprove the cited algebro-geometric statements about the Wiman sextic or the published Wiman line-arrangement census. Those are explicit premises of the proof. No claim of independent validation is made.
