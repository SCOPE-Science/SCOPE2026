# Independent mathematical audit

## correctness

PASS

The class consists of exactly (7-1)!=720 cyclic orders, represented as permutations beginning 0, and each orientation query is a well-defined Boolean comparison of clockwise positions. A fresh independent full enumeration found all 128 response strings on the seven displayed triples. For the upper VC bound, relabeling acts transitively on oriented triples up to response complementation, so any shattered eight-support has a representative containing (0,1,2); an exhaustive 720-concept bitmask search applies the necessary 2^(8-k) remaining-witness bound to each partial response cell, pruning only branches that cannot extend, with surviving-prefix counts [0,1,28,290,1572,3669,2903,711,0]. This proves no eight-support. Separately the supplied depth-nine JSON was evaluated by a new JS implementation against all 720 concept rows, confirming 511 internal queries and 512 unique valid leaf witnesses with no split contradiction. Cardinality 720<1024 excludes depth ten. Independently direct enumerations of n=3..6 lower supports and concept-count upper bounds agree. The computation is exhaustive over this finite universe; no n>=8 claim is made.

## originality

PASS

The closest exact cyclic-order source establishes sizes through six and an n=7 lower bound but not the exact seven-label VC upper bound or adaptive depth-nine. General online learning and cyclic hypergraph equivalences provide definitions and encodings rather than these finite numbers. The specific result survives statement-level comparison; an older unindexed enumeration is possible.

## value

PASS

A first strict divergence between fixed-query and adaptive-query complexity in a natural family of orientation concepts, with complete finite obstruction and certificate, is a motivated and reusable exact boundary for combinatorial learning; n=7 is the first unresolved natural size, not an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
