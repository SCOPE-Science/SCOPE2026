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

# Reproducible verification

Run `python verify.py` with the standard Python library; no external package is required. The code constructs exact rational Bray–Curtis distances and checks all two-species integer profiles for ordered positive masses up to eight and all three-species integer profiles for ordered positive masses up to four. It checks equality for each explicit two-species extremal construction and never uses floating-point tolerances.

Expected run result: `VERIFY_OK mass_triples=288 2d_profiles=48840 3d_profiles=25942 exact_witnesses=288`.

The complete argument for arbitrary real masses is in `RESULT.md`: the incident distances obey reverse-triangle lower bounds, while the endpoint distance obeys a triangle upper bound; the weighted incident-distance lower envelope yields the closed extremal ratio. The exact extremizer meets all constraints, and elementary sign analysis establishes both strict mass boundaries. The executable tests supplement this proof; they do not establish any infinite-range assertion by themselves.

The unrestricted sharp \(3/2\) result is prior work, and no independent assessment has been conducted. Potential stronger coverage in inaccessible relevant literature is an acknowledged limitation.
