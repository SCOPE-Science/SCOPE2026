# Exact unrestricted variable-width theories of finite threshold graphs

## Finding
Let \(G,H\) be nonempty finite simple **threshold graphs**, meaning graphs built from one vertex by repeatedly adjoining either an isolated vertex or a vertex adjacent to every existing vertex. Work in the pure undirected adjacency-and-equality language, without counting quantifiers.

For distinct vertices define *vicinal comparison* by \(x\preceq y\) when every vertex outside \(\{x,y\}\) adjacent to \(x\) is also adjacent to \(y\). In every threshold graph this is a total preorder. Its equivalence classes \(B_0<\cdots<B_{t-1}\) are the twin classes, ordered from smaller to larger vicinal neighborhood. Each class of size at least two is either a clique or an independent set; edges between distinct classes are all present or all absent. The **ordered twin skeleton** consists of this ordered list, its internal clique/independent bits (omitted for singleton classes), and all between-class adjacency bits.

**Theorem.** For every integer \(k\ge3\),
\[
G\equiv_{\mathrm{FO}^{k}}H
\quad\Longleftrightarrow\quad
\begin{gathered}
\text{the ordered twin skeletons agree, and}\\
\min(|B_i(G)|,k)=\min(|B_i(H)|,k)
\quad\text{for every corresponding class }i.
\end{gathered}
\]
Here \(\equiv_{\mathrm{FO}^{k}}\) means agreement on **all** first-order sentences using at most \(k\) reusable variables, with no bound on quantifier depth. A singleton class carries no internal adjacency bit.

Each \(\mathrm{FO}^{k}\) equivalence class in the family has a **unique smallest representative up to isomorphism**, obtained by keeping exactly \(\min(|B_i|,k)\) vertices in each twin class. Its order is
\[
\sum_{i=0}^{t-1}\min(|B_i|,k).
\]
The cutoff is sharp for every \(k\ge3\): the stars \(K_{1,k}\) and \(K_{1,k+1}\) are \(\mathrm{FO}^{k}\)-equivalent but not \(\mathrm{FO}^{k+1}\)-equivalent. For graphs with the same ordered skeleton and different class sizes whose smaller differing size is at least three, the least distinguishing width is exactly one more than the smallest such differing size.

## Assumptions and scope
All graphs are finite, nonempty, simple, undirected, and loopless, and have a threshold-graph construction as stated above. Graph logic uses only equality and adjacency; no creation sequence, vertex labels, order relation, degree predicate, counting quantifier, or numerical parameter is in the language. The statement applies to connected and disconnected threshold graphs. The theorem does **not** assert the displayed classification for arbitrary cographs or all graphs with repeated twins.

The ordered skeleton is an invariant of the graph, not a chosen construction string. In particular, two nonsingleton twin classes with different internal bits are distinct; when a class has only one vertex its hypothetical loop/interior bit is *not* meaningful and is omitted.

## Proof
**1. Vicinal preorder and twins.** Define
\[
x\preceq y\ \Longleftrightarrow\
\forall z\bigl((z=x)\lor(z=y)\lor(\neg E(x,z))\lor E(y,z)\bigr).
\]
This is a formula with just the variable names \(x,y,z\). If a new isolated vertex is added to a threshold graph, it is below every old vertex in this comparison. If a new universal vertex is added, it is above every old vertex. The comparison of two old vertices is unchanged, since both have the same adjacency to the new vertex. Starting from the one-vertex graph, induction proves the relation is a total preorder. Its symmetric part is exactly
\[
x\sim y\iff \forall z\notin\{x,y\},\ E(x,z)\leftrightarrow E(y,z),
\]
namely twinhood. This is an equivalence relation. The equivalence classes are uniform internally (all edges or no edges) and all cross-edges between two classes have one value. A strict vicinal comparison between distinct classes gives distinct degrees, so class order is canonical.

**2. Every skeleton coordinate is definable with three variables.** Define a unary formula \(C_0(x)\) asserting \(\forall y\,x\preceq y\). Inductively, after defining \(C_0,\ldots,C_{i-1}\), set
\[
C_i(x):=\bigwedge_{j<i}\neg C_j(x)\ \land\
\forall y\Bigl(\bigwedge_{j<i}\neg C_j(y)\ \to\ x\preceq y\Bigr).
\]
In a finite total preorder, this defines precisely its \(i\)-th equivalence class when that class exists. Each formula uses only three **distinct variable names**: every occurrence of the binary comparison uses its third variable locally; a recursively inserted unary formula may alpha-rename and shadow names inside its own quantifier scopes, without capturing any free variable. Thus membership in each class is definable in \(\mathrm{FO}^{3}\). The existence of \(C_i\), and hence the number of classes, is distinguishable at three variables.

For any \(k\ge3\), the sentence requiring \(j\) pairwise different vertices satisfying \(C_i\), for \(1\le j\le k\), uses at most \(k\) variable names. Within each conjunct the local quantifiers used in \(C_i\) may shadow other variables and do not affect the already evaluated distinctness conjuncts. Hence \(\mathrm{FO}^{k}\) determines precisely \(\min(|B_i|,k)\). Sentences with two outer existential variables and the corresponding unary class formulas as conjuncts (using at most three variable names in total) determine the internal edge/nonedge bit whenever a class has at least two vertices, and all cross-class adjacency bits. Consequently, \(\mathrm{FO}^{k}\)-equivalence implies agreement of the complete truncated ordered skeleton.

**3. Permanent back-and-forth.** Conversely, suppose the truncated ordered skeletons coincide. Match every occupied pebble's class index across the two graphs, and preserve equality between pebbles. All adjacency and equality atoms are then preserved by the skeleton. In any round, remove the moving pebble. If its new source vertex equals an occupied vertex, use the corresponding already occupied target vertex. Otherwise, let \(i\) be its class. There are at most \(k-1\) occupied distinct target vertices. If the source class has fewer than \(k\) vertices, the corresponding target class has exactly the same size and the number occupied there is identical. If it has at least \(k\) vertices, the target class has at least \(k\), so an unused target vertex exists. This works symmetrically from either graph, at every round. The resulting indefinite \(k\)-pebble strategy proves equivalence at **unrestricted** quantifier depth.

**4. Sharpness and minimum representative.** Keeping the first \(\min(|B_i|,k)\) vertices of each class produces an induced threshold graph: threshold graphs are closed under induced subgraphs. Each class remains nonempty and no two originally different classes merge. Indeed, for a strict vicinal comparison choose vertices \(x\) and \(y\) in two classes and an outside vertex \(z\) adjacent to exactly one of them. If \(z\) belongs to a third class, that class retains a representative with the same adjacency pattern. If \(z\) belongs to either compared class, that class originally has at least two vertices, so the truncation retains at least two distinct representatives, allowing a witness \(z\) different from the selected \(x,y\). Thus every strict comparison has a witness after truncation, and the preorder order is preserved. Its skeleton and truncated sizes are unchanged, so step 3 proves equivalence. Step 2 forces any equivalent threshold graph to have exactly the same skeleton and at least the displayed number of vertices in each class, proving minimal order and uniqueness. Stars with \(k\) versus \(k+1\) leaves have the same skeleton, but the independent leaf class sizes agree when truncated at \(k\) and disagree at \(k+1\). The asserted sharp variable-width separation follows. In the equal-skeleton case, the least integer \(k\ge3\) witnessing any size difference is the least width exceeding a smaller unequal class size. The matching strategy of step 3 also works at widths one and two (its sufficiency direction does not need definability of the classes), so when all smaller unequal sizes are at least three these lower widths do not distinguish either. This proves the stated minimum-width assertion.

## Verification
The standalone Python 3 programs in `check_vicinal.py` and `check_pebbles.py` use only the standard library. Run with `python3 check_vicinal.py` and `python3 check_pebbles.py`. The former exhausts all \(511\) canonical threshold creation words of order at most nine, checks preorder totality/transitivity and compression at widths three and four, and checks four sharp star boundaries. The latter independently computes stable, noncounting tuple-refinement classes and compares them with ordered-degree-class signatures over all \(127\) creation words of order at most seven at width three, and all \(31\) words of order at most five at width four. Its \(8{,}001\) and \(465\) pair comparisons, respectively, all agree with the theorem. Exact deterministic console outputs are provided in the two accompanying text files. These finite tests corroborate, but do not replace, the all-size and unbounded-depth proof.

## Relationship to prior work
Threshold graphs and creation-string representations go back to Chvátal and Hammer, and cograph representations are developed by Corneil, Perl, and Stewart. Lampis, *Model Checking Lower Bounds for Simple Graphs* (arXiv:1302.4266, Section 3, especially Theorem 3.2), proves a nonelementary lower bound for full first-order model checking on connected threshold graphs using a reduction from binary words. That result concerns **unrestricted numbers of variables** and does not state the present exact fixed-width equivalence relation. Grohe and Otto, *Pebble Games and Linear Equations*, supply general finite-variable pebble-game foundations but no threshold-specific ordered-skeleton classification. Results concerning complete multipartite graph logical width address a strictly different class (only restricted star/complete intersections with threshold graphs), and do not imply the all-threshold-graph result. The proof here uses the elementary graph-definability and pebble-game methods directly, without inferring historical novelty from searches alone.

## Limitations
The theorem does not cover widths one and two; the sharpness assertion is only for widths at least three. The classification is for counting-free logic; counting quantifiers can distinguish different twin multiplicities. No bound on quantifier **rank** is imposed. The defining formulas \(C_i\) are fixed separately for each finite class index, so the theorem does not assert one bounded-depth formula uniformly names an unbounded number of twin classes. General cographs need not have a total vicinal preorder. Historical priority remains qualified: a more general theorem about definable total twin quotients could imply this classification even if no exact matching statement was found. No independent mathematical audit has been performed.

## References
1. V. Chvátal and P. L. Hammer, *Aggregation of inequalities in integer programming*, Stanford technical report STAN-CS-75-518 (August 1975); Annals of Discrete Mathematics 1 (1977), 145–162. Exact first-public calendar day not established.
2. D. G. Corneil, Y. Perl, and L. K. Stewart, *A Linear Recognition Algorithm for Cographs*, SIAM J. Comput. 14 (1985), 926–934, DOI:10.1137/0214065. Publisher identifies online availability on 2006-07-13; earlier printed release day was not independently established.
3. M. Lampis, *Model Checking Lower Bounds for Simple Graphs*, arXiv:1302.4266 (first posted 2013-02-18); Logical Methods in Computer Science 10(1:18) (2014), DOI:10.2168/LMCS-10(1:18)2014.
4. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990 (first posted 2012-04-09), CSL 2012, DOI:10.4230/LIPIcs.CSL.2012.289 (proceedings publication 2012-09-03).
