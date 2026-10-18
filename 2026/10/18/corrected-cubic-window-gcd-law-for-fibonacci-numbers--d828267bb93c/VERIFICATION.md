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

# Reproducibility

Run `python3 verify.py` in the directory containing the proof and verifier. The script uses only the Python standard library and integer arithmetic. It checks the exact closed formula for all even lengths \(2\le k\le400\), against 31 consecutive direct integer window sums for each length; additionally it verifies 6,200 shifted cubic-difference congruences, Cassini norms, the first-power and cube endpoint gcds, and the cubic telescoping expression. Representative values are \(C_3(6)=2\), \(C_3(8)=9\), \(C_3(12)=4\), \(C_3(16)=63\), and \(C_3(24)=216\).

The checker is a finite regression test; no finite range establishes the theorem for all even lengths. The infinite argument consists of the matrix gcd identity, the local cube-root classification, the endpoint-difference gcd identity, and an exact two-adic valuation comparison, as written in RESULT.md. Independent audit has not been performed.
