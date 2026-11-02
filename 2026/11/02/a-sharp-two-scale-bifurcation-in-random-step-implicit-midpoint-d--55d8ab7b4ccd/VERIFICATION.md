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

# Reproduction and limits

Install the requirements listed in `requirements.txt`, then execute `python verify.py` from this folder. The verified run reports 6,847 passed exact-symbolic, exact-rational, finite-horizon and numerical check groups, with critical logarithmic half-spread \(1.316957896924817\) and length ratio \(13.928203230275505\). The script covers the midpoint multiplier, rational reduction, derivative, candidate minima, quartic critical coefficient, finite-horizon binomial identity and near-critical scaling. No random dataset or external file is required.

The mathematical proof in `RESULT.md` covers every \(a\ge0\), \(\lambda>0\), \(h>0\), deterministic nonzero initial state and nonnegative integer iteration count. The finite tests are consistency checks rather than certificates for the uncountable parameter ranges. This verification covers the specific formula, optimization criterion and separate exact-arithmetic finite-termination observation; it does not certify fixed-time approximation error, physical-time cost, floating-point behavior or general matrices.
