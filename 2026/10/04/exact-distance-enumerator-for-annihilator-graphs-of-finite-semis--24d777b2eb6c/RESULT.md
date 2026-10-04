# Exact distance enumerator for annihilator graphs of finite semisimple rings

## Finding

Let
\[
R=F_1\times\cdots\times F_n,\qquad n\ge 2,
\]
where each \(F_i\) is a finite field of order \(q_i\). Let \(G=AG(R)\) be the annihilator graph whose vertices are the nonzero zero-divisors and in which distinct \(x,y\) are adjacent when
\[
\operatorname{ann}(xy)\ne \operatorname{ann}(x)\cup\operatorname{ann}(y).
\]
Define
\[
Q=\prod_{i=1}^n q_i,\qquad
A=\prod_{i=1}^n(q_i-1),\qquad
B=\prod_{i=1}^n(q_i^2-2q_i+2),
\]
\[
P=\prod_{i=1}^n(q_i^2-q_i+1),\qquad
N=Q-A-1.
\]
Then \(G\) has \(N\) vertices, two vertices are adjacent exactly when their supports are incomparable under inclusion, and every nonadjacent pair of distinct vertices has distance two. Consequently
\[
|E(G)|=\frac{Q^2+B-2P}{2}.
\]
With the convention that the coefficient of \(x^0\) counts vertices, the Hosoya polynomial is
\[
H(G;x)
=
N+\frac{Q^2+B-2P}{2}x
+
\left(
\binom{N}{2}-\frac{Q^2+B-2P}{2}
\right)x^2,
\]
and the Wiener index is
\[
W(G)=N(N-1)-\frac{Q^2+B-2P}{2}.
\]

## Assumptions and scope

The ring is a finite direct product of at least two fields. Equivalently, this covers all finite commutative semisimple rings having at least two simple factors.

The graph is the annihilator graph introduced by Badawi: its vertex set consists of nonzero zero-divisors, and its adjacency condition compares \(\operatorname{ann}(xy)\) with the set-theoretic union \(\operatorname{ann}(x)\cup\operatorname{ann}(y)\). This is different from annihilating-ideal graphs and from zero-product graphs whose vertices or adjacency rules are different.

## Proof

For a vertex \(x=(x_1,\ldots,x_n)\), write
\[
S(x)=\{i:x_i\ne0\}.
\]
Because \(x\) is a nonzero zero-divisor, \(S(x)\) is a nonempty proper subset of \([n]\). For each nonempty proper \(S\subset[n]\), the number of vertices having support \(S\) is
\[
w_S=\prod_{i\in S}(q_i-1).
\]
Hence
\[
|V(G)|
=
\sum_{\varnothing\ne S\subsetneq[n]}w_S
=
\prod_i(1+q_i-1)-1-\prod_i(q_i-1)
=
Q-A-1=N.
\]

The annihilator of \(x\) is the coordinate ideal supported on \(S(x)^c\). Thus for vertices with supports \(S,T\),
\[
\operatorname{ann}(xy)
=
I_{(S\cap T)^c}
=
I_{S^c\cup T^c}
=
\operatorname{ann}(x)+\operatorname{ann}(y).
\]
For two ideals \(I,J\), the set union \(I\cup J\) equals the sum \(I+J\) exactly when \(I\subseteq J\) or \(J\subseteq I\). Therefore
\[
x\sim y
\quad\Longleftrightarrow\quad
S(x)\ \text{and}\ S(y)\ \text{are incomparable under inclusion}.
\]

It follows that every nonedge has distance two. If two distinct vertices have the same support \(S\), choose \(j\notin S\); a vertex of support \(\{j\}\) is adjacent to both. If \(S\subsetneq T\), choose \(a\in T\setminus S\) and \(b\notin T\). The support \(\{a,b\}\) is incomparable with both \(S\) and \(T\), hence gives a common neighbor. The case \(T\subsetneq S\) is symmetric. Thus all distinct pairs have distance one or two.

It remains to count the distance-one pairs. Let
\[
C=\sum_{\varnothing\ne S\subseteq T\subsetneq[n]}w_Sw_T.
\]
Before the restrictions \(S\ne\varnothing\) and \(T\ne[n]\), each coordinate has three states: outside \(T\), in \(T\setminus S\), or in \(S\). Their respective weights are \(1\), \(q_i-1\), and \((q_i-1)^2\). Therefore
\[
\sum_{S\subseteq T}w_Sw_T
=
\prod_i\left(1+(q_i-1)+(q_i-1)^2\right)
=
P.
\]
Inclusion-exclusion for \(S=\varnothing\) and \(T=[n]\) gives
\[
C=P-Q-AQ+A.
\]

The weight of equal-support ordered pairs is
\[
D=\sum_{\varnothing\ne S\subsetneq[n]}w_S^2
=
B-1-A^2.
\]
Hence the total weight of ordered support pairs that are comparable is \(2C-D\). The total weight of all ordered support pairs is \(N^2\), so the number of ordered adjacent vertex pairs is
\[
N^2-(2C-D).
\]
Dividing by two,
\[
|E(G)|=\frac{N^2+D-2C}{2}.
\]
Substituting \(N=Q-A-1\), \(C=P-Q-AQ+A\), and \(D=B-1-A^2\) simplifies to
\[
|E(G)|=\frac{Q^2+B-2P}{2}.
\]

Since all nonedges have distance two, the distance-two pair count is
\[
\binom{N}{2}-|E(G)|.
\]
The displayed Hosoya polynomial follows. Finally,
\[
W(G)
=
|E(G)|
+
2\left(\binom{N}{2}-|E(G)|\right)
=
N(N-1)-|E(G)|,
\]
which gives the stated formula.

## Verification

The proof is symbolic and does not depend on finite experimentation. The included replay independently constructs the support classes and then expands them to labeled vertices for several tuples of finite-field orders. It verifies the annihilator-adjacency criterion, all-pairs distances, the edge formula, the Hosoya coefficients, and the Wiener formula. The replay returns `VERIFY_OK`.

## Relationship to prior work

Badawi introduced the annihilator graph using the same annihilator-union adjacency condition. Afkhami, Khashyarmanesh, and Rajabi subsequently studied this graph for several structural classes and ring families, including finite quotient rings, but their published abstract emphasizes planarity, outerplanarity, ring-graph structure, clique number, and polynomial/fraction-ring behavior rather than distance enumerators.

A 2022 survey of Wiener indices of graphs over rings explicitly identifies annihilator graphs among the established ring-graph classes for which Wiener-index investigation remains a natural direction. The present formula resolves that direction for the full class of finite commutative semisimple rings.

A 2020 paper using the phrase “annihilator graph of \(\mathbb Z_n\)” employs a different graph: its displayed definition is based on zero products and its graph contains \(0\) as a universal vertex. Its Hosoya and Wiener formulas therefore concern a different object and do not imply the formulas above.

Later work on support-class methods for finite reduced rings is closely related structurally, but the support-incomparability distance enumeration above is independent of field sizes except through the multiplicities \(w_S\).

## Limitations

The theorem does not cover finite rings with nonzero Jacobson radical. The bibliographic search located no equivalent Hosoya or Wiener formula for Badawi’s annihilator graph of a product of fields, but an equivalent result could exist under different graph terminology or in an unindexed source.

The later finite-reduced-ring support literature was checked at abstract level only, so it remains a residual bibliographic risk rather than evidence of coverage.

## References

1. A. Badawi, “On the Annihilator Graph of a Commutative Ring,” *Communications in Algebra* 42 (2014), DOI 10.1080/00927872.2012.707262.
2. M. Afkhami, K. Khashyarmanesh, and Z. Rajabi, “Some results on the annihilator graph of a commutative ring,” *Czechoslovak Mathematical Journal* 67 (2017), DOI 10.21136/CMJ.2017.0436-15.
3. T. Asir, V. Rabikka, A. M. Anto, and N. Shunmugapriya, “Wiener index of graphs over rings: a survey,” *AKCE International Journal of Graphs and Combinatorics* (2022), DOI 10.1080/09728600.2022.2140088.
4. A. A. Ahmed, B. N. Mohammed, and A. F. Arif, “Hosoya Polynomial, Wiener Index, Coloring and Planar of Annihilator Graph of \(\mathbb Z_n\),” *Al-Rafidain Journal of Computer Sciences and Mathematics* (2020), DOI 10.33899/csmj.2020.167337.
