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
# Verification of the crown-graph three-cut formulas

The mathematical argument is in `RESULT.md`. The independent-of-symbolic-packages checker `CHECK.py` runs under Python 3 standard library and checks the first three newly covered parameters \(n=5,6,7\) from the graph definition. Execute `python3 CHECK.py` from a directory containing the extracted files. Its final line is `CHECK_OK finite tests; parameter-uniform proof is mathematical.`

The checker exhaustively enumerates simplices of the cut complex and its Alexander dual and verifies the chessboard-plus-matching decomposition with no gaps. It computes boundary ranks in characteristics \(101\) and \(103\), reconstructing the predicted Betti groups of the dual, and tests all permutations up to conjugacy together with part interchange using exact signed fixed-face sums. It also checks the face-vector formulas. The expected rank values for the two nonzero homology groups of the cut complex are \((1,5)\), \((19,6)\), and \((71,7)\) for these three parameters, respectively.

**Limits of computation:** A check in two finite characteristics is not an integer Smith-normal-form certificate and cannot on its own exclude torsion at other primes or establish every parameter. Torsion-freeness and the all-parameter character formulas follow instead from the shellability theorem, integral Alexander duality, and the proved combinatorial orbit enumeration. No external independent audit is asserted.
