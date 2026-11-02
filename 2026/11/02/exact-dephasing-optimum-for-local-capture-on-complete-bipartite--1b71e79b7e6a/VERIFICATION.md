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

The included `proof_check.py` is standalone apart from dependencies listed in `requirements.txt`. Execute `python proof_check.py` in a directory containing both files. Actual check output is embedded in `CHECKS.txt`.

The verifier substitutes the proposed full-size integrated amplitudes into the eight reduced equations and evaluates the lifetime and optimizing derivative identities exactly using SymPy: **11 exact checks passed**. It separately constructs the full \(N^2\)-dimensional Markovian Lindblad matrix for nine bipartition sizes, three positive rate triples, and four initial mixture weights, finding **108 passing linear-system comparisons** (maximum relative discrepancy \(1.35\times10^{-14}\); maximal residual \(9.22\times10^{-15}\)). It additionally brackets the rate optimum and checks strict monotonicity numerically in **30 passing trials**.

The all-size claims rest on the written Hilbert–Schmidt dissipation, exact integrated-entry equations, and elementary calculus, not on finite numerical samples. The checker does not verify nonuniform dephasing, onsite disorder, multiple sinks, or interacting many-body systems. Independent scientific validation remains unperformed.
