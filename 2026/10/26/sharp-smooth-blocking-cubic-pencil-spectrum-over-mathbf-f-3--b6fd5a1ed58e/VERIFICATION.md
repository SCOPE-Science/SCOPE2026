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

The mathematical computation was checked by two distinct exact approaches. Run `g++ -O3 -std=c++17 verify_census.cpp -o verify_census && ./verify_census`, `python3 verify_pencils_groebner.py`, and `python3 verify_global_groebner.py` in a directory containing all companion files. Python requires SymPy. Their deterministic console outputs are supplied in `verify_census.expected.txt`, `verify_pencils_groebner.expected.txt`, and `verify_global_groebner.expected.txt`.

The C++ implementation enumerates all normalized cubic pencils through the displayed blocking cubic, all projective ternary cubic equations, and the complete projective matrix group. It uses finite-field arithmetic in degrees one, two and three. The Python programs instead compute unit ideals in all three projective charts; this decides geometric smoothness over the algebraic closure without finite sampling. Both independent calculations recover precisely the same 312 canonical coefficient vectors. The sorted C++ output `pencils_recomputed.txt` and the Python output `pencils_groebner_recomputed.txt` must each equal `accepted_pencils_reference.txt` byte for byte. These computations certify only the explicitly enumerated finite domain, not analogous claims in larger fields. No independent audit is asserted.
