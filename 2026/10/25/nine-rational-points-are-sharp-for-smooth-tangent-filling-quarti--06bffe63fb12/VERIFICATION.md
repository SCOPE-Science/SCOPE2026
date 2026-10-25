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

The exact checks are reproducible from three standalone programs included alongside this file.

Run `g++ -O3 -std=c++17 verify_dual_blocking.cpp -o dual` followed by `./dual`. This exhaustively enumerates the 7,888,725 eight-line subsets of the 31-line projective plane over \(\mathbf F_5\), confirming that each covering subset contains a complete six-line pencil.

Run `g++ -O3 -std=c++17 verify_pencil_lower.cpp -o pencil` followed by `./pencil`. This enumerates all 34,375 rational contact-point patterns for six lines through a fixed rational point, all nonzero solutions to their exact linear constraints, and discards rationally singular forms. The smallest number of rational curve points among remaining forms is nine. The number of tested configuration–equation incidences is not a count of inequivalent or distinct quartic curves.

Run `python3 verify_examples.py` using SymPy. This verifies each example's nine rational curve points, nine distinct tangent lines, complete coverage of the 31 rational plane points, and three exact unit Jacobian Gröbner bases over \(\mathbf F_5\). A unit ideal of homogeneous derivatives on all three charts proves smoothness over the algebraic closure. The first example's dual tangent configuration contains a full pencil and the second does not.

The finite exact lower-bound enumeration tests rational nonsingularity as a **necessary** condition, and does not claim that every enumerated form is geometrically smooth. Its coverage of all geometrically smooth full-pencil candidates follows from that inclusion. Neither reference output log alone substitutes for the source algorithms. The main theorem does not classify all extremal curves and has not received independent external audit.
