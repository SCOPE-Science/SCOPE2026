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

# Reproduction and proof limits

Run `python check_pebbles.py`, `python check_orbits.py`, and `python check_terms.py` with Python 3. No downloads or third-party dependencies are required. Their stdout records are included as `check_pebbles.out`, `check_orbits.out`, and `check_terms.out`.

The first script builds small commuting-permutation structures from pairs of lattice generators and direct sums. It extracts orbit stabilizer signatures independently of syntactic formula construction, computes complete term-displacement atomic diagrams for selected variables, and iterates the simultaneous one-variable-replacement type refinement to stability. Its 348 comparisons across widths 1, 2, and 3 agree with truncation classification. Its finite scope does not prove arbitrary widths, actions, or depths.

The second script independently enumerates all ordered commuting pairs of permutations on labelled sets of sizes 1 through 6. It canonicalizes transitive components by generator-first traversal, compares the observed counts with the index-subgroup divisor sum, and verifies isomorphism-class counts via an independent Euler-product dynamic program. It also produces coefficients through degree 12 for widths 1, 2, and 3.

The third script independently constructs 87 period lattices of index at most ten, testing the quantifier-free stabilizer formula against every ordered pair of orbit types and all orbit points (54,114 point checks).

The proof of the infinite result is self-contained in `RESULT.md`, using a one-variable stabilizer tester, a finite disjoint-orbit sentence, a permanent pebble-game invariant, and Hermite normal form. The finite checks are corroboration and must not be treated as exhaustive infinite certification. There has been no independent mathematical audit.
