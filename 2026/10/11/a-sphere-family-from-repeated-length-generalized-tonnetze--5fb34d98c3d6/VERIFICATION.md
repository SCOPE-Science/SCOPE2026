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
The proof is symbolic. For \(k\ge4\), the defining increment multiset contains one \(2\) and \(k-1\) copies of \(1\), with total \(k+1\). Every displayed prefix sum before the final increment is distinct modulo \(k+1\), so every defining facet has exactly \(k\) vertices. When the increment \(2\) is last, the facet based at \(x\) is \(\{x,x+1,\ldots,x+k-1\}\), missing exactly \(x-1\); varying \(x\) gives all facets of \(\partial\Delta^k\).

`verify.py` independently reconstructs the defining facets for \(4\le k\le10\), compares them to all codimension-one faces of a \(k\)-simplex, and checks the complete face vector. It also replays the missing-vertex coverage identity through \(k=64\). The file `certificate.json` records the expected formulas and the verified finite ranges.

The finite replay is not used as a proof for unbounded \(k\). No claim is made for other nongeneric length vectors, and no independent audit has been performed.
