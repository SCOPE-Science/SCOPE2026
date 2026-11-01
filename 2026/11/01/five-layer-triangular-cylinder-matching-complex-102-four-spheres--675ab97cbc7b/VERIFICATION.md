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

# Executable verification
Run `python3 verify.py` using Python 3 and its standard library. The checker regenerates the graph, enumerates *every* matching simplex, independently obtains the matching-polynomial coefficients from vertex deletion, builds a fixed pivot-based discrete-Morse matching, and constructs all codimension-one gradient directions. It verifies the pairing condition, all critical dimensions, and acyclicity by a full topological sort. It evaluates signed simplicial Lefschetz traces of each of the twelve graph automorphisms and independently checks them via whole-edge-orbit matchings. It then checks the six irreducible rational representation multiplicities.

Observed successful output:
```
VERIFY_OK edges=27 faces=11977 incidences=55209 pairs=5937 critical=(1 in degree 0, 102 in degree 4) symmetry=all_12_automorphisms
```

The finite exhaustive assertions certify the combinatorial premises of the proof. Forman's discrete-Morse theorem and the classical Lefschetz trace and character-orthogonality formulas complete the paper-level deductions; none of those general theorems is implemented as a formal proof assistant. The calculation does not establish any result for larger cylinders. Independent audit has not been performed.
