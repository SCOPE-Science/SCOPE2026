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

The proof is symbolic and applies to every nontrivial Steiner \(2\)-design. Its critical checks are:

1. Bipartiteness forces the neighborhood complex to split into point-side and block-side components.
2. The Steiner condition makes distinct block simplices share at most one vertex, and distinct point-star simplices share exactly one block.
3. A simplex can be collapsed relative to all its vertices onto any chosen spanning tree; the induction proof is given in `RESULT.md`.
4. Because no positive-dimensional face is shared between different maximal simplices, these collapses can be performed independently.
5. The collapsed point-side graph has \(v\) vertices and \(b(k-1)\) edges; the block-side graph has \(b\) vertices and \(v(r-1)\) edges. Both are connected.
6. The design identity \(bk=vr\) makes both cycle ranks equal to \(\mu=vr-v-b+1\).

`verify.py` reconstructs \(S(2,2,5)\), \(AG(2,3)\), \(PG(2,2)\), and \(PG(2,3)\), verifies all pair-incidence axioms, constructs both neighborhood components, and performs explicit elementary collapses to facet trees. Its output is stored in `verification_output.txt`.

The finite replay is corroborative only. It does not certify existence or correctness for untested parameter sets; the all-parameter claim is established by the proof above.
