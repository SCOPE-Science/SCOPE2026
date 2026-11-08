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

# Verification and limitations

The all-index proof is in `RESULT.md`, Steps 1–4. The only exceptional denominator in any generalized coefficient is one factor of \(t\), and the least available numerator power is \(q^4\). The exceptional first coefficient is \({4\brack2}_f=-q^4(t+1)/t\). The separate index-divisibility test is \(f_4/f_2=q^2/t\). All values used to assert the infinite result are derived symbolically with explicit hypotheses.

Run `python3 artifacts/check.py` in the package root and compare deterministic output with `artifacts/check_output.txt`. The script uses only the Python standard library, reconstructs terms from the recurrence, and checks integrality using exact integer products and divisibility. Tests cover 1,950 parameter pairs through \(n=23\), and five binomid nondivisible pairs through \(n=100\). Passing finite checks is supplemental and not an exhaustive test of arbitrary \(n\), \(q\), or \(t\).

The theorem concerns signed nonzero integer sequences (not all-positive ones), binomid integrality at the original triangular level, and index divisibility. It does not establish the stronger binomid-pyramid property or resolve the full general order-two classification. No independent audit has been performed.
