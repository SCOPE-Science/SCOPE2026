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

The proof covers all integer factor orders \(m,n\ge4\). The accompanying program independently constructs the tensor-product graph and evaluates power domination by repeated unique-unobserved-neighbor propagation without calling the closed formula to determine graph validity. Run `python3 verification/verify_power_direct_product.py`; compare standard output with `verification/output.txt`.

All subsets were checked for \((m,n)=(4,4),(4,5),(5,4)\), comprising \(2^{16}+2\cdot 2^{20}=2{,}162{,}688\) graph-monitoring tests. For each board its full coefficient histogram agreed with the formula. Nine further board shapes were checked with deterministic sampling and complete two-vertex enumeration (34,503 checks). All were successful. In addition, the maximum deficient coefficient degree and minimum-set counts agreed with the stated formulas for these nine boards.

These tests verify the implementation and finite instances only. They do not provide an exhaustive proof for arbitrary graph orders; that is furnished by the explicit combinatorial proof. The polynomial is not asserted to be globally graph-distinguishing, and no independent external audit has occurred.
