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
# Finite verification

From the directory containing this file, run `sh reproduce.sh` with a C++17 compiler and Python 3. There are no downloaded data dependencies or third-party Python modules. The script compiles the two standalone C++ source files from their embedded contents, executes them, then executes `verify_small.py`.

`count_ordered.cpp` enumerates all cliques containing the zero triple using increasing vertex indices in a 343-vertex compatibility graph formed from direct coordinatewise distinction. `count_coloring.cpp` instead derives adjacency by complementing coordinatewise confusability and visits cliques in greedy-color reverse order. Each complete recursion counts eight-word solutions and proves that no nine-word solution contains the zero triple. Both must report exactly `38259704` and `0`. Translational transitivity turns this rooted result into an exhaustive global proof, not a sampling estimate.

`verify_small.py` checks each of the 211876 four-subsets of the two-use space, excludes two-use five-cliques by an independent exact recursion, checks the product construction and explicit indecomposable eight-word witness, and reproduces every decomposition and translation-orbit count using integer arithmetic. The program produces:

```
ORDERED rooted_eight=38259704 rooted_nine=0
COLORING rooted_eight=38259704 rooted_nine=0
SMALL oneuse_pairs=7 twouse_maxima=1715 twouse_no_five=true
STRUCTURE all=1640384809 decomposable=35329 indecomposable=1640349480 pure=343 translation_orbits=4782463
WITNESS indecomposable_valid=true
VERIFY_OK root8=38259704 root9=0 N3=1640384809 decomposable=35329 indecomposable=1640349480
```

The code establishes exact finite statements only for the specified seven-symbol, three-use channel and one-versus-two-coordinate decomposition notion. It does not classify equivalence under all automorphisms or establish any infinite-length statement.
