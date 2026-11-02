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

# Exact computational verification

Run `python3 verify_klein28.py` in this directory with Python 3 and only its standard library. The script recomputes all 3276 determinant norms over the imaginary quadratic integer ring, all 378 pair intersections in characteristic zero, and all reduced-line and point incidences over the finite residue fields at primes 2, 3, 7, and 11. It also enumerates the eight points of the characteristic-seven conic, verifies that the 28 reduced lines equal all its secants, and checks every characteristic-eleven line has nine triple and three quadruple points. The success marker is `KLEIN28_EXACT_ALL_PRIMES_2_3_7_11_INCIDENTS_AND_CONIC_PASS`.

Exact finite calculations certify the finite enumerations, not unspecified mathematical universality. The exclusion of every other prime follows from the proof that all nonzero triple determinants have norms supported only on 2, 3, 7, and 11. The input forms are those of [1], faithfully encoded as quadratic-integer coefficient pairs. This is an independently executable checker, not an independent mathematical audit; independent validation remains unperformed.
