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

The proof was reconstructed from the definitions of the Lovász neighborhood complex and elementary simplicial collapse. The critical local condition is that every face with at least two vertices belongs to a unique common-neighbor simplex; in a simple bipartite graph this is equivalent to the absence of a \(4\)-cycle for the faces used by the collapse.

The bundled script `artifacts/verify.py` independently enumerates every connected labeled bipartite square-free graph on at most six vertices. On both side components it rebuilds all nonempty faces, executes the exact descending-cardinality collapse sequence, verifies that each lower face has exactly one strict coface and that the paired upper face is maximal, checks the final face set against the claimed graph spine, and checks equality of graph cycle ranks before and after the forest contraction. The bundled output reports \(1501\) graphs checked without failure.

The finite checker is only a sanity test. It does not establish the theorem for arbitrarily large graphs. The all-size result follows from the uniqueness-of-support argument in the proof. No assertion is made for graphs containing a \(4\)-cycle, where two common-neighbor simplices may share an edge and the proposed local free-face condition can fail.
