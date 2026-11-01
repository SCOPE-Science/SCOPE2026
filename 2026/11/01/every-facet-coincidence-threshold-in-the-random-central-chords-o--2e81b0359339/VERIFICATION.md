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

The standalone `central_chord_checker.py` was executed using Python, numpy and scipy. It reported `PASS: 69 independent numerical consistency checks`. These include 22 comparisons of simulated Haar-direction CDF values with analytical expressions in dimensions two and three, six exact-formula-to-quadrature comparisons for the two-face event in dimension three, and tests of the onset constants in dimensions three and four. The dimensions-two and -three CDF comparison uses 250,000 Gaussian directions in each dimension with a fixed seed. The terminal coefficient and general beta-integral constant are derived analytically in RESULT.md. The finite computations do not establish the result for every dimension.

The proof also verifies that each active overlap integral has a strictly positive leading coefficient, that lower-order overlaps remain real analytic across later thresholds, and that the terminal tail uses a separate complement event (not an extrapolation of the right-onset formula). Numerical output should not be used as a substitute for the proof. Historical priority remains qualified by the inaccessible complete texts of Coleman (1981) and Steinerberger (2011).
