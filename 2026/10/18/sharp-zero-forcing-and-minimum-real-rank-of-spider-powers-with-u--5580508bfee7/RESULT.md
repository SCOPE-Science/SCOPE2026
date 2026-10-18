# Sharp zero forcing and minimum real rank of spider powers with unequal arms

## Finding

**Theorem.** Let \(m\ge2\) and \(k\ge1\) be integers. Let \(T=T(\ell_1,\ldots,\ell_m)\) be the tree formed by attaching \(m\) internally disjoint paths of lengths \(\ell_i\) to one common hub, with every \(\ell_i\ge k+1\). Then the ordinary \(k\)-th graph power satisfies

\[
Z(T^k)=M_{\mathbb R}(T^k)=(m-1)k,
\qquad
\operatorname{mr}_{\mathbb R}(T^k)=1+\sum_{i=1}^m\ell_i-(m-1)k.
\]

Here \(Z\) is the ordinary zero forcing number, \(M_{\mathbb R}\) is the maximum nullity of a real symmetric matrix with off-diagonal nonzero pattern exactly the graph, and \(\operatorname{mr}_{\mathbb R}\) is the corresponding minimum rank. In fact, the minimum rank is attained by an explicit **entrywise nonnegative integer symmetric matrix**. The unequal-arm theorem includes the equal-arm identity proposed as Conjecture 10 of Abiad–Flagg–Ghasemi Nezhad–Zeijlemaker (2026). The substantive previously unresolved regime is \(m\ge3\), \(k\ge3\); the path, ordinary-tree, and square-of-tree boundaries are acknowledged below.

## Assumptions and scope

All graphs are finite, undirected and simple. Write \(c\) for the hub and \(v_{i,j}\) for the vertex at distance \(j\) along arm \(i\), for \(1\le i\le m\) and \(1\le j\le\ell_i\). The vertex set has \(N=1+\sum_i\ell_i\) vertices. Two distinct vertices are adjacent in \(T^k\) exactly when their distance in \(T\) is at most \(k\). Thus a hub-to-arm edge occurs exactly at depth \(j\le k\), a within-arm edge exactly when \(0<|a-b|\le k\), and a between-arm edge exactly when \(a+b\le k\).

A set \(S\) of initially black vertices is zero forcing when repeated steps of the rule “a black vertex with precisely one white neighbour makes that neighbour black” turn all vertices black. If \(\mathcal S_{\mathbb R}(G)\) denotes real symmetric matrices whose nonzero off-diagonal positions are exactly edges of \(G\), define \(M_{\mathbb R}(G)=\max_{A\in\mathcal S_{\mathbb R}(G)}\dim\ker A\) and \(\operatorname{mr}_{\mathbb R}(G)=|V(G)|-M_{\mathbb R}(G)\). No assertion is made for arms shorter than \(k+1\), for nonsymmetric matrix classes, or for positive semidefinite minimum rank.

## Proof

**1. A forcing set of size \((m-1)k\).** Initially blacken the last \(k\) vertices on each arm \(i<m\), leaving the hub and last arm white. Complete each blackened arm in turn, using the moves

\[
v_{i,t+k}\longrightarrow v_{i,t}\qquad
(t=\ell_i-k,\ell_i-k-1,\ldots,1).
\]

The forcing vertex has depth \(t+k>k\), so it sees neither the hub nor a different arm; among vertices in its own distance-\(k\) neighbourhood, only \(v_{i,t}\) remains white. All of the first \(m-1\) arms become black. Now perform

\[
v_{1,k}\to c,\quad
v_{1,k-j}\to v_{m,j}\ (j=1,\ldots,k-1),\quad
c\to v_{m,k},\quad
v_{m,t-k}\to v_{m,t}\ (t=k+1,\ldots,\ell_m).
\]

Each force has exactly one white neighbour: the first vertex has no neighbour in the untouched arm and sees the hub; the next vertices see successively one new vertex at depth \(j\) of the last arm; the hub then sees only its depth-\(k\) vertex; and each subsequent last-arm force sees only the next outward vertex, all other arms being black. Empty index ranges are omitted. This argument does not require equal arm lengths. Hence \(Z(T^k)\le(m-1)k\).

**2. A real symmetric matrix of nullity at least \((m-1)k\).** For each arm \(i\), let \(C_i\) be the \((\ell_i-k)\)-by-\(\ell_i\) matrix whose row \(t\) has ones in the consecutive columns \(t,t+1,\ldots,t+k\), and zeroes elsewhere. Set \(D_i=C_i^{\mathsf T}C_i\), and let \(D=\operatorname{diag}(D_1,\ldots,D_m)\). Every pair of different arm positions at distance at most \(k\) lies in some one of these windows. For distinct positions \(a\ne b\), the entry \((D_i)_{ab}\) is positive if and only if \(0<|a-b|\le k\); all other off-diagonal entries vanish.

Let \(E_i:\mathbb R^{\ell_i}\to\mathbb R^k\) extract the first \(k\) coordinates. Define \(U:\bigoplus_i\mathbb R^{\ell_i}\to\mathbb R^k\) by \(U(x_1,\ldots,x_m)=\sum_iE_ix_i\). Define the \(k\)-by-\(k\) symmetric matrix \(B\) by \(B_{ab}=1\) if \(a+b\le k\), and \(B_{ab}=0\) otherwise, and let \(h=(1,\ldots,1)^{\mathsf T}\in\mathbb R^k\). Order all vertices with the hub first and construct

\[
A=\begin{pmatrix}
0 & h^{\mathsf T}U\\
U^{\mathsf T}h & D+U^{\mathsf T}BU
\end{pmatrix}.
\]

The hub–arm blocks have entry one at exactly depths \(1,\ldots,k\). Off-diagonal blocks between different arms have entry one precisely at pairs of depths summing to at most \(k\). The diagonal block on arm \(i\) equals \(D_i+E_i^{\mathsf T}BE_i\); its off-diagonal entries are strictly positive precisely for \(0<|a-b|\le k\). Thus \(A\in\mathcal S_{\mathbb R}(T^k)\); it is a symmetric matrix with nonnegative integer entries.

The first \(\ell_i-k\) columns of \(C_i\) form an upper triangular square matrix with diagonal entries one, so \(C_i\) has full row rank and \(\dim\ker C_i=k\). More explicitly, the equation for the successive row sums determines every coordinate after the first \(k\) uniquely, so the map \(E_i:\ker C_i\to\mathbb R^k\) is an isomorphism. Consequently

\[
\mathcal K=\{(x_1,\ldots,x_m):C_ix_i=0\ \text{for all }i,\ \sum_iE_ix_i=0\}
\]

has dimension \(mk-k=(m-1)k\): there are \(mk\) freely chosen initial coordinates and exactly \(k\) independent linear sum constraints. For every \(x\in\mathcal K\), the vector \((0,x)\) lies in \(\ker A\), because \(D_ix_i=C_i^{\mathsf T}C_ix_i=0\) and \(Ux=0\) make both block rows vanish. Hence \(M_{\mathbb R}(T^k)\ge\dim\ker A\ge(m-1)k\).

**3. Matching the bounds.** For every graph \(G\), \(M_{\mathbb R}(G)\le Z(G)\): if \(S\) is zero forcing and a null vector of \(A\in\mathcal S_{\mathbb R}(G)\) vanishes on \(S\), the row corresponding to any valid force \(u\to v\) has only the term \(A_{uv}x_v\) potentially nonzero, since \(u\) and all its other neighbours already have zero coordinates; as \(A_{uv}\ne0\), it follows that \(x_v=0\). By induction the entire vector is zero, so restriction of \(\ker A\) to \(S\) is injective. Thus \(\dim\ker A\le|S|\) for every \(A\). Combining this inequality with Steps 1 and 2 yields

\[
(m-1)k\le M_{\mathbb R}(T^k)\le Z(T^k)\le(m-1)k,
\]

proving both identities and the minimum-rank formula.

## Verification

The standalone Python 3 file `verify_spider_powers.py` independently forms each tree, obtains its power by breadth-first neighbourhood exploration, forms the integer matrix from its sliding windows, and checks the exact off-diagonal support. It constructs \((m-1)k\) explicit independent integer kernel vectors, checks each matrix product exactly, computes rational matrix rank without floating point, and verifies every move of the claimed forcing schedule against the current white neighbourhood. It tests 53 instances including unequal-arm cases with \(2\le m\le5\) and \(1\le k\le4\), and separately checks 10,981 subminimal seeds by directly running the zero forcing closure. Its observed output is reproduced in `verification_output.txt`. These finite tests corroborate, but do not substitute for, the universal argument above.

For instance, with three arms of lengths \((4,5,6)\) and \(k=3\), the graph has 16 vertices and the theorem gives \(Z=M_{\mathbb R}=6\) and \(\operatorname{mr}_{\mathbb R}=10\).

## Relationship to prior work

Abiad, Flagg, Ghasemi Nezhad and Zeijlemaker, *The Zero Forcing Number of Graph Powers* (first posted 2026-10-02, arXiv:2610.03892, version updated 2026-10-06), Proposition 9, prove the upper bound \(Z(S_m(\ell)^k)\le(m-1)k\) for equal arms, and state equality as Conjecture 10. The equality for all such arms is resolved here by a new explicit matrix nullity lower bound; the forcing upper bound is also given directly for arbitrary lengths. Their article's spectral bounds do not themselves establish the spider lower bound. The minimum-rank consequence has the same scope as this nullity equality.

DeAlba, Grout, Kim, Kirkland, McDonald and Yielding (2012) determine the minimum rank of powers of **paths** and investigate strict powers of trees. Chang and Lin, *Minimum Rank of Powers of Cycles and Trees* (author-hosted PDF, Theorem 4.1), determine maximum nullity of the **square** of an arbitrary tree. Ordinary tree zero forcing at \(k=1\) is classical. Accordingly, the claimed novel mathematical region is the higher-power spider case \(m\ge3\), \(k\ge3\), including unequal arms; the formula for the previously solved boundaries is not represented as a separate contribution. Published indexed work on minimal zero forcing sets of unpowered spiders and on power domination polynomials of spiders concerns different operations or parameters and does not imply this graph-power nullity equality.

## Limitations

The minimum arm-length assumption \(\ell_i\ge k+1\) is essential to the supplied proof; shorter arms require separate analysis and are not covered. No result is asserted for all trees, for graph-power grids, or for positive semidefinite minimum rank. Computational runs are finite checks; the infinite theorem relies on the algebraic construction and explicit forcing schedule. Bibliographic searching cannot establish absolute priority or exclude unpublished/poorly indexed equivalences. Independent mathematical audit has not been performed.

## References

1. A. Abiad, M. Flagg, S. Ghasemi Nezhad and S. Zeijlemaker, *The Zero Forcing Number of Graph Powers*, arXiv:2610.03892 (first submitted 2026-10-02), Proposition 9 and Conjecture 10. https://arxiv.org/abs/2610.03892
2. L. M. DeAlba, J. Grout, I.-J. Kim, S. Kirkland, J. J. McDonald and A. Yielding, *Minimum rank of powers of trees*, Electronic Journal of Linear Algebra **23** (2012), 151–163. https://doi.org/10.13001/1081-3810.1511
3. G. J. Chang and J. C.-H. Lin, *Minimum rank of powers of cycles and trees*, Theorem 4.1, author-hosted full text: https://www-math.nsysu.edu.tw/~chlin/Publications/Articles/GJpower.pdf
