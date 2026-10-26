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

# Reproducible exact checks

Run `python3 verify.py` with standard Python 3. Its output begins with `CERTIFICATE_OK prime_head_options 24 connected_components 14 gaps 13 overlaps 10 total_density 1` and lists all fourteen components, endpoint multipliers, rational natural densities, and the corresponding small-prime valuation types.

The code performs exact `Fraction` arithmetic and certifies the five finite prime-tail inequalities, the strict three-term Nagura consequence, four head-exponent threshold comparisons, 23 interval overlap/gap decisions using rigorous zeta bounds, total component count, exact extreme endpoints and density sum one.

The program's checks certify the finite rational comparisons only. The infinite tail-interval and arithmetic-density arguments, along with Nagura's published prime-interval theorem, are established separately in the proof. The present self-review does not amount to independent mathematical validation.
