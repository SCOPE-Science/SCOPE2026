# Projective geometry and clique spectra of rank-one nilpotent commuting graphs

## Finding
Let \(K=\mathbb F_q\) be any finite field, \(n\ge 2\), and let \(\Gamma_{n,q}\) be the simple graph on all nonzero rank-one matrices \(A\in M_n(K)\) satisfying \(A^2=0\), with distinct matrices adjacent exactly when they commute. All maximal cliques, the entire clique polynomial, the degree, and the diameter are determined as follows.

For each proper nonzero subspace \(0<U<K^n\), define
\[
\mathcal X_U=\{A\ne0: \operatorname{rank} A=1,\ \operatorname{im}A\subseteq U\subseteq\ker A\}.
\]
**Every maximal clique is exactly one \(\mathcal X_U\), and different subspaces give different maximal cliques.** If \(r=\dim U\), then
\[
|\mathcal X_U|=\frac{(q^r-1)(q^{n-r}-1)}{q-1},\qquad
\#\{\mathcal X_U:\dim U=r\}=\begin{bmatrix}n\\r\end{bmatrix}_q.
\]
In particular, the total number of maximal cliques is \(\sum_{r=1}^{n-1}\begin{bmatrix}n\\r\end{bmatrix}_q\), and the clique number is attained precisely for \(r=\lfloor n/2\rfloor\) or \(r=\lceil n/2\rceil\), where identical dimensions are counted once.

Define for \(k\ge1\)
\[
T_k=\sum_{r=1}^{n-1}\begin{bmatrix}n\\r\end{bmatrix}_q
 \sum_{j=0}^{r}(-1)^{r-j}q^{\binom{r-j}{2}}
 \begin{bmatrix}r\\j\end{bmatrix}_q
 \left(\frac{(q^j-1)(q^{n-r}-1)}{q-1}\right)^k,\qquad T_0=1.
\]
Then \(T_k\) counts all ordered, pairwise commuting \(k\)-tuples of vertices with repetitions permitted. The complete clique polynomial \(C_{n,q}(z)=\sum_{k\ge0}c_kz^k\) is determined by \(c_0=1\) and, for \(k\ge1\),
\[
c_k=\frac1{k!}\sum_{j=1}^k s(k,j)T_j,
\]
where \(s(k,j)\) is the **signed** Stirling number of the first kind; \(c_k=0\) for \(k>\omega(\Gamma_{n,q})\).

The graph has \(\frac{(q^n-1)(q^{n-1}-1)}{q-1}\) vertices and is regular of degree
\[
q^{n-1}-2+\left(\begin{bmatrix}n-1\\1\end{bmatrix}_q-1\right)(q^{n-2}-1).
\]
Its connectedness and diameter have a dimension trichotomy: for \(n=2\), it is a disjoint union of \(q+1\) copies of \(K_{q-1}\); for \(n=3\), it is the \(K_{q-1}\)-clique blow-up of the line graph of the point-line incidence graph of \(\mathrm{PG}(2,q)\), hence has diameter \(3\); for every \(n\ge4\), it has diameter exactly \(2\).

## Assumptions and scope
The field order \(q\) ranges over all prime powers, including characteristic two. Matrices are full \(n\)-by-\(n\), not restricted to an upper-triangular coordinate algebra, and vertices exclude the zero matrix. Adjacency is equality \(AB=BA\), not merely simultaneous triangularizability or existence of commuting conjugates. The Gaussian coefficient \(\begin{bmatrix}a\\b\end{bmatrix}_q\) counts \(b\)-subspaces of \(K^a\). All counts concern actual labeled matrices, not similarity classes. A clique is a set of distinct vertices. Repeated vertices are allowed only in the auxiliary tuple counts \(T_k\).

## Proof
**1. The zero-product lemma.** Any vertex is an outer product \(A=u\varphi\), where \(u\in K^n\setminus\{0\}\), \(\varphi\in(K^n)^*\setminus\{0\}\), and \(\varphi(u)=0\); two presentations define the same matrix precisely by the simultaneous reciprocal scalar change. For two vertices \(A=u\varphi\) and \(B=v\psi\), their products are \(AB=\varphi(v)u\psi\) and \(BA=\psi(u)v\varphi\). If \(\langle u\rangle\ne\langle v\rangle\), these products have different image lines whenever nonzero, so equality forces both products to vanish. If the image lines agree, each covector annihilates that line, and both products vanish automatically. Thus **commutation is equivalent to \(AB=BA=0\)** for all such pairs.

**2. Exhaustive and unique maximal-clique classification.** For any nonempty family \(S\) of mutually commuting vertices, put \(U=\sum_{A\in S}\operatorname{im}A\). Because all ordered products vanish, \(U\subseteq\bigcap_{A\in S}\ker A\), so \(S\subseteq\mathcal X_U\). The subspace \(U\) is nonzero and proper. Conversely, the defining inclusions make any two elements of \(\mathcal X_U\) mutually annihilate. Moreover, \(\sum_{A\in\mathcal X_U}\operatorname{im}A=U\): for each nonzero \(u\in U\), choose a nonzero functional annihilating \(U\). Similarly, \(\bigcap_{A\in\mathcal X_U}\ker A=U\): all nonzero functionals annihilating \(U\) occur in these outer products. If a vertex \(B\) commutes with every element of \(\mathcal X_U\), zero-products give \(\operatorname{im}B\subseteq U\subseteq\ker B\), hence \(B\in\mathcal X_U\). Thus \(\mathcal X_U\) is maximal. Every maximal clique equals its containing \(\mathcal X_U\), and \(U\) is recovered from its images. Counting nonzero outer products with \(u\in U\) and \(\varphi\in U^\perp\) gives the displayed cardinalities; maximizing their product minimizes \(q^r+q^{n-r}\).

**3. All commuting tuples and clique polynomial.** For an ordered commuting \(k\)-tuple, the sum \(U\) of its images is uniquely determined, with \(1\le\dim U\le n-1\); all its covectors annihilate \(U\). Fix \(U\) of dimension \(r\). For any \(W\le U\) of dimension \(j\), exactly \(a(j,r)=\frac{(q^j-1)(q^{n-r}-1)}{q-1}\) nonzero rank-one operators have image in \(W\) and kill \(U\). Their ordered \(k\)-tuples number \(a(j,r)^k\). Möbius inversion on the lattice of subspaces of \(U\), whose interval Möbius function is \((-1)^dq^{\binom d2}\) in codimension \(d\), forces the span of all images to be **exactly** \(U\). Sum over \(\begin{bmatrix}n\\r\end{bmatrix}_q\) choices of \(U\). This proves \(T_k\). A tuple with precisely \(j\) distinct entries corresponds to choosing a \(j\)-vertex clique and an onto map from \(\{1,\ldots,k\}\) to its vertices, giving \(T_k=\sum_{j=1}^k j!S(k,j)c_j\). The displayed signed Stirling inversion therefore determines all \(c_j\). Because the graph is finite, this is a polynomial, not just a formal infinite series.

**4. Vertex number and degree.** Choose image line \(L\), in \(\begin{bmatrix}n\\1\end{bmatrix}_q\) ways, then one of \(q^{n-1}-1\) nonzero functionals annihilating it, fixing a generator of \(L\). For a fixed vertex with image \(L\) and kernel \(H\), its commuting partners sharing image \(L\) number \(q^{n-1}-1\), including itself. Each other image line \(M\subseteq H\), of which there are \(\begin{bmatrix}n-1\\1\end{bmatrix}_q-1\), supports exactly \(q^{n-2}-1\) partners killing both \(L\) and \(M\). Subtract the vertex itself to get the stated degree.

**5. Diameters.** For \(n=2\), a square-zero rank-one operator has identical image and kernel line, and zero-products occur precisely when lines agree. For \(n=3\), a vertex corresponds to a flag \(L\subset H\), a point lying on a line of the projective plane, together with one of \(q-1\) nonzero scalar copies. Two different flags commute precisely when they share their point or their line; this is the indicated clique blow-up of a line graph. Every two projective-plane incidence edges are joined by at most three steps in its line graph: if their lines meet at \(R\), the intermediate flags \((R,H)\) and \((R,H')\) make a three-edge route. Choose two flags \((P,H)\), \((Q,H')\) with \(P\notin H'\) and \(Q\notin H\) to rule out a path of length at most two. Hence diameter \(3\).

For \(n\ge4\), given any two vertices \(A,B\), select \(0\ne w\in\ker A\cap\ker B\); this exists because the intersection has dimension at least \(n-2\). The space spanned by \(\operatorname{im}A\), \(\operatorname{im}B\), and \(w\) has dimension at most three, so choose a nonzero covector \(\eta\) annihilating that span. Then \(C=w\eta\ne0\) has rank one, squares to zero, and both products in each pair \((A,C)\), \((B,C)\) vanish. Noncommuting vertices, for instance \(E_{12}\) and \(E_{23}\), exist, so diameter is exactly \(2\).

## Verification
A standalone standard-library Python 3 program, `verify_rankone_nilpotent.py`, enumerates all nonzero rank-one square-zero matrices directly over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\) (including an explicit quadratic model of the last), multiplies matrices independently to determine graph edges, computes degrees, tuple counts through arity three, maximal cliques via a pivoted backtracking search, connected components, and diameters. It compares the observed outputs with the formulas; output `VERIFY_OK`. Tested parameters: \((n,q)=(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2)\). In particular, for \((n,q)=(4,2)\), there are \(105\) vertices, \(30\) maximal cliques of size \(7\), \(35\) of size \(9\), and diameter \(2\). Finite tests are corroboration, not the proof for arbitrary dimensions or fields.

## Relationship to prior work
Ou and Zhong (2016) study automorphisms of a commuting graph for the **upper triangular rank-one** matrix set; their object includes nondiagonalizable and semisimple forms under a fixed flag, rather than the full conjugacy-invariant nonzero square-zero rank-one locus. Their main automorphism classification does not state the all-arity clique enumeration here. Britnell and Wildon (2010) study whether similarity classes contain some commuting representatives, notably nilpotent partition types. Existence between classes is weaker than the exact matrix-level induced graph and maximal-family census. Ginsburg, Julius and Velasquez (2020) classify certain linear maps preserving Lie products equal to a fixed nonzero rank-one nilpotent, not the zero-Lie-product relation restricted to that nilpotent orbit. These distinct questions motivate checking the fine projective geometry of mutual annihilation; standard rank-one factorization and subspace-lattice Möbius inversion are not represented as new principles.

## Limitations
The graph deliberately excludes higher-rank square-zero matrices, other nilpotent partitions, and zero. The graph is on actual matrices, not projectivized similarity classes. The result does not classify graph automorphisms or independence numbers. Despite directed searches in published research records and relevant primary papers, equivalent coverage under terms such as zero-product graphs, matrix annihilation graphs, or projective flag geometry cannot be excluded; exhaustive publication priority and independent audit are not claimed.

## References
1. S. Ou and J. Zhong, *Automorphisms of a commuting graph of rank one upper triangular matrices*, Electronic Journal of Linear Algebra **31** (2016), 774–793, DOI: 10.13001/1081-3810.3064.
2. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811 (2010); Journal of the London Mathematical Society, DOI: 10.1112/jlms/jdq088.
3. V. Ginsburg, H. Julius and R. Velasquez, *On maps preserving Lie products equal to a rank-one nilpotent*, Linear Algebra and its Applications **593** (2020), 212–227, DOI: 10.1016/j.laa.2020.02.007 (first online 2020-02-07).
