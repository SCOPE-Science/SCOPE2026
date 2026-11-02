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

# Finite and infinite verification

The proof of the universal large-cycle bound is in `RESULT.md`, Section “Proof,” part 2. It is a direct winning-strategy argument and is not inferred from the finite census.

The first reproducible check is `python3 verify_rank4.py`. It enumerates all ordered tuples of length three and four, allowing repeated vertices, and constructs their zero-round diagrams and all successive exact one-point-extension sets. Each size from 3 to 24 is included with every possible move. Expected output ends in `RANK4_SQUARE_CYCLES_ALL_CHECKS_PASS`, reporting rank-three classes `{3,4,5}`, singletons 6 through 10, and common class 11 through 24, and rank-four classes `{3}`, `{4,5}`, singletons 6 through 18, and common class 19 through 24.

The independent implementation is C++17: compile `c++ -O2 -std=c++17 verify_independent.cpp -o verify_independent` and execute `./verify_independent`. It uses integer-indexed tuples and explicit sorted sets, separate from the Python tuple product implementation; it asserts the same partitions and prints `INDEPENDENT_INTEGER_INDEX_RANK4_PASS` and `INDEPENDENT_INTEGER_INDEX_RANK3_PASS`.

Checks completed: both programs were run successfully on the included source implementations; all finite cases reported the specified classes. Verification is deterministic, with no random sampling, approximate numeric equality, or downloaded lookup tables. The all-size deduction uses transitivity together with the separately proved upper bound. The codes do not attempt to verify the mathematical induction mechanically or establish historical novelty. Independent external scientific audit is not performed.
