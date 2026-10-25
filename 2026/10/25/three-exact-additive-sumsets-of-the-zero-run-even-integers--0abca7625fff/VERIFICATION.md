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

Execute `python3 verify.py` using only Python 3's standard library. This compares the direct base-two zero-run definition to the three-branch recurrence through \(n=50{,}000\); constructs valid two-summand witnesses for both \(A+A\) and \(A+2A\) through \(n=50{,}000\); checks the corresponding \(A+4A\) representations through that range and directly enumerates it through \(n=4{,}096\); and confirms the Fibonacci dyadic enumeration through \(k=14\). All checks completed successfully using the packaged code. The finite checks do not establish the infinite theorem; the detailed strong induction and combinatorial counting proof appear in `RESULT.md`.

Independent audit: not performed. No external certificate is asserted.
