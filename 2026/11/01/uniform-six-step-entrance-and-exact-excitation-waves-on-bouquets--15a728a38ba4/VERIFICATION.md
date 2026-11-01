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

# Verification of the square-bouquet excitation classification

The claims are for the explicitly defined labelled graph and update rule in `RESULT.md`. Reproduce the all-size finite-state argument using `python3 finite_certificate.py`. This checks each of the 27 possible local petal starts under every possible intrinsic hub word of length eleven, filtering on the exact necessary OR-stimulus compatibility conditions; it leaves twelve feasible words, and verifies equality of the full local states at times six and ten in every case. This is an exhaustive finite proof of the universal identity, valid for any number of petals.

The same Python script checks all 93 locally possible edge-circulation updates, all color-zero-winding distributions, the exact three phase patterns, the complete 81-state one-petal boundary, and the sharp example traces. Its expected final line is `FINITE_CERTIFICATE_OK`; see `finite_certificate_output.txt` for actual observed output.

An independently coded C++17 full functional-graph census is supplied in `full_state_census.cpp`. Reproduce using `g++ -std=c++17 -O3 full_state_census.cpp -o full_state_census` and `./full_state_census`. The observed output in `full_state_census_output.txt` gives the fixed-point basin, four-cycle basin, primitive-orbit counts and sharp entrance time for each petal count 1 through 4. These finite examples cross-check but are not used as an inference for arbitrary petal counts.

The novelty check compares mathematical implications, not titles alone. Existing general circulation criteria cover extinction versus sustained activity, but they do not supply the exact uniform entrance-time and four-orbit census. Research priority outside the inspected materials remains uncertain. No external independent audit or formal certification has been undertaken.
