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

# Reproduction and limitations

Run the included standalone Python 3 program with `python3 johnson_threshold_verify.py` (standard library only). The program enumerates every unordered vertex pair and equidistant landmark family by the original distance predicate in all nine Johnson graph instances with \(6\le n\le10\) and \(3\le k\le\lfloor n/2\rfloor\); it independently compares the maximum sizes, separation cases, and counts of distinct extremal bisectors. It checks 1,444 parameter pairs up to \(n=80\) against the exact binomial-count formula and further finite rational-inequality instances. Expected terminal line: `VERIFY_OK`.

The source is included in full alongside the scientific writeup; no external datasets or generated certificates are needed. The all-parameter result is established by the algebraic coefficient comparisons in RESULT.md, not by finite enumeration. Full priority verification and independent mathematical audit remain unperformed.
