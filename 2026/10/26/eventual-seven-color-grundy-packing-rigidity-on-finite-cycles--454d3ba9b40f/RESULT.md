# Eventual seven-color Grundy packing rigidity on finite cycles

## Finding
Let \(C_n\) be the simple cycle on the vertices \(0,1,\ldots,n-1\), with indices modulo \(n\). For every integer \(n\ge28\),
\[
\Gamma_\rho(C_n)=7.
\]
The equality also holds at the five additional orders \(n\in\{22,23,24,26,27\}\). In fact, \(\Gamma_\rho(C_n)\le7\) for every integer \(n\ge3\).

For each residue \(r\in\{0,1,2,3\}\) modulo four, an explicit valid seven-color word of length \(28+r\) is specified below. Inserting any nonnegative number of copies of the block \((1,2,1,3)\) at its indicated cut produces a valid greedy packing seven-coloring of the enlarged cycle. Thus the theorem gives a uniform, finite, independently checkable witness construction for every order at least \(28\).

## Assumptions and scope
Graphs are finite and simple unless explicitly identified as the doubly infinite path \(\mathbb Z\). A packing coloring assigns a positive integer to each vertex so that vertices both assigned color \(i\) have graph distance strictly larger than \(i\). The greedy packing algorithm processes vertices in an arbitrary order and assigns to each the smallest color whose distance-\(i\) packing condition remains satisfied with earlier assignments. Its maximum possible number of colors is \(\Gamma_\rho\). These are the definitions of Gözüpek and Peterin [1].

For vertices at positions \(s,t\) of the cycle, the distance is \(\min\{|s-t|,n-|s-t|\}\). A *greedy packing word* is a positive-integer cyclic word obtainable by a run of the greedy packing algorithm. All entries of the displayed witnesses are in \(\{1,\ldots,7\}\). The cycle's vertices and their displayed cyclic order are distinguished; no orbit quotient is taken.

## Proof
**1. Characterization of greedy packing words.** A cyclic word \(w\) is greedy packing if and only if both of the following hold for every vertex \(v\) of color \(i=w(v)\): (P) every other vertex of color \(i\) has distance greater than \(i\); and (G) for each smaller color \(j<i\), at least one vertex of color \(j\) lies at distance at most \(j\) from \(v\). Necessity of (P) follows from packing feasibility. Necessity of (G) follows because each smaller color must already be unavailable when \(v\) is colored. Conversely, process all vertices of color \(1\), then of color \(2\), and so on, in arbitrary order within each color class. Condition (P) makes their prescribed color available. Condition (G) makes every smaller color unavailable through an earlier vertex. Therefore the algorithm assigns precisely the displayed colors. In particular, both conditions are determined solely by the radius-seven rooted cyclic word whenever all colors are at most seven.

**2. Universal upper bound.** If \(3\le n\le7\), the bound is immediate because a first-fit run on \(n\) vertices cannot use more than \(n\) colors. Suppose \(n\ge8\). The color-one class is maximal independent, hence dominating; a single vertex cannot dominate a cycle of order at least four, so it has at least two vertices. Since every color below the largest used color must occur, the largest color \(k\) is at most \(n-1\). Now repeat the word periodically along the doubly infinite path with vertex set \(\mathbb Z\). For two distinct same-color occurrences in different periods, their distance is at least the corresponding cyclic distance, except for repetitions of the very same vertex, whose spacing is \(n>k\); consequently (P) is preserved. Every witness to (G) in the cycle admits a periodic lift along an interval of the same shortest-path length, so (G) is also preserved. The resulting periodic coloring is therefore a greedy packing coloring of \(\mathbb Z\) by the characterization in part 1. Gözüpek and Peterin [1, Theorem 6.6] establish \(\Gamma_\rho(\mathbb Z)=7\). It follows that \(\Gamma_\rho(C_n)\le7\) for all \(n\ge3\).

**3. Finite witness words.** The following rows record the order, the witness word as a sequence of single-digit colors, and the insertion cut measured as a zero-based Python list index. In each row, the block is placed *before* the entry at the cut, and the entries are read cyclically. The first five rows are independent smaller witnesses; the final four are the infinite-family seeds.

| Order | Witness word | Cut for the infinite-family seeds |
| ---: | --- | ---: |
| 22 | `7121531241251312614213` | — |
| 23 | `71231521431251321614213` | — |
| 24 | `712315213412151312614213` | — |
| 26 | `72135124132142151321631241` | — |
| 27 | `721351214312143125121631241` | — |
| 28 | `7312416123152142131412153121` | 18 |
| 29 | `73124161231521341213142151321` | 16 |
| 30 | `712315121421321431251312614213` | 13 |
| 31 | `7312416123152141312132142151321` | 17 |

(The executable witness table in `verify.py` is authoritative for the literal single-digit sequences and cut indices; the verifier checks the specified order of every row.)

**4. Exact finite checks, with a local extension lemma.** Let \(B=(1,2,1,3)\). Write \(W_r\) for the displayed witness of length \(28+r\), and \(c_r\) for its cut. Set \(W_{r,t}=W_r[0:c_r]\,B^t\,W_r[c_r:]\), interpreted as a cyclic word, for integers \(r\in\{0,1,2,3\}\) and \(t\ge0\). The standalone `verify.py` tests conditions (P) and (G) directly for all nine original words and all \(W_{r,t}\) with \(t=0,1,2,3,4,5,10,25\). It additionally simulates the original first-fit algorithm on each word with vertices ordered by nondecreasing prescribed color. These finite tests, implemented as exact integer comparisons, pass.

Here is why checking \(t=4\), together with the pure periodic block, establishes **all** \(t\ge4\). Properties (P) and (G) can be checked independently at each root using a rooted radius-seven neighborhood. The original seed segment has length at least \(28>14\); for \(t\ge4\), the inserted segment has length \(4t\ge16>14\). Hence no rooted radius-seven neighborhood can meet both junctions through either segment. Rooted neighborhoods meeting one junction are independent of \(t\) once \(t\ge4\), and are identical to the corresponding neighborhoods when \(t=4\). Neighborhoods meeting neither junction lie wholly in the unchanged original segment or wholly in the bi-infinite repetition \(\ldots B B B\ldots\). The former occur in the \(t=4\) check. For the latter, check directly the four possible rooted phases of the period-four word: color \(1\) repeats at distance two; color \(2\) repeats at distance four and has adjacent color \(1\); color \(3\) repeats at distance four and sees color \(1\) at distance one and color \(2\) at distance two. Hence the pure periodic neighborhood satisfies (P) and (G). All radius-seven neighborhoods that meet a junction or stay entirely in the original seed occur already in \(W_{r,4}\). Those rooted in the interior of the inserted block and meeting neither junction satisfy (P) and (G) by the periodic-word check. Thus every \(W_{r,t}\) satisfies both conditions for all \(t\ge4\). The cases \(t=0,1,2,3\) are covered by the explicit finite checks.

For each \(n\ge28\), there is a unique choice of \(r\in\{0,1,2,3\}\) and \(t\ge0\) with \(n=28+r+4t\). The corresponding \(W_{r,t}\) is therefore a greedy packing seven-coloring of \(C_n\). Combining this lower bound with part 2 proves the asserted equality. The five extra orders follow directly from the separate finite witnesses.

## Verification
Run `python3 verify.py` in the directory containing the embedded standalone verifier. It requires only Python's standard library. The verifier checks each literal word's order, both radius/distance conditions for every vertex, and a separate first-fit replay in nondecreasing-color order. For the four extension families it additionally verifies eight exact insertion counts, including \(t=4\) as the finite premise of the local-extension proof. `verification_output.txt` records the observed deterministic result. The checkable finite premises are not presented as evidence of an infinite theorem absent the local-extension argument given above.

## Relationship to prior work
Gözüpek and Peterin [1] introduced this greedy packing invariant and proved \(\Gamma_\rho(\mathbb Z)=7\) and the exact values for finite paths, including \(\Gamma_\rho(P_n)=7\) when \(n\ge25\) (Theorem 6.6). Their proof and witness for paths do not, by themselves, produce cyclic seven-color witnesses with the wraparound constraints. The present conclusion is the eventual **cycle** equality and its four-residue constructive gluing argument; neither the invariant nor its infinite-path upper bound is claimed as new. Other uses of the phrase “Grundy coloring” concern ordinary proper coloring or different packing constraints and do not automatically establish the first-fit *packing* cycle theorem.

## Limitations
The theorem does not decide the exact Grundy packing chromatic number for all orders below \(28\): outside the five additionally displayed orders, no lower bound of seven is asserted. The four-residue construction may not give every possible greedy packing seven-coloring. Mathematical priority in unindexed literature and independent validation remain open; the recorded review is not an independent audit.

## References
[1] D. Gözüpek and I. Peterin, *Grundy Packing Coloring of Graphs*, arXiv:2409.00697 (first available 2024-09-01; revised 2025-03-19), particularly the greedy packing coloring definition in Sections 2–3 and Theorem 6.6. https://arxiv.org/abs/2409.00697
