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

The analytic proof uses only the following exact ingredients.

1. The nonzero vectors of \(L_0\) of \(\ell_1\)-length at most \(3\) are six vectors \(\pm2e_i\) of length \(2\) and eight odd sign vectors of length \(3\).
2. For \(1\le r\le3/2\), only the six length-\(2\) vectors give positive-volume pair intersections.
3. One such lens has exact volume \(4(r-1)^3/3\).
4. Distinct short neighbors differ by \(\ell_1\)-length \(4>2r\), excluding positive-volume triple intersections.
5. With three unordered lenses per covolume-\(4\) cell, exact inclusion-exclusion gives \(d(r)=(r-1)^3\) and \(u(r)=r(3-r)(3-2r)/3\).

The bundled `verify.py` uses only Python's standard library. It exhaustively enumerates the lattice vectors in the finite norm range relevant to item 1 and checks the polynomial endpoint and near-threshold identities with exact rational arithmetic. Replaying the script after extracting it from the reopened ledger row returns `VERIFY_OK`.

The computation is supplementary. No finite enumeration is used to infer a statement beyond the explicitly bounded lattice-vector range, and the universal scale formulas are proved symbolically above.
