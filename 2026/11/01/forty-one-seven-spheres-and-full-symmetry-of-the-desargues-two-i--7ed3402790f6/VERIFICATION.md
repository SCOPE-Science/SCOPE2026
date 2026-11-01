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
# Finite verification

The self-contained program `verify_desargues_higher.py` uses only the Python standard library. Its assertions reconstruct twenty vertices and thirty edges from the \(2\)- versus \(3\)-subset incidence presentation. It enumerates exactly \(62{,}048\) nonempty admissible faces and cross-checks them by independent exhaustive processing of all \(2^{20}\) subsets. The checked f-vector, matching, DAG topological sort, and character calculations are documented in the accompanying `verify_desargues_higher.out` output.

The augmented discrete-Morse matching contains \(31{,}004\) pairs, and the reversed entire Hasse DAG visits all \(62{,}049\) faces. Its remaining forty-one unmatched faces all have dimension seven. Removing the augmented empty-face pair leaves one critical vertex, giving the integral homotopy classification. For each of the \(14\) conjugacy classes of the full \(240\)-element automorphism group, signed simplicial fixed-face enumeration yields the seventh-homology trace. Exact irreducible-character inner products prove the stated multiplicities, the central eigenspace ranks and the invariant rank.

Replay instruction: `python3 verify_desargues_higher.py`. The successful run ends `ALL_CHECKS_PASS`. This verifies the precise finite input and deductions described above; an external or independent mathematical audit has not been performed. The proof assumes the standard discrete-Morse equivalence theorem, elementary representation-theoretic character orthogonality and finite-group rational homology averaging. No claim is made for arbitrary graphs, other independence parameters, or integral equivariant lattice splitting.
