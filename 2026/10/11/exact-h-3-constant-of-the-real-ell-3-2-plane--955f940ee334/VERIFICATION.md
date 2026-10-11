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

Run `python3 verify_h3_l3.py` with Python 3. The checker uses only the standard library and returns `VERIFY_OK` on success.

The replay checks the critical finite algebra behind the proof. It recomputes the Sylvester resultant of the two stationarity equations at twenty-five distinct integer values of the remaining variable; because the determinant and claimed factorization each have degree at most twenty-four, exact agreement at those points certifies the polynomial identity. It also reconstructs the positive degree-six Bernstein expansion of \(-q_6\), checks the exact root bracket \(1/4<t_*<3/10\), verifies the endpoint sign inequalities for the second ordered branch, and confirms the positive diagonal defect that separates the interior maximum from the boundary.

Finally, the script isolates the unique quartic root by deterministic bisection and reconstructs the displayed value to high precision. That decimal calculation is a consistency check only. The proof of uniqueness and global maximality uses the exact monotonicity, Bernstein, resultant, concavity, and boundary arguments recorded in `RESULT.md`.

The verification does not claim a result for general \(p\), general \(\ell_q\), higher dimensions, or complex scalars.
