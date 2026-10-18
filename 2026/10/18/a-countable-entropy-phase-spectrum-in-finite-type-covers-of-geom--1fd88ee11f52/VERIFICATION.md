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

# Verification and reproducibility

The statement follows from the complete proof in `RESULT.md`. The first-return graph has states indexed by the capped number of zeros since the last 1; its return lengths and Perron root can be reproduced from the explicit recurrence. The error estimate uses the first two terms of a geometric-power tail and a Taylor expansion about the simple renewal root. Both the complete cluster set and cover-plateau criterion are proved analytically for all integer bases and lengths.

Run `python check.py` with Python 3 using only the standard library. A completed check tested 96 pairs of bases and cover lengths: \(b\in\{2,3,4,5\}\) and \(1\le n\le24\). It also compared the independent short-word description with the finite automaton for every \(n\le9\), and numerically compared rescaled entropy errors with the proved leading term where \(n\ge12\). A separate 90-digit check of representative geometric-power boundaries and near-boundary phases corroborated the predicted values. None of these finite tests alone proves the asymptotic, uniqueness, or infinite accumulation-set statements.

Scientific limits: the conclusions require the precise geometric return set and the canonical finite-type cover. The argument does not establish analogous laws for general sparse return sets. Reproducibility does not replace independent examination of the proof or novelty comparison.
