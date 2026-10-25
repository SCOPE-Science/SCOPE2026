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
# Verification and limits

The supplemental `verify_chain_commuting.py` is a standalone standard-library Python program. Execute it with `python verify_chain_commuting.py`. It independently implements integer residue-ring and truncated-polynomial-ring arithmetic, maps coefficient vectors by primitive projective coordinates, and checks that **all** coefficient-vector pairs have the same commutation relation after mapping. It also checks that the map is bijective and that each valuation stratum has the predicted number of vectors and centralizer size.

Checked parameter pairs: \((p,m)=(2,2),(2,3),(3,2),(5,2)\). The respective unordered-with-diagonal coefficient-vector comparisons number \(136,2080,3321,195625\), and all passed. A second layer directly implements three-coordinate group multiplication for **both** coefficient-ring types at \((p,m)=(2,2)\), testing all \(64^2\) ordered element pairs for consistency with the derived determinant criterion; both checks passed.

Observed output includes `CASE_OK` for all four configurations, `VERIFY_OK all direct commuting-graph comparisons and group-product checks`, and `GROUP_PRODUCTS_OK` twice. The test is finite corroboration: it does not establish the general theorem for arbitrarily long chains or residue fields of nonprime order. Those cases are covered by the mathematical argument using residue quotients, compatible projective-line trees, and exact centralizer counting.

The published class-two counterexamples by O'Brien are recognized as prior work; independent scholarly validation of the exact new classification has not been performed.
