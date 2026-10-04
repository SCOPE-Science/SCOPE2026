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

Run `python3 artifacts/verify.py`. The verifier uses only the Python standard library.

It reconstructs the sixteen-point target order from the explicit cover relations, computes transitive closure, and enumerates every function from the four-point source. A map is retained exactly when all four source cover inequalities are respected. The count is independently recomputed as the sum of squares of common-upper-set sizes for the two source minima.

The pointwise order on all retained maps is then computed exactly. Comparability components are found by union--find. Each component is reduced by repeatedly checking the defining beat-point condition in the current active subposet: a least strict upper element or a greatest strict lower element.

The program verifies the component-size multiset \(1{,}024,64,64,17,\ldots,17\), the exact deletion totals, the identity of the sixteen-map core with the constant maps, equality of its inherited order with \(K_{1,0}\), the crown structure of each eight-map core, and singleton cores for each size-\(17\) component.

Expected output:

`VERIFY_OK maps=1288 components=11 sizes=1024,64,64,17x8 deletions=1248 up=368 down=880 core=40`

The finite computation proves only the stated direct-map claim for the specified source and target. It does not classify subdivided source maps or arbitrary finite Klein-bottle models.
