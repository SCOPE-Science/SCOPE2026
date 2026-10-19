# Zero-forcing classification of the degree-five Clebsch graph

## Finding

Let \(G\) denote the degree-five Clebsch graph, not its degree-ten complement, and let \(\mathcal Z_G(z)=\sum_{k=0}^{16}z(G;k)z^k\) count its zero-forcing sets by cardinality. Its **complete zero-forcing polynomial** is

\[
\mathcal Z_G(z)=3872z^{10}+3632z^{11}+1760z^{12}+560z^{13}+120z^{14}+16z^{15}+z^{16}.
\]

In particular, \(G\) has exactly 9,961 zero-forcing sets, its zero-forcing number equals its real maximum nullity, \(Z(G)=M(G)=10\), and its exactly 3,872 inclusion-minimal zero-forcing sets all have cardinality ten: the graph is *well-forced*. All 3,872 minimum zero-forcing sets complete the synchronous color-change process in exactly two rounds, so both extremal propagation times are two. Under \(\operatorname{Aut}(G)\), of order 1,920, the minimum sets form exactly seven orbits of respective sizes 960, 960, 480, 480, 480, 320, and 192. Their complements are represented by the white-set bit masks 303, 363, 287, 399, 873, 407, and 857. A complete 18-orbit census of six-element white sets appears in `six_white_orbit_certificate.csv`.

## Assumptions and scope

The vertex set is \(V=\mathbb F_2^4\), represented by integers 0 through 15 with binary-vector addition as bitwise XOR. Two distinct vertices \(x,y\) are adjacent if \(x\oplus y\in S=\{1,2,4,8,15\}\). All statements refer to this simple, undirected, five-regular graph. Initially a subset \(B\subseteq V\) is black. In each synchronous round, *every* white vertex adjacent to some black vertex having exactly one white neighbor becomes black. The set \(B\) is zero forcing if all vertices eventually become black. An inclusion-minimal zero-forcing set has no proper zero-forcing subset; a minimum set has least possible cardinality. The polynomial counts distinct labeled vertex subsets, not just symmetry classes. \(M(G)\) is the maximum nullity among real symmetric matrices having nonzero off-diagonal entries precisely on the graph edges; diagonals are unrestricted.

## Proof

**Spectral lower bound and a witness.** The characters \(\chi_a(x)=(-1)^{a\cdot x}\), for \(a,x\in\mathbb F_2^4\), diagonalize the adjacency matrix \(A\). If the Hamming weight of \(a\) is \(w\), the corresponding eigenvalue is \(4-2w+(-1)^w\). Thus \(A\) has eigenvalues 5 once, 1 ten times, and \(-3\) five times. The admissible real symmetric matrix \(A-I\) therefore has nullity ten. For any zero-forcing set \(B\), if \(v\in\ker(A-I)\) vanishes on \(B\), the row equation at a black vertex with one white neighbor forces \(v\) to vanish there too, because its edge coefficient is one. Induction through any full forcing process gives \(v=0\); hence restriction to coordinates in \(B\) is injective on this kernel, so \(|B|\ge10\). Conversely, choose initially white vertices \(W=\{0,1,2,3,5,8\}\), whose mask is 303; the ten other vertices are black. In the first synchronous round, black vertices 15, 14, 6, and 11 respectively force 0, 1, 2, and 3. In the second round, black vertices 1 and 0 force 5 and 8. Therefore \(Z(G)=10\); combining the general restriction argument for arbitrary admissible matrices with this example proves \(M(G)=10\).

**Why the automorphism group is full.** The five generator vectors sum to zero, and every four are independent. Thus each of the \(5!\) permutations of these generators extends uniquely to an invertible linear map of \(\mathbb F_2^4\) preserving the graph; composing with sixteen translations gives 1,920 distinct automorphisms. Conversely, an automorphism is determined by its image of vertex 0 and by a permutation of the five neighbors of 0: every other vertex is uniquely the XOR of a pair of distinct generators, and is the unique common neighbor of that pair other than 0. Hence there are no additional graph automorphisms.

**Exhaustive finite count.** The file `verify_white.cpp` independently enumerates all \(2^{16}=65,536\) initial black masks, applies the synchronous color-change rule with bit masks, and counts successful masks by size and by rounds. A different file, `verify_group.py`, independently enumerates the same 65,536 masks using Python sets, checks that all inclusion-minimal successful masks have size ten, generates and verifies all 1,920 automorphisms, and partitions all \(\binom{16}{6}=8,008\) complementary six-white masks into eighteen disjoint symmetry orbits. The latter program checks all eighteen rows of the embedded orbit certificate, including exactly seven successful orbits and the seven sizes listed in the finding. Each finite loop has explicitly bounded ranges that exhaust its stated domain; the complete programs are part of this result rather than merely supplying execution logs. The asserted polynomial, well-forcedness, propagation-time statement, and seven-orbit classification follow from these exact finite enumerations.

The exact propagation-time refinement for larger initial black sets is: size eleven, 272 one-round and 3,360 two-round sets; size twelve, 1,280 one-round and 480 two-round sets; sizes thirteen, fourteen, and fifteen, respectively 560, 120, and 16 one-round sets; the all-black set takes zero rounds. In particular, all 3,872 size-ten forcing sets take exactly two rounds.

## Verification

Run from a directory containing all three supplied artifacts: `python3 verify_group.py`; then `g++ -O2 -std=c++17 -Wall -Wextra -o verify_white verify_white.cpp && ./verify_white`. The two checks reconstruct the graph independently from the stated five XOR generators. The C++ checker visits all 65,536 black masks and tests every one-vertex deletion from each forcing set. The Python checker recomputes the same polynomial with a separate set-based transition rule, checks every candidate inclusion-minimal set, verifies all 1,920 claimed maps preserve adjacency, proves they exhaust the automorphism group using the structural argument above, and compares a fresh 18-orbit classification with `six_white_orbit_certificate.csv`. The numerical assertions are exact integer comparisons without randomness, tolerances, or unproved search cutoffs.

## Relationship to prior work

Zero forcing and its basic inequality \(M(G)\le Z(G)\) originate in the AIM Minimum Rank–Special Graphs Work Group (2008). Hogben, Huynh, Kingsley, Meyer, Walker, and Young (2014), especially Definitions 1.1, 1.3, and 1.7, formalize minimum and maximum simultaneous propagation times. Boyer and collaborators (2018) introduce and study the zero-forcing polynomial for several graph families. Grood and collaborators (2023) develop well-forced graphs, focusing on structural results and trees. Nazari and Karimi Radpoor (2012, Theorem 3.3 and Table 1) discuss zero forcing of nontrivial powers of the Clebsch graph, whose second power is complete and has forcing number fifteen; that is not the degree-five original graph studied here. The degree-five Clebsch graph is the known Cayley graph and strongly regular graph on sixteen vertices with automorphism group of order 1,920; those classical graph facts are not claimed as new. The new classification here concerns the exact zero-forcing polynomial, all inclusion-minimal sets, and the orbits and propagation times of minimum sets of this particular graph. None of the directly inspected general papers states these complete graph-specific enumerations; priority relative to inaccessible or unindexed work remains uncertain.

## Limitations

The exhaustive claims hold only for the stated sixteen-vertex, five-regular graph, not its ten-regular complement or an infinite family. The argument establishes no general classification of well-forced strongly regular graphs. The minimum-nullity equality follows from an explicit matrix and the established elementary forcing inequality, not a characterization of all admissible matrices. Scientific priority has not been independently certified; a relevant foundational publisher article could not be fully retrieved for content comparison. The computational verification is finite, explicit and complete for this graph, and is not a machine-checked formal proof of its surrounding exposition.

## References

1. AIM Minimum Rank–Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications **428** (2008), 1628–1648. DOI: https://doi.org/10.1016/j.laa.2007.10.009 .
2. L. Hogben, M. Huynh, N. Kingsley, S. Meyer, S. Walker, M. Young, *Propagation time for zero forcing on a graph*, arXiv:1410.4191v1 (2014-10-15), https://arxiv.org/html/1410.4191v1 .
3. K. Boyer et al., *The zero forcing polynomial of a graph*, arXiv:1801.08910v1 (2018-01-26), https://arxiv.org/html/1801.08910v1 .
4. C. Grood et al., *Well-forced graphs*, arXiv:2312.14298v1 (2023-12-21), https://arxiv.org/html/2312.14298v1 .
5. A. Nazari and M. Karimi Radpoor, *Minimum Rank of Graphs Powers Family*, Open Journal of Discrete Mathematics **2** (2012), 65–69, https://doi.org/10.4236/ojdm.2012.22012 .
6. *Clebsch graph*, background graph construction and spectrum, https://en.wikipedia.org/wiki/Clebsch_graph .
