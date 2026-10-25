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

The accompanying programs use only Python 3 standard-library modules. Execute `python3 verify_spectrum.py` and `python3 verify_independent.py` from the extracted package directory. Their outputs must exactly match the corresponding `.log` files. The first program computes every labeled square from four independent row permutations, all legal \(2\times2\) trades, all \(144^2\) entries of \(BB^{\mathsf T}\), the integer annihilator identity on the complete standard basis, and exact trace values through degree four. This establishes the characteristic polynomial through the bipartite singular-value transfer. The second program independently builds Latin squares by recursive column-restriction search and generates trades through symbol-transpositions; it also computes all-pairs BFS distances. Both reconstruct the same canonical adjacency SHA-256 and report a 576-vertex connected graph of diameter six.

This verification is exhaustive for the finite graph of labeled order-four Latin squares. It does not establish publication priority, results in arbitrary orders, or independent external review. The full text of the most directly relevant 2026 spectral-branch working paper could not be accessed; only its public description was compared.
