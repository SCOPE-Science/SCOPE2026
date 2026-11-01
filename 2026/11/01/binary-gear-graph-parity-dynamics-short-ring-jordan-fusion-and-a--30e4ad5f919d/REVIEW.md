# Scientific review

## Correctness — PASS

The open-neighborhood update has the exact polynomial representation in `RESULT.md`, equation (1). Characteristic-two Chinese remaindering separates one hub-coupled primary factor from an invertible cyclic factor. On the exceptional factor, the exact square and cube of the local update give rank sequences determining the claimed nilpotent Jordan partitions: one block of length one for odd \(n\), \((3,1,1)\) when \(n\equiv2\pmod4\), and \((e,e,1)\) when \(4\mid n\). On the complementary factor, a two-by-two determinant calculation gives the displayed polynomial-gcd fixed-point dimensions. Fitting decomposition and Möbius inversion complete the entry-time and primitive-orbit counts. The proof verifies all parameters, not just a sample. Standalone `gear_verify.py` passed 2,326 rank checks and 1,984 return-count kernel checks for \(3\le n\le64\), plus direct enumeration of 174,720 states for \(3\le n\le8\).

## Originality — PASS, qualified

Marr–Hütt (arXiv:cond-mat/0502509v1, inspected full text in HTML and representative PDF page) considered binary network automata with degree-density threshold flip rules, rather than the present additive neighbor-XOR map. Berman–Borer–Hungerbühler (DOI 10.1007/s00591-021-00297-5, inspected open full HTML, including Theorem 4 and Propositions 7–9) concerns user-selected Lights Out switch sequences, not autonomous \(F_n^t\). Martin–Odlyzko–Wolfram (DOI 10.1007/BF01223745) developed polynomial state-transition algebra for homogeneous finite cellular automata, but the complete article was not available for full inspection; its abstract and beginning were checked, and this historical uncertainty remains explicit. Gear-graph sources identify the graph class and unrelated invariants. Searches of graph aliases, nilpotent blocks, return-time counts, polynomial gcds and published research records yielded no stronger or equivalent all-gear theorem. A negative search is not proof of uniqueness.

## Value — PASS

The family is an established wheel-subdivision/Jahangir graph class, and its binary recurrent behavior is not settled by graph size, bipartiteness or the generic finite-matrix method. The exact classification exhibits a nontrivial short-ring fusion at \(n\equiv2\pmod4\), periodic-state fractions that jump between odd and even sizes, complete nilpotency on power-of-two gears, and an all-time arithmetic recurrence census. These are coherent structural invariants of the whole infinite family rather than a list of small examples.

## Closest literature and limitations

The most relevant inspected sources are Marr–Hütt's full 2005 arXiv paper on topology-dependent automata and Berman–Borer–Hungerbühler's 2021 open article on graph Lights Out; their different dynamics are compared explicitly above. The foundational 1984 paper of Martin–Odlyzko–Wolfram was not accessible in complete form. Sutner’s 1990 article connecting the σ-game with cellular automata was inspected only through its publisher abstract, which concerns directed graph games and rectangular grids. A differently presented historical derivation in either source cannot be ruled out. The result is confined to the binary synchronous open-neighborhood rule on simple gear graphs. Computational tests do not certify the infinite formula independently.

Self-review: passed. Independent audit: not yet performed.
