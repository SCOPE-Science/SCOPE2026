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

The proof is symbolic and applies to all finite products of nonempty chains. Finite verification is supplemental, not an induction over arbitrary exponent tuples.

Run `python3 verify_divisor_fo2.py` and `python3 check_fo2_formulas.py` alongside the bundled source files. The recorded `verification_output.txt` and `formula_output.txt` were produced by the respective commands. The program independently constructs finite products, computes coordinatewise comparability, determines maximal ranks of incomparable elements to atoms, and determines the least rank of elements above the atoms of each fingerprint type. A second routine applies noncounting modal color refinement to a bounded family and checks that its spectra are distinct. The refinement is a sufficient distinguishing witness, not the foundation of the full proof.

The tests cover 102 exponent multisets with total exponent at most ten and lattice size at most 120, including the two different 48-element divisor lattices with exponent multisets \((5,1,1,1)\) and \((3,3,2)\). The modal routine covers 57 structures. The independent formula generator tests bound-variable shadowing and direct first-order semantics for two concrete separating formulas, including a same-support, different-multiplicity pair. Code uses only the Python standard library.

No computation certifies historical priority, the unbounded theorem, or independent mathematical audit. All those boundaries are described in RESULT.md.
