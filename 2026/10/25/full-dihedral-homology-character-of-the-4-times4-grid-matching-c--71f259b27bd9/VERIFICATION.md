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

# Exact verification of the square-grid matching-complex character

Execute `python3 verify.py` using Python 3.9+; no third-party Python packages are required. The verifier independently generates the 24 graph edges and all 10,012 augmented matchings. It constructs the deterministic edge-toggle partial matching, checks all 47,968 oriented Hasse arrows with a complete DAG topological sort, and obtains exactly ten cardinality-five and six cardinality-six critical faces. There are 4,998 matched simplex pairs.

For every matched incidence block used by the elimination, the program builds all signed entries from oriented boundaries, checks unit diagonal pivots, verifies acyclic triangular dependencies, and solves exactly over the integers. It checks the complete critical differential, an integral \(4\times4\) minor of determinant \(-1\), and two independent kernel vectors. Crucially, it verifies the complete original-chain identities, not only small numerical ranks.

It then constructs genuine integral cycles for the two generators in degree five, applies all eight grid automorphisms with orientation signs, subtracts exact boundaries, checks equality with integer combinations of the basis cycles, and calculates degree-five character traces. Separately, it enumerates signed fixed simplices for the reduced Lefschetz traces, derives degree-four traces and checks all irreducible character identities and invariant dimensions.

The verified run emitted:
```
EXHAUSTIVE_MORSE_ACYCLICITY 10012 47968
INTEGRAL_MORSE_DIFFERENTIAL_RANK_FOUR 10 6 unimodular_minor -1
ALL_EIGHT_DIHEDRAL_CHARACTERS_VERIFIED {(0, 0): 6, (0, 1): 0, (1, 0): 2, (1, 1): -2, (2, 0): 2, (2, 1): 0, (3, 0): 2, (3, 1): -2} {(0, 0): 2, (0, 1): 0, (1, 0): 0, (1, 1): 0, (2, 0): -2, (2, 1): 0, (3, 0): 0, (3, 1): 0}
DEGREE_FOUR_AND_FIVE_MODULES_AND_QUOTIENT_VERIFIED
```

Scope: exhaustive finite exact calculation for the stated 16-vertex grid. It is not an independent external certification, publication-priority guarantee, or proof of a general formula for larger grids. The quotient conclusion uses standard rational invariance under a finite simplicial group action after barycentric subdivision.
