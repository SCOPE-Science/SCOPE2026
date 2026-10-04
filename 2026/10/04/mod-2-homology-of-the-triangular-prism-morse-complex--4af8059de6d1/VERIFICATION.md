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

Run `python3 verify.py`. It uses only the Python standard library. The program reconstructs the graph and primitive vector fields, exhaustively enumerates all acyclic compatible sets, independently recomputes the face counts from undirected forests and unmatched-root choices, constructs every augmented boundary over \(\mathbb F_2\), checks \(\partial^2=0\), computes each rank from both column and transposed-row representations, and checks the graph parameters used in the comparison with prior work. The expected terminal marker is `VERIFY_OK`.

The computation proves only the finite mod-\(2\) homology claim stated in RESULT.md. It does not establish integral homology, absence of odd torsion, a homotopy type, or a prism-family theorem.
