# The complete 2-factor spectrum of the McGee graph and its eight symmetry classes

## Finding
Let \(G\) be the McGee graph, the cubic girth-seven cage on 24 vertices. For any spanning 2-regular subgraph \(F\), let \(\lambda(F)\) be the ascending multiset of its cycle lengths. Its **complete 2-factor spectrum**, counting unlabelled edge subsets in a fixed graph, is

\[
\sum_{F\subseteq G\text{ a 2-factor}}t_{\lambda(F)}
=42t_{(24)}+6t_{(12,12)}+12t_{(8,8,8)}.
\]

In particular, there are exactly 60 distinct 2-factors (equivalently, 60 perfect matchings), exactly 42 undirected Hamiltonian cycles, and every cycle of every spanning 2-factor has length divisible by four. Under the full automorphism group of order 32, the 60 perfect matchings constitute exactly eight orbits: for type \((8,8,8)\) their sizes are \(4,8\); for type \((12,12)\) they are \(2,4\); and for type \((24)\) they are \(2,8,16,16\). As a corollary, the graph admits exactly 204 proper edge colorings by a fixed set of three named colors, or 34 after identifying color permutations.

## Assumptions and scope
Use vertex set \(V=\{0,1,\ldots,23\}\), with indices modulo 24. The edges are the 24 rim pairs \(\{i,i+1\}\), together with the 12 chords \(\{i,i+s_i\}\), where \(s_i\) is periodic with period 3 and takes the values \((-12,7,-7)\). Repeated unordered chords are included once. This is the standard LCF model \([-12,7,-7]^8\), yielding 36 edges, degree three, girth seven and diameter four. A perfect matching contains twelve pairwise disjoint edges incident with each vertex exactly once. A 2-factor contains degree two at every vertex; cycles are unoriented.

## Proof
**Bijection.** Since every vertex has degree three, for a perfect matching \(M\), its edge complement \(E(G)\setminus M\) has degree two at each vertex and is a 2-factor; conversely, the complement of any 2-factor is a perfect matching. The maps are mutual inverses. Thus a finite exhaustive perfect-matching census proves an exhaustive 2-factor census.

**Exhaustive recursion.** For any subset of available vertices \(S\), let \(p(S)\) count perfect matchings of the induced graph. Then \(p(\varnothing)=1\), and for nonempty \(S\), if \(v\) is its least vertex,

\[
p(S)=\sum_{w\in N(v)\cap S}p(S\setminus\{v,w\}).
\]

Each solution belongs to exactly one branch, because \(v\) has exactly one partner. The attached `verify.py` implements both this memoized counting recurrence and a separate explicit recursion recording every matching. They independently give \(p(V)=60\). For each of the 60 complete edge sets, it deletes those twelve edges and traces every degree-two connected component until it closes. The results are exactly 42 occurrences of \((24)\), 6 of \((12,12)\), and 12 of \((8,8,8)\). The independent `verify_independent.cpp` reconstructs the graph and traverses matchings using the *fewest-available-partners* branching rule and an independent cycle tracer, obtaining the identical three counts. This exhausts all cases by the bijection, not by a sample of finite subsets.

**Symmetry.** A vertex permutation is an automorphism exactly when it preserves all pairwise shortest-path distances. The attached Python code backtracks over every injection compatible with the already assigned distances; every admissible image is considered, and only impossible partial maps are pruned. It finds exactly 32 permutations, all checked against the edges. Applying these permutations to all 60 matchings, it identifies eight disjoint orbits of sizes \(4,8\), \(2,4\), and \(2,8,16,16\) according to cycle type. Complete representative matchings are recorded in `orbits.csv`, and the full census in `matchings.csv`; the verifier checks the tables against its independent enumerations.

**Edge-coloring corollary.** If a proper three-edge coloring is fixed, the edges of the first color form a perfect matching \(M\). The complementary even cycles alternate the other two colors. Conversely, for any matching \(M\), each complementary cycle can be colored alternately in exactly two ways. A 2-factor with \(c\) cycles therefore yields \(2^c\) colorings with the first named color on \(M\). Summing over all 60 matchings gives \(42\cdot2+6\cdot4+12\cdot8=204\). The symmetric group on three named colors acts freely on these proper colorings because all three colors occur, so there are \(204/6=34\) unordered color-class partitions. This derives only a corollary of the same complete 2-factor statement.

## Verification
From the directory containing the four attached reproducibility artifacts, execute `python3 verify.py`. For an independent implementation use `g++ -std=c++17 -O2 verify_independent.cpp -o verify_independent` and then execute `./verify_independent`. Both runs were completed on the supplied source files and printed the asserted 60 matchings and \((42,6,12)\) type distribution. The Python verifier additionally checked girth seven, diameter four, all 32 automorphisms, eight symmetry orbits, and every row in the CSV files. The C++ checker does not read the CSV and chooses a different matching branching order. All enumeration code is finite and terminates at the empty available-vertex set.

## Relationship to prior work
McGee's original four-page paper constructs this 24-vertex cubic cage and exhibits a Hamiltonian circuit but does not enumerate its 2-factors or perfect matchings. The MathWorld McGee entry lists the LCF notation, Hamiltonicity and group order 32 but not the matching cycle-spectrum. Björklund--Husfeldt--Kaski--Koivisto give a vertex-exponential Tutte-polynomial algorithm and tabulate the McGee graph's Tutte coefficients in their appendix; these coefficients are not an enumeration of complementary perfect-matching cycle types. Candráková--Lukoťka establish bounds on cycle covers and chosen 2-factors in general cubic graphs, not the exact McGee 2-factor distribution. The same numerical subinvariants could nevertheless have appeared in an unindexed census; see Limitations.

## Limitations
The result concerns this fixed 24-vertex graph and its 2-factors; it does not assert an infinite-family theorem or any independent review. Exhaustiveness follows from transparent finite recursions and independent code, but executions were not separately checked by an external mathematical auditor. A potentially relevant 2017 thesis, *Structures of Derived Graphs*, was not fully accessible; an earlier unindexed enumeration remains a priority risk. The 1960 source establishes the graph's original publication month, not a verified individual day; the date recorded in metadata is the earliest exact-day public arXiv source among the selected literature, not a claim that the graph was unpublished before 2007.

## References
1. W. F. McGee, “A Minimal Cubic Graph of Girth Seven,” *Canadian Mathematical Bulletin* 3 (1960), 149–152, DOI: 10.4153/CMB-1960-018-1. Full four-page public PDF: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B6AF32607F85BC1B3D1159BE3F0A601E/S0008439500050463a.pdf/a-minimal-cubic-graph-of-girth-seven.pdf .
2. E. W. Weisstein, “McGee Graph,” MathWorld, https://mathworld.wolfram.com/McGeeGraph.html .
3. A. Björklund, T. Husfeldt, P. Kaski, M. Koivisto, “Computing the Tutte polynomial in vertex-exponential time,” arXiv:0711.2585, first posted 2007-11-16, https://arxiv.org/abs/0711.2585 .
4. B. Candráková, R. Lukoťka, “Short cycle covers on cubic graphs using chosen 2-factor,” arXiv:1509.07430, first posted 2015-09-24, https://arxiv.org/abs/1509.07430 .
