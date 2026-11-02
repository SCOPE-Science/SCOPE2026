# Self-review

## Correctness (C): PASS

The target domain, length bound, exact prefix requirement, and one-sided rewriting rule are explicit. A length-one step leaves the prefix-`01` sector forever; the remaining two operations are to prepend `01` or `010`. The positions of successive `1` symbols uniquely decode these blocks before the specified suffix, proving uniqueness of **every** derivation and the exact step count. The geometric series gives the full length–distance enumerator. Same-parity Fibonacci words have the needed suffix relation, initial `010`, and gaps of two or three between successive `1` symbols. The bound-four witnesses are explicit. Forward and reverse independent finite verifiers passed 1,750 general targets, 63 Fibonacci pairs and two boundary examples; the infinite conclusion is deductive, not extrapolated from the tests.

## Originality (O): PASS with residual priority risk

The closest paper is Cabrera Salamanca–Smith (arXiv:2607.20405v1, 22 July 2026), inspected in full HTML. It establishes generation of same-parity Fibonacci words, but not all-seed path uniqueness or the regular-language and generating-function identity. Its companion repository's README and entire `derive.cpp` were inspected: they claim an optimized shortest derivation algorithm for Fibonacci inputs, **already addressing the computational shortest-path special case**, but do not characterize all arbitrary-seed paths or establish the universal closed enumerator. The 2014 general-distance and bounded-duplication works provide algorithms and regular-closure results, not an identified exact free two-generator sector from accessible material. The bounded paper's PDF and full general-distance text remained partly inaccessible, so residual priority risk is real. Related published mathematical-record and historical-claim searches found no direct equivalent; negative search results alone do not establish originality.

## Value (V): PASS

A newly motivated operation receives a complete regular-language classification and an exact distance-refined growth series for every seed in a natural invariant prefix class, with a sharp boundary at the next allowed duplication length. The exact simultaneous Fibonacci-pair formula and uniqueness result provide a structural explanation beyond the recent construction, rather than a small unmotivated numerical improvement.

## Limitations

No assertion is made for targets beginning `00`, suffix duplications, arbitrary prefix bounds, or mixed-parity Fibonacci pairs. Published algorithms may already compute individual Fibonacci shortest paths. Full access to all historically relevant material and independent mathematical validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
