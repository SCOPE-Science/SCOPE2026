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

# Computational and mathematical verification

The all-\(n\) theorem is proved by the degree identity, the injectivity of the pair-product code \((2^a-1)(2^b-1)\), the complete pair-multiset inversion, and symmetric-group transitivity. These proof steps do not rely on numerical tests.

`python3 verify_direct.py` enumerates full partition-Hasse digraphs for \(n=1,\ldots,8\), computes two refinement rounds from a uniform initial colour, and confirms that the second colour classes coincide with the integer block-size types. At \(n=8\) this graph has \(4140\) vertices. It verifies the explicit distinct first-round collision at \(n=14\) and checks the two-adic product valuation identity for \(4005\) unordered positive exponent pairs.

`python3 verify_types.py` separately builds the weighted directed quotient by block-size type for every \(n=1,\ldots,36\). It computes exact merge counts and exact splitting counts as quotient edge weights and checks that the second refinement round separates every block-size type, including the \(17977\) types at \(n=36\). It also exhaustively verifies that one round separates all types exactly when \(n\le13\) over the tested size range; the proof's explicit collision and singleton-extension argument covers every larger size.

Recorded program outputs are stored in `direct_output.txt` and `types_output.txt`. All scripts require Python 3 standard library only. The finite computations do not by themselves certify the unbounded theorem, historical originality or independent validation.
