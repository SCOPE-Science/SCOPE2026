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

# Reproduction procedure

Run `python CHECK.py` using Python 3 with the public packages `sympy`, `numpy`, `scipy`, and `mpmath`. The standalone checker symbolically compares four independently expressed Taylor identities, including the critical fourth-cumulant constant; numerically integrates the original physical moment hierarchy and compares 24 moments with a separate Kummer-function calculation; and compares six finite large-time fourth cumulants plus a critical-limit window to the asymptotic formula.

The analytical theorem's infinite-time quantifier follows from the locally uniform Kummer expansion and Cauchy coefficient extraction established in RESULT.md, not from finite experiments. The broad exact Fourier characteristic function used in the proof is due to Boyer and Majumdar (arXiv:2312.13439), so these checks do not independently derive that established input. The finite comparisons do not establish publication novelty or independently certify the mathematical result.
