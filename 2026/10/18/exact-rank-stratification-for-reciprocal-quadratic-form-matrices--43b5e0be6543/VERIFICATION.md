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

The standalone `verify.py` uses only Python's standard library. It constructs the full matrix entries, independently computes their rank by elimination over the prime field, independently constructs the quadratic extension with basis \(1,\alpha\) satisfying \(\alpha^2=-c\alpha-d\), and checks the multiplicative order of \(z=\alpha/\beta=(-1,-c/d)\) in that basis against the stated rank formula.

Command: `python3 verify.py`.

Executed test domain: all \(c\in\mathbb F_p\), all nonzero \(d\in\mathbb F_p\) with nonsquare discriminant, for \(p=5,7,11,13,17,19,23\). Per-prime case counts: 10, 21, 55, 78, 136, 171, 253; total 724. All comparisons passed (`ALL_OK 724`). No reliance on external package downloads.

The test does not establish the all-prime theorem, the novelty claim, or independent validation. The proof in `RESULT.md` supplies the universal argument. Integer valuation optimality is not asserted.
