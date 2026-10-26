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

# Verification record

The standalone `verify.py` independently enumerates each of the \(\binom Na\) binary words for every \(4\le N\le11\) and every \(1\le a<N\). It calculates the centered Wilcoxon rank sum, the complete run count, and each boundary transition directly from the word. It checks all analytic local and global covariances against rational arithmetic; it additionally checks the three distinct sign patterns at total length eight. The local execution printed `PASS: 591 exact-rational checks, including all compositions N=4..11 and three N=8 regimes`.

For the infinite family, verification rests on the conditional two-position finite-population variance identity and the exact sum of centered squared boundary positions, both shown in `RESULT.md`. Numerical checks alone do not prove the general identity. The first-order zero follows from rank-order reversal. The three-phase inequalities follow from exact endpoint and center formulas and positivity of the displayed threshold differences. No independent audit or external formal proof certification has been performed.
