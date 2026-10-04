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
# Verification

Run `python verify_tournament_torsion.py` with Python and SymPy available. The program performs the following checks from explicit tournament adjacency bits rather than loading a topology table:

1. It recursively generates tournament isomorphism representatives through order \(7\) and obtains counts \(1,1,2,4,12,56,456\). The final count \(456\) agrees with McKay's independent catalogue.
2. For each of all \(532\) representatives it constructs the full out-neighborhood complex by downward closure of all out-neighborhoods.
3. It constructs every integral simplicial boundary matrix with the increasing-vertex orientation and verifies \(\partial_k\partial_{k+1}=0\).
4. It computes \(\ker \partial_k/\operatorname{im}\partial_{k+1}\) using exact Smith-normal-form basis changes over \(\mathbb Z\). No torsion invariant factor larger than \(1\) occurs.
5. It independently computes every mod-\(2\) Betti number by bitwise Gaussian elimination and checks agreement with the free integral ranks when the exact calculation is torsion-free.

A successful replay prints `TORSION_WITNESSES []` and terminates with `VERIFY_OK`.

The computation proves only the finite domain \(|V(T)|\le 7\). It does not test any tournament on eight or more vertices and does not establish general torsion-freeness. The exact integer result depends on SymPy's Smith normal form implementation; the separate mod-\(2\) calculation checks ranks but, by itself, would not detect all possible odd torsion.
