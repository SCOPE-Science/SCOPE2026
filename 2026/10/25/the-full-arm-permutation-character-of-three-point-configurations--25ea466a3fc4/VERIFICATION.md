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

# Verification and reproducibility

Run `python3 verify_star_three.py` using Python 3.8 or later. No third-party dependencies are needed. The companion `verify_star_three_output.txt` stores the original program output; fresh execution must end in `VERIFY_OK`.

The program constructs two-edge arms around a single center, lists unordered triples of vertices and graph edges with pairwise disjoint closures, and partitions these cubical cells by dimension. For every tested arm permutation it directly maps graph vertices and edges, identifies setwise-fixed cubical cells, and takes the signed trace from the parity of induced permutations of their oriented edge coordinates. It explicitly compares the alternating signed trace with the stated cycle-count character, checks connectivity of the 0/1-dimensional cubical skeleton, and compares Euler characteristic with the known three-particle radial-tree Betti rank. These operations are independently encoded in the program, not hard-coded from the final character expression.

Exhaustive arm-permutation coverage: 3 arms (6 elements), 4 arms (24), 5 arms (120). Additionally, one representative of each conjugacy class of the groups on 6 and 7 arms is checked, for 41 conjugacy classes total. The space itself is a finite model at each sample size, and all its cells are enumerated. These finite checks are consistency tests **only**, not a proof of the all-parameter statement.

Proof dependency for arbitrarily many arms: the inclusion of the Abrams discretized space into the collision-free configuration space is a canonical equivariant homotopy equivalence under sufficient subdivision. The one-essential-vertex theorem makes reduced rational homology vanish outside degree one. The signed fixed-cell orbit generating function is exact for all cycle lengths and yields the character by coefficient extraction; the fixed-subspace formula uses exact expectations of permutation cycle counts. The absence of a covering published character was assessed in the cited primary papers and database searches but is not independently certified.
