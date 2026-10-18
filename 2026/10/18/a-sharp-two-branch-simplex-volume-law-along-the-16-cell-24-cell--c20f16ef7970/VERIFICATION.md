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

# Reproducing the truncated-16-cell simplex certificate

Run `python3 verify.py` from this folder, with a C++17 compiler available as `g++`. The program itself compiles `enumerate.cpp` to a temporary directory and leaves no generated inputs or compiler dependencies in the research package. Only Python's standard library is required.

The enumerator constructs 48 affine-in-parameter vertices from four coordinate indices and signed pairs, fixes an initial vertex by signed-permutation symmetry, enumerates all 178,365 remaining vertex quadruples, and computes determinants using 24 permutation terms with integer polynomial coefficients. It collapses signs to 258 distinct polynomial profiles and counts their exact multiplicities. The Python stage verifies exact degree-four Bernstein positivity on the two algebraic intervals split at \(\sqrt2-1\), evaluates breakpoint ties exactly in \(\mathbb Q(\sqrt2)\), and performs an independent rational determinant spot-check of every polynomial-profile representative. It then constructs complete signed-permutation orbits and verifies incidence-graph counts and exact same-sign alignment for the 48 movable-apex pairs.

Expected terminal output includes `PASS: 178365 vertex-anchored determinants` and the phase counts 192, 288, 96. This establishes the stated finite certificate conditional on execution of the supplied transparent source; the universal implications from the certificate are proved analytically in `RESULT.md`. Sampling alone cannot establish the continuum bound, and no independent audit has been performed. The full equality structure at the isolated breakpoint remains unproved beyond the vertex-supported count.
