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

The proof uses the exact cyclic vertex--edge bracket relations given in Gallo--Videla, Section 3. The key determinant reduces to two alternating perfect matchings in each connected support component, with the number of components controlled by \(\gcd(n,3)\). The separate triangle computation handles \(C_3\). Full mixed rank is equivalent to full noncentral Kirillov rank; singularity forces an even rank at most \(2n-2\).

Execute `python3 verify_cycle_index.py` with Python 3; its implementation needs no third-party modules. It computes full alternating Kirillov matrices directly from the source bracket rules and exact row reduction over prime fields of orders two, three and five and the extension field of order four. Results for \(n=3,\ldots,18\) validate the constructive witnesses in all four fields, 6,419 central parameter choices are exhaustively checked, and 12,730 small noncentral parameter combinations are exhaustively checked. The recorded exact output is `verification_output.txt`; a successful execution ends with `VERIFY_OK`.

The experiments cannot prove the infinite-range index formula, establish the determinant identity for arbitrary length, or demonstrate originality. Those matters depend on the written argument and source comparison. Independent validation was not performed.
