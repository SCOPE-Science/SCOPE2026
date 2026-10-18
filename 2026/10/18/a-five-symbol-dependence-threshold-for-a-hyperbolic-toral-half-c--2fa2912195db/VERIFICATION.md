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

# Reproducibility and verification

The proof is self-contained in `RESULT.md`. The file `VERIFY_CHECKER.py` uses only the Python standard library. Run `python3 VERIFY_CHECKER.py` from the directory containing the files. It prints `VERIFY_OK` if every exact assertion and finite-grid diagnostic succeeds.

The exact tests compute the five row vectors and five primitive integer circuits; verify the unimodular matrix and the cubic Cayley–Hamilton identity; evaluate the unique nonzero fourth moment exactly as `1/8265`; and enumerate all 32 five-sign assignments with exact rational probabilities, checking normalization, positivity, and the 30 nontrivial marginals of sizes at most four. Additional tests establish only finite sanity checks (three-row determinants for indices less than twelve and two discrete-Fourier grids). The complete all-time triple independence rests on a positive-eigenvalue polynomial root argument in the proof, not these finite tests. The infinite Fourier series is controlled analytically by Poisson smoothing and the absolutely convergent fourth-order resonance series.

The source's 2011-03-06 public date is the original arXiv submission date of the background toral-automorphism reference, not the publication date of this finding. Scientific priority is not independently certified. Independent audit has not been performed.
