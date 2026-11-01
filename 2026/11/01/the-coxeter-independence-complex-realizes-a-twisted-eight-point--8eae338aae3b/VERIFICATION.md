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

# Reproduction of exact checks

Run `python3 verify_coxeter_symmetry.py` with Python 3.10 or newer. The verifier uses only the Python standard library. `verification_output.txt` is the recorded successful run, including the final marker `COXETER_SYMMETRY_VERIFY_OK`.

The program independently rebuilds the Fano plane and all 28 non-line triples, verifies the 42 disjointness edges, enumerates all 196,008 nonempty independent-set faces, and performs a complete acyclic-Morse certificate on 1,319,724 codimension-one incidences. Exactly one critical vertex and seven critical six-cells remain, establishing the required homology concentration by the discrete-Morse theorem.

It enumerates all 336 graph automorphisms by exhaustive adjacency/nonadjacency-preserving backtracking, constructs eight Sylow-seven subgroups, and checks the character identity for each group element via an exact deletion–closed-neighborhood recurrence. It directly enumerates the signed fixed simplices for eight representative order/sign/fixed-point types as an independent orientation check. The output confirms both the exact character norm \(336/336=1\) and the rational invariant-space dimensions for the full group, its sign kernel, and a Sylow-seven subgroup.

The script is an exact finite certificate for the specified graph. It does not compute integral equivariant lattices or classify other graphs, and its successful execution is not an independent external audit.
