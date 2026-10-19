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

# Independent finite-enumeration diagnostic (not an independent audit)

Run `python verify.py` with Python 3's standard library. The script enumerates every environmental sequence of lengths 1 through 7 and every initial binary cylinder of length \(n+1\), weights the environmental paths by exact rational Markov probabilities, and directly counts the surviving paths. For each of seven rational persistence parameters it compares first and second survivor moments with independent two-by-two and three-by-three transfer-matrix multiplication. The execution returned:

`VERIFY_OK: 49 exact independent first/second survival moments; 999 positive spectral-gap witnesses`

The program also verifies \(p=0\) and \(p=1\) zero-variance laws, the \(p=0\) Jordan formula, and \(p=1/2\) geometric first-moment law. The 999 floating-point spectral-gap checks are numerical diagnostics, not a formal proof; the exact polynomial identity and its inequality proof appear in `RESULT.md`. The test does not independently establish an infinite-horizon theorem or audit historical novelty.
