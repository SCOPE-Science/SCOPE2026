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

Execute `python3 verify.py` with the accompanying file. It needs only standard-library Python.

The checker constructs the sixteen vertices and twenty-four edges from the modular graph definition, confirms graph diameter four and the eight disjoint antipodal pairs, enumerates all scale-two simplices, produces and verifies 118 pairs as a global acyclic Hasse matching, and performs exact signed integer chain cancellations. The verified critical-cell counts are one in degree zero, nine in degree two, and two in degree three. Every canceled boundary pivot equals \(\pm1\) and the resulting integral Morse differential is identically zero.

It checks two explicit integral top-degree cycles and their independent primitive coordinates, enumerates every one of the 96 graph automorphisms, rechecks adjacency preservation through backtracking, calculates signed simplex Lefschetz traces, and verifies both the degree-two and degree-three full characters. For the scale-three cross-polytope, it checks the top orientation character. Rational invariant dimensions are \(0,1\) at radius two in degrees two and three and \(1\) at radius three in degree seven. Graph degree-one invariants also vanish.

Expected final marker: `MOBIUS_KANTOR_RIPS_EXACT_MORSE_96_CHARACTER_OK`.

These tests are a reconstructible finite proof certificate rather than an infinite-family computation. No formal external certification or independently performed audit is asserted.
