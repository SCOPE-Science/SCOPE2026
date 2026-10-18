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

Run `python3 verify.py` with Python 3 standard libraries. The program uses literal index-subset enumeration to identify every constrained pattern of target length, a separately coded greedy arch-and-spacer criterion, and exact integer coefficient arithmetic using inclusion–exclusion rather than assuming the rational answer. It tests binary, ternary, and four-symbol alphabets with both positive and zero comparison gaps; it also checks all possible exact universality indices for binary words through length nine and ternary words through length seven. Exact shortest-word coefficients are checked for additional parameter values. The expected terminal line is `ALL CHECKS PASSED`.

The finite computations neither exhaust all parameters nor certify priority. The all-parameter result rests on the six proof steps in `RESULT.md`; the limiting stochastic result requires the standard strong law for independent integrable waiting times. An independent audit has not been performed.
