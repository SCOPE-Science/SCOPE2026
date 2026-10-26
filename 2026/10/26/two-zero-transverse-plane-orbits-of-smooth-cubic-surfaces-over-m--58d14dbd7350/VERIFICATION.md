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

# Reproducibility and limits

Compile and run `check_sections.cpp` with a C++17 compiler, for example `g++ -O3 -std=c++17 check_sections.cpp -o check_sections && ./check_sections`. This runs the exhaustive enumeration over all binary cubic forms, produces `zero_cubics.txt`, and prints the full geometric smoothness and transverse-section spectra. Compare `check_sections.out`.

Run `python check_orbits.py` from the same directory to reconstruct the two projective orbits of the 1708 exceptional masks using elementary coordinate generators. Compare `check_orbits.out`. Run `python check_representatives.py` with SymPy installed to check all thirty plane sections of the two normal-form representatives using characteristic-two Gröbner bases. Compare `check_representatives.out`.

These executions have been completed on the supplied source files. The finite arithmetic is exhaustive for degree-three four-variable equations over \(\mathbf F_2\) only. The primary literature novelty comparison remains subject to the acknowledged unavailable Dickson-derived full text. No independent audit or third-party validation is claimed.
