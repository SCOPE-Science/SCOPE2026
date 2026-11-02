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

# Reproducibility and limits

Run `python3 verify_sandwich.py` in the directory containing this file and compare stdout with `verification_output.txt`. The program exhausts all binary words of lengths 0 through 14 for each \(1\le b\le5\). Its dynamic program finds the largest subsequence avoiding \(0\,1^b\,0\) using the greedy matched-prefix state, while a separate combinatorial implementation minimizes over intervals between zero occurrences. The two values agree in 163,835 cases. The maximum over each length agrees with the piecewise formula in 75 cases. It additionally tests 960 constructions and 1,201 directly generated deletion masks.

The exhaustive range is deliberately finite. The theorem for unbounded \(b\), \(r\) and word length depends on the zero-gap identity and case analysis in `RESULT.md`, not on extrapolation from the checker. No independent external mathematical audit or theorem-prover certification is asserted.
