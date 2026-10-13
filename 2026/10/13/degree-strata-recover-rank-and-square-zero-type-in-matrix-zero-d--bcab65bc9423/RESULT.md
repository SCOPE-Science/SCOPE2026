# Degree strata recover rank and square-zero type in matrix zero-divisor graphs

## Finding

Let \(q\) be a prime power and \(n\ge3\). Let \(G_{n,q}\) be the underlying simple graph of the standard directed zero-divisor graph of \(M_n(\mathbb F_q)\): the vertices are the nonzero singular matrices, and distinct matrices \(A,B\) are adjacent exactly when \(AB=0\) or \(BA=0\).

If \(A\) has rank \(r\), define \(\varepsilon(A)=1\) when \(A^2=0\) and \(\varepsilon(A)=0\) otherwise. Then
\[
\deg_{G_{n,q}}(A)=2q^{n(n-r)}-q^{(n-r)^2}-1-\varepsilon(A).
\tag{1}
\]
The degree determines both \(r\) and \(\varepsilon(A)\).

For the complete degree distribution, let
\[
R_{n,r}(q)=\frac{\prod_{i=0}^{r-1}(q^n-q^i)^2}{\prod_{i=0}^{r-1}(q^r-q^i)}
\tag{2}
\]
be the number of rank-\(r\) matrices. Let
\[
S_{n,r}(q)={n\brack r}_q{n-r\brack r}_q\,|GL_r(q)|
\tag{3}
\]
when \(2r\le n\), and put \(S_{n,r}(q)=0\) when \(2r>n\). If
\[
d_r=2q^{n(n-r)}-q^{(n-r)^2}-1,
\]
then degree \(d_r\) has multiplicity \(R_{n,r}(q)-S_{n,r}(q)\), and degree \(d_r-1\) has multiplicity \(S_{n,r}(q)\). Thus every graph automorphism preserves matrix rank and the square-zero locus.

## Assumptions and scope

The graph is the underlying undirected simple graph obtained from the usual directed zero-divisor graph of the full matrix ring \(M_n(\mathbb F_q)\). The result is stated for \(n\ge3\); the same degree formula also holds in dimension two, but that case is excluded here because its image-kernel cell structure is already separately understood.

All matrices have entries in the finite field \(\mathbb F_q\), with \(q\) an arbitrary prime power. Since a nonzero matrix over a field is a zero-divisor exactly when it is singular, the vertex set is exactly the set of matrices of ranks \(1,\ldots,n-1\).

## Proof

Fix a vertex \(A\) of rank \(r\), acting on \(V=\mathbb F_q^n\). Consider the two linear subspaces of \(M_n(\mathbb F_q)\)
\[
L_A=\{B:AB=0\},\qquad R_A=\{B:BA=0\}.
\]
The condition \(AB=0\) says that every column of \(B\) lies in \(\ker A\), whose dimension is \(n-r\). Hence
\[
\dim L_A=n(n-r).
\tag{4}
\]
Similarly, \(BA=0\) says that \(B\) vanishes on \(\operatorname{im}A\), so \(B\) factors through \(V/\operatorname{im}A\), again giving
\[
\dim R_A=n(n-r).
\tag{5}
\]

For the intersection, both conditions hold exactly when \(B\) factors as a linear map
\[
V/\operatorname{im}A\longrightarrow \ker A.
\]
Therefore
\[
\dim(L_A\cap R_A)=(n-r)^2.
\tag{6}
\]
Every nonzero matrix in \(L_A\cup R_A\) is singular, because either its image is contained in the proper subspace \(\ker A\) or it has the nonzero subspace \(\operatorname{im}A\) in its kernel. Inclusion-exclusion gives
\[
|L_A\cup R_A|=2q^{n(n-r)}-q^{(n-r)^2}.
\tag{7}
\]
The zero matrix is not a vertex, so one element must always be removed. The matrix \(A\) itself lies in this union exactly when \(A^2=0\); in that case it must also be removed because the graph has no loops. Equation (1) follows.

It remains to show that degrees identify the two algebraic labels. For \(t=1,\ldots,n-1\), define
\[
f(t)=2q^{nt}-q^{t^2}-1.
\]
For \(1\le t\le n-2\),
\[
f(t+1)-f(t)=2q^{nt}(q^n-1)-q^{t^2}(q^{2t+1}-1).
\]
Since \(n-t\ge2\), after dividing by \(q^{t^2}\) the first term is at least \(2q^{2t}(q^n-1)\), which exceeds \(q^{2t+1}-1\). In fact the difference is greater than one. Thus the pairs \(\{f(t),f(t)-1\}\) for different \(t\) are disjoint. Since \(t=n-r\), the degree determines \(r\), and within a fixed rank the one-unit decrement determines whether \(A^2=0\).

Formula (2) is the standard count of rank-\(r\) endomorphisms. To count the square-zero rank-\(r\) matrices, write \(U=\operatorname{im}A\) and \(K=\ker A\). The condition \(A^2=0\) is equivalent to \(U\subseteq K\). Such a matrix exists only when \(2r\le n\). Choose \(K\) of dimension \(n-r\), then choose \(U\subseteq K\) of dimension \(r\), and finally choose the induced isomorphism \(V/K\to U\). This gives exactly
\[
{n\brack r}_q{n-r\brack r}_q\,|GL_r(q)|,
\]
which is (3). Subtracting these matrices from the total rank count yields the stated multiplicities.

## Verification

The accompanying `verify.py` directly constructs the graph for \(M_3(\mathbb F_2)\), checks every vertex degree by matrix multiplication, and confirms all rank/square-zero strata. It also checks representative vertices over \(\mathbb F_3\), validates the rank and square-zero counting formulas for a range of small parameters, and verifies that the proposed degree strata are pairwise disjoint.

The finite computations corroborate the formulas but do not replace the arbitrary-prime-power proof from the annihilator subspaces (4)--(7) and the flag count for square-zero matrices.

## Relationship to prior work

Božić and Petrović introduced the matrix-ring zero-divisor graph framework used here and study connectivity and diameter for matrix rings; the paper is classified primarily under \(16S50\). Later work on matrix zero-divisor graphs develops structural, domination, automorphism, and compressed-graph questions.

A dedicated 2023 paper studies the adjacency spectrum of exactly the two-by-two finite-field graph. It classifies scalar equivalence cells and obtains bounds for the remaining quotient eigenvalues rather than an all-dimension degree-stratification theorem. The present result concerns a different invariant and, for \(n\ge3\), a different dimensional regime.

A separately checked prior result on this graph determines zero forcing only for \(M_2(\mathbb F_q)\). Its complete two-dimensional image-kernel structure covers dimension two, which is why the theorem here is explicitly stated for \(n\ge3\). No implication from that result determines the all-rank degree strata in higher dimensions.

## Limitations

The result is for full matrix rings over finite fields and for the underlying simple graph. It does not determine the complete automorphism group, spectrum, or isomorphism classification for \(n\ge3\).

Although degree recovers rank and square-zero status inside a fixed graph \(G_{n,q}\), no claim is made here that the degree multiset alone reconstructs \(n\) and \(q\) among all matrix-ring graphs.

## References

1. I. Božić and Z. Petrović, “Zero-Divisor Graphs of Matrices Over Commutative Rings,” *Communications in Algebra* 37 (2009), 1186–1192. DOI: 10.1080/00927870802465951.
2. K. Masalkar, A. Khairnar, A. Lande, and L. Kadam, “On spectrum of the zero-divisor graph of matrix ring,” arXiv:2312.09934 (2023).
3. A. R. Ashrafi and A. Tadayyonfar, “The Zero Divisor Graph of 2 × 2 Matrices Over a Field,” *Quaestiones Mathematicae* 39 (2016), 977–990. DOI: 10.2989/16073606.2016.1241958.
4. T. Tamizh Chelvam, “Graphs from matrices - a survey,” *AKCE International Journal of Graphs and Combinatorics* (2024). DOI: 10.1080/09728600.2024.2332780.
