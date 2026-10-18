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

The 15-dimensional kernel of the full 13-point evaluation map was rebuilt from all degree-six monomials. Every one of the 14,348,906 nonzero vectors was enumerated, with the rational smoothness and quadratic Taylor contact conditions checked over \(\mathbf F_3\). Group-generator orbits cover all candidates with 11 or 9 rational flexes, and exact Jacobian Groebner bases distinguish geometrically singular from smooth representatives in all three charts. A second computation explicitly substitutes each tangent-line parameter at the 13 rational points and compares orders, independently of the stored quadratic jets. Both programs agree that the three nine-flex smooth orbits each contain 5,616 projective equations.

Requirements: Python 3 with SymPy and a C++17 compiler. In the `verify` directory run `python make_jets.py`, `g++ -O3 -std=c++17 enumerate.cpp -o enumerator`, `./enumerator > enumeration_replay.txt`, `python orbits.py`, `python check_orbits.py`, and `python independent_contact.py`. Compare with embedded exact reference outputs. This is computational exhaustive evidence for a finite problem, not independent validation.
