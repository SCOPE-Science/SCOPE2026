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

# Verification
The standalone `verify.cpp` builds the original graph, independently simulates threshold activation to its fixed point, and enumerates every nonempty source set for each \(3\le n\le9\) for core thresholds one, two, and three. It compares full polynomial coefficients from independent structural enumerations against direct source-set histograms for thresholds two and three, checks the claimed middle-phase gap criterion for every source set, and checks minimum-source sizes and counts in all three phases.

Run: `g++ -std=c++17 -O3 -Wall -Wextra verify.cpp -o verify && ./verify`. On success the last line is `VERIFY_OK`. The universal proof is the combinatorial gap and independent-set argument in `RESULT.md`; no finite-range inference is used for universal quantifiers.

Limitations: checks use ordinary 32-bit masks for at most 18 graph vertices, bounded by the stated verification range. The code is not an independent mathematical certification.
