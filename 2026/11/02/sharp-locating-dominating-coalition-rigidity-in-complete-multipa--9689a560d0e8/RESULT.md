# Sharp locating–dominating coalition rigidity in complete multipartite graphs

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete multipartite graph with \(r\ge2\) labelled parts and \(n_i\ge2\) vertices in every part. An *LD-set* is a dominating vertex set whose open-neighborhood signatures distinguish every two vertices outside it. A *locating–dominating coalition partition* (LDC-partition) is a partition into nonempty classes, no class individually an LD-set, in which every class belongs to a pair whose union is an LD-set. Write \(C_L(G)\) for the largest possible number of classes.

**Theorem.** For every such graph,
\[
C_L(G)=\begin{cases}
4,&n_1=\cdots=n_r=2,\\
3,&\text{otherwise}.
\end{cases}
\]
Moreover, for the cocktail-party graph \(H_r=K_{2,\ldots,2}\) on \(2r\) labelled vertices, the number \(A_r\) of **unlabelled four-class partitions of the labelled vertex set** satisfying the LDC condition is
\[
\boxed{A_r=2^{r-3}\left(4^r-5\cdot2^r+6\right)}\qquad(r\ge2).
\]
The four-class partitions admit a structural classification: in every part its two vertices lie in distinct partition classes; form a simple graph on the four classes, connecting two classes when a multipartite part has one vertex in each. This graph is exactly one of \(2K_2\), \(P_4\), or \(C_4\), with every edge type used at least once. Conversely, every such assignment determines an LDC-partition. Repeated uses of an edge type are allowed and counted.

The first values of \(A_r\), for \(r=2,3,4,5,6\), are respectively \(1,30,364,3480,30256\).

## Assumptions and scope
The parts are nonempty twin classes of size at least two; singleton parts are excluded. The graph and all its vertices are labelled, but **partition classes are not named**. A coalition pair must consist of two distinct classes that are *individually not* locating–dominating. Open neighborhoods, rather than closed-neighborhood identifying codes, are used for the location condition. The number \(A_r\) counts only maximum-cardinality LDC-partitions of \(H_r\).

## Proof
**1. An exact criterion for LD-sets.** Let \(P_1,\ldots,P_r\) be the partite sets and \(D\subseteq V(G)\). We claim that
\[
D\text{ is an LD-set}\quad\Longleftrightarrow\quad |P_i\setminus D|\le1\text{ for every }i.
\tag{1}
\]
Indeed, two vertices outside \(D\) in the same part have identical open neighborhoods and are not located. Conversely, if at most one vertex per part is outside \(D\), then \(|D\cap P_i|\ge n_i-1\ge1\) for every \(i\). An outside vertex in \(P_i\) has the nonempty signature \(D\setminus P_i\), and signatures for outside vertices from different parts are distinct because both of their respective selected part intersections are nonempty. Thus domination and location hold.

**2. The auxiliary multigraph.** Fix a vertex partition \(\mathcal P=\{B_1,\ldots,B_k\}\) with all classes nonempty. Construct a multigraph \(J(\mathcal P)\) on \(\{1,\ldots,k\}\): for every pair of distinct vertices \(u,v\) in the same graph part, insert an edge between the indices of the two blocks containing \(u\) and \(v\). The edge is a loop if those indices coincide; parallel edges do not change vertex covers. A subset of block indices meets every edge of \(J\) if and only if its union of partition blocks leaves at most one vertex outside in each part. Therefore (1) yields
\[
B_i\text{ is LD}\iff\{i\}\text{ covers }J,\qquad
B_i\cup B_j\text{ is LD}\iff\{i,j\}\text{ covers }J.
\tag{2}
\]
Consequently \(\mathcal P\) is an LDC-partition exactly when \(J\) has no one-vertex cover and every one of its \(k\) vertices occurs in at least one two-vertex cover.

**3. A four-class universal bound.** In any loop-allowing multigraph with no one-vertex cover and with every vertex contained in a two-vertex cover, there are at most four vertices. If the graph has two vertex-disjoint edges, any two-vertex cover must use an endpoint of each; hence every vertex that can belong to such a cover lies among their at most four endpoints. Otherwise its edges are pairwise intersecting. Since they have no common vertex (that would be a one-vertex cover), their underlying support is precisely a triangle: choose intersecting edges \(ab\) and \(ac\), then an edge missing \(a\) must be \(bc\), and any edge meeting all three must lie on these same three vertices. Thus at most three vertices occur in two-vertex covers. Applying (2) gives \(C_L(G)\le4\).

For a four-block LDC-partition, \(J\) cannot contain a loop: a loop at \(v\) forces every two-vertex cover to contain \(v\), whereas an edge avoiding \(v\) (which exists because \(v\) is not itself a cover) restricts the other cover element to at most its two endpoints. Then at most three vertices can participate. Nor can \(J\) contain a triangle: both members of any two-vertex cover must come from that triangle, again leaving at most three possible participants. If some original part had three vertices, then among their partition-block indices either two coincide, creating a loop, or all three are distinct, creating a triangle. Therefore a four-class partition requires \(n_i=2\) for every part.

**4. Sharp constructions.** When some \(n_i\ge3\), choose distinct \(x,y\in P_i\) and use the three classes \(\{x\},\{y\},V(G)\setminus\{x,y\}\). Neither singleton is an LD-set, since the other multipartite parts of size at least two are untouched. The large class is not an LD-set, since it omits two vertices in one part. The large class combined with either singleton omits just one vertex, so it is an LD-set by (1). The three classes thus form an LDC-partition.

When every part has size two, write \(P_i=\{x_i,y_i\}\). Use four classes
\[
B_1=\{x_1\}\cup\{x_i:3\le i\le r\},\quad
B_2=\{y_2\}\cup\{y_i:3\le i\le r\},\quad
B_3=\{y_1\},\quad B_4=\{x_2\}.
\]
For \(r=2\) the auxiliary graph is \(2K_2\); for \(r\ge3\) it is the path \(B_3-B_1-B_2-B_4\). In both cases there is no one-vertex cover, and every vertex belongs to a two-vertex cover. Equation (2) proves that these are four-block LDC-partitions. This establishes the exact dichotomy.

**5. Classification and count at equality.** If a four-class partition exists, all original parts have size two, and their two vertices belong to distinct classes (otherwise the auxiliary graph has a loop). The underlying auxiliary graph is therefore simple, on four vertices. It has neither an isolated vertex (such a vertex in a two-cover would make its partner a one-cover), a loop, nor a triangle. It has no one-vertex cover. The only possibilities are \(2K_2\) (disconnected), \(P_4\), and \(C_4\) (connected). Directly, each of these three graphs has no one-vertex cover and every vertex belongs to a two-vertex cover, so the converse follows from (2).

There are respectively \(3\), \(12\), and \(3\) labelled simple graphs of these forms on the four block labels. If the chosen form has \(q\) edges, assign the \(r\) labelled multipartite parts surjectively to its \(q\) edge types in \(q!\,\left\{\begin{smallmatrix}r\\q\end{smallmatrix}\right\}\) ways, where the braces denote a Stirling number of the second kind. Each part's two labelled vertices can be oriented onto the chosen endpoints in exactly two ways. Dividing by \(4!\), since permuting the four temporary block labels changes no partition, yields
\[
A_r=\frac{2^r}{24}\left[3\cdot2!\left\{\begin{smallmatrix}r\\2\end{smallmatrix}\right\}
+12\cdot3!\left\{\begin{smallmatrix}r\\3\end{smallmatrix}\right\}
+3\cdot4!\left\{\begin{smallmatrix}r\\4\end{smallmatrix}\right\}\right].
\]
Using the elementary Stirling-number inclusion–exclusion formulas gives exactly \(2^{r-3}(4^r-5\cdot2^r+6)\). The argument holds also for \(r=2\), since the terms with more than \(r\) edge types vanish. This completes the proof.

## Verification
Run `python3 verify.py` from the same directory as this document. It requires only the Python standard library. The program constructs the original labelled graph adjacency and checks domination and distinct open-neighborhood signatures directly, independently of the twin-class lemma. It examines **every unlabelled vertex partition** for ten multipartite size profiles, including \((2,2,2,2,2)\), and confirms both the maximum number of coalition blocks and all four-block counts. A separate exhaustive search checks the abstract loop-allowing two-cover obstruction on every nonempty five-vertex edge/loop pattern. A separate edge-type assignment calculation verifies \(A_r\) for \(2\le r\le6\) without enumerating vertex partitions. The finite checks corroborate but do not replace the proof for arbitrary \(r\) and part sizes.

## Relationship to prior work
Chellali, Dobrynin, Foucaud, Golmohammadi and Valenzuela-Tripodoro introduced locating–dominating coalition partitions and proved the general bound \(C_L(G)\le |V(G)|-\gamma_L(G)+2\), as well as exact results for paths, cycles, and the smallest extremal graphs [1]. For complete multipartite graphs with all \(n_i\ge2\), equation (1) implies the familiar \(\gamma_L(G)=\sum_i n_i-r\); consequently that general bound gives only \(C_L(G)\le r+2\), not the constant sharp bound and its equality rigidity above. Their Proposition 4.1 already includes \(K_{2,2}\cong C_4\) as a four-class boundary case; that small case is not presented as new. The present contribution is the all-part-size dichotomy, the structural classification of four-class equality, and the infinite-family enumeration. Other known locating–dominating-set and unrelated coalition variants do not by themselves specify these coalition partitions.

## Limitations
The theorem does not include complete multipartite graphs with singleton parts, arbitrary graphs with twins, or coalition notions based on dominating sets alone. It counts only the four-class maxima in the all-size-two case; it does not count the three-class maxima in the mixed-size case. Historical priority against unindexed work under different names remains a risk. The proof and computations have not undergone an independent mathematical audit.

## References
[1] M. Chellali, A. A. Dobrynin, F. Foucaud, H. Golmohammadi, and J. C. Valenzuela-Tripodoro, *Locating-dominating coalitions in graphs*, arXiv:2602.18760v2 (2026); first publicly posted 2026-02-21. Full text: https://arxiv.org/html/2602.18760v2.
