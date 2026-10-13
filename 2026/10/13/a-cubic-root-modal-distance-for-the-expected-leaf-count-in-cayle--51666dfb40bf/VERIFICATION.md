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

The proof is self-contained in `RESULT.md`. Run `python3 verify.py` with Python 3 and its standard library. Expected terminal line begins with `PASS exact conditional means and distance frequencies:` and reports 28 conditional cases among 280392 Prüfer-coded labelled trees, 35 determinant checks, 11026 exact transition checks and 148 modal cases.

The checker actually compares all labelled trees through eight vertices against the closed form using rational arithmetic; no Monte Carlo approximations are used. For \(n\le150\), it separately tests algebraic transitions and peak locations, but the all-size claims rest on the principal-minor forest proof and monotone cubic inequality. The script is not a formal proof assistant and its finite ranges do not exhaust the infinite domain. The proof assumes no constrained degree sequence, no fixed root, and no simultaneous conditioning of the two distinguished vertices to be leaves.

Primary-literature checks cover the full 2003 Wiener-index paper and the 2021 full-text distance-profile and leaf-bias results; historical equivalence under alternate tree-enumerator names remains a residual risk. The self-review is not an independent external audit.
