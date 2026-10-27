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

# Reproduction of the exact finite-field enumeration

Work in the directory containing these files. The programs do not require internet access or third-party datasets. Python with NumPy and SymPy and a C++17 compiler are required for the complete replay. Run `python hyperflex_prep.py` to rebuild the 52 flag constraints; `python hyperflex_orbit_prep.py` to rebuild four generating substitution matrices; compile `g++ -O3 -std=c++17 hyperflex_enum.cpp -o hyperflex_enum` and `g++ -O3 -std=c++17 hyperflex_orbits.cpp -o hyperflex_orbits`; run `./hyperflex_enum`; run `python hyperflex_filter.py`; run `python independent_rational_smoothness.py`; run `./hyperflex_orbits`; run `python hyperflex_smooth.py`; run `python hyperflex_reps.py` and `python contact_table.py`.

`hyperflex_enum.cpp` performs full kernel enumeration and produces all hyperflex-count candidate lists. `hyperflex_filter.py` tests gradients at the 13 rational points. `independent_rational_smoothness.py` implements the same mathematical criterion independently using only the Python standard library and matches all 52,884 exact candidate indices, as recorded in `independent_rational_smoothness.txt`. `hyperflex_orbits.cpp` enumerates full projective closure using standard generators, and `hyperflex_smooth.py` checks the Jacobian ideal on the three standard affine charts for all 18 representatives. The included `hyperflex_orbits.json` lists every orbit member, and `representative_contacts.json` includes contact witnesses. The summary files record actual completed program outputs.

Expected exact counts: 7,174,453 total scalar-normalized nonzero quartic equations, 52 rational point-line flags, 9,997 candidate equations with at least five flags and zero rationally nonsingular among them, 87,750 equations with four flags, 52,884 rationally nonsingular candidates with four flags, 18 orbits, three geometrically smooth orbits of sizes 1,872, 234, 234, and 2,340 smooth equality equations total. This method establishes complete finite enumeration only for this field and degree; it is not evidence of uniqueness in any larger domain. Self-review has been performed, not independent audit.
