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
# Verification and reproducibility

Run `python3 verify.py` in the extracted directory; the script uses only the Python standard library. It enumerates every profile satisfying its six specified type-total vectors and one-vacancy constraint and compares the exact potential change with the individual moving agent's exact payoff gain for every directed legal move. The utilities are deliberately heterogeneous quadratic rational functions, covering nonmonotonic shapes. Across the six cases there are exactly 2,556 checked transitions and 1,024 strict improvements; the tests print individual case counts and fail by assertion on any discrepancy. The separate two-vacancy check reconstructs four named states of \(K_{3,3}\) and checks the exact gains \(2/3\to1\), \(0\to2/3\), \(2/3\to1\), \(0\to2/3\), returning to the initial state.

The universal theorem is proved by the exact marginal-potential identity and finite count-matrix argument in `RESULT.md`; these bounded calculations do not claim to enumerate every graph, utility function, or profile. No independent external audit or validation is claimed.
