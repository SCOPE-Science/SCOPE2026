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

# Verification and boundaries

The analytical proof in `RESULT.md` is the source of the infinite-family claim. The supplied `verify.py` uses exact rational Gaussian elimination on full signed systems and separately evaluates the proposed reduced formula. Its deterministic seed, small connected components (possibly cyclic), rational anchoring parameters, and seven hostile-link strengths give 4,550 randomized rational comparisons plus six hand-computable benchmark comparisons: **4,556 cases passed**. The benchmarks verify zero thresholds at \(t=3/2\), \(t=2\), and \(t=3\), including a case with uniform anchoring. Run `python3 verify.py` with standard Python 3.

Verification establishes numerical and algebraic consistency on tested finite configurations only, not a universal proof, exhaustive classification of all graphs, or an independent audit. The proof supplies positive definiteness, exact harmonic extension, endpoint solution, strict Green-profile inequalities, sign thresholds and connectedness. The literature-priority assessment is provisional and is described in `REVIEW.md` and `AUDIT.json`.
