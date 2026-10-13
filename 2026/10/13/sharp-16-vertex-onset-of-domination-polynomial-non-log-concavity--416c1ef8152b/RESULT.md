# Sharp 16-vertex onset of domination-polynomial non-log-concavity in trivially perfect graphs

## Finding
For a finite simple graph \(G\), write
\[
D_G(z)=\sum_{k=0}^{|V(G)|}d_k(G)z^k,
\]
where \(d_k(G)\) counts dominating vertex sets of cardinality \(k\). Call a coefficient sequence **log-concave** if \(d_k^2\ge d_{k-1}d_{k+1}\) at every interior index, including boundary zeros.

**Theorem.** For all finite trivially perfect graphs \(G\) the following hold.

1. If \(1\le |V(G)|\le15\), then \(D_G(z)\) has log-concave coefficients.
2. At order \(16\), exactly **one distinct domination polynomial** is not log-concave. Its coefficient vector, indexed by exponents \(0,\ldots,16\), is
   \[
   (0,1,15,230,1205,3615,7378,11080,12735,11410,8005,4368,1820,560,120,16,1).
   \]
   A realizing graph is \(W_{3,5}=K_1\vee(3K_5)\). The defect at degree two is \(15^2-1\cdot230=-5\). Uniqueness is of the **polynomial**, not asserted of the graph up to isomorphism.
3. Every trivially perfect graph on at most \(16\) vertices has a unimodal domination polynomial. Within the natural three-blade family \(W_{3,m}=K_1\vee(3K_m)\), log-concavity holds precisely for integer \(1\le m\le4\) and fails for every integer \(m\ge5\).

The order-16 statement is an exact finite classification, not an empirical extrapolation. The already-known polynomial formula for clique windmills is *not* claimed as a new result.

## Assumptions and scope
Graphs are finite, simple, and undirected. A set \(S\subseteq V(G)\) dominates \(G\) if every vertex lies in \(S\) or has a neighbor in \(S\). Trivially perfect means containing no induced four-vertex path or four-cycle; equivalently, the class is generated from \(K_1\) by disjoint union and adjoining a universal vertex. We use the empty graph solely for the recurrence, with domination polynomial \(1\).

A coefficient sequence with an initial string of zeros is log-concave in the usual inequality sense. Domination-polynomial coefficients have no *internal* zeros: every superset of a dominating set is dominating, so every size between the minimum dominating size and the graph order occurs.

The finite uniqueness statement concerns distinct coefficient vectors. Several nonisomorphic graphs can generally share one graph polynomial, so no unverified graph-isomorphism uniqueness is claimed.

## Proof
**1. Exact polynomial-image recurrence.** For each integer \(n\ge1\), let \(\mathcal P_n\) be the set of distinct domination polynomials of all \(n\)-vertex trivially perfect graphs, and let \(\mathcal C_n\) be the corresponding subset for connected graphs. Start from \(\mathcal P_0=\{1\}\) and \(\mathcal P_1=\mathcal C_1=\{z\}\). For \(n\ge2\), define
\[
\mathcal C_n=\bigl\{Q(z)+z(1+z)^{n-1}:Q\in\mathcal P_{n-1}\bigr\}.
\]
If a new universal vertex is selected in a dominating set, all old vertices are optional, giving \(z(1+z)^{n-1}\). If it is not selected, the selected old vertices must dominate the nonempty old graph, giving \(Q(z)\). Every connected trivially perfect graph has a universal vertex, and removing one leaves a trivially perfect graph; hence the recurrence is complete in both directions.

For each unordered partition \(\lambda=(n_1,\ldots,n_r)\) of \(n\) into \(r\ge2\) positive parts, let \(\mathcal C_{n_1}\cdots\mathcal C_{n_r}\) denote the set of products of one polynomial chosen from each factor family. Then
\[
\mathcal P_n=\mathcal C_n\ \cup\!
\bigcup_{\substack{n_1\le\cdots\le n_r,\ r\ge2\\n_1+\cdots+n_r=n}}
\mathcal C_{n_1}\cdots\mathcal C_{n_r}.
\]
This is exact because a disconnected graph decomposes into connected components and domination polynomials multiply under disjoint union. Repeated graph types or repeated polynomials may be discarded: the assertion is about the *image of the domination-polynomial map*, and multiplication/addition depend only on each image polynomial.

**2. Exhaustive finite cutoff.** The attached `verify.py` implements both recurrences with exact Python integers and coefficient tuples, enumerates unordered component-size partitions, deduplicates equal polynomials, and tests every inequality \(d_k^2\ge d_{k-1}d_{k+1}\) for each generated polynomial of orders \(2\) through \(15\). It obtains, respectively, \(2,4,9,20,48,115,284,713,1821,4701,12283,32374,86063,230337\) distinct polynomials, and **zero** violations for each order. It independently tests all labeled graphs through order five by the induced-forbidden-subgraph definition and direct domination-set enumeration, agreeing with the polynomial-image families.

The connected order-16 polynomials are exactly the image of \(\mathcal P_{15}\) under \(Q\mapsto Q+z(1+z)^{15}\). This map is injective, so there are \(230337\) distinct candidates, and exact integer checks find **one** violating coefficient vector: the vector stated above. There is no need to enumerate disconnected graphs at order 16: each component has at most 15 vertices and thus has a nonnegative log-concave domination-coefficient sequence without internal zeros. Such sequences are closed under convolution. One proof of this standard fact uses the equivalent nonnegativity of all \(2\times2\) minors of their Toeplitz matrices; convolution corresponds to matrix multiplication, and the \(2\times2\) Cauchy–Binet formula preserves nonnegativity. Therefore every disconnected order-16 domination polynomial is log-concave. Combined with the checked connected case, this proves the uniqueness statement for **all** order-16 graphs.

The only exceptional coefficient vector increases through its coefficient at degree eight and thereafter decreases. Every other polynomial through order 16 is log-concave with no internal zeros and hence unimodal. This proves the unimodality assertion.

**3. Sharpness and infinite continuation.** For the three-blade windmill \(W_{3,m}\), the known exact formula is
\[
D_{W_{3,m}}(z)=z(1+z)^{3m}+\bigl((1+z)^m-1\bigr)^3.
\]
Its first nonzero coefficients are \(d_1=1\), \(d_2=3m\), and \(d_3=\binom{3m}{2}+m^3\). The log-concavity inequality at degree two fails precisely when
\[
(3m)^2<\binom{3m}{2}+m^3
\quad\Longleftrightarrow\quad
2m^2>9m+3.
\]
For integer \(m\ge1\) this is equivalent to \(m\ge5\). In particular, \(m=5\) gives an order-16 trivially perfect graph with \(d_2^2-d_1d_3=225-230=-5\). For \(m\le4\), the order is at most 13, so the first part of the theorem proves complete log-concavity. This establishes the exact three-blade threshold and supplies failures of unbounded order.

## Verification
Run `python3 verify.py` using Python 3.8+ (standard library only). Its exact output is preserved in `verify_output.txt`. The package includes all source code and the actual replay result, not just a summary or a completion claim. The independent small-graph crosscheck examines all labeled simple graphs of orders 1 through 5, recognizes trivially perfect graphs by excluded induced \(P_4,C_4\), and checks domination directly. The 16-vertex windmill is independently checked by all \(2^{16}=65536\) vertex subsets. The order-15 and connected order-16 enumerations involve exact polynomial-image sets, not sampled graphs or truncated coefficient ranges.

The finite computation verifies a finite assertion because the structural recurrences cover **every** graph in the finite domain. It does not establish any unspecified all-orders unimodality theorem or an all-orders uniqueness of obstructions. Convolution closure and the explicit family argument are mathematical proofs, not computational extrapolations.

## Relationship to prior work
Omar, *New Perspectives on the Unimodality of Domination Polynomials* (first public January 20, 2026), proves log-concavity for threshold graphs and proposes total positivity methods for further hereditary classes. Threshold graphs form a proper subclass of trivially perfect graphs; the cited paper does not give a sharp log-concavity boundary for all trivially perfect graphs.

Rather, *On domination polynomials of some graphs* (2025), provides the already-known polynomial of equal-parameter generalized friendship graphs and a more general formula for clique-join graphs. Its Theorem 2.16 already implies the polynomial used for \(W_{3,m}\). The new result here is **not** that formula or the single easily calculated defect. It is the globally sharp order-16 lower bound and uniqueness of the exceptional coefficient vector **across every trivially perfect graph**, with a complete reproducible finite image enumeration.

The standard closure characterization of trivially perfect graphs is documented, for example, by Drange and Pilipczuk. The convolution theorem is classical and appears, for example, in work of Johnson and Goldschmidt. A prior counterexample to domination-polynomial log-concavity among unrestricted graphs of order nine does not settle the minimum within the narrower trivially perfect class.

## Limitations
The proof establishes a *sharp finite cutoff* and a complete single-order polynomial-image classification, rather than an analytic classification of all non-log-concave trivially perfect graphs at arbitrarily high orders. At order 16, uniqueness is for the coefficient sequence only; it is not a census of isomorphism classes producing the vector. The finite certificate assumes the exact structural characterization of trivially perfect graphs and the code's correct execution; an independent external audit has not been performed. Prior literature might contain an unindexed equivalent statement under quasi-threshold or rooted-forest terminology. The earlier clique-join domination formula is fully credited.

## References
1. Mohamed Omar, *New Perspectives on the Unimodality of Domination Polynomials*, arXiv:2601.14494v1, first public January 20, 2026; https://arxiv.org/html/2601.14494.
2. Bilal Ahmad Rather, *On domination polynomials of some graphs*, Journal of Combinatorial Mathematics and Combinatorial Computing 126 (2025), 279–289, DOI 10.61091/jcmcc126-19; https://combinatorialpress.com/jcmcc-articles/volume-126/on-domination-polynomials-of-some-graphs/.
3. P. G. Drange and M. Pilipczuk, *A Polynomial Kernel for Trivially Perfect Editing*, Algorithmica 80 (2018), Proposition 2; DOI 10.1007/s00453-017-0401-6.
4. Oliver Johnson and Christina Goldschmidt, *Preservation of log-concavity on summation*, ESAIM Probability and Statistics 10 (2006), 206–215, DOI 10.1051/ps:2006008.
5. Iain Beaton and Jason I. Brown, *On the Unimodality of Domination Polynomials*, arXiv:2012.11813 (2020).
