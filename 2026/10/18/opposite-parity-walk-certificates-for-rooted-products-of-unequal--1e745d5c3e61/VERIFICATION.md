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

# Verification and reproduction

All tests below were actually executed from the accompanying standalone source files using Python 3. The first three scripts require only the Python standard library; `verify_automorphisms.py` requires NetworkX 3.6.1. Commands are run from the directory containing the scripts.

- `python verify_direct.py`: 105 unequal odd cycle pairs, 33,855 graph vertices, 9,465 expected rooted profiles. Actual output is in `output_direct.txt`.
- `python verify_walks.py`: separately computed geodesic lengths, geodesic multiplicities and first opposite-parity walk lengths using two distinct BFS constructions on the same 105 graph pairs. Actual output is in `output_walks.txt`.
- `python verify_profiles.py`: checked algebraic signature injectivity across 4,950 pairs with odd \(5\le m<n\le203\), covering 13,601,775 profiles. Actual output is in `output_profiles.txt`.
- `python verify_automorphisms.py`: explicitly enumerated all rooted graph automorphisms for \((m,n)=(5,7),(5,9),(7,9)\), confirming group order four and the exact reflection orbits. Actual output is in `output_automorphisms.txt`.

The tests use distinct algorithms: literal one-dimensional neighbour-colour refinement, standard shortest-path BFS, BFS on a doubled parity-state graph, combinatorial binomial evaluation, and general rooted graph-isomorphism enumeration. They are finite checks, not an exhaustive proof for unbounded odd lengths. The all-length correctness rests on the lattice-lift and binomial-injectivity arguments in `RESULT.md`. No independent audit has been conducted.
