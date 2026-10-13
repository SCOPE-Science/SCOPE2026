# Scientific assessment

**Correctness (PASS).** The proof identifies mutually reachable hub routes except at the four patterns; after an exceptional deletion, a constructive hub route makes the remaining \(2^k-3\) states strongly connected, leaving two singleton SCCs. The constant-hub diameter equality is proved by a safe overlap shortcut plus a lower-bound ordered pair. All table entries are finite exhaustive shortest-path computations with source artifacts; the independent string-based checker confirms both SCC and distance claims for \(2\le k\le7\). The full histogram range is only \(2\le k\le10\).

**Originality (PASS, qualified).** Baseline directed de Bruijn connectivity and diameter are established in earlier literature [1]. Muñoz–Gómez [2] establish almost-disjoint paths; Loguinov et al. [3] discuss weak self-loop nodes; Mao–Yang [4] work on *undirected* fault routing; Padró–Morillo–Muñoz [5] study a replacement-route digraph. These statements do not give the specific four exceptional words, the exact 1/1/large SCC decomposition, or the finite *directed induced-survivor* diameter histograms. Possible unindexed equivalent computations and the uninspected complete text of Du–Hwang [6] remain residual risks; a negative index search is not a proof of global originality.

**Value (PASS).** The finding resolves which one-node failures partition the network and measures latency degradation at every other node through dimension ten. The exact nonmonotone five-to-six-bit worst-case overhead provides a useful boundary benchmark; determining both vulnerability locations and multiplicities matters beyond mere connectivity one.

Self-review: passed. Independent audit: not yet performed.

References [1]–[6] are identified in RESULT.md.
