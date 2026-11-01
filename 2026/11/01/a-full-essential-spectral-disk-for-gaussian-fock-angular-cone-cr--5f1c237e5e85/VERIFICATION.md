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

# Reproducible verification

Run `python3 CHECK.py` in this directory using Python 3 with its standard library. The checker passes 1,838 supplementary assertions: exact beta-tail and binomial Pascal formulas over five rational apertures and 121 lattice pairs each; local peak comparisons for three angles and three fiber sizes; and the strict ordinary-norm/spectral-radius separation for one aperture.

The numerical checks cover finitely many degrees and cannot prove the infinite-dimensional assertion. The proof of the spectral classification in `RESULT.md` instead uses uniform Stirling estimates, relative-entropy tails, compact-fiber spectral theory and an explicit resolvent-growth argument. Computations neither infer spectral membership from finite matrices nor claim complete mathematical certification.

The scientific comparison cites accessible full texts and indicates that the abstract of an otherwise relevant article is not a complete full-document inspection. The spectral result is subject to independent assessment; no independent audit has been conducted.
