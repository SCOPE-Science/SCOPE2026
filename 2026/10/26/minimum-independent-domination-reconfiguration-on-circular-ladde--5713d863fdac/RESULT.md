# Minimum independent-domination reconfiguration on circular ladders

## Finding
For every integer \(n\geq 3\), put \(P_n=C_n\square K_2\), \(k=2\lceil n/4\rceil\), and \(h=n-k\). Let \(\mathscr I(P_n)\) have as vertices all *minimum-cardinality independent dominating sets* of \(P_n\), with two sets adjacent when a single selected vertex is replaced by one other vertex and the result remains a minimum independent dominating set. All vertices of \(P_n\) are distinctly labeled by their column in \(\mathbb Z/n\mathbb Z\) and their top/bottom layer.

Then \(i(P_n)=k\), and the exact vertex and edge counts of the reconfiguration graph are
\[
|V(\mathscr I(P_n))|=\frac{2n}{k}\binom{k}{h},\qquad
|E(\mathscr I(P_n))|=2n\binom{k-2}{h-1}.
\]
For \(h=k\), the latter binomial coefficient is interpreted as zero. The graph is bipartite. If \(4\mid n\), it consists of exactly four isolated vertices; otherwise it is connected. If \(n\equiv3\pmod4\), it is the cycle \(C_{2n}\).

More precisely, if \(0<h<k\), the number of its vertices of degree \(2r\) is
\[
\boxed{\ \frac{2n}{r}\binom{h-1}{r-1}\binom{k-h-1}{r-1}\ }
\quad (1\le r\le\min(h,k-h)),
\]
and there are no other degrees. If \(h=k\), all four vertices have degree zero. Thus, across this infinite prism family, every nonisolated minimum-independent-domination exchange graph has maximum degree at most six.

## Assumptions and scope
The cycle \(C_n\) is the simple \(n\)-cycle with \(n\ge3\), and the Cartesian product has rung edges \((j,0)(j,1)\) and cycle edges \((j,a)(j+1,a)\). A set is independent if no pair of its vertices is adjacent; it dominates if every vertex not selected has a selected neighbor. Its minimum possible cardinality is \(i(P_n)\). All subsets are counted with their actual labeled positions, not modulo automorphism.

The reconfiguration edge permits a one-for-one exchange preserving *both* independence and domination at the minimum cardinality; intermediate sets are always required to remain minimum. In any graph, a one-for-one exchange between independent dominating sets must move along an original edge: the newly inserted vertex is dominated by the starting set, while independence of the destination excludes adjacency to every surviving vertex. This general token-jump/token-slide equality is not claimed as new.

## Proof
**1. Cyclic-word characterization.** Represent a selected vertex in column \(j\) by \(A\) (top) or \(B\) (bottom), and an unoccupied column by \(0\). The rung forbids selecting both layer vertices in the same column. Two consecutive occupied columns must bear opposite letters to preserve independence. Every zero column must have two occupied neighbors bearing opposite letters; otherwise its two unselected vertices cannot both be dominated. Consequently zeros are isolated, and after removing zeros, all occupied letters alternate \(A,B,A,B,\ldots\) around the circle. Conversely, every cyclic word with isolated zeros and alternating occupied letters is an independent dominating set. Therefore its number \(k'\) of occupied columns is even, and its number \(h'=n-k'\) of zero columns satisfies \(1\le h'\le k'\) when at least one zero exists. In a fully occupied cycle, alternating colors are possible only for even \(n\); these have larger cardinality than the minima below. The smallest possible even \(k'\ge n/2\) is \(k=2\lceil n/4\rceil\). Since \(h=n-k\) satisfies \(1\le h\le k\), a cyclic word with \(h\) separated zeros and alternating occupied letters exists, proving \(i(P_n)=k\).

**2. Exact vertices.** Mark an occupied top-layer vertex as the root and enumerate the \(k\) occupied vertices cyclically starting there. Let \(b_j\in\{0,1\}\) record whether a zero occurs after the \(j\)-th occupied vertex. Exactly \(h\) of the \(k\) gap bits are ones, and the root's position is any of the \(n\) columns. Every pair (root column, gap vector of weight \(h\)) reconstructs a valid configuration uniquely; conversely, every configuration is represented once for each of its \(k/2\) top-layer occupied vertices. Hence the exact number of configurations is \(n\binom{k}{h}/(k/2)=2n\binom{k}{h}/k\).

**3. Allowed exchanges and degrees.** A replacement must be an original edge (as noted in the scope). It cannot move along a rung, since changing the layer of exactly one occupied column contradicts the forced alternating pattern with its closest other occupied columns. Thus a replacement moves an occupied vertex into an adjacent zero column. It is legal exactly when the resulting zeros remain isolated. In gap coordinates it interchanges a neighboring pair \(01\leftrightarrow10\) of bits on the cyclic list of length \(k\). Hence the degree is the number of unequal neighboring gap-bit pairs, or twice the number \(r\) of cyclic runs of ones. For \(0<h<k\), the number of cyclic binary gap vectors of length \(k\), weight \(h\), and exactly \(r\) runs of ones is
\[
\frac{k}{r}\binom{h-1}{r-1}\binom{k-h-1}{r-1}.
\]
This follows by choosing positive lengths for the \(r\) runs of ones and \(r\) intervening runs of zeros, then marking a run's starting position and dividing by the \(r\) choices of marked run. Multiplying by \(n/(k/2)\) gives the asserted exact degree distribution. Summing the degrees over all rooted words, each of the \(k\) cyclic locations contributes \(2\binom{k-2}{h-1}\) adjacent unequal-bit arrangements; accounting for \(n\) root columns and \(k/2\) root choices per physical configuration, then halving, gives \(2n\binom{k-2}{h-1}\) exchange edges. If \(h=k\), all gaps equal one, so all degrees are zero.

**4. Connectivity.** When \(h=k\), the count in step 2 is four and no gap swap is possible: the graph is four isolated vertices. Otherwise \(0<h<k\). Consider *labeled occupied tokens* whose layers alternate in their fixed cyclic order, distinguishing one top token as token zero. The state is its column \(p\in\mathbb Z/n\mathbb Z\) together with a binary gap vector \(b\) of length \(k\), weight \(h\). Moves of tokens other than token zero swap adjacent gap bits across positions \(0,1,\ldots,k-1\) regarded as a path, and hence connect all such gap vectors while keeping \(p\) fixed. Because \(0<h<k\), first arrange the bits so that the last bit is zero and the first bit is one. Moving token zero forward changes its column from \(p\) to \(p+1\) and swaps those two gap bits. Then moves of other tokens restore the original gap vector without moving token zero. Thus \((p,b)\) connects to \((p+1,b)\) for every starting state. These unit shifts, together with arbitrary fixed-root gap rearrangements, connect all labeled states. Forgetting token names maps onto all original minimum independent dominating sets, so \(\mathscr I(P_n)\) is connected.

**5. Bipartiteness and exceptional structures.** For an occupied-top root, let \(\varepsilon(b)=\sum_{j=0}^{k-1}j b_j\pmod2\). Changing the top root reindexes the occupied tokens by an even shift, and \(k\) is even, so this parity is independent of that choice. Every legal gap swap interchanges positions with odd index difference (including the cyclic boundary), so it reverses \(\varepsilon\). This is a bipartition. When \(h=k-1\), every cyclic gap vector has exactly one zero; every configuration has degree two. The graph is connected by step 4, with \(2n\) vertices by step 2, and is therefore \(C_{2n}\). The equality \(h=k-1\) is equivalent to \(n\equiv3\pmod4\). Finally \(k-h\le3\) for all \(n\ge3\), so the run bound in step 3 makes every nonisolated degree at most six.

## Verification
Two standalone Python 3 programs in this package reconstruct the claims independently.

`verify_bitmask.py` constructs the two-layer graph directly as bit-mask neighborhoods, enumerates every vertex subset for \(3\le n\le10\), tests independence and domination directly, and constructs full one-token-jump and slide graphs. It compares minimum cardinality, exact vertex and edge counts, connected components, and the agreement of jump and slide adjacencies with the formulas above.

`verify_cyclic_words.py` independently enumerates all ternary cyclic words for \(3\le n\le13\), using local feasibility tests without the bit-mask implementation. It constructs the slide graph from words and checks exact counts, connected components, degree multiplicities, and a complete graph bipartiteness test. It also separately checks connectivity of the labeled-gap state graph for every even \(2\le k\le8\) and \(1\le h<k\). The recorded full program outputs accompany the code. Both programs were executed directly. These finite computations check the proof's consequences; the proof of the all-\(n\) theorem is the preceding symbolic argument.

## Relationship to prior work
The classical independence-domination literature concerns the minimum size of a maximal independent set and counts of dominating independent sets. Nagy's 2015 treatment includes maximal independent sets among \(k\)-dominating independent sets and examines extremal numbers, but not this prism-family reconfiguration classification. Brewster, Mynhardt and Teshima (2023) define \(i\)-graphs, establish basic structural constraints and realizability constructions, and explicitly note that token jumping and token sliding agree for independent domination in every graph; that general fact is already known and is credited here. Their inspected text does not classify the \(i\)-graphs of circular ladders.

Allagan's 2026 full text counts *minimum dominating sets* of prisms rather than minimum *independent dominating sets*, and does not determine the corresponding exchange graphs. Some regimes overlap: its minimum-domination counts already agree with the cardinalities here when \(n\equiv0,3\pmod4\) and the two domination minima coincide. The new classification specifically includes the different invariant, exact degree distribution, bipartiteness, exchange edges, and complete connectivity behavior; it is not an immediate reformulation of that counting theorem. Accessible prior-record comparisons found related circular-ladder independence-complex homology and different prism invariants, not this claim.

## Limitations
The result applies only to the Cartesian-product prisms \(C_n\square K_2\), with labeled vertices, and only to minimum-cardinality independent dominating sets. It does not classify the entire domination reconfiguration graph, the spectrum of all maximal independent sets, or reconfiguration distances. The priority assessment is based on accessible sources and searches, not exhaustive indexing of every thesis, book, or unpublished computation. Independent scientific audit has not been performed.

## References
- Z. L. Nagy, *On the number of k-dominating independent sets*, arXiv:1504.03224v1, first posted 2015-04-13; updated text arXiv:1504.03224v2, https://arxiv.org/html/1504.03224v2.
- R. C. Brewster, C. M. Mynhardt, L. E. Teshima, *Reconfiguration of Minimum Independent Dominating Sets in Graphs*, arXiv:2303.06299, first posted 2023-03-11, https://arxiv.org/abs/2303.06299.
- J. Allagan, *Exact Dominion of the Prism Graph: Enumeration by Congruence Class via Cyclic Words*, arXiv:2601.03488v1, first posted 2026-01-07, https://arxiv.org/abs/2601.03488; accessible full text at https://www.researchgate.net/publication/399559830_Exact_Dominion_of_the_Prism_Graph_Enumeration_by_Congruence_Class_via_Cyclic_Words.
