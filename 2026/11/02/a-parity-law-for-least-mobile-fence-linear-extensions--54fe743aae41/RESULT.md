# A parity law for least-mobile fence linear extensions

## Finding

**Theorem.** For each integer \(n\ge3\), let \(F_n\) denote the fence poset on labels \(1,\ldots,n\) with cover relations \(2i-1<2i\) and \(2i+1<2i\) whenever both labels lie in the ground set. Let \(G_n\) have one vertex for each linear extension of \(F_n\), with edges joining extensions obtained by exchanging two consecutive positions holding incomparable elements. Then:

1. The minimum degree of \(G_n\) is \(\lceil n/2\rceil-1\).
2. If \(n=2m\), exactly one linear extension has minimum degree; the graph induced by the minimum-degree vertices is \(K_1\).
3. If \(n=2m+1\), exactly \(2^m\) linear extensions have minimum degree; the graph they induce is \(2^{m-1}K_2\), a disjoint union of edges.
4. The diameter of \(G_n\) is \(\binom{n-1}{2}\). This last identity follows also from the standard incomparable-pair distance description of a linear-extension graph; it is included as supporting geometry, not the proposed novel part.

In particular, the least-mobile stratum of a connected linear-extension graph switches, with parity, between a singleton and exponentially many vertices paired by disjoint legal exchanges.

## Assumptions and scope

The fence \(F_n\) is a finite height-two poset: the odd labels are minimal; the even labels are maximal; an odd label is less than an even label exactly when their difference is one. All unspecified distinct label pairs are incomparable. A *linear extension* is a word listing each label once and respecting every order relation. An adjacent exchange is legal if and only if the exchanged elements are incomparable. An adjacent *bump* is a consecutive word pair whose elements are comparable; every other consecutive word pair is a *jump*. The degree of a word in \(G_n\) is its number of jumps, because every jump gives a distinct legal adjacent swap. The theorem concerns all \(n\ge3\), including both parities and their smallest instances.

## Proof

**1. Lower bound via a path matching.** If two consecutive elements of a linear extension are comparable, their labels differ by one. Moreover a given element cannot belong to two consecutive comparable pairs: any such triple would be a chain of length three, whereas \(F_n\) has height two. Therefore the comparable consecutive pairs form a matching in the label path \(1-2-\cdots-n\). At most \(\lfloor n/2\rfloor\) bumps occur. Since any extension has \(n-1\) adjacent pairs, its degree is at least \(n-1-\lfloor n/2\rfloor=\lceil n/2\rceil-1\). Explicit optimal words in the next steps show attainment.

**2. Even labels: unique optimal extension.** For \(n=2m\), the unique matching of cardinality \(m\) in the path on the labels consists of the edges \(\{1,2\},\{3,4\},\ldots,\{2m-1,2m\}\). An extension with \(m\) bumps must place each corresponding ordered pair as a consecutive block \((2i-1,2i)\). The additional fence comparabilities \(2i+1<2i\) force the block \((2i+1,2i+2)\) before \((2i-1,2i)\). Thus there is exactly one possible word:

\[
(2m-1,2m,\,2m-3,2m-2,\,\ldots,\,1,2).
\]

This word is a linear extension and has exactly \(m\) bumps, hence degree \(m-1\). Uniqueness proves the singleton induced stratum.

**3. Odd labels: exact enumeration.** Suppose \(n=2m+1\). Every matching of \(m\) edges in the label path leaves exactly one unmatched vertex, necessarily an odd label \(u=2j+1\), for a unique \(j\in\{0,\ldots,m\}\). The matching is forced on either side of \(u\): left pairs \(\{1,2\},\ldots,\{2j-1,2j\}\), and right pairs \(\{2j+2,2j+3\},\ldots,\{2m,2m+1\}\). In a linear extension with these \(m\) bumps, each pair is a consecutive block, oriented with its odd minimal element first. Left blocks occur in descending index order, as \((2j-1,2j),\ldots,(1,2)\); right blocks occur in ascending index order, as \((2j+3,2j+2),\ldots,(2m+1,2m)\). Because \(u\) must precede the even labels next to it, it must occur before both block chains and hence first. All remaining fence relations either lie within blocks or order one of these two chains, so *every shuffle of the two ordered block chains is a linear extension*. There are exactly \(\binom mj\) shuffles for fixed \(j\). Summing over the \(m+1\) possible unmatched positions gives

\[
\#\{w:\deg_{G_n}(w)=m\}=\sum_{j=0}^{m}\binom mj=2^m.
\]

**4. Adjacency of the minimizers.** Fix an odd-length minimizer. It starts with its unmatched odd label \(u\), followed by the odd member of the first block in its shuffle. These two consecutive minimal elements are incomparable and may be exchanged. After their swap, the even partner of that first block is still adjacent to \(u\); its old bump is replaced by the new bump \((u,\text{even partner})\). The unmatched label moves from \(u\) one odd step left or right, so the result again has \(m\) bumps and is another minimizer.

There is no other exchange between minimizers. Swapping within a two-element block is not legal because its members are comparable. Swapping across the boundary of two successive complete blocks breaks both internal block adjacencies. In the resulting four-element segment, at most one new comparable adjacent pair can appear, since the new consecutive pair of the two odd block leaders is incomparable, and the new pair of the even block tails is also incomparable. Thus the bump count decreases. The unique remaining boundary is that of \(u\) with the first block, already treated. Hence every odd-length minimizer has exactly one neighbor among minimizers. A finite simple one-regular graph with \(2^m\) vertices is \(2^{m-1}K_2\).

**5. Diameter (contextual complement).** Every allowed adjacent swap reverses exactly one incomparable unordered label pair. For any two extensions \(w,v\), the shortest-path distance is the number of incomparable pairs whose relative orders differ: the lower bound is immediate, while sorting the first element of \(v\) to the front of \(w\) by adjacent swaps never crosses a comparable element, and induction proves an equal upper bound. Consequently distance is at most the number of incomparable pairs, \(\binom n2-(n-1)=\binom{n-1}{2}\). To attain this bound, set

\[
A_n=(1,3,2,5,4,7,6,\ldots),
\]

truncated after label \(n\) (for even \(n\), append the final even label), and let \(B_n\) be the reverse sequence of the adjacent ordered blocks \((1,2),(3,4),\ldots\), preceded by the last odd label when \(n\) is odd. Thus \(A_7=(1,3,2,5,4,7,6)\), \(B_7=(7,5,6,3,4,1,2)\), and \(A_6=(1,3,2,5,4,6)\), \(B_6=(5,6,3,4,1,2)\). Both words respect all relations. The orders of every two odd labels and every two even labels are opposite; for an odd label \(2i-1\) and an even label \(2j\), their orders agree precisely for \(i=j\) and \(i=j+1\), the comparable cases. Therefore *every incomparable pair* has reversed order. Their distance attains the upper bound.

## Verification

The standalone `verify_primary.py` constructs all linear extensions by predecessor-bitmask recursion, computes each jump degree directly and checks the exact minimum, optimal multiplicities and induced exchanges for every \(3\le n\le11\). It also checks the explicit diametral pair and its incomparable-pair reversal count. Run `python3 verify_primary.py` in a directory containing the source file.

The independent standalone `verify_independent.cpp` performs its own depth-first enumeration of the extensions, computes degrees while inserting entries, packs the optimal words and independently reconstructs every optimal-to-optimal adjacent swap, for every \(3\le n\le13\). Compile and run with `c++ -O3 -std=c++17 verify_independent.cpp -o verify_independent && ./verify_independent`. The two programs use separate implementations and data representations. Both return their specified `PASS` marker. These finite computations corroborate the mathematical argument and are not evidence for its validity beyond their enumerated ranges.

## Relationship to prior work

The standard graph of linear extensions and adjacent-transposition move, the jump/bump number and general graph-connectivity theory long predate this result. Pruesse and Ruskey (1994) study fast Gray-code generation by adjacent transpositions. Naatz (2000) relates the graph's vertex connectivity to the jump number; this is not, by itself, a count or induced-subgraph classification of *all* jump-optimal extensions. Bondarenko (2011) explicitly characterizes regularity and degree-related structure for classes of linear-extension graphs. The accessible complete six-page article was examined; its degree-versus-jump background is credited and it does not give the above fence-specific parity enumeration or induced matching. The fence is also the classical zigzag poset, and its linear extensions correspond (under inverse permutation convention) to alternating permutations. Thus title-based searches alone would not settle the issue; the mathematical comparison is with the *least-degree adjacent-swap subgraph*.

The proposed contribution is specifically the all-size \(1\)-versus-\(2^m\) minimizer census and the exact induced \(2^{m-1}K_2\) structure; the diameter observation is supporting context and does not establish novelty. Complete source inspection of Naatz (2000) could not be obtained, so possible prior equivalent statements remain an explicit risk, as does obscure jump-optimal-extension enumeration literature. The result is not claimed independently audited.

## Limitations

The theorem is specific to the alternating fence posets and the adjacent-position transposition move; it is not a classification for all posets or for arbitrary transpositions. It does not determine the complete degree distribution of \(G_n\), the number of shortest paths, or its spectral invariants. Existence of a prior equivalently formulated enumeration cannot be logically ruled out by a search. Every claim about arbitrary \(n\) relies on the proof above; the executables check only the explicitly stated finite ranges.

## References

1. G. Pruesse and F. Ruskey, “Generating Linear Extensions Fast,” *SIAM Journal on Computing* **23** (1994), 373–386. DOI: `10.1137/S0097539791202647`.
2. M. Naatz, “The Graph of Linear Extensions Revisited,” *SIAM Journal on Discrete Mathematics* **13** (2000), 354–369. DOI: `10.1137/S0895480199352609` (abstract inspected; full text inaccessible).
3. O. S. Bondarenko, “Regular Subgraphs of Linear Extension Graphs,” *Matematychni Studii* **36** (2011), 6–11. DOI: `10.30970/ms.36.1.6-11`; full text: `https://matstud.org.ua/texts/2011/36_1/6-11.pdf`.
4. D. B. West, “Generating Linear Extensions by Adjacent Transpositions,” *Journal of Combinatorial Theory, Series B* **58** (1993), 58–64.
