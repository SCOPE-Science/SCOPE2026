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

# Verification of finite support classification

The executable file `artifacts/verify_kummer.py` depends only on Python's standard library. It reconstructs the sixteen six-point blocks, verifies each pair occurs in two blocks, evaluates all \(560\) triple conditions, and checks the mod-two edge cocycle on each. It computes rank \(104\) for the \(120\)-by-\(320\) triangle-boundary matrix using exact binary elimination; the rank \(15\) of the complete-graph vertex-edge boundary then gives first homology of dimension one. It identifies the \(60\) isotropic affine four-point planes, examines all \(65536\) subsets, and checks the noncarrier cardinality profile \((1,16,120,320,320,96,16,0,\ldots,0)\). Finally, it enumerates the \(720\) symplectic linear transformations and their \(16\) translations and checks transitivity on the \(240\) omitted triangles.

The check is exhaustive for this finite instance; no independent audit has been performed and no claim is made about general biplanes, integral minimal carriers, or the full automorphism group beyond the explicit affine subgroup.
