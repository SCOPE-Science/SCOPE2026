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

# Reproducibility and boundaries

The proof in `RESULT.md` uses the published finite spanning-tree formula for the Lipschitz-free \(p\)-norm and supplies the additional tree-shortcut and scalar minimization arguments. All parameters are explicit, and the result is finite-dimensional for each fixed number of sources.

Run `python3 CHECKER.py` to enumerate every labelled spanning tree for 27 sample combinations of coefficients, exponent and hub radius; compare each exact finite-tree minimum with the proposed subset formula. The checker additionally verifies the radical threshold bracket and a genuinely partial-route example, totalling 29 comparisons. This finite computation cannot certify all \(p\), \(t\), dimensions, or masses.

The comparisons with the 2018/2020, 2023/2024 and 2026 primary papers used their public full texts. Related published records available only by title and scientific summary create residual novelty uncertainty. No independent mathematical audit or publication-priority certification has been performed.
