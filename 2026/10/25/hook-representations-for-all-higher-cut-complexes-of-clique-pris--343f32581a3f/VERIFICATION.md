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

The supplied `verify.py` uses only Python 3 standard-library modules. Its signed reduced Lefschetz calculation enumerates actual faces of the ordinary cut complex, computes orientation signs of preserved simplices, and compares the result with the exterior-power and layer-exchange character for all \(212\) tested conjugacy-class representatives across \(2\le n\le6\) and \(2\le k\le n\). All tested cases in the claimed domain \(n\ge k\ge4\) are included.

The independent graph-construction path enumerates induced disconnected \(k\)-subsets using adjacency and connectivity, and compares literal face membership with the structural description in the proof for \(25{,}488\) subset cases. Direct mod-two boundary elimination verifies six \((n,k)\)-cases: \((4,4),(5,4),(5,5),(6,4),(6,5),(6,6)\), with nonzero Betti numbers respectively \(1,4,1,10,5,1\), in the theorem's predicted degrees.

These finite computations do not independently establish an infinite-parameter theorem. The proof supplies that step through the dual cover, relative homology, and equivariant Alexander duality. Character agreement alone would not prove homology concentration without that separate argument. No independent external audit has been performed.
