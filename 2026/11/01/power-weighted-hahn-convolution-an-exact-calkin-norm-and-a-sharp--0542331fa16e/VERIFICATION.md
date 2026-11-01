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

The proof is contained in `RESULT.md`; the exact weighted-difference isometry, compact shift decomposition, finite-rank approximation bounds, and analytic Wiener/Fredholm arguments are fully symbolic and apply uniformly to every stated real exponent and permitted sequence. The operator and symbol normalization is fixed there; external lemmas used are classical unilateral-shift Fredholm theory and the analytic Wiener inverse theorem.

The standalone `check.py` is intended to be executed with `python check.py` using only Python's standard library. The program checks 17,928 exact-rational or numerical finite statements: weighted tail-sum inverse identities, conjugated powers of the right shift, positive-column formulas at integer exponents, and the asymptotic rate for sample exponents. Its finite tests neither establish Fredholmness nor prove the universal infinite-dimensional theorem; those conclusions require Steps 1–5 of the analytic proof.

The first-public motivating preprint is arxiv:2606.22912v1 (2026-06-22). Stronger/surrounding mathematical results not covered are described in `REVIEW.md` and `AUDIT.json`. There is no independent external audit, no claimed proof assistant certification, and no claim of an exhaustive priority search.
