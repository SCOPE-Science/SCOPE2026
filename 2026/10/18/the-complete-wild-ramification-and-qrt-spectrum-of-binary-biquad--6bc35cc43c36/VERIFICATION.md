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

# Reproduction and scope

Run the two stand-alone programs in an environment with Python 3. The Gröbner program `check_qrt_sympy.py` requires SymPy, while `qrt_f2_verify_independent.py` requires only the standard library.

`check_qrt_sympy.py` verifies the unit-Jacobian ideals on all four affine charts of all 511 nonzero masks and prints `GROEBNER_SMOOTH_COUNT 144` followed by `GROEBNER_OK`. This computes geometric smoothness, not rational-point smoothness.

`qrt_f2_verify_independent.py` separately enumerates the homogeneous coefficient-space orbit action by swap/shear and factor interchange, detects geometric singularities in an explicit \(\mathbf F_{16}\) point universe for cross-checking, constructs the two rational ruling involution permutations and checks the six signature rows. It prints `MINIMAL_SINGULAR_DEGREES [(1, 318), (2, 49)]`, `SMOOTH_FORMS 144`, `NUMBER_ORBITS 6`, and `VERIFIED_OK`. `TABLE.tsv` contains the same six rows.

The global-order proof is in `RESULT.md`: the deck involutions are elliptic reflections and their product a rational translation. Without that lemma, rational finite-point cycling alone would not establish global periodicity. Singular-point searches over a finite extension are auxiliary only; the algebraically closed smoothness criterion is supplied by the Gröbner calculations. No independent audit has been conducted.
