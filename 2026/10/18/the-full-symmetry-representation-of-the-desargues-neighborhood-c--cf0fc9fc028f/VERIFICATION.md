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

# Exact reproducibility and limits

Execute `python check_characters.py` and `python check_homology.py` with Python 3 standard library only. Each program builds the simplex list independently rather than relying on stored matrices or screenshots.

`check_characters.py` checks exactly 10 vertices, 30 edges, ten 2-faces per component; all 120 symmetric-group permutations; their 7 conjugacy-class signed chain traces and homology characters; every degree-five Specht character via Jacobi–Trudi; the exact irreducible decomposition; all 60 full flags of a component in one orbit. It also checks that every 1-simplex is associated to just one 2-simplex.

`check_homology.py` independently constructs the 10-by-30 first boundary and 30-by-10 second boundary, verifies boundary composition zero and exact ranks 9 and 10 using rational Gaussian elimination, constructs 21 fundamental integral graph cycles, quotients by ten primitive triangle relations, and computes actual quotient-homology linear maps for one representative of each of the seven cycle types. Their traces agree with the claimed character values without relying on signed Lefschetz traces or supplied irreducible tables.

The structural derivation of the integral free-abelian homology uses a unit 10-by-10 boundary minor, not merely a finite-field rank. The global orbit-space result uses transitivity of complete flags and the inversion-free barycentric subdivision action, not homology averaging. Both checkers terminate with explicit PASS lines. Independent audit and any claim of exhaustive bibliographic priority remain unperformed.
