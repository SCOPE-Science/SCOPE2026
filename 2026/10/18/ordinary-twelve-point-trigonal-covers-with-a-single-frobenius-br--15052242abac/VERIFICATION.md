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

# Reproduction and mathematical checks

The included `verify_classification.py` uses only Python 3's standard library. Run `python3 verify_classification.py` from this package directory. The expected counts are exactly 48 irreducible degree-five monic polynomials in 8 free affine orbits and 312 degree-seven monic polynomials in 52 such orbits, with first representatives in increasing coefficient order printed by the program.

Scientific generality rests on the Riemann–Hurwitz and Deuring–Shafarevich formulas, the rational-fibre argument, Castelnuovo–Severi uniqueness of degree-three maps in genus greater than four, and the finite centralizer of Frobenius in the group of permutations of the branch roots. The polynomial enumeration is a diagnostic check only; it does not independently establish infinitely many genera or global novelty. The claim concerns \(\mathbf F_3\)-rational, not geometric, automorphisms and isomorphisms.
