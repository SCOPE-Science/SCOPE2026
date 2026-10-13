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

The proof in `RESULT.md` derives the unrestricted theorem algebraically from the complete multiplication relations. The bundled Python 3 checker (`verify_skew_star.py`) contains separately implemented direct matrix construction from the multiplication table, derives the dimension of the twisted-derivation solution space using Gaussian elimination, checks each displayed basis parameterization map against every product, and enumerates all small-field choices to test square zero and rank. Its final line is `VERIFY_OK` when all checks pass.

Run `python3 verify_skew_star.py`. Prime-field exhaustive cases: \((m,s,q)=(2,1,2),(2,1,3),(2,1,5),(3,1,2),(4,2,2),(2,0,3)\). Their rank-count arrays in increasing rank are respectively \((1,2,3)\), \((1,4,12)\), \((1,8,40)\), \((1,3,5,3)\), \((1,4,10,12,9)\), \((1,4,4)\). An extra direct finite-extension-field enumeration over \(\mathbf F_4\) in the two-leaf swap case yields \((1,6,21)\).

The checker uses standard Python alone and independently solves the twisted-Leibniz linear system for the six prime-field cases. Direct enumeration does not cover all field orders, all star sizes, or any alternate notion of derivation or equivalence. Those unrestricted aspects are justified only by the written proof, not by a finite computational certificate. No independent audit has been performed.
