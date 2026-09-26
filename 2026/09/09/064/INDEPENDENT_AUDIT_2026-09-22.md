# Independent audit — 2026/09/09/064

## Correctness — PASS

I independently enumerated the 35 triples ordered by sum and lexicographic order, recursively included a triple only when all its immediate down-shift predecessors were present, and obtained 352 distinct order ideals. Enumerating all five-vertex subsets and cyclic orders gave 252 distinct tight-C5 edge masks. Testing each ideal against those masks left exactly 68 C5-free ideals, with the exact stated edge-count histogram and a unique 16-edge maximum consisting of the 15 triples through vertex 0 plus 123. I also evaluated all 5,040 vertex permutations of each of the 68 ideals: their canonical forms are 68 distinct values, and no permutation of one ideal lands on a different shifted-free ideal. This independently checks the full finite headline.

The census has no direct extremal reduction: a general C5-free 3-graph cannot necessarily be shifted while staying C5-free. Therefore the 16-edge maximum is only among shifted ideals, and these 68 are not a full flag-algebra basis of C5-free 7-vertex graphs.

## Originality — PASS, finite data

The checked Kamčev–Letzter–Pokrovskiy work treats asymptotic tight-cycle density for sufficiently long lengths; the flag-algebra prior work does not list this restricted 7-vertex census. The 68-class table is a specific reproducible enumeration, with no claimed new asymptotic theorem.

## Scientific value — PASS, limited

The exact small shifted-family table and unique extremal can serve as a consistency check for compression experiments. Since shifting need not preserve the forbidden condition, its use toward the C5 Turán density requires additional arguments and it does not yield an upper bound.

## Sources

- Original RESULT.md and METADATA.json; independent 35-poset/252-mask/5,040-permutation computation above.
- Kamčev–Letzter–Pokrovskiy, https://arxiv.org/abs/2209.08134 .
- Falgas-Ravry–Vaughan, https://arxiv.org/abs/1110.1623 .
