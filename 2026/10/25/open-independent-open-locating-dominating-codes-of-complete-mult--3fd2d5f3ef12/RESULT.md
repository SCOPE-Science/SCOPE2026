# Open-independent open-locating-dominating codes of complete-multipartite line graphs

## Finding
For integers \(r\ge2\) and \(n_1,\ldots,n_r\ge1\), put \(G=K_{n_1,\ldots,n_r}\), \(N=\sum_{i=1}^r n_i\), and \(H=L(G)\). A set \(S\subseteq V(H)\) is an **open-independent open-locating-dominating code** (an \(\mathrm{OLD}_{\mathrm{oind}}\)-set) if all signatures \(N_H(v)\cap S\), \(v\in V(H)\), are nonempty and pairwise different, and every selected vertex has exactly one selected neighbor. Define \(C(n_1,\ldots,n_r)\) as the number of such codes on the given labeled graph.

**Classification and exact enumeration.** Every code consists of the edges of pairwise vertex-disjoint two-edge paths in \(G\), possibly leaving exactly one vertex of \(G\) unused. More precisely:

1. If \(N=3k\), with \(k\ge1\), codes exist precisely when \(\max_i n_i\le2k\). They correspond bijectively to partitions of \(V(G)\) into \(k\) triples, with a distinguished center in each triple adjacent to its other two vertices. Every code has \(2k\) vertices in \(H\), and
   \[
   C(n_1,\ldots,n_r)=\left(\prod_{i=1}^r n_i!\right)
     [x_1^{n_1}\cdots x_r^{n_r}]\exp Q(x_1,\ldots,x_r),
   \]
   where
   \[
   Q(x_1,\ldots,x_r)=\frac12\sum_{i\ne j}x_i^2x_j
        +3\sum_{1\le i<j<\ell\le r}x_i x_jx_\ell.
   \]
2. If \(N=3k+1\), with \(k\ge1\), codes exist precisely when a part has size \(2k+1\). This part is necessarily unique, and every code leaves one vertex of it unused, matches its remaining \(2k\) vertices in pairs, and joins each pair to a distinct vertex outside that part. Every code has \(2k\) vertices in \(H\), and
   \[
   C(n_1,\ldots,n_r)=\frac{(2k+1)!}{2^k}.
   \]
3. In all other cases, including \(N\equiv2\pmod3\), no such code exists: \(C(n_1,\ldots,n_r)=0\).

These expressions provide the complete code-cardinality polynomial: if the code count is nonzero, the polynomial is \(C(n_1,\ldots,n_r)z^{2\lfloor N/3\rfloor}\), and otherwise it is zero. In particular, all codes for any fixed \(G\) have the same cardinality.

**Consequences.** The triangular graph \(L(K_{3k})\) has exactly \((3k)!/(2^k k!)\) such codes, each of size \(2k\); \(L(K_n)\) has none when \(3\nmid n\). For \(G=K_{2,2,2}\), the exact number is \(42\). A complete \(r\)-partite graph with equal positive part sizes \(q\) has an admissible line-graph code if and only if \(3\mid rq\).

## Assumptions and scope
Graphs are finite, simple, with all part sizes positive and at least two nonempty parts. The vertices are labeled, while individual code vertices are not given a separate labeling. A vertex of \(H=L(G)\) is an edge of \(G\), and two line-graph vertices are adjacent if their edges have a common endpoint. Codes are *sets*, not ordered lists. The notation \([x_1^{n_1}\cdots x_r^{n_r}]\) means coefficient extraction in the formal multivariate power series over the rational numbers. The displayed exponential is formal and its coefficient of total degree \(N\) requires finitely many terms.

## Proof
**Step 1: disjoint path components.** A code \(S\) induces a matching in the line graph \(H\): every selected line-graph vertex has exactly one neighbor in \(S\). Thus the chosen edges of \(G\) form pairs of adjacent edges, with no endpoint shared between different pairs. Each pair is a two-edge path on three vertices, with a unique center. Write \(k\) for the number of paths and \(U\) for the vertices of \(G\) not covered by any path; thus \(|U|=N-3k\).

For a vertex \(v\in V(G)\), define \(T(v)\) to be the chosen edges incident with \(v\). An unused vertex has \(T(v)=\varnothing\), a path endpoint has a singleton \(T(v)\), and a path center has a two-element \(T(v)\). For an unchosen edge \(uv\), its line-graph signature is exactly \(T(u)\cup T(v)\). For a chosen edge, its signature is the singleton consisting of its partner in the same path.

**Step 2: at most one unused vertex.** If \(U\) has two vertices in different parts, the edge joining them has empty signature, impossible. Suppose instead that two unused vertices \(u,u'\) belong to the same part \(P\). If a selected-path endpoint \(v\) lies outside \(P\), the unchosen edge \(uv\) has a singleton signature matching the signature of the partner of the chosen edge incident with \(v\). Hence all endpoints must belong to \(P\). Every path center must therefore lie outside \(P\), and any center \(w\) gives two distinct unchosen edges \(uw,u'w\) with identical signatures \(T(w)\), also impossible. Hence \(|U|\le1\).

If \(U=\{u\}\) and \(u\in P\), the same singleton-collision argument forces every path endpoint into \(P\); its center must then lie outside \(P\). Thus \(|P|=2k+1\) and the complement of \(P\) has exactly \(k\) vertices. If \(U=\varnothing\), \(N=3k\), and no path can have all three vertices in a single part.

**Step 3: sufficiency and uniqueness of signatures.** Conversely, take any partition of all vertices into two-edge paths, each using at least two parts, and choose their two edges. The signature of each chosen edge is its partner, a distinct singleton. The sole possible unchosen edge with both endpoints in one path is the edge between the two endpoints; when this edge exists, its signature is exactly the pair of chosen edges from that path. Every edge between two different paths has a signature containing nonempty contributions from precisely those two paths. Within each path, the maps from its three vertices to the incident chosen-edge subsets are injective (the two endpoints give two different singletons; the center gives their pair). Thus all signatures are nonempty and distinct.

Now suppose there is one unused vertex \(u\) in a part \(P\), with every path having both endpoints in \(P\) and its center outside \(P\). The preceding signatures remain distinct. The only additional graph edges are those joining \(u\) to path centers. Each has the two selected edges of its center's path as its signature. No edge between the endpoints of that path exists because those endpoints lie in \(P\), and signatures involving two paths have labels from two different paths. Therefore these extra signatures are also nonempty, distinct, and new. This proves the exact structural characterization.

**Step 4: existence at multiples of three.** A path uses at most two vertices of each part, so \(\max_i n_i\le2k\) is necessary for a path factor when \(N=3k\). Conversely, a multiset of \(3k\) colored vertices in which no color occurs more than \(2k\) times can be split into \(k\) nonmonochromatic triples. Here is an induction: the case \(k=1\) is immediate. When \(k\ge2\), if a color occurs \(2k\) times, take two vertices of that color and one of another; if a color occurs \(2k-1\) times, take one vertex of that color and two of other colors (for the sole boundary case \(k=2\), choose both from a color that occurs three times if necessary); otherwise choose any nonmonochromatic triple. In each case, the remaining \(3(k-1)\) vertices have maximum color multiplicity at most \(2(k-1)\), permitting induction. Every nonmonochromatic triple in a complete multipartite graph has a center adjacent to the two other vertices: for types \((2,1)\), choose the singly occurring part, and for types \((1,1,1)\), any vertex works. This constructs the required factor. The \(N=3k+1\) condition was already shown necessary in Step 2 and sufficient in Step 3. All other congruence cases are excluded by \(|U|\le1\).

**Step 5: exact enumeration.** In a perfect three-vertex path factor, a triple with two vertices in part \(i\) and one in part \(j\ne i\) has exactly one allowed center; a triple drawn from three distinct parts has exactly three choices of center. The labeled exponential formula for sets of such components gives \(\exp Q\), with the factor \(1/2\) compensating for the unordered pair from part \(i\). Multiplying the coefficient by \(\prod_i n_i!\) restores the labels. For \(N=3k+1\), choose the lone unused vertex from the unique part of size \(2k+1\), then assign its remaining vertices in unordered pairs to the \(k\) distinctly labeled centers outside: \((2k+1)(2k)!/2^k=(2k+1)!/2^k\). All constructed codes are distinct and Steps 1–3 exhaust the possibilities.

## Verification
The accompanying standalone Python program `VERIFY.py` enumerates the candidate selected-edge subsets directly in the line graph and checks every open-neighborhood signature. For every integer-partition part profile with \(3\le N\le8\) and at least two parts (57 profiles), it compares the direct counts with the claimed cases and, when \(3\mid N\), separately evaluates the formal-exponential coefficient by exact rational polynomial arithmetic and checks a separate recursive path-factor count. It additionally checks triangular graph cases and both multipartite shapes \((5,2)\) and \((5,1,1)\), each giving 30 codes. All checks passed. Finite enumeration supports but does not prove the infinite assertions, which follow from the argument above. Execute `python3 VERIFY.py` using the Python 3 standard library.

## Relationship to prior work
Seo and Slater introduced and studied open-independent open-locating-dominating sets in 2017, and Cappelle, Coelho, Foulds and Longo developed structural and complexity results, publicly available by March 14, 2021. The existing general necessary signature conditions and their investigated graph classes do not themselves provide the complete-multipartite line-graph factorization or the enumerators stated here. A previously established exact rook-graph classification gives the complete bipartite subfamily \(L(K_{a,b})=K_a\square K_b\); that specialization is not a new result here. The new statement extends to arbitrarily many parts, uses three-different-part path components and gives a unified sharp existence criterion plus a multivariate code census. The triangular graph specialization is another consequence. Published work on independent point-set domination of line graphs concerns a different neighborhood condition and does not directly imply the open-locating statement.

## Limitations
Novelty has been assessed against the accessible references and search results, not against all possible unpublished or unindexed literature. This theorem does not classify the same codes for arbitrary line graphs, and it does not supply separate closed factorial products for every multipartite profile beyond the exact coefficient formula. The verification samples only small graphs; the general claims depend on the proof. The previously known rook subfamily is explicitly excluded from any novelty claim.

## References
1. S. J. Seo and P. J. Slater, "Open-independent, open-locating-dominating sets," Electronic Journal of Graph Theory and Applications 5(2), 179–193 (2017), DOI: 10.5614/ejgta.2017.5.2.2, https://www.ejgta.org/index.php/ejgta/article/download/210/pdf_47.
2. M. R. Cappelle, E. Coelho, L. R. Foulds and H. J. Longo, "Open-independent, open-locating-dominating sets: structural aspects of some classes of graphs," arXiv:2103.07972 (first posted 2021-03-14); Discrete Mathematics & Theoretical Computer Science 24:1 (2022), DOI: 10.46298/dmtcs.8440, https://dmtcs.episciences.org/en/articles/8440/download.
3. P. Gupta, A. Goyal and R. Jain, "Independent point-set domination in line graphs," AKCE International Journal of Graphs and Combinatorics 18(3), 180–185 (2021), DOI: 10.1080/09728600.2021.1995307, https://eld.bl.uk/catalog/100149030418_0x000001 (different domination concept).
