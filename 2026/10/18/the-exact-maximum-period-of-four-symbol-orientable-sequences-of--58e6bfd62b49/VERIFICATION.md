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

The exact certificate is the 106-symbol line in `WITNESS.txt`. Running `python3 verify.py` reconstructs every cyclic window, independently generates all four-symbol nonpalindromic reversal-pair classes, checks uniqueness, and reports the omitted reversal classes. `CHECK_OUTPUT.txt` records the actual output of that execution.

For the universal upper bound, the proof in `RESULT.md` gives a mathematical, not computational, contradiction to any period exceeding \(106\). Its nonstandard counting steps are explicitly verified in the proof; the code additionally checks the full-graph degree \((3,4)\) for every repeated-leading-doublet vertex. Direct enumeration of windows does not itself establish the infinite universal bound; that role belongs to the degree argument.

The result has not been independently audited or scientifically validated.
