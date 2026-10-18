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

# Verification and boundaries

`python3 VERIFY.py` is a standard-library standalone replay. It reconstructs Möbius-ladder edges, connected induced triples, and the complete four-face classification from graph adjacency; it checks each listed free-face removal against all remaining cofaces. The verified domain of the finite replay is \(4\le n\le40\), including \(n=4\), with exactly \(6n\) collapse pairs and final connected-graph Betti rank \(2n^2-8n+1\). Independently, it exhaustively enumerates the ordinary cut-complex faces and performs mod-two boundary reduction at \(n=4,5,6\). The complete output from this execution is embedded in `VERIFY_OUTPUT.txt`.

No bounded computation is used as an infinite proof. Uniform freeness of the listed faces, classification of all triangles and tetrahedra, and connectedness after all collapses prove the Alexander-dual reduction for arbitrary \(n\ge4\). Combinatorial Alexander duality and the Hurewicz/Whitehead argument give the integral homotopy classification. No Lean, external certification, independent audit or human validation is claimed.
