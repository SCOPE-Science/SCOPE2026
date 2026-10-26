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
# Reproducibility and proof checks

The mathematical proof is in RESULT.md, with domain, normalization, closed-form cavity solutions, Bessel limiting identities, and an explicit hypergeometric expansion. Run `python verify.py` with the versions described in `requirements.txt`.

The script independently enumerates the first-attempt order of every bond in short finite paths, using exact rational Plackett–Luce order weights, and matches the corresponding first-success recursion. It also compares independent numerical integrations of the cavity IVP with the closed Bessel solution at positive finite times, and extrapolates finite-path expected coverages using a recurrence distinct from the infinite-chain differential-equation derivation. Finally it tests the homogeneous \(e^{-2}\) value and the two-term strongly staggered expansion.

Observed execution: 18 exact-rational arrival-order comparisons, 24 cavity/Bessel comparisons, 15 finite-path thermodynamic comparisons, and four benchmark/asymptotic checks passed. These computational tests are finite and do not certify the infinite-chain identity or historical novelty; the written analytical proof supplies the infinite-parameter argument. No independent audit was performed.
