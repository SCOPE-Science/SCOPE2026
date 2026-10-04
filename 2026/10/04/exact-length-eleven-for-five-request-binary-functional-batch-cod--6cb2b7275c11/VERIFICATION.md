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

Run `python3 verify.py` with Python 3 and the standard library.

The script reconstructs, for each of the seven nonzero vectors of \(\mathbb F_2^3\), the unique singleton recovery and the three unordered complementary-pair recoveries of size two. It then checks all \(462\) multisets of five nonzero queries against the explicit multiplicity vector \((1,1,1,2,2,2,2)\), using exact integer capacities and exhaustive backtracking.

For the lower bound it independently enumerates all \(8008\) seven-part nonnegative integer compositions of \(10\), verifies the sharp maximum \(24\) for the pair-minimum sum, verifies the sharp maximum \(34\) for \(\sum_q A_q\), and confirms that no total-ten multiplicity vector can supply five disjoint locality-two recoveries for every repeated query. This finite enumeration corroborates the analytic balancing proof; it is not extrapolated beyond the stated finite domain.

As a supplemental stress test, the script enumerates all total-eleven multiplicity vectors satisfying every repeated-query capacity, obtains exactly \(77\), and checks every one against all \(462\) query multisets. This census is verification evidence only; the finding does not claim an isomorphism classification.

Expected final line: `VERIFY_OK`.
