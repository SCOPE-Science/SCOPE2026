# Independent mathematical audit

## correctness

PASS

For each nondecreasing word-map f, f(S) is a singleton iff f(min S)=f(max S), so reduce each subset to one of n(n+1)/2 ordered pairs. Inspected frozen census.cpp (blob 4bca34cd5dc132bf86d057e5252e9b6a36195cd1): enumerates all C(2n-1,n) monotone maps, every unordered pair of letter maps, forms exact inverse pair-state transitions, and reverse-BFS layers from every diagonal. The program asserts 0,1,2,3,4,5,6,7,9 for n=1..9 and exactly two unordered normalized n9 extremals, hence four ordered. Independent Python reverse pair BFS checked the enumeration mechanism exhaustively for n<=5, and independent forward BFS for the explicit n9 maps from (1,6) returned shortest word babbaabbb length 9. N9 full 590976100 ordered-pair computation was inspected but not independently rerun: no false claim of its execution. Its complete source loops provide a bounded finite exhaustive certificate, beyond finite extrapolation.

## originality

PASS

Binary monotonic automaton subset-synchronization is a published problem; the new assertion is the first exact n<=9 threshold and the chain-normalized extremal classification, not the general asymptotic lower/upper bounds. In the reviewed primary work these sharper small-size data were not stated or implied; best-of-knowledge PASS with unindexed-census risk.

## value

PASS

Exact first failure of the linear n−1 bound is a natural minimal-size frontier in binary monotone subset synchronization; isolating n=9 and classifying all chain-normalized extremal maps can guide constructions and benchmarking. This is not simply a renamed asymptotic theorem, and no n>=10 assertion is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
