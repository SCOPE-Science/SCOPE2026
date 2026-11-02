# Hereditary leaf-event log-submodularity and a bipartite independence boundary

## Finding

Let \(T\) be a uniformly random spanning tree of a complete multipartite graph \(G=K_{n_1,\ldots,n_r}\), with \(r\ge2\), \(n_i\ge1\), and \(n=\sum_i n_i\ge3\). Write \(V_i\) for its part classes, \(L_v=\mathbf1\{\deg_T(v)=1\}\), and
\[\Phi(S)=\Pr(L_v=1\text{ for every }v\in S).\]
For \(S\subsetneq V(G)\), with \(s_i=|S\cap V_i|\), the exact all-marked-leaf probability is
\[
\Phi(S)=\left(\frac{n-|S|}{n}\right)^{r-2}
\prod_{i=1}^r\left(1-\frac{|S|-s_i}{n-n_i}\right)^{n_i-1}.
\tag{1}
\]
Set \(\Phi(V(G))=0\). The convention \(0^0=1\) applies only to factors with zero exponents.

**All-order lattice inequality.** For every \(A,B\subseteq V(G)\),
\[
\Phi(A\cup B)\Phi(A\cap B)\le\Phi(A)\Phi(B). \tag{2}
\]
For \(r\ge3\), (2) is strict if \(A\setminus B\) and \(B\setminus A\) are nonempty and \(\Phi(A)\Phi(B)>0\). Equivalently, after conditioning on any feasible set of marked vertices being leaves, the events that two disjoint nonempty further sets consist entirely of leaves have strictly negative covariance whenever the individual conditional event probabilities are positive.

**Sharp structural boundary.** For \(r=2\), the complete random leaf-indicator vectors in the two distinct vertex classes are independent. In contrast, for every \(r\ge3\) all distinct individual leaf indicators are strictly negatively correlated. Neither claim asserts full negative association for arbitrary nonlinear functions of disjoint leaf-indicator families.

## Assumptions and scope

All graphs are finite, simple, and labeled. Exactly \(r\) nonempty part classes occur, and a spanning tree is sampled uniformly among the \(\tau(G)\) distinct labeled spanning trees. Each vertex is a leaf exactly when its tree degree is one. For \(n\ge3\), two leaves cannot be adjacent. Formula (1) is evaluated for proper marked sets, including sets whose probability is zero; the whole-set event is impossible. A conditional strict-inequality assertion is made only when its stated conditioning and individual conditional events have positive probability.

## Proof

**Counting marked leaves.** For \(S\subsetneq V\), every tree in which all vertices of \(S\) are leaves has the unique form: a spanning tree of the induced graph \(G[V\setminus S]\), together with, for every marked vertex \(v\in S\cap V_i\), one edge connecting \(v\) to an unmarked vertex outside \(V_i\). Its number of possible attachment vertices is \(n-n_i-|S|+s_i\). Conversely these choices always give such a tree. Thus the number of eligible trees is
\[
\tau(G[V\setminus S])\prod_{i=1}^r(n-n_i-|S|+s_i)^{s_i}.
\tag{3}
\]
The classical complete multipartite tree count is
\[\tau(K_{m_1,\ldots,m_r})=m^{r-2}\prod_i(m-m_i)^{m_i-1},\]
with zero-size part classes removed in degeneracies, and the one-vertex tree count defined as one. For a direct argument avoiding degenerate exponent conventions, use the matrix-tree formula or count the reduced graph independently for the cases where it has at most one vertex. Substituting \(m_i=n_i-s_i\) into (3), canceling \(\tau(G)=n^{r-2}\prod_i(n-n_i)^{n_i-1}\), and collecting each base's exponents \((n_i-s_i-1)+s_i=n_i-1\) proves (1) whenever \(G[V\setminus S]\) has at least two vertices and is connected. If it is disconnected, its tree count is zero and at least one non-singleton part exhausts the reduced graph, giving a zero factor on the right of (1). If only one vertex remains, the attachment count directly agrees with the right side: either that vertex is adjacent to every marked vertex and all choices are unique, or the count is zero. Thus (1) holds at all proper-set boundaries.

**Log-submodularity.** On the domain of positive factors, the logarithm of the right side of (1), up to an additive constant, is
\[
(r-2)\log(n-|S|)+\sum_{i=1}^r(n_i-1)\log(n-n_i-|S\setminus V_i|).
\tag{4}
\]
Each summand is submodular as a function of \(S\): it is a concave logarithm of a positive affine function of a subset cardinality. Explicitly, if adding elements creates two nonzero distinct increments \(p,q\), then \(x(x+p+q)<(x+p)(x+q)\) for \(x,p,q>0\); reversing this identity gives the required inequality after taking logarithms. Nonnegative linear combinations preserve submodularity. If any needed probability vanishes, (2) follows by monotonicity of \(\Phi\) or passage to a positive-factor limit. When \(r\ge3\), the first logarithmic term has positive weight and gives strictness for incomparable \(A,B\) with positive right-hand probabilities. The case \(A\cup B=V\) has zero left-hand product and is also strict.

For disjoint nonempty \(A,B,H\) with \(\Phi(H\cup A)\Phi(H\cup B)>0\), apply (2) to \(H\cup A\) and \(H\cup B\), then divide by \(\Phi(H)^2\) to obtain the asserted conditional negative covariance.

**Bipartite independence.** If \(r=2\), with part sizes \(a,b\) and marked subsets \(S_A,S_B\), (1) reduces to
\[
\Phi(S_A\cup S_B)=\left(1-\frac{|S_B|}{b}\right)^{a-1}
\left(1-\frac{|S_A|}{a}\right)^{b-1}.
\tag{5}
\]
This is a product of a function of \(S_A\) and a function of \(S_B\). Since all mixed products of Bernoulli leaf indicators factor in this way, inclusion-exclusion gives independence of the full indicator vectors. For \(r\ge3\), strictness with singleton disjoint sets implies strict negative covariance for each distinct pair.

**Joint distribution.** Let \(N_i=\sum_{v\in V_i}L_v\). All factorial moments, and hence their finite joint distribution, can be reconstructed by
\[
\mathbb E\prod_{i=1}^r z_i^{N_i}=
\sum_{0\le s_i\le n_i}\left(\prod_{i=1}^r\binom{n_i}{s_i}(z_i-1)^{s_i}\right)
\Phi(\mathbf s),
\tag{6}
\]
where \(\Phi(\mathbf s)\) is (1) for any marked set with the indicated partwise cardinalities, with \(\Phi(n_1,\ldots,n_r)=0\).

## Verification

The provided `verify.py` independently generates Prüfer-coded labeled trees, removes edges forbidden by the multipartite structure, decodes their edges, obtains leaves from decoded vertex degrees, and exactly checks each probability in (1) against enumeration. It also tests (2) for every ordered pair of marked subsets. The checks covered 36 complete multipartite size profiles with total order between three and seven, 64,538 admissible trees, 2,704 exact rational probability identities, and 277,632 integer inequalities. Run with `python verify.py`. Enumeration is finite corroboration only; (1)–(6) follow from the proof for all allowed parameters.

## Relationship to prior work

Eğecioğlu and Remmel (1994) gave a bijection and the complete multipartite spanning-tree count, and their Section 6 derives one-vertex leaf probabilities and asymptotics. Their coding framework supplies a natural route to (1). Lewis (1999) used Prüfer sequences and discussed distributions of vertices of a given degree; only the abstract was accessible for this comparison, so a stronger historical derivation of (1) cannot be ruled out. Grimmett and Winkler (2003) discuss edge negative association of random forests and trees; that is about edge indicators, not the hereditary joint leaf-event lattice inequality (2). The principal claim here is the sharp, strict all-order leaf-event inequality and the independence/strict-dependence boundary across the number of classes, rather than the classical tree enumeration itself.

## Limitations

No claim is made about independence within a single bipartite class, full negative association of arbitrary functions of leaf indicators, edge-event negative association, or other host graph families. The all-set probability formula is a direct consequence of standard tree enumeration, and the lattice inequality is specific to its factorization; the possibility of earlier equivalent occupancy-type formulations is a concrete priority risk. Lewis (1999) was not inspected in full. The exact date cited for the dated probability-literature anchor refers to the first public arXiv version, not to the older combinatorial literature with incompletely documented dates. Independent scientific validation has not been performed.

## References

1. Ö. Eğecioğlu and J. B. Remmel, *A Bijection for Spanning Trees of Complete Multipartite Graphs* (1994), full article: https://sites.cs.ucsb.edu/~omer/DOWNLOADABLE/multipartite94.pdf.
2. R. P. Lewis, *The Number of Spanning Trees of a Complete Multipartite Graph*, Discrete Mathematics 197–198 (1999), 537–541, DOI: 10.1016/S0012-365X(98)00260-X.
3. G. R. Grimmett and S. N. Winkler, *Negative Association in Uniform Forests and Connected Graphs*, arXiv:math/0302185, first submitted 17 February 2003, https://arxiv.org/abs/math/0302185.
