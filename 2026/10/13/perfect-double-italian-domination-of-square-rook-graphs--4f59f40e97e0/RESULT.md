# Perfect double Italian domination of square rook graphs
## Finding
For every integer
\[
n\ge3,
\]
let
\[
R_n=K_n\square K_n.
\]
Equivalently, \(R_n\) is the square rook graph, the Hamming graph \(H(2,n)\), and the line graph \(L(K_{n,n})\).

Then
\[
\gamma_{dI}^{p}(R_n)=2n.
\]

More strongly, write the labels as an \(n\times n\) matrix
\[
X=(x_{ij}),\qquad x_{ij}=f(v_{ij}),
\]
where \(v_{ij}\) is adjacent to \(v_{i'j'}\) exactly when \(i=i'\) or \(j=j'\), but not both. A function \(f\) is minimum perfect double Italian if and only if
\[
\sum_{j=1}^{n}x_{ij}=2\quad\text{for every }i
\]
and
\[
\sum_{i=1}^{n}x_{ij}=2\quad\text{for every }j.
\]
Consequently every minimum function uses only labels \(0,1,2\).

If \(M_n\) denotes the number of minimum functions, then
\[
M_n
=
n!\sum_{\pi\in S_n}2^{-c_{\ge2}(\pi)}
=
(n!)^2[z^n]\frac{e^{z/2}}{\sqrt{1-z}},
\]
where \(c_{\ge2}(\pi)\) is the number of cycles of the permutation \(\pi\) having length at least \(2\). Equivalently,
\[
M_n
=
(n!)^2
\sum_{j=0}^{n}
\frac{1}{2^j j!}
\frac{\binom{2(n-j)}{n-j}}{4^{\,n-j}}.
\]
For example,
\[
M_3=21,\qquad M_4=282,\qquad M_5=6210.
\]

## Assumptions and scope
All graphs are finite, simple, and undirected.

The perfect double Italian domination convention is that of Hao, Jalilolghadr, and Mojdeh: a function
\[
f:V(G)\to\{0,1,2,3\}
\]
is perfect double Italian when every vertex \(v\) with
\[
f(v)\in\{0,1\}
\]
satisfies
\[
3\le \sum_{u\in N[v]} f(u)\le4.
\]
Its weight is
\[
\omega(f)=\sum_{v\in V(G)}f(v),
\]
and \(\gamma_{dI}^{p}(G)\) is the minimum possible weight.

For \(R_n\), let
\[
r_i=\sum_{j=1}^{n}x_{ij},
\qquad
c_j=\sum_{i=1}^{n}x_{ij},
\qquad
W=\sum_{i,j}x_{ij}.
\]
Because the closed neighborhood of \(v_{ij}\) is its row together with its column, intersecting only at \(v_{ij}\),
\[
\sum_{u\in N[v_{ij}]}f(u)=r_i+c_j-x_{ij}.
\tag{1}
\]

The theorem is stated for \(n\ge3\). The boundary \(n=2\) is the cycle \(C_4\) and belongs to the standard-cycle regime already treated in the foundational literature.

## Proof
We first prove
\[
W\ge2n.
\]

Suppose instead that
\[
W<2n.
\]
Since the row sums add to \(W\), some row has
\[
r_i\le1.
\]
Since the column sums also add to \(W\), some column has
\[
c_j\le1.
\]
At their intersection,
\[
x_{ij}\le \min\{r_i,c_j\}\le1,
\]
so the perfect double Italian condition applies. By (1),
\[
\sum_{u\in N[v_{ij}]}f(u)
=
r_i+c_j-x_{ij}
\le2,
\]
contradicting the required lower bound \(3\). Therefore
\[
\gamma_{dI}^{p}(R_n)\ge2n.
\tag{2}
\]

For the matching upper bound, choose any permutation
\[
\pi\in S_n
\]
and set
\[
x_{i,\pi(i)}=2
\]
for every \(i\), with every other entry \(0\). Every row and every column then has sum \(2\). A zero entry has closed-neighborhood sum \(4\), while a label-\(2\) vertex is unconstrained. Hence this is a perfect double Italian function of weight \(2n\). Together with (2),
\[
\gamma_{dI}^{p}(R_n)=2n.
\tag{3}
\]

Now let \(f\) be minimum, so \(W=2n\). We show every row has sum exactly \(2\). If some row had
\[
r_i=0,
\]
then every entry in that row would be zero. Equation (1) and the lower perfect condition would force
\[
c_j\ge3
\]
for every column \(j\), and therefore
\[
W=\sum_j c_j\ge3n,
\]
contradicting \(W=2n\).

If instead some row had
\[
r_i=1,
\]
then that row contains exactly one label \(1\), say in column \(j_0\), and all its other entries are zero. For every \(j\ne j_0\), equation (1) at the zero entry gives
\[
1+c_j\ge3,
\]
so
\[
c_j\ge2.
\]
At the unique label-\(1\) entry,
\[
1+c_{j_0}-1=c_{j_0}\ge3.
\]
Thus
\[
W=\sum_j c_j\ge2(n-1)+3=2n+1,
\]
again a contradiction.

Hence every row has sum at least \(2\). Since their total is exactly \(2n\),
\[
r_i=2
\]
for every \(i\). By the symmetric argument,
\[
c_j=2
\]
for every \(j\).

Conversely, suppose every row sum and every column sum is \(2\). Then every entry is at most \(2\). If
\[
x_{ij}=0,
\]
equation (1) gives closed-neighborhood sum \(4\). If
\[
x_{ij}=1,
\]
it gives closed-neighborhood sum \(3\). Entries labeled \(2\) are unconstrained. Thus every such matrix is a perfect double Italian function of weight \(2n\). This proves the complete equality classification.

It remains to count the minimum functions. A nonnegative integer matrix with every row and column sum \(2\) is the biadjacency matrix of a \(2\)-regular bipartite multigraph on two labeled \(n\)-vertex parts. Every such multigraph decomposes into two perfect matchings, so its matrix can be written
\[
X=P+Q
\]
for permutation matrices \(P,Q\).

For an ordered pair \((P,Q)\), let
\[
\pi=P^{-1}Q.
\]
A fixed point of \(\pi\) corresponds to a doubled matching edge. Every cycle of \(\pi\) of length at least \(2\) corresponds to a nontrivial even cycle component of the bipartite multigraph and has exactly two alternating decompositions into the two perfect matchings. Hence a matrix arising from \((P,Q)\) is counted
\[
2^{c_{\ge2}(\pi)}
\]
times among ordered matching decompositions. Therefore
\[
M_n
=
n!\sum_{\pi\in S_n}2^{-c_{\ge2}(\pi)}.
\tag{4}
\]

The weighted permutation exponential generating function is
\[
\exp\left(
z+\frac12\sum_{\ell\ge2}\frac{z^\ell}{\ell}
\right)
=
\frac{e^{z/2}}{\sqrt{1-z}}.
\]
Taking the coefficient of \(z^n\) in (4) gives
\[
M_n
=
(n!)^2[z^n]\frac{e^{z/2}}{\sqrt{1-z}},
\]
and expansion of the two factors gives the displayed finite sum.

## Verification
The included verifier evaluates the defining closed-neighborhood inequality directly.

For
\[
n=2,3,4,
\]
it exhausts every labeling of total weight at most \(2n\), with labels in \(\{0,1,2,3\}\). It finds no feasible function below weight \(2n\), and every feasible function of weight \(2n\) has all row sums and all column sums equal to \(2\). The resulting minimum-function counts are
\[
3,\quad21,\quad282,
\]
matching the coefficient formula.

The verifier also evaluates the coefficient formula exactly, using rational arithmetic, through \(n=10\). The first ten counts are
\[
1,3,21,282,6210,202410,9135630,545007960,41514583320,3930730108200.
\]
The finite computation corroborates the theorem; the arbitrary-\(n\) result follows from the row-column proof.

## Relationship to prior work
Hao, Jalilolghadr, and Mojdeh introduced perfect double Italian domination in the convention used here. Their paper was published online on 21 June 2023, lists Mathematics Subject Classification 05C69, gives the closed-neighborhood interval definition above, studies standard families and extremal values, and proves NP-completeness even on bipartite graphs. Targeted inspection of its searchable full text found no occurrence of “rook,” “Hamming,” “Cartesian,” “line graph,” “product,” or “complete bipartite,” and targeted searches under the equivalent descriptions
\[
K_n\square K_n,\qquad H(2,n),\qquad L(K_{n,n})
\]
did not locate an exact square-rook theorem.

A 2024 paper uses the name “perfect Roman \(\{3\}\)-domination” for a stricter condition: a label-\(0\) vertex must have open-neighborhood weight exactly \(3\), and a label-\(1\) vertex open-neighborhood weight exactly \(2\). That condition is not equivalent to the 2023 perfect double Italian interval condition. In particular, the minimum functions classified here can have zero vertices with closed-neighborhood weight \(4\), so the 2024 exact-sum parameter does not imply this theorem. Its inspected text also contains no rook, Hamming, or line-graph specialization.

The nearest internal comparisons concern different invariants on complete multipartite or chain graphs, or ordinary Roman-type domination on complete prisms. None specializes to the perfect double Italian row-column constraints of \(K_n\square K_n\).

## Limitations
The theorem concerns the 2023 perfect double Italian interval convention and should not be conflated with the stricter 2024 exact-sum “perfect Roman \(\{3\}\)” convention.

The boundary \(R_2=C_4\) is excluded from the originality claim because the foundational source already treats cycles.

No claim is made for rectangular rook graphs
\[
K_m\square K_n
\]
with \(m\ne n\), higher-dimensional Hamming graphs, or nonminimum perfect double Italian functions.

The literature comparison cannot rule out a differently phrased or non-indexed treatment under another line-graph or coding-theoretic name.

## References
1. G. Hao, P. Jalilolghadr, D. A. Mojdeh, “Perfect double Italian domination of a graph,” AKCE International Journal of Graphs and Combinatorics 20(3) (2023), 247–257, DOI 10.1080/09728600.2023.2218457; published online 21 June 2023.
2. A. Almulhim, “Perfect Roman \(\{3\}\)-Domination in Graphs: Complexity and Bound of Perfect Roman \(\{3\}\)-Domination Number of Trees,” Journal of Mathematics (2024), article 1900923, DOI 10.1155/jom/1900923; version of record online 24 December 2024.
