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

The exact basis action, finite-path termination, pairwise-orthogonal long paths, adjoint Weyl sequences, exterior resolvent, and eigenvalue exclusions were reconstructed analytically. Their hypotheses are explicit in `RESULT.md`.

The Python standard-library checker `check_monomial_spectrum.py` was run against the package source and reported 9096 successful exact assertions. Finite checks concern coefficient ratios and sample finite paths only; the spectral conclusions are not inferred from any finite truncation.

Limitations: the proof assumes distinct coprime degrees and regular variation of strictly positive coefficient weights. The comparisons to historical literature leave a stated priority risk, including an incompletely accessible 2026 Blaschke-product article. No independent mathematical audit or external certification has occurred.
