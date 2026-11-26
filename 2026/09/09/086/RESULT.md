# Complete census of tight-5-cycle-free 3-graphs on six vertices

## Finding

On a fixed six-vertex set, exactly **371229** of the \(2^{20}\) simple 3-uniform hypergraphs are \(C_5^3\)-free. These make up **835** isomorphism types. The maximum edge count is 13, attained by a unique type whose labeled orbit has size 60. The seven types with 12 edges have orbit sizes 90, 45, 15, 180, 360, 360 and 15 in canonical-code order.

| Edges | Labeled | Types |
|---:|---:|---:|
|0|1|1|
|1|20|1|
|2|190|3|
|3|1140|7|
|4|4845|21|
|5|15432|42|
|6|37680|91|
|7|70140|146|
|8|95820|195|
|9|88220|176|
|10|46336|111|
|11|10280|33|
|12|1065|7|
|13|60|1|

All larger edge counts have zero entries. With triples indexed lexicographically on \(\{0,1,\ldots,5\}\) and the first triple assigned the low bit, the unique extremal type has canonical mask 131056. Its triples are `023 024 025 034 035 045 123 124 125 134 135 145 234`, with degree vector \((6,6,7,7,7,6)\). The full canonical catalogue is in `artifacts/census_types.json`.

## Definitions and proof

A copy of \(C_5^3\) consists of the five consecutive cyclic triples of a sequence of five distinct vertices; containment does not require the copy to be induced. Enumerate all \(6\cdot5\cdot4\cdot3\cdot2=720\) ordered choices. They produce 72 distinct 20-bit masks. For each distinct mask \(c\), mark \(c\lor y\) for every submask \(y\) of its bitwise complement within the 20-bit universe. This marks precisely all containing 3-graphs: every marked graph contains the indicated five-edge copy, and every copy is in the list. Popcount on the unmarked masks gives the labeled column.

Next traverse the unmarked masks in increasing order. At the first as-yet unseen mask, generate its images under all 720 vertex permutations, remove duplicates and mark the full orbit as seen. Freeness is invariant under relabeling, and orbits partition the unmarked masks; the first encountered mask is thus exactly its orbit's minimum. Tally each orbit by popcount, retaining its cardinality and minimum for the catalogue. Both enumerations cover the entire finite universe. The accompanying code tests all displayed counts and the extremal representative and can compare every catalogue entry.

## Verification

Run `python3 check_census.py` with the Python 3 standard library. To check every stored row as well, supply `artifacts/census_types.json` as the single argument, relative to the record package. The optional comparison checks edge counts, minimum mask and orbit size for each row and exact agreement of the canonical-code set.

## Context and limits

Containment is already meaningful on five vertices, the order of the cycle itself. Six is the first larger host order: here copies can use different five-subsets of the same host. The complete admissible six-vertex types are the local input to any order-six induced-type or flag-algebra calculation excluding just \(C_5^3\); a maximum edge count alone would not determine that input. The census does not prove a transfer lemma or an asymptotic Turán-density claim.

Kamčev–Letzter–Pokrovskiy, [arXiv:2209.08134](https://arxiv.org/abs/2209.08134), place the single tight 5-cycle in the Turán program. Bodnar–Leon–Liu–Pikhurko, [arXiv:2506.03223](https://arxiv.org/abs/2506.03223), address the forbidden pair \(\{C_4^3,C_5^3\}\) and particular longer single cycles. These asymptotic results and their SDP computations are not the unrestricted six-vertex catalogue considered here.
