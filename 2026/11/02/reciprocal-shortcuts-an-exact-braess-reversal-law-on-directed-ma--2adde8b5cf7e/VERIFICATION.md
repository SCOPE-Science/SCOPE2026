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

# Verification of the reciprocal-chord classification

Run `python verify.py` from the directory containing this file. The checker uses only Python standard-library `fractions`, `itertools`, and exact Gaussian elimination, and constructs the negative Markov generator directly from its graph definition.

**Executed:** `python verify.py` returned `PASS 845 exact-rational checks`.

Tests cover every \(n\in\{4,\ldots,10\}\), each allowed offset \(k\), seven rational pairs of independent additional rates, two separate resolvent test arguments, equality at the exceptional four-state case, strict symmetric link deterioration, optimal budget allocations, and the opposite-rate reversal at \(n=7,k=3\). The Kemeny result is independently reconstructed as the quotient of sums of principal minors, rather than using the package's stated coefficient expansion to compute the left side.

**Limits:** Numerical or finite exact checks alone cannot prove the unbounded-dimensional statement. The proof in `RESULT.md` verifies the characteristic polynomial and its derivative relations algebraically for all allowed inputs. Independent expert audit and comprehensive historical-priority certification have not been performed.
