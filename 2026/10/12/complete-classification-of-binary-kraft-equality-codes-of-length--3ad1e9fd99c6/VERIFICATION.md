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

Compile and run `verify_bitmask.cpp` with a C++17 compiler, and run `verify_independent.py` under Python 3. Both use only standard libraries. The first enumerates all choices of length-three and length-four words with Kraft equality, represents dangling suffixes as a directed finite graph, rejects codeword-reachable residuals, and checks finite-delay status from cycles. The second independently enumerates the same 1,901,636 candidates with literal binary strings and repeated Sardinas--Patterson suffix sets. All candidate and accepted cardinalities match `CENSUS.csv`, and both identify precisely the four sets in `EXCEPTIONS.tsv`.

The full candidate-space calculation includes \(a\in\{1,2,3,4,5,6,7\}\) and no other nontrivial Kraft profiles. The proof makes no claim beyond those finite cases. Codeword reversal and global bitwise complementation were checked to generate the exception orbit. Neither a failed search nor source inaccessible in full is used as proof of novelty. Independent audit remains unperformed.
