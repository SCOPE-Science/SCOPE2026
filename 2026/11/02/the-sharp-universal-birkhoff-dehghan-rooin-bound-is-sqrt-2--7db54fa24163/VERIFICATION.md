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

# Verification
The universal inequality follows analytically from \(d=\|su-v\|\ge s\), \(d\ge |s-1|\), the triangle inequality, and the exact polynomial factorization \((2s-3)^2(8s-3)\ge0\). The extremal example is an explicit norm-one pair in real \(\ell_\infty^2\), and the lower equality is verified on Hilbert spaces. These checks cover all \(s>0\) and all real Banach spaces of dimension at least two by proof, not by sampling.

The separate standalone checker `check.py` uses only Python's standard-library exact rational arithmetic and passes 3,510 assertions (envelope identities, piecewise inequalities, square-plane Birkhoff witnesses, and rational-grid norm comparisons). It cannot prove an assertion quantified over uncountably many vectors or scales.

Primary source material inspected: Du–Hu–Zhang–Liu, arXiv:2609.27754v1, pp. 5–7 and 16–17, including the source's exact scale identity and its asserted sharp upper bound. The full 23-page 2024 Fu–Li comparison article was also inspected and does not impose the ordered Birkhoff constraint. Further source comparisons and remaining limits are documented in `REVIEW.md` and `AUDIT.json`. No independent mathematical audit has been performed, and publication priority is not certified.
