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

# Exact verification

Run `python3 verify_clebsch_action.py` using Python 3. This standalone file reconstructs all data from \(A=\mathbb F_2^4\) and edge differences \((1,2,4,8,15)\). It enumerates every nonempty independent set among the sixteen vertices, checking the face vector and degree/common-neighbor numbers. It then reconstructs a greedy acyclic matching using the explicit vertex order in RESULT.md, checks all 1,200 nonempty face-poset cover relations and topologically sorts the associated gradient digraph.

For each of the \(16\cdot5!=1920\) affine automorphisms the program directly computes signed fixed faces and separately computes the signed count of compatible vertex-orbit blocks. Both are compared to the proposed closed character formula with integer arithmetic. Finally all sixteen translation Fourier multiplicities are computed and asserted. The complete actual output is embedded in `verification_output.txt`; it ends `VERIFY_OK`.

The finite exhaustiveness is mathematical evidence only for this specific 16-vertex graph and its 1920 automorphisms. It does not certify unenumerated larger folded cubes, mathematical originality in unindexed sources, or independent external validation.
