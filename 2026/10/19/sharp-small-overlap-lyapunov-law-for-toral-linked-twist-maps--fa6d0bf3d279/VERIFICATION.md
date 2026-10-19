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

The manuscript's proof rests on four universally quantified analytical checks: (i) the induced return derivative and time identity, (ii) invariance of the positive cone and two distinct expansion inequalities, (iii) the bound on short-return probability obtained by conditioning on the conserved horizontal coordinate and applying a union bound, and (iv) conditional Kac recurrence and Jensen's inequality.

Run `python verify.py` using a standard Python 3 interpreter. It tests a finite grid of exact rational parameters and return-count pairs using `fractions.Fraction`, and numerically checks the derived enclosure against selected orbitwise exponents with deterministic initial conditions. Passing these finite checks is not a computer-assisted proof of the theorem, of ergodicity, or of novelty. The complete proof is in `RESULT.md`; no third-party files or online APIs are needed to run the script.

The prior paper [1] supplies ergodicity and the induced shear decomposition; [2] supplies further context. Independent audit is not yet performed.
