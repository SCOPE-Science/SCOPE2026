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

# Reproducibility of finite checks

Run the included file with `python3 verify.py`, using only the Python standard library. It independently enumerates all \(d\)-by-\(d\) matrices over \(\mathbb F_2\) or \(\mathbb F_3\), checks all cyclic products, computes rank profiles by modular Gaussian elimination, and compares to the Gaussian-product formula. Ten fully enumerated parameter configurations include cycles of lengths \(2,3,4,5\) and dimensions one or two. The finite checker additionally enumerates the feasible combinatorial rank profiles for cycle lengths \(2\) through \(7\), with small dimensions, and verifies the asserted dominant profiles. The observed result was `VERIFY_OK`.

The algorithm counts all matrices only in these stated finite cases; it does not attempt an exhaustive check for all prime powers, vertex dimensions, or cycle lengths. The general finite-field result and asymptotic conclusions are established by image/kernel flag counting, explicit module decomposition, monicity, and the integer-degree comparison in `RESULT.md`. No external or independent review is claimed.
