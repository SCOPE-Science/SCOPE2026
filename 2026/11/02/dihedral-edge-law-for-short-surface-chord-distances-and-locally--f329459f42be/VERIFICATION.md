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

## Analytic verification
The small-radius coefficient follows from exact integrals over polygon covariograms and two-face wedges, including all ordered face-pair types and a bounded vertex remainder. The rectangular-box polynomial follows from six exactly integrated rectangular covariograms and twelve exactly integrated right-angle wedge pairs. The box collision is an exact equality of the sum and the pairwise-product sum, not a numerical coincidence.

## Reproducible numerical checks
Run `python check_local.py` and `python check_wedge.py` from the extracted package directory with NumPy and SciPy. For four boxes and radii below the shortest side, 2,097,152 independently mapped surface-point pairs per box had CDF discrepancies less than \(1.6\times10^{-4}\). Eleven deterministic radius checks compare the two noncongruent collision boxes with precision \(10^{-13}\). Four independently parameterized dihedral cone integrals, each with 4,194,304 scrambled Sobol points, agreed with the exact angle coefficient within \(7\times10^{-7}\). These tests are finite approximate checks, not certificates of an infinite theorem.

## Remaining limitations
No computer proof of global uniqueness or originality. Mathematical proof does not cover nonconvex singular surfaces, volume samples, surface shortest-path distances or large radii for boxes. Human inspection of the unavailable complete 1999 Mathai and 2001 Osada sources is still necessary for historical priority.
