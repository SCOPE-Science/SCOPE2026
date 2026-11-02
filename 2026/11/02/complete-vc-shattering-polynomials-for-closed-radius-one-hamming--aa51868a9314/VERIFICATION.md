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

# Verification details

The script `check_hamming_shattering.py` uses only Python's standard library. For each test case, it constructs the complete Hamming vertex set, computes closed radius-one balls by coordinate disagreement, enumerates all supports of the tested sizes, and counts supports realizing every possible Boolean trace. It independently evaluates the stated coefficient formulas and (in dimension at least three) the sum of all three structural type counts. The saved output in `verification_output.txt` records the completed run.

All sixteen parameter cases pass, including \((d,q)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2),(4,3),(5,2),(6,2)\) and one-dimensional boundaries. Four-point non-shattering was directly checked in several cases. The mathematical proof, not finite checks, establishes the unrestricted all-parameter formula and non-shattering of all larger supports.

No independent mathematical audit has been performed. Historical-priority searches are non-exhaustive.
