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

# Exact verification
Run `python3 verify_pappus_full_aut.py` using Python 3.10+ standard library. The complete reconstruction was executed successfully before final packaging.

* The graph has 18 vertices, 27 edges and 216 automorphisms; its group has 13 conjugacy classes.
* The independence complex has 2,598 augmented faces; its nine augmented binary boundary ranks are \((1,17,109,329,472,274,74,16,2)\).
* It has mod-two reduced homology concentrated in degree four, of dimension ten. Rational concentration follows by the universal coefficient theorem and rational rank by the Euler characteristic.
* The full 216-element signed simplicial fixed-face traces agree with the independent signed permutation-cycle and quotient-independence-polynomial method.
* Both proposed irreducible characters satisfy exact orthogonality and all 169 class-algebra multiplication checks using rational arithmetic, and sum to the full homological Lefschetz character.
* The trace average is zero, yielding rationally acyclic full symmetry quotient.

Completion strings: `PAPPUS_FULL_216_AUTOMORPHISM_CHARACTER_VERIFIED` and `PAPPUS_DIRECT_SIGNED_TRACE_ALL_216_VERIFIED`.

The finite script proves this exact graph-level character assertion, not a general family theorem. The representation is rational but its integral equivariant lattice is not determined. Independent mathematical validation has not been performed.
