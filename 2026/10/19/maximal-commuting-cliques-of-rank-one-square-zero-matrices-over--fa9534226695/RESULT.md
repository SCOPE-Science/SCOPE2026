# Maximal commuting cliques of rank-one square-zero matrices over finite fields

## Finding

Let \(n\ge3\), let \(q\) be any prime power, and put \(V=\mathbb F_q^n\). Define \(\mathcal N\) to be the set of nonzero rank-one endomorphisms \(A:V\to V\) satisfying \(A^2=0\), and let \(\Gamma\) be the simple graph on \(\mathcal N\), with distinct vertices adjacent if and only if they commute. For each nonzero proper subspace \(W<V\), define
\[
\mathcal C_W=\{A\in\mathcal N:\operatorname{im}A\subseteq W\subseteq\ker A\}.
\]

**Complete maximal-clique classification.** The sets \(\mathcal C_W\), for all \(0<W<V\), are exactly the maximal cliques of \(\Gamma\); distinct subspaces give distinct maximal cliques. For \(r=\dim W\),
\[
|\mathcal C_W|=[r]_q(q^{n-r}-1),\qquad [r]_q=\frac{q^r-1}{q-1}.
\]
There are precisely \({n\brack r}_q\) maximal cliques of that size indexed by \(r\)-subspaces (different dimensions may have the same size), where \({n\brack r}_q\) is the Gaussian binomial coefficient. Therefore
\[
\omega(\Gamma)=\frac{(q^{\lfloor n/2\rfloor}-1)(q^{\lceil n/2\rceil}-1)}{q-1}.
\]
Every vertex belongs to exactly \(\sum_{j=0}^{n-2}{n-2\brack j}_q\) maximal cliques.

**Complete clique-count polynomial.** Let \(c_k\) count unordered \(k\)-vertex cliques, for each integer \(k\ge1\), and let \((a)_{\underline k}=\prod_{i=0}^{k-1}(a-i)\). Then
\[
 c_k=\frac1{k!}\sum_{r=1}^{n-1}{n\brack r}_q
  \sum_{j=0}^r(-1)^{r-j}q^{\binom{r-j}{2}}{r\brack j}_q
  \bigl([j]_q(q^{n-r}-1)\bigr)_{\underline k}.
\]
This is a finite exact formula for every clique size; in particular \(c_k=0\) for \(k>\omega(\Gamma)\). It counts every clique just once, including those contained in several maximal cliques.

For \(n=4,q=2\), the graph has \(105\) vertices and \(65\) maximal cliques, with \(15\) of size \(7\), \(35\) of size \(9\), and \(15\) more of size \(7\). Its exact clique counts for sizes \(1\) through \(9\) are
\[
(105,1260,3780,5460,5040,3150,1290,315,35).
\]

## Assumptions and scope

The field is finite and may have characteristic two. The vertex set excludes the zero operator and excludes higher-rank square-zero operators. The edge condition is matrix commutation; the proof establishes that for rank-one square-zero vertices it is equivalent to mutual annihilation. A clique is a set of *distinct* vertices. Maximal means inclusion-maximal, whereas maximum means largest cardinality. There is no fixed choice of basis in the classification. The integer \(n\) is at least three; the elementary formulas also make sense in dimension two, but that boundary is not asserted as a separate novelty claim.

The full-matrix graph of all noncentral matrices, the graph of upper-triangular matrices, and the graph including higher-rank nilpotents are different objects.

## Proof

**1. Rank-one commutativity collapses to zero products.** Every \(A\in\mathcal N\) has a factorization \(A=u\varphi\), where \(u\in V\setminus\{0\}\), \(\varphi\in V^*\setminus\{0\}\), and \(\varphi(u)=0\). Similarly write \(B=v\psi\), with \(\psi(v)=0\). Their products are
\[
AB=\varphi(v)u\psi,\qquad BA=\psi(u)v\varphi.
\]
Suppose \(AB=BA\ne0\). Equality of these nonzero rank-one operators forces \(\langle u\rangle=\langle v\rangle\) and \(\langle\varphi\rangle=\langle\psi\rangle\), so \(B\) is a nonzero scalar multiple of \(A\). But then \(AB\) is a scalar multiple of \(A^2=0\), a contradiction. Thus \(AB=BA\) implies \(AB=BA=0\). Conversely, mutual annihilation implies commutation.

**2. Every clique lies in a canonical one.** If \(S\) is a nonempty clique, let \(W_S=\sum_{A\in S}\operatorname{im}A\). For any \(A,B\in S\), Step 1 gives \(BA=0\) (also when \(A=B\) since \(A^2=0\)). Hence \(W_S\subseteq\ker B\) for every \(B\in S\), and by definition \(\operatorname{im}B\subseteq W_S\). Thus \(S\subseteq\mathcal C_{W_S}\). Because \(S\) contains a nonzero matrix, \(W_S\ne0\); because every \(B\in S\) is nonzero and annihilates \(W_S\), we must have \(W_S\ne V\).

**3. Each canonical clique is maximal and its subspace is recoverable.** Fix \(0<W<V\). For any \(A,B\in\mathcal C_W\), both compositions are zero, so \(\mathcal C_W\) is a clique. Its images span all of \(W\): given any nonzero \(u\in W\), choose a nonzero functional \(\varphi\in(V/W)^*\) and set \(A=u\varphi\). Its kernel contains \(W\), and \(\operatorname{im}A=\langle u\rangle\). Thus \(W=\sum_{A\in\mathcal C_W}\operatorname{im}A\), so the assignment \(W\mapsto\mathcal C_W\) is injective.

If \(B=v\psi\in\mathcal N\) commutes with every member of \(\mathcal C_W\), Step 1 gives \(BA=AB=0\) for every \(A\in\mathcal C_W\). Since the images of all these \(A\) span \(W\), this forces \(\psi(W)=0\), or \(W\subseteq\ker B\). Moreover, choosing arbitrary \(u\in W\setminus\{0\}\) and \(\varphi\in W^\perp\setminus\{0\}\), the equation \((u\varphi)B=0\) yields \(\varphi(v)=0\). All functionals vanishing on \(W\) therefore annihilate \(v\), so \(v\in W\), i.e. \(\operatorname{im}B\subseteq W\). Hence \(B\in\mathcal C_W\), establishing maximality. Step 2 shows no other maximal cliques exist.

**4. Count the maximal cliques and their incidences.** Fix \(W\) of dimension \(r\). Its nonzero image lines number \([r]_q\). For each such line select a fixed nonzero generator \(u\). Every nonzero functional annihilating \(W\) gives a different rank-one operator \(u\varphi\), and their number is \(q^{n-r}-1\). This proves the size formula. There are \({n\brack r}_q\) choices of \(W\). Maximizing
\[
[r]_q(q^{n-r}-1)=\frac{q^n-q^r-q^{n-r}+1}{q-1}
\]
reduces to minimizing \(q^r+q^{n-r}\), attained precisely at the integer(s) nearest \(n/2\), yielding the maximum-clique formula. A vertex \(A\) is in \(\mathcal C_W\) exactly for intermediate subspaces \(\operatorname{im}A\subseteq W\subseteq\ker A\). Since \(\dim(\ker A/\operatorname{im}A)=n-2\), these are counted by \(\sum_{j=0}^{n-2}{n-2\brack j}_q\).

**5. Count every smaller clique without overcounting.** For an ordered tuple of \(k\ge1\) distinct mutually annihilating vertices, let \(W\) be the span of their images, uniquely determined by the tuple. At a fixed subspace \(W\) of dimension \(r\), first count tuples whose images lie in some \(U\le W\) but whose kernels contain \(W\). If \(\dim U=j\), there are exactly \([j]_q(q^{n-r}-1)\) available vertices, so the ordered distinct tuple count is its falling factorial of length \(k\). Apply Möbius inversion on the subspace lattice of \(W\), using
\[
\mu(U,W)=(-1)^{r-j}q^{\binom{r-j}{2}}.
\]
It yields the inner sum in the stated formula, the count with image-span *exactly* \(W\). Multiply by the number \({n\brack r}_q\) of such \(W\), sum over nonzero proper \(W\), and divide by \(k!\) for the ordering. Uniqueness of the image-span guarantees no double counting.

All steps apply to every prime power and all specified dimensions.

## Verification

The accompanying `checker.py` uses only the Python standard library. It enumerates all actual rank-one square-zero matrices, constructs adjacency using full matrix multiplication, independently finds inclusion-maximal cliques with Bron–Kerbosch search, and compares them to the subspace-indexed family. It also independently enumerates cliques of sizes up to four and checks their counts against the Möbius formula. Tested parameter pairs are \((n,q)=(2,2),(2,3),(3,2),(3,3),(4,2)\); the two-dimensional cases are boundary checks, not a separate novelty assertion.

The tests return `ALL_EXACT_CHECKS_PASSED`. In particular, at \((n,q)=(4,2)\) there are \(105\) vertices and \(65\) maximal cliques with maximum size \(9\); the first four clique counts are \(105,1260,3780,5460\). This finite computation corroborates but does not replace the general proof.

## Relationship to prior work

Cheraghpour, Ghosseiri, Jafari and Seyfpour (arXiv:2402.12619v1, first public 2024-02-20) determine clique structure for the full commuting graph of \(2\)-by-\(2\) upper-triangular rings. Their Theorem 2.11 treats that ring graph, not the graph on *all* rank-one square-zero matrices in arbitrary dimension. Ou and Zhong (doi:10.13001/1081-3810.3064) classify graph automorphisms for rank-one upper-triangular matrices, a different vertex restriction and goal. Britnell and Wildon (arXiv:1001.0811v1, Sections 1 and 4) study existence of commuting representatives of nilpotent similarity classes, rather than classifying all commuting rank-one square-zero cliques or the full size distribution of cliques. The present result is an exact all-clique enumeration for a distinct but naturally related graph.

## Limitations

The result is restricted to rank-one square-zero endomorphisms and does not classify cliques containing higher-rank nilpotents or arbitrary commuting matrices. Its originality has been compared with specific relevant accessible treatments, not exhaustively certified against all historical terminology; equivalent clique enumeration hidden in older matrix-semigroup or subspace-geometry literature remains possible. The finite tests cover prime fields only, while the general finite-field conclusion follows from the algebraic proof rather than extrapolation. Independent mathematical validation has not been performed.

## References

1. H. Cheraghpour, M. N. Ghosseiri, M. Jafari and F. Seyfpour, *On Commuting Graphs of Triangular Rings*, arXiv:2402.12619v1 (2024-02-20), especially Theorem 2.11. https://arxiv.org/pdf/2402.12619
2. S. Ou and J. Zhong, *Automorphisms of a Commuting Graph of Rank One Upper Triangular Matrices*, Electronic Journal of Linear Algebra 31 (2016), 774–793, doi:10.13001/1081-3810.3064. https://journals.uwyo.edu/index.php/ela/article/download/1729/1729/1729
3. J. R. Britnell and M. Wildon, *On Types and Classes of Commuting Matrices over Finite Fields*, arXiv:1001.0811v1 (2010), especially Section 4. https://arxiv.org/pdf/1001.0811
