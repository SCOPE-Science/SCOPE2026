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

# Reproducibility

Run `python3 verify_t3.py` using Python standard-library functionality. It expands the explicit one-/two-bad-coordinate sums and an independently formulated selected-edge generating-product coefficient DP and complement omitted-edge DP for all \(k=7,\ldots,11\). It verifies the finite exceptional intersections at \(k=7,8\), all error-count distributions through binomial inversion, the previously tabulated \(k=7\) failure count, and explicit sharpness witnesses. It additionally checks 4,500 deterministic direct random observation sets as a supplementary consistency test.

`verification_output.txt` is the actual recorded exact-arithmetic output. The finite code does not prove the asymptotic estimate or all-length incidence bound; these follow from the arguments in `RESULT.md`.

The integer-product expansions have no randomized arithmetic, floating-point rounding, external packages, hidden lookup tables, or unavailable data dependencies. The only random checks use fixed seeds.

Scientific limits: no independent proof audit has been performed, and potential equivalent results in unindexed literature remain possible.
