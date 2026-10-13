# Zero forcing polynomials recognize comaximal graphs with no field local factors

## Finding

Let \(R\cong\prod_{i=1}^{r}R_i\) be a finite commutative ring, where \(r\ge1\), every \(R_i\) is local and not a field, \(\mathfrak m_i\) is its maximal ideal, \(s_i=|\mathfrak m_i|\), and \(q_i=|R_i/\mathfrak m_i|\). Put \(S=\prod_i s_i\). For each \(A\subseteq[r]\), define \(w_A=S\prod_{i\in A}(q_i-1)\), and put \(N=|R|=\sum_{A\subseteq[r]}w_A\). For the full comaximal graph \(\Gamma(R)\) on the elements of \(R\), \[\mathcal Z(\Gamma(R);u)=u^{N-2^r}\prod_{A\subseteq[r]}(u+w_A).\] Hence \(Z(\Gamma(R))=M(\Gamma(R))=N-2^r\), the real symmetric minimum rank is \(2^r\), and the minimum zero forcing sets are exactly the complements of one vertex from every unit-pattern class. Moreover the polynomial recovers \(r\), the product \(S=\prod_i|\mathfrak m_i|\), and the unordered multiset \(\{q_1,\ldots,q_r\}\); consequently it determines \(\Gamma(R)\) up to graph isomorphism within this no-field-local-factor class.

The number of minimum zero forcing sets is
\[
\prod_{A\subseteq[r]}w_A
=
S^{2^r}
\left(\prod_{i=1}^{r}(q_i-1)\right)^{2^{r-1}}.
\]

## Assumptions and scope

Let
\[
R\cong R_1\times\cdots\times R_r,
\qquad r\ge1,
\]
be finite and commutative. Each \(R_i\) is assumed local and not a field, with maximal ideal \(\mathfrak m_i\),
\[
s_i=|\mathfrak m_i|\ge2,
\qquad
q_i=|R_i/\mathfrak m_i|\ge2.
\]

The full comaximal graph \(\Gamma(R)\) has vertex set \(R\); distinct \(x,y\) are adjacent when
\[
Rx+Ry=R.
\]

For a graph \(G\), \(\mathcal Z(G;u)\) denotes the standard zero forcing polynomial, \(Z(G)\) the zero forcing number, \(M(G)\) the real symmetric maximum nullity, and \(\operatorname{mr}(G)\) the corresponding minimum rank.

## Proof

For \(x=(x_1,\ldots,x_r)\in R\), define its unit pattern
\[
U(x)=\{i:x_i\in R_i^\times\}.
\]
For each \(A\subseteq[r]\), let
\[
C_A=\{x\in R:U(x)=A\}.
\]
Since a finite local ring has
\[
|R_i^\times|=s_i(q_i-1),
\]
the class size is
\[
|C_A|
=
\prod_{i\in A}s_i(q_i-1)
\prod_{i\notin A}s_i
=
S\prod_{i\in A}(q_i-1)
=
w_A.
\tag{1}
\]

Two elements \(x\in C_A\) and \(y\in C_B\) are comaximal exactly when, in every local coordinate, at least one coordinate is a unit. Hence
\[
x\sim y
\quad\Longleftrightarrow\quad
A\cup B=[r].
\tag{2}
\]
The class \(C_{[r]}\), consisting of all units, is a clique. Every other \(C_A\) is independent. In each case vertices in a common class are twins.

Thus a zero forcing set can leave at most one white vertex in every \(C_A\). If two vertices of one class were white, every vertex outside that class would see either both or neither, and the two could not be separated by a first force.

Conversely suppose at most one white vertex remains in each class. Let \(\mathcal W\) be the set of white unit patterns. If \(\mathcal W\ne\varnothing\), choose an inclusion-maximal
\[
T\in\mathcal W.
\]
Consider the complementary type
\[
T^c=[r]\setminus T.
\]
Because every local factor is a nonfield, every class size in (1) is at least \(2\). Therefore \(C_{T^c}\) contains a blue vertex even if it also contains its one allowed white representative.

A white type \(U\in\mathcal W\) is adjacent to a vertex of type \(T^c\) exactly when
\[
U\cup T^c=[r],
\]
equivalently
\[
T\subseteq U.
\]
By maximality of \(T\), the only white type with this property is \(T\). Hence a blue vertex of \(C_{T^c}\) has exactly one white neighbor and forces the white vertex of \(C_T\).

Deleting \(T\) from \(\mathcal W\) and repeating proves that every profile with at most one white vertex per unit-pattern class is zero forcing.

For a class of size \(w_A\), the forcing set either contains all \(w_A\) vertices or omits exactly one of them. Its contribution is
\[
u^{w_A}+w_Au^{w_A-1}
=
u^{w_A-1}(u+w_A).
\]
Multiplying over all \(2^r\) classes gives
\[
\mathcal Z(\Gamma(R);u)
=
u^{N-2^r}
\prod_{A\subseteq[r]}(u+w_A).
\tag{3}
\]
The least exponent gives
\[
Z(\Gamma(R))=N-2^r,
\]
and a minimum set omits exactly one vertex from every class.

For the minimum-rank statement, let \(Q_r\) be the \(2^r\times2^r\) matrix indexed by subsets of \([r]\) with
\[
(Q_r)_{A,B}
=
\begin{cases}
1,&A\cup B=[r],\\
0,&\text{otherwise}.
\end{cases}
\]
After complementing both subset indices, \(Q_r\) becomes the disjointness matrix
\[
D_r=
\begin{pmatrix}
1&1\\
1&0
\end{pmatrix}^{\otimes r}.
\]
The \(2\times2\) factor is invertible, so \(Q_r\) has full rank
\[
2^r.
\tag{4}
\]

Let \(X\) be the vertex-by-class incidence matrix. Then
\[
XQ_rX^{\mathsf T}
\]
has exactly the required off-diagonal zero pattern of \(\Gamma(R)\): equation (2) controls different classes, while the diagonal entry of \(Q_r\) is nonzero only for the all-unit class. Since every class is nonempty, \(X\) has full column rank. Equation (4) yields a graph-pattern matrix of rank \(2^r\), so
\[
\operatorname{mr}(\Gamma(R))\le2^r.
\]
The standard inequality
\[
M(G)\le Z(G)
\]
gives
\[
\operatorname{mr}(\Gamma(R))
=
N-M(\Gamma(R))
\ge
N-Z(\Gamma(R))
=
2^r.
\]
Therefore
\[
\operatorname{mr}(\Gamma(R))=2^r,
\qquad
M(\Gamma(R))=Z(\Gamma(R))=N-2^r.
\tag{5}
\]

Finally, the nonzero root magnitudes of (3) are the multiset
\[
\mathcal R
=
\left\{
S\prod_{i\in A}(q_i-1):A\subseteq[r]
\right\}.
\tag{6}
\]
Its cardinality with multiplicity is \(2^r\), so the polynomial recovers \(r\). Its smallest value is \(S\), hence \(S\) is recovered.

Normalize (6) by \(S\). This gives all subset products of
\[
a_i=q_i-1\ge1.
\]
If exactly \(t\) of the \(a_i\) equal \(1\), then the normalized root \(1\) has multiplicity \(2^t\), so \(t\) is recovered. Dividing all normalized-root multiplicities by \(2^t\) leaves the complete subset-product multiset of the factors \(a_i>1\). These factors are recovered greedily: after the already recovered factors have generated their subset products, the smallest unexplained product is the next smallest factor. Removing all newly generated products and iterating recovers the full multiset \(\{a_i\}\), including repetitions. Therefore the polynomial recovers
\[
\{q_i\}=\{a_i+1\}.
\]

The class sizes (1) and adjacency rule (2) depend only on \(S\) and the unordered multiset \(\{q_i\}\). Hence these recovered data determine the graph up to isomorphism in the stated class.

## Verification

The accompanying `verify.py` was read from its packaged path before replay.

It constructs the unit-pattern quotient, verifies its exact rank through five local factors, and exhausts every at-most-one-white type profile through four factors. At four factors this is
\[
2^{16}=65536
\]
profiles.

At the full graph level, it exhaustively tests every vertex subset for the realizable examples corresponding to
\[
\mathbb Z/4,\qquad
\mathbb Z/9,\qquad
\mathbb Z/4\times\mathbb Z/4,
\]
and reproduces the entire polynomial (3).

It also checks a mixed
\[
\mathbb Z/4\times\mathbb Z/9
\]
unit-pattern decomposition and replays the root-multiset recovery algorithm on examples containing repeated residue-field sizes and several residue fields of order \(2\).

Exact replay output:

```text
quotient r=1: rank=2
quotient r=2: rank=4
quotient r=3: rank=8
quotient r=4: rank=16
quotient r=5: rank=32
profiles r=1: 4 forcing profiles
profiles r=2: 16 forcing profiles
profiles r=3: 256 forcing profiles
profiles r=4: 65536 forcing profiles
q=(2,), s=(2,): weights=[2, 2], N=4, Z=2, min_sets=4
q=(3,), s=(3,): weights=[3, 6], N=9, Z=7, min_sets=18
q=(2, 2), s=(2, 2): weights=[4, 4, 4, 4], N=16, Z=12, min_sets=256
mixed q=(2, 3), s=(2, 3): weights=[6, 6, 12, 12], predicted_Z=32
recover q=(2,), S=2 -> q=(2,), S=2
recover q=(2, 3), S=6 -> q=(2, 3), S=6
recover q=(2, 2, 5), S=40 -> q=(2, 2, 5), S=40
recover q=(3, 4, 7), S=168 -> q=(3, 4, 7), S=168
recover q=(2, 3, 3, 5), S=270 -> q=(2, 3, 3, 5), S=270
VERIFY_OK
```

These finite checks corroborate the proof. The arbitrary-\(r\) result follows from the inclusion-maximal forcing argument, the Kronecker rank identity, and exact multiset inversion.

## Relationship to prior work

Samei studies the full comaximal graph on ring elements, together with its nonunit subgraphs, and treats diameter, girth, cycles, domination, and ring-theoretic characterizations. The publication record gives Mathematics Subject Classification \(13A99\).

A recent full-text structural study proves that the comaximal graph of every commutative Artinian ring is an \(H\)-join of complete and null graphs. In its notation, vertices with the same unit-coordinate pattern form one factor, and two factors are joined exactly when their patterns cover all local coordinates. That paper computes the Wiener index and adjacency spectrum, but does not study zero forcing.

General zero forcing polynomial theory supplies the invariant and standard extremal tools. Targeted searches under “comaximal”, “co-maximal”, “zero forcing”, “zero forcing polynomial”, “minimum rank”, “maximum nullity”, “H-join”, and “unit pattern” did not locate the factorization (3), the exact rank statement (5), or the inverse recovery of \(S\) and the residue-field orders.

The closest same-object semantic result concerns total and paired domination of a reduced comaximal subgraph rather than standard zero forcing on the full graph.

## Limitations

Every local factor is assumed to be a nonfield. A field factor has maximal ideal size \(1\), creating singleton unit-pattern classes; then the source class \(C_{T^c}\) used in the forcing proof need not contain a blue vertex.

The polynomial recovers only the product
\[
S=\prod_i|\mathfrak m_i|,
\]
not the individual maximal-ideal sizes. This is sharp at the graph level: the class sizes themselves depend on the \(s_i\) only through this product.

The recovered residue-field orders are unordered. This is sufficient because permuting local coordinates gives the same unit-pattern blow-up graph.

The minimum-rank statement is over real symmetric graph-pattern matrices.

## References

1. K. Samei, “On the Comaximal Graph of a Commutative Ring,” *Canadian Mathematical Bulletin* 57 (2014), 413–423. DOI: 10.4153/CMB-2013-033-7. Issue date 14 June 2014.
2. A. Y. Hummdi, J. Rani, S. Krishnan, and J. Nisar, “On the Spectra and Wiener Index of the Comaximal Graph of a Commutative Ring,” *Symmetry* 18 (2026), 1269. DOI: 10.3390/sym18081269.
3. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” *Discrete Applied Mathematics* 258 (2019), 35–48. arXiv:1801.08910.
4. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
