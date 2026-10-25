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
# Reproducibility and verification

## Exact scope

The result concerns the finite abstract simplicial complex of independent vertex sets of the simple graph on all 32 binary five-tuples, with edges joining tuples at Hamming distance one. The homology groups and integral group action are proven, not the full unstable homotopy type.

## Self-contained reproduction

Run `python3 verify.py` under Python 3.9+ (standard library only). The program requires no external files and makes no network calls. It regenerates every face via a complete include/exclude recursion, creates the deterministic sequential toggle matching, and checks that the associated directed Hasse graph is acyclic by a topological sort covering all nonempty simplices. It then generates ten signed crosspolytope cycles, independently checks their boundaries, and performs an exact integer Morse projection. A 10-by-10 Bareiss determinant of -1 certifies a full-rank, **index-one** basis of the integral seventh homology. Finally it verifies the permutation-orientation sign for each sphere and the signed Lefschetz trace for all 3,840 automorphisms of the five-cube.

The recorded output `verification_output.txt` ends `VERIFY_OK`. The expected counts are 254,475 faces including empty, 127,231 matched pairs, critical cells of dimensions 0, 5, and 7 with counts 1, 1, and 10, and 1,844,864 codimension-one incidences. The proof does not substitute a finite characteristic calculation for an unbounded theorem: the graph and every input range have exactly the specified finite sizes.

## Mathematical boundaries

Rational dimensions alone were established in prior literature and are not a novelty claim. Absence of critical six-cells and four-cells proves the integral homology statement; it does **not** imply that attaching maps from the seven-cells are nullhomotopic. The equivariant theorem is a statement about integral homology lattices, not a fully equivariant homotopy equivalence. No independent audit has been performed.
