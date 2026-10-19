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
# Verification of finite-characteristic Laurent Euler derivations

The proof is self-contained in `RESULT.md` and covers arbitrary characteristic-\(p\) fields and all \(n\ge1\). The provided `verify.py` independently performs exhaustive calculations on finite prime-field coefficient models. Run `python verify.py` in the extracted package.

Nine checks passed with triples \((p,n,f)\) equal to \((2,1,2)\), \((3,1,2)\), \((5,1,2)\), \((2,2,2)\), \((3,2,2)\), \((5,2,2)\), \((3,2,3)\), \((2,3,2)\), and \((3,3,1)\). Each check enumerates the determinant-\(\pm1\) reduction group, the full action on weight coefficient lists, all orbit sizes and counts, and image sizes of the exponent homomorphism. All predicted indices and conjugacy-class totals were verified.

The computational input models the \(\mathbb F_p\)-vector space underlying \(\mathbb F_{p^f}\), which is valid because the classification uses only additive prime-field linear algebra, not finite-field multiplication. Computation does not prove the infinite family; that follows from the separate general proof and elementary generation of \(\operatorname{SL}_n(\mathbb F_p)\).

No external or independent mathematical audit is claimed.
