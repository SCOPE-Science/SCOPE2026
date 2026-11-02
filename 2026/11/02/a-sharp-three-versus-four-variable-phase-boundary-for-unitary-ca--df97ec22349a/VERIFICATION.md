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

The two independently coded exhaustive tests are `check_direct.py` and `check_patterns.py`; their standard-output JSON is stored verbatim in `direct.out` and `patterns.out`. Both scripts use only the Python standard library. The first constructs graphs using gcd over all 149 moduli from 2 through 150, and separately checks fourteen products of complete graphs. The second does not use that first program's graph generator: it enumerates coordinate tuples and checks the exact four witness-count formulas against every unordered pair of distinct anchors, with a further eight explicit three-anchor obstructions. Recorded output equality was checked after code execution.

The full theorem for all finite commutative rings uses the algebraic proof, not finite extrapolation. The field-coordinate enumerations use coordinate values as *labels*: no addition or multiplication table for nonprime fields is required, since only equality of field elements determines unitary adjacency in a field product. Radical nonzero cases are represented among the modular samples. A finite test cannot establish historical priority or independent audit.
