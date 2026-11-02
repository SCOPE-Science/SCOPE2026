# Parity-gap spectra and exact enumeration of perfect forests in complete bipartite graphs

## Finding

For positive integers \(a,b\), let \(K_{a,b}\) be the complete bipartite graph with two distinctly labelled shores of sizes \(a\) and \(b\). A **0-perfect forest** is a spanning forest in which every vertex has odd degree and every connected component induces a tree in the ambient graph. In particular, distinct components need not be mutually anticomplete.

Let \(C_{a,b}(t)=\sum_F t^{c(F)}\), summing over all 0-perfect forests, where \(c(F)\) is the number of tree components. Then the exact labelled bivariate exponential generating function is

\[
\boxed{\sum_{a,b\ge0}\frac{x^a y^b}{a!b!}C_{a,b}(t)
 =\exp\!\bigl(t[x\sinh y+y\sinh x-xy]\bigr).}
\]

The empty graph contributes the constant term \(1\). Hence for every \(a,b\ge1\), the polynomial \(P_{a,b}(z)=\sum_F z^{|E(F)|}\) is obtained exactly by

\[
\boxed{P_{a,b}(z)=z^{a+b}a!b! [x^a y^b]\exp\!\bigl(z^{-1}[x\sinh y+y\sinh x-xy]\bigr).}
\]

The apparent negative powers cancel after coefficient extraction; the formula defines an ordinary polynomial.

If \(a+b\) is odd, no such forest exists. If \(1\le a\le b\) and \(a+b\) is even, set

\[
\kappa(a)=\begin{cases}
1,&a=1,\\
2,&a\ge2\text{ even},\\
3,&a\ge3\text{ odd}.
\end{cases}
\]

Then the numbers of components and edges that actually occur are respectively

\[
\boxed{c(F)\in\{\kappa(a),\kappa(a)+2,\ldots,a\}},\qquad
\boxed{|E(F)|\in\{b,b+2,\ldots,a+b-\kappa(a)\}.}
\]

Every displayed integer occurs, and no others do. In particular the minimum and maximum edge counts are \(b\) and \(a+b-\kappa(a)\); all intermediate edge counts of the opposite parity are absent. The number of minimum-edge forests is

\[
\boxed{b![y^b](\sinh y)^a
 =\frac{1}{2^a}\sum_{j=0}^{a}(-1)^{a-j}\binom aj(2j-a)^b.}
\]

For even \(4\le a\le b\), exactly \(ab\) forests attain the maximum edge count (two induced odd stars with opposite shores as their centers). For \(a=1\) the unique star attains both bounds; for \(a=2\) and even \(b\), the unique attainable edge count is \(b\), with \(2^{b-1}\) forests.

For instance, \(P_{4,4}(z)=24z^4+16z^6\), whereas \(P_{5,5}(z)=120z^5+400z^7\). There are no forests at the intervening edge counts.

## Assumptions and scope

Graphs are finite, simple, undirected and labelled within each bipartition shore. Two forests are different if their selected edge sets differ. A component being *induced* means it contains every ambient edge between vertices of that component; edges between different components are allowed in the ambient graph. A forest with all vertices of odd degree has no isolated vertices. The results use the standard definition of a 0-perfect forest; they do **not** count edge decompositions of the complete bipartite graph into stars.

The bivariate generating function also covers zero-sized shores with the usual empty-graph convention; the spectra and extremal statements require positive shores.

## Proof

**Component classification.** Consider a connected induced subtree \(T\) of \(K_{a,b}\) containing at least one edge. If \(T\) contained two vertices from each shore, those four vertices would induce a 4-cycle, contradicting that \(T\) is a tree. Consequently exactly one shore contributes one vertex, and \(T\) is a star. Every leaf has degree one. Its center has odd degree exactly when its number \(k\) of leaves is odd. Thus the allowed component types are precisely \(K_{1,k}\) with positive odd \(k\). Conversely every vertex partition into such induced stars determines a unique 0-perfect forest: include exactly the edges within each star block. This proves a bijection, without any assumption about the ambient edges between blocks.

**Enumeration.** An odd star centered in the first shore has the two-sort exponential generating function \(x\sinh y\), while a star centered in the second shore has \(y\sinh x\). A one-edge star is counted in both orientations, so subtract its generating term \(xy\) once. Stars with three or more leaves have a unique center and therefore no remaining duplication. The resulting connected-component series is \(x\sinh y+y\sinh x-xy\). Applying the exponential formula for a labelled unordered set of components, with weight \(t\) per component, proves the bivariate identity. Since every forest has \(a+b-c(F)\) edges, substitution \(t=z^{-1}\) gives the edge polynomial.

**Necessary support conditions.** Every allowed star has an odd positive number of vertices in *each* shore: \((1,k)\) or \((k,1)\), with \(k\) odd. Hence for a forest of \(c\) components, \(a\equiv b\equiv c\pmod2\), \(c\le\min(a,b)\), and the total order \(a+b\) is even. If \(a=1\), necessarily \(c=1\). If \(a\ge2\), \(c=1\) is impossible because the sole induced star would have to occupy only one vertex from one shore. Therefore \(c\ge2\) when \(a\) is even, and \(c\ge3\) when \(a\ge3\) is odd. These are precisely the stated necessary bounds.

**Every admissible value occurs.** Assume \(2\le a\le b\), and take any integer \(c\) between \(\kappa(a)\) and \(a\) satisfying \(c\equiv a\pmod2\). Choose one vertex of the second shore as the center of a star. Give it \(a-c+1\) first-shore leaves, a positive odd number. The remaining \(c-1\) first-shore vertices are each centers of their own star. Distribute the remaining \(b-1\) second-shore vertices among these centers in positive odd-sized blocks. This is possible because \(b-1\ge c-1\) and \(b-1\equiv c-1\pmod2\): give one leaf to each center and add the remaining even number of leaves in pairs. This yields a 0-perfect forest with exactly \(c\) components. For \(a=1\), the single induced star with all \(b\) second-shore vertices exists because \(b\) is odd. Necessity and sufficiency are proved. A forest with \(c\) components has exactly \(a+b-c\) edges, proving the claimed parity-gapped edge spectrum.

**Extremal multiplicities.** If \(c=a\), every component has precisely one first-shore vertex. Thus each labelled first-shore vertex receives an odd, nonempty group of second-shore neighbors, with all second-shore vertices used once. By the labelled product rule the number is \(b![y^b](\sinh y)^a\); expansion of \((e^y-e^{-y})^a/2^a\) gives the displayed finite alternating sum. For even \(a\ge4\), a two-component forest must contain one star centered in each shore: two stars centered in the same shore would use only two vertices of that shore, contradicting \(a\ge4\) and \(b\ge4\). The two centers can be chosen in \(ab\) ways and then each noncenter vertex is forced into the star centered in the opposite shore. For \(a=2\), both vertices of the first shore each head an odd star; the number of odd subsets of the even-sized opposite shore is \(2^{b-1}\). The \(a=1\) case is immediate. All assertions follow.

## Verification

The standalone `verify.py` independently enumerates edge subsets of \(K_{a,b}\), tests acyclicity by disjoint sets, checks odd degree at every vertex, and checks that every ambient edge whose endpoints belong to the same selected component is present. This does not assume the star classification. It compares the resulting component-count distribution to the coefficient recurrence independently obtained by distinguishing a first-shore vertex. In one run, all \(190{,}798\) edge subsets across 19 graph instances were tested, and the exact predicted support was additionally checked for 180 parameter pairs. Output: `VERIFY_OK direct_graphs=19 edge_subsets=190798 support_pairs=180`.

These are finite corroborating checks only. Infinite validity rests on the component bijection and explicit construction above. Run with `python3 verify.py` using only the Python standard library.

## Relationship to prior work

Gutin and Yeo's *Perfect Forests in Graphs and Their Extensions* (first posted May 1, 2021) studies the minimum- and maximum-edge problems, proving in particular that finding a maximum-size 0-perfect forest is NP-hard in general. Its inspected theorem statements and relevant sections do not supply the exact two-sort enumerator or the complete parity-gapped spectrum for complete bipartite graphs. The general existence theorem due to Scott (2001) is much weaker than the present labelled enumeration. Classical induced-star partition results concern existence of partitions into bounded stars and do not by themselves enumerate odd-star partitions with the induced-forest condition and sharp edge support. Work on *edge decompositions* of complete bipartite graphs into odd stars partitions the entire edge set, which is a different object.

## Limitations

This is a special-family exact result, not a polynomial-time algorithm for arbitrary graphs, and it does not classify 1-perfect forests. The displayed counts are for labelled vertex sets, not graph-isomorphism classes. Publication priority is provisional: similar formulas could exist under different terminology, especially labelled odd-star factors. No independent mathematical audit has been conducted.

## References

- G. Gutin and A. Yeo, *Perfect Forests in Graphs and Their Extensions*, arXiv:2105.00254v1 (first public posting May 1, 2021), subsequently MFCS 2021, DOI:10.4230/LIPIcs.MFCS.2021.54.
- A. D. Scott, *On induced subgraphs with all degrees odd*, Graphs and Combinatorics 17 (2001), 539–553.
- Y. Egawa, M. Kano, and A. K. Kelmans, *Star partitions of graphs*, Journal of Graph Theory 25 (1997), 185–190, DOI:10.1002/(SICI)1097-0118(199707)25:3<185::AID-JGT2>3.0.CO;2-H.
- Purwanto and F. A. Winanthi, *Odd star decomposition of complete bipartite graphs* (2020), DOI:10.1063/5.0000521 (edge-decomposition problem, different from spanning induced forests).
