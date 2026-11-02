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

# Reproducibility and limitations

Run `python3 verify_gap_product.py` using the accompanying source file. It requires only Python's standard library and uses exact `Fraction` arithmetic to compare direct four-triple enumeration against the closed form across \(27{,}000\) exhaustive integer-gap triples, \(10{,}000\) additional seeded large-integer triples, and four rational points in the sharpness family. It checks that each tested ratio is below \(5/2\). All checks passed from the present files.

The strict bound over all positive real gaps is certified by the case proof in `RESULT.md`, not by finite enumeration. The nonattained supremum arises as one gap tends to zero within the all-distinct domain. No independent mathematical audit has been performed.
