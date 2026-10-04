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

The analytical proof checks three points: both consecutive colour classes are transitive; the cross-part orientation has the displayed topological order; and the tournament contains the directed triangle \(0\to m\to2m\to0\), which excludes one colour.

`verify.py` reconstructs the tournament directly from its modular definition and checks all three properties for every integer \(1\le m\le200\). The computation is a stress test and is not used to extrapolate the universal theorem.
