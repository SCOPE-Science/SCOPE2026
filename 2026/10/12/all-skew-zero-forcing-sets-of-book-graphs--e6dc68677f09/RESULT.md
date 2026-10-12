# All skew zero forcing sets of book graphs
## Finding
For every integer \(n\ge1\), let the book graph be
\[
B_n=K_{1,n}\mathbin{\square}P_2.
\]
Label its common edge by \(ab\), and label page \(i\) by the four-cycle \(a x_i y_i b a\). Thus
\[
U=\{b,x_1,\ldots,x_n\},\qquad V=\{a,y_1,\ldots,y_n\}
\]
are the two bipartition classes, each of cardinality \(n+1\).

An initial set \(S\subseteq V(B_n)\) is a skew zero forcing set if and only if
\[
S\cap U\ne\varnothing\qquad\text{and}\qquad S\cap V\ne\varnothing.
\]
Therefore the complete skew zero forcing polynomial is
\[
\mathcal Z_-(B_n;x)
=\sum_{S\text{ skew zero forcing}}x^{|S|}
=\big((1+x)^{n+1}-1\big)^2.
\]
In particular,
\[
Z^-(B_n)=2,
\qquad
\#\{\text{minimum skew zero forcing sets}\}=(n+1)^2,
\]
and the failed skew zero forcing number is
\[
F^-(B_n)=n+1.
\]
The minimum sets are exactly the pairs containing one vertex of \(U\) and one vertex of \(V\). The maximum failed sets are exactly the two bipartition classes.

## Assumptions and scope
Graphs are finite, simple, and undirected. The skew color-change rule permits any vertex, regardless of its current color, to force its unique white neighbor. The polynomial counts all initial skew zero forcing sets by cardinality.

The theorem is stated for every \(n\ge1\). At \(n=1\), the book graph is \(C_4\), and the formula gives \(4x^2+4x^3+x^4\), so the boundary case is included rather than treated separately.

## Proof
Let \(W\) be a set of white vertices. Call \(W\) skew-stalled when no vertex has exactly one neighbor in \(W\). Equivalently,
\[
|N(z)\cap W|\ne1\qquad\text{for every vertex }z.
\]
A starting set \(S\) fails to skew force precisely when its initial white complement contains a nonempty skew-stalled set: a nonempty final white set is skew-stalled, while a skew-stalled subset can never lose any of its own vertices during the forcing process.

We first classify all nonempty skew-stalled sets in \(B_n\). Write \(A\) and \(B\) for the indicators of \(a\in W\) and \(b\in W\), respectively. Since
\[
N(x_i)=\{a,y_i\},
\]
the stalled condition at \(x_i\) says that \(A+\mathbf 1_{\{y_i\in W\}}\) is not equal to \(1\). Both summands are binary, so
\[
y_i\in W\quad\Longleftrightarrow\quad a\in W
\]
for every \(i\). Similarly, because
\[
N(y_i)=\{b,x_i\},
\]
we obtain
\[
x_i\in W\quad\Longleftrightarrow\quad b\in W
\]
for every \(i\).

Hence every skew-stalled set is one of
\[
\varnothing,\qquad U,\qquad V,\qquad U\cup V.
\]
Each listed set is indeed skew-stalled: for \(U\), vertices in \(U\) have zero neighbors in \(U\), every \(y_i\) has exactly two neighbors in \(U\), and \(a\) has \(n+1\) neighbors in \(U\); the argument for \(V\) is symmetric, and the whole vertex set is stalled because every vertex has degree at least two.

Now let \(W_0=V(B_n)\setminus S\). It contains a nonempty stalled set exactly when it contains \(U\) or \(V\). Since \(U\) and \(V\) partition the vertex set, this is equivalent to
\[
S\cap U=\varnothing\quad\text{or}\quad S\cap V=\varnothing.
\]
Thus \(S\) skew forces exactly when it meets both bipartition classes.

To enumerate all such sets, choose a nonempty subset of \(U\) and independently a nonempty subset of \(V\). The ordinary generating function is therefore
\[
\big((1+x)^{n+1}-1\big)^2.
\]
Its least nonzero degree is \(2\), with coefficient \((n+1)^2\). A failed set is a subset of one bipartition class, so its maximum possible size is \(n+1\). This proves all asserted formulas.

## Verification
The accompanying `verify.py` constructs \(B_n\) directly and independently simulates the skew color-change rule for every initial subset for \(1\le n\le8\). For each subset it compares the simulation with the bipartition-intersection criterion. It also compares every polynomial coefficient with \(\big((1+x)^{n+1}-1\big)^2\), and checks the minimum forcing size, number of minimum sets, and maximum failed size.

Running the packaged verifier gives:

`VERIFY_OK n_range=1..8 subset_checks=349520 criterion_checks=349520 coefficient_checks=96 minimum_checks=24 max_order=18`

The finite computation is a stress test through order \(18\); the proof above establishes the theorem for arbitrary \(n\).

## Relationship to prior work
DeAlba's skew-zero-forcing paper gives the skew color-change rule, matching-based results for bipartite graphs, and several scalar formulas for named families. Its accessible full text does not contain the term “book.” Its Cartesian-product list includes grids and products \(K_s\mathbin{\square}P_t\) in ranges that do not include \(K_{1,n}\mathbin{\square}P_2\). Its theorem identifying minimum skew forcing sets from maximum matchings assumes all maximum matchings are uniquely restricted; this hypothesis fails for every book graph here because \(B_n\) has \(n+1\) distinct perfect matchings. Thus those statements do not imply the present all-set classification or polynomial.

Later work develops general closure, complexity, and failed-skew-zero-forcing theory. The recent failed-skew literature retrieved for comparison treats path powers, circulants, and previously studied standard families, but no exact book-graph all-set formula was identified. General closure or hypergraph-burning equivalences provide frameworks for deciding skew forcing; they do not themselves perform the book-specific stalled-set classification above.

The same graph family also appears in literature under the standard definition \(B_n=K_{1,n}\mathbin{\square}P_2\), including work on unrelated graph polynomials and invariants. Those same-object sources establish nomenclature but do not address skew zero forcing.

## Limitations
No claim is made that the skew color-change rule, the book graph, or the general theory of skew-stalled sets is new. The accepted claim is the exact book-specific characterization of every initial skew zero forcing set and the consequences derived from it.

Focused semantic-index and literature searches cannot logically exclude every unindexed thesis or older local source. The strongest residual originality risk is an overlooked source that specializes general skew forcing to book graphs under another name. The proof and checker establish correctness independently of that bibliographic risk.

## References
1. L. M. DeAlba, “Some results on minimum skew zero forcing sets, and skew zero forcing number,” arXiv:1404.1618. Version 1 posted 6 April 2014; the manuscript lists AMS classifications 05C50 and 15A03.
2. J. Cooper and G. Fickes, “Zero loci of nullvectors and skew zero forcing in graphs and hypergraphs,” arXiv:2303.17419.
3. A. Johnson, A. Vick, R. Flórez, and D. A. Narayan, “Failed Skew Zero Forcing Numbers of Path Powers and Circulant Graphs,” AppliedMath 5 (2025), 32. DOI: 10.3390/appliedmath5020032.
4. E. W. Weisstein, “Book Graph,” MathWorld, defining \(B_n=K_{1,n}\mathbin{\square}P_2\).
5. P. Dhanya and V. Anil Kumar, “Equi Neighbor Polynomial of Some Binary Graph Operations,” Journal of Combinatorial Mathematics and Combinatorial Computing 119 (2024), 35–43. DOI: 10.61091/jcmcc119-04.
