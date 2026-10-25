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

# Reproduction and limits

Run `python3 verify_cycle_product.py` using Python 3 with its standard library; no external packages or downloads are required. Expected final line:

`CYCLIC_PRODUCT_CHARACTERS_VERIFIED [(3, 2, 17, 0), (3, 3, 33, 0), (3, 4, 61, 0), (6, 2, 323, 1), (6, 3, 1649, 3), (9, 2, 5777, 0), (12, 2, -1, 1)]`

Full independent-set enumeration and signed augmented Lefschetz traces were checked for \((m,n)=(3,2),(3,3),(3,4),(6,2),(6,3),(9,2)\). The last pair \((12,2)\) tests the transfer-matrix formula and character arithmetic, but does **not** enumerate faces. Each rotation is checked against both the closed character formula and the proposed induced-word representation. The verifier also checks necklace invariant dimensions and character nonnegative integral Fourier multiplicities for these examples.

Critical mathematical proof obligations are discharged in RESULT.md: (1) the cited homology-concentration theorem applies for all \(r\ge1,n\ge2\); (2) invariant simplicial faces and their orientation signs reduce to the signed fixed-orbit sum; (3) the explicit transfer matrix has eigenvalues giving the claimed trace for every \(d\ge1\); and (4) character comparison yields the stated positive rational representation decomposition. Numerical character Fourier checks are auxiliary and do not establish those statements for arbitrary parameters.

Independent mathematical audit: not performed.
