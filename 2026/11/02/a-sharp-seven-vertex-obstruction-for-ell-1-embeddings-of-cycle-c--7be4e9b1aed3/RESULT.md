# A sharp seven-vertex obstruction for \(\ell_1\) embeddings of cycle-complement metrics

## Finding
For every integer \(n\ge5\), let \(A_n=\overline{C_n}\) be the graph-theoretic complement of the simple cycle on \(\mathbb Z/n\mathbb Z\), with each edge of \(A_n\) assigned length one. Its finite shortest-path metric is \(d_n\). Let \(c_1(A_n)\) denote the infimum of the bi-Lipschitz distortion of embeddings of \((V(A_n),d_n)\) into a real \(\ell_1\) space. Then
\[
c_1(A_5)=c_1(A_6)=1,\qquad c_1(A_7)=\frac65,\qquad c_1(A_n)\ge\frac65\quad(n\ge8).
\]
Consequently, among all these connected cycle-complement graphs, exactly those with \(n=5,6\) are isometrically \(\ell_1\)-embeddable. A seven-vertex cut inequality gives a uniform gap of at least one fifth for every \(n\ge7\), and this constant is sharp as a uniform lower bound because equality holds for \(n=7\).

## Assumptions and scope
All graphs are finite, simple, undirected and unweighted, and all target spaces are real \(\ell_1\) spaces. The notation \(\overline{C_n}\) means complement as a simple graph, not complement of a metric. For distinct cyclic labels \(i,j\) and every \(n\ge5\),
\[
d_n(i,j)=\begin{cases}2&j-i\equiv\pm1\pmod n,\\1&\text{otherwise.}\end{cases}
\]
Indeed, the nonedges of \(A_n\) are exactly the original cycle edges, and their endpoints have a common neighbor in \(A_n\): among \(n\) vertices, only four are forbidden as a potential intermediate vertex. All distance statements below use this shortest-path metric, including when selecting seven vertices from a larger graph.

The distortion of an injective map \(f\) is the product of its optimal Lipschitz and inverse-Lipschitz constants. Rescaling allows normalization \(d_n(i,j)\le\|f(i)-f(j)\|_1\le c\,d_n(i,j)\) for every pair of distinct vertices.

## Proof
**Reduction to cuts.** On any finite vertex set, the \(\ell_1\) metric induced by a collection of vectors is a nonnegative linear combination of cut semimetrics \(\delta_S(i,j)=|\mathbf1_S(i)-\mathbf1_S(j)|\). For a real coordinate, this follows by integrating the thresholds separating its finitely many values; sum over coordinates and take limits if necessary. Thus every linear inequality valid for every cut is valid for every finite \(\ell_1\) metric.

**The seven-cycle obstruction.** Label the vertices of \(A_7\) by \(0,\ldots,6\) modulo seven. For each cut \(S\), put
\[
E_k(S)=\sum_{i=0}^{6}\delta_S(i,i+k\bmod7),\qquad k\in\{1,2,3\}.
\]
The following exact cut inequality holds:
\[
3E_1(S)\le E_2(S)+4E_3(S).\tag{1}
\]
This is a fully finite lemma: the standalone checker evaluates each side in integer arithmetic for every one of the \(2^7=128\) subsets, including complementary cuts. The code's two loops over all masks prove (1), without tolerance or random sampling. By the cut representation, for every \(\ell_1\) metric \(\rho\) on these seven vertices, inequality (1) holds with \(E_k(\rho)=\sum_i\rho(i,i+k)\). If \(d_7\le\rho\le c d_7\), then \(3E_1(\rho)\ge3\cdot7\cdot2=42\), whereas \(E_2(\rho)+4E_3(\rho)\le7c+4\cdot7c=35c\). Hence \(c\ge6/5\).

**A universal seven-vertex obstruction for larger cycles.** For a cut on seven linearly labeled vertices \(0,\ldots,6\), one has
\[
\begin{split}
\sum_{i=0}^5\delta_S(i,i+1)\le{}&\delta_S(0,3)+\delta_S(0,4)+\delta_S(0,5)\\
&+\delta_S(1,4)+2\delta_S(1,5)+\delta_S(1,6)\\
&+\delta_S(2,5)+\delta_S(2,6)+\delta_S(3,6).\tag{2}
\end{split}
\]
For complete reproducibility, the independent second exhaustive loop of the standalone checker verifies (2) exactly for every one of the \(128\) cuts. The nine terms on the right have total coefficient \(10\), and all their index separations lie between three and five.

Fix \(n\ge8\) and restrict \(d_n\) to seven consecutive cyclic labels \(0,\ldots,6\). Each of the six consecutive pairs on the left of (2) has graph distance \(2\). Every pair on the right has graph distance \(1\), because its cyclic index difference is neither one nor \(n-1\). Thus an arbitrary normalized noncontracting \(\ell_1\) embedding would give \(12\le10c\), proving \(c_1(A_n)\ge6/5\). No monotonicity of distortion in \(n\) is assumed.

**Sharpness and the two isometric cases.** For a subset \(S\subset\mathbb Z/n\mathbb Z\), define the averaged cut metric
\[
D_{n,S}(i,j)=\frac1n\sum_{h=0}^{n-1}\delta_{S+h}(i,j).
\]
It is a genuine \(\ell_1\) semimetric; each nonnegative linear combination of these averages gives an explicit finite-dimensional \(\ell_1\) embedding. Because it is translation invariant, it suffices to list its value at a cyclic separation \(k\le\lfloor n/2\rfloor\).

For \(n=5\), take \(S=\{0,2\}\): the vector of distances for separations one and two is \((4/5,2/5)\). Therefore \(\rho=(5/2)D_{5,S}\) has distances \((2,1)\), identical to \(d_5\).

For \(n=6\), take \(T=\{0,3\}\), \(U=\{0,2,4\}\): their distance vectors at separations one, two and three are respectively \((2/3,2/3,0)\) and \((1,0,1)\). Hence \(\rho=(3/2)D_{6,T}+D_{6,U}\) has distances \((2,1,1)\), identical to \(d_6\).

For \(n=7\), take \(T=\{0,3\}\), \(U=\{0,2,4\}\): their three separation-distance vectors are \((4/7,4/7,2/7)\) and \((6/7,2/7,4/7)\). Therefore
\[
\rho=\frac75\big(D_{7,T}+D_{7,U}\big)
\]
has distances \((2,6/5,6/5)\), so \(d_7\le\rho\le(6/5)d_7\). This matches the lower bound and concludes the theorem.

## Verification
Run the companion standalone Python standard-library program with `python3 check_anticircle.py`. It exactly enumerates \(128\) cut masks for each of (1) and (2), checks every pair for all three rational cut embeddings, and additionally checks the shortest-path formula for sample sizes \(5\) through \(34\). The reported successful replay was:

`CHECK_OK: 256 complete cut inequalities; 5,6,7 exact embeddings; n=5..34 graph distances`

The universal \(n\ge8\) conclusion is analytical: it applies a single verified seven-vertex cut inequality to consecutive labels in every graph. No finite-range experiment is used as a substitute for this quantifier.

## Relationship to prior work
The established cut-cone description and general \(\ell_1\) graph-embedding theory are classical. Deza and Laurent's work studies isometric \(\ell_1\) graph metrics and rigidity; its results for cycle graphs cannot be transferred without examination to the different metrics on their complements. Abraham, Filtser, Gupta and Neiman establish general distortion bounds for families of shortest-path metrics, not the sharp cycle-complement formula stated here. Knill studies exactly these cycle-complement graphs, but his displayed results concern combinatorics, topology and spectral quantities rather than cut-metric distortion. Historical work of Deza--Huang and Shpectorov concerns qualitative conditions on graph/complement pairs admitting \(\ell_1\) embeddings and may cover some qualitative boundary statements; those are not separately claimed as new. The asserted contribution is the sharp quantitative \(6/5\) obstruction uniformly over all complements of cycles of order at least seven, attained at order seven, together with explicit matching small examples. A matching earlier quantitative theorem was not identified, but priority has not been independently established.

## Limitations
The theorem does not determine the exact distortion when \(n\ge8\); only the uniform sharp lower bound is claimed. There are no assertions for disconnected graph complements of cycles of length below five, for arbitrary edge weights, or for embeddings into a target norm other than real \(\ell_1\). The validity of the two finite cut inequalities is exhaustively demonstrated by the included executable certificate; it has not been replaced by a shorter symbolic inequality proof. An older article on complementary \(\ell_1\)-graphs was not accessible in full, leaving a historical-priority risk. The work has not received an independent audit.

## References
- I. Abraham, A. Filtser, A. Gupta, and O. Neiman, *Metric Embedding via Shortest Path Decompositions*, first arXiv version August 14, 2017, https://arxiv.org/abs/1708.04073 .
- M. Deza and M. Laurent, *\(\ell_1\)-Rigid Graphs*, Journal of Algebraic Combinatorics 3 (1994), 153--175, https://doi.org/10.1023/A:1022441506632 .
- O. Knill, *Graph complements of circular graphs*, arXiv:2101.06873, https://arxiv.org/abs/2101.06873 .
- S. Shpectorov, *Complementary \(\ell_1\)-graphs*, Discrete Mathematics 192 (1998), 323--331, https://doi.org/10.1016/S0012-365X(98)0007X-1 .
- M. Deza and T. Huang, *Complementary \(\ell_1\)-graphs and related combinatorial structures*, https://doi.org/10.1007/3-540-61576-8_76 .
