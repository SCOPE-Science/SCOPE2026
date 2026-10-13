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

# Reproduction and limits

The finite proof is reproduced using the complete, standalone `check_python.py` and `check_cpp.cpp` sources included here. They enumerate every reversal orbit of binary eight-character words, test each possible proper overlap, generate the necessary pairwise-compatibility graph, enumerate every maximal clique, and then test complete selected code sets for every possible forbidden triple splice. The second checker uses integer bitmasks and pivoted Bron--Kerbosch recursion, independently of the first string-based implementation.

```sh
python3 check_python.py > python_out.txt
g++ -std=c++17 -O2 -Wall -Wextra -pedantic check_cpp.cpp -o verify_cpp
./verify_cpp > cpp_out.txt
cmp python_out.txt cpp_out.txt
cmp python_out.txt optimal_codes.txt
```

Both checks passed on the packaged artifact sources and yielded exactly twelve eighteen-word self-reflective comma-free codes; the graph-only upper-bound census had sixteen candidate maximum-weight cliques, of which four failed the required third-word overlap test. The definitive aggregate counts appear in the first line of `optimal_codes.txt`.

Completeness requires the Bron--Kerbosch maximal-clique traversal; it is not inferred from an arbitrary time-limited graph search or the supplied output alone. The exact theorem holds at binary length eight only. The verification checks correctness of the finite computation; it does not establish independent publication priority or general performance under substitutions, insertions or deletions.
