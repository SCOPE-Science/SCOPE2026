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

The exact main result is proved by (i) a chord-by-chord perimeter identity on the full-edge-sampling event, (ii) exact directed circular-gap density and an elementary integral, (iii) the empty-edge exponential union bound, and (iv) independent finite-neighborhood Poisson void limits with uniform moment tails.

The standalone script `verify.py` requires Python 3 standard library only. Run `python3 verify.py` from this package directory. Its regression suite checks direct sampled-hull perimeters against the corner identity on full-edge events; numerical quadrature of the angle and variance formulas; and a Monte Carlo rectangle estimate. It does not formally verify the infinite-dimensional distributional or all-sample-size statements; these depend on the arguments in RESULT.md.

The source comparison was mathematical rather than bibliographic-title-only. The earlier local corner point-process limit can yield the scaled limiting distribution; the finite-sample \(1/(N+1)\) angular identity and exponentially small shape-memory estimate are additional. Priority outside reviewed sources and independent scrutiny remain open.
