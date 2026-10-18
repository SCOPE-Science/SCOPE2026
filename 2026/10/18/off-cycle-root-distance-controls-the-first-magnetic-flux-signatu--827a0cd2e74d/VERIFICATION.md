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

Run `python3 verify.py` with a standard Python 3 installation. The expected successful output is `VERIFY_OK rooted_unicyclic_profiles= 96 lengths= 3 .. 13 orders= 4 .. 20`.

The checker builds explicit finite unicyclic weighted graphs, enumerates each rooted closed-walk moment as an integer Laurent polynomial in a formal unit-modulus flux variable, and constructs the return-probability Taylor coefficients as exact fractions. It checks that the coefficients at all orders below the parity-dependent predicted threshold are flux-independent. At the threshold, it checks both signed nonconstant Laurent coefficients and the absence of any other flux harmonics. Cases comprise six cycle lengths, four root distances, two attachments and two weight assignments. Root-on-cycle cases are included only as independently formulated boundary controls and are not used to infer the theorem for off-cycle roots.

This is a finite collection of exact checks, not exhaustive verification over all graphs, weights or dimensions. The unlimited quantifiers rely on the walk-lift and parity proof in `RESULT.md`. The recent closely related rooted-moment paper was compared through its available abstract and a detailed third-party description; its inaccessible full text is a material originality limitation. Independent audit has not been performed.
