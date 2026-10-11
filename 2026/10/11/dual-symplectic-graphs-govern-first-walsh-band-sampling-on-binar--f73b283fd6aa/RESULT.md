# Dual symplectic graphs govern first-Walsh-band sampling on binary quadrics

## Finding
Let \(m\ge1\), \(n=2m\), and \(Q:\mathbb F_2^n\to\mathbb F_2\) be a quadratic function with \(Q(0)=0\) and nonsingular polar form. Put \(X_Q=\{x:Q(x)=0\}\). Compress multiplication by \(\mathbf1_{X_Q}\), on the uniform probability space \(\mathbb F_2^n\), to the \((n+1)\)-dimensional Walsh band spanned by the constant character and all \(n\) coordinate characters. Call this self-adjoint operator \(K_Q\).

The complete spectrum of \(K_Q\) is the following graph-theoretic spectrum, with multiplicities:
\[
\operatorname{spec}(K_Q)=\left\{\frac12+\frac{\varepsilon}{2^{m+1}}\lambda:\lambda\in\operatorname{spec}(J_{n+1}-2\widetilde A)\right\}.
\]
Here \(\varepsilon\in\{-1,1\}\) is the normalized quadratic Gauss sign, \(A\) is the zero-diagonal symmetric binary matrix inverse to the polar matrix of \(Q\), \(\widetilde A=\operatorname{diag}(0,A)\), and \(J_{n+1}\) is the all-ones matrix. Binary entries of \(A\) are regarded as ordinary integer entries in this real symmetric matrix. Every simple graph with an odd number of perfect matchings can occur as \(A\), and each choice of \(\varepsilon\) is realizable with that graph.

The restriction is injective on this Walsh band for all \(m\ge2\) and for \(m=1,\varepsilon=1\). In the sole exceptional case \(m=1,\varepsilon=-1\), its rank is one. Thus every nonsingular binary quadric of dimension at least four is a uniqueness sampling set for all complex first-band Walsh polynomials, regardless of coordinate presentation.

The first nontrivial case \(m=2\) admits a full arithmetic spectral census: the 28 labelled four-vertex graphs with invertible binary adjacency matrix have exactly three characteristic polynomials \(\det(zI-(J_5-2\widetilde A))\), with counts as follows:
\[
\begin{array}{c|c|c}
\text{graph type}&\text{polynomial}&\text{number}\hline
2K_2\text{ or paw}&(z-2)^2(z+2)(z^2-3z-2)&15\\
P_4&(z-1)(z^2-2z-4)^2&12\\
K_4&(z-2)^4(z+3)&1
\end{array}
\]
The graph labels are conventional names for the disjoint union of two edges, the triangle with a pendant edge, the four-vertex path, and the complete four-vertex graph. Consequently each Gauss sign exhibits exactly three distinct first-band sampling spectra in dimension four, even though nondegenerate binary quadratics of a fixed Gauss sign are linearly equivalent.

For the important symplectic-pair presentation, where \(A\) is a perfect matching on \(2m\) vertices, the graph eigenvalues are explicitly \(2\) with multiplicity \(m\), \(-2\) with multiplicity \(m-1\), and
\[
\lambda_{\pm}=\frac{2m-1\pm\sqrt{(2m-1)^2+8}}2
\]
with multiplicity one each. Substitution into the spectrum formula gives the sharp sampling condition number on this entire infinite family.

## Assumptions and scope
Throughout, dot products and matrix inverses used for the quadratic and its polar form are over \(\mathbb F_2\). Spectra, characteristic polynomials, operator norms, and the displayed all-ones matrices are over \(\mathbb R\) or \(\mathbb C\). For \(\chi_u(x)=(-1)^{u\cdot x}\), the full Hilbert space has inner product \(\langle f,g\rangle=2^{-n}\sum_x f(x)\overline{g(x)}\), so the Walsh characters form an orthonormal basis. Set \(E=\{0,e_1,\ldots,e_n\}\), \(H_E=\operatorname{span}_{\mathbb C}\{\chi_u:u\in E\}\), and \(K_Q=P_{H_E}M_{\mathbf1_{X_Q}}P_{H_E}|_{H_E}\). Its eigenvalues are squared singular values of restriction to \(X_Q\) with the induced, unrenormalized ambient probability norm. A normalized conditional measure on \(X_Q\) would multiply all eigenvalues by \(2^n/|X_Q|\).

Define \(B(x,y)=Q(x+y)+Q(x)+Q(y)\) and let \(B\) also denote its invertible alternating matrix. Put \(A=B^{-1}\) over \(\mathbb F_2\), and define \(Q^*(u)=Q(Au)\). Define \(\varepsilon=2^{-m}\sum_x(-1)^{Q(x)}\), which is a sign by the nondegenerate Gauss identity. The diagonal sign matrix \(D\) has entries \(D_{uu}=(-1)^{Q^*(u)}\), for \(u\in E\) in the indicated order.

## Proof
**1. Quadratic Gauss identity.** For any \(h\in\mathbb F_2^n\), the derivative identity is \(Q(x+h)+Q(x)=B(x,h)+Q(h)\). Therefore
\[
\left(\sum_x(-1)^{Q(x)}\right)^2
=\sum_h(-1)^{Q(h)}\sum_x(-1)^{B(x,h)}=2^n.
\]
Nondegeneracy eliminates every \(h\ne0\), so the sum equals \(\varepsilon2^m\). Replacing \(x\) by \(x+Au\) gives, for every \(u\),
\[
2^{-n}\sum_x(-1)^{Q(x)+u\cdot x}=\varepsilon2^{-m}(-1)^{Q^*(u)}.
\]
Consequently \(|X_Q|=2^{n-1}+\varepsilon2^{m-1}\).

**2. Exact compression.** Since \(\mathbf1_{X_Q}=(1+(-1)^Q)/2\), character orthogonality gives
\[
(K_Q)_{uv}=\frac12\mathbf1_{u=v}
+\frac{\varepsilon}{2^{m+1}}(-1)^{Q^*(u+v)}.
\]
The polar form of \(Q^*\) is \(B^*(u,v)=u^TA v\), because the polar matrix of \(Q\) is \(B\). Thus
\[
(-1)^{Q^*(u+v)}=D_{uu}D_{vv}(-1)^{u^TAv}.
\]
For \(u,v\in E\), the matrix \(((-1)^{u^TAv})_{u,v}\) has every diagonal entry \(1\), entries \(1\) involving index zero, and entry \(-1\) at a distinct coordinate pair precisely when it is an edge of the graph \(A\). It is exactly \(S_A=J_{n+1}-2\widetilde A\). Therefore
\[
K_Q=D\left(\frac12I_{n+1}+\frac{\varepsilon}{2^{m+1}}S_A\right)D,
\]
and the asserted entire spectrum follows, including repeated or zero eigenvalues.

**3. Graph realization.** Every invertible alternating \(B\) has an alternating inverse \(A\), since for \(v=Bu\) one has \(v^TA v=u^TBu=0\). Conversely an invertible alternating binary adjacency matrix \(A\) determines a nonsingular alternating \(B=A^{-1}\), hence a quadratic refinement \(Q\) with that polar matrix. The determinant of an alternating matrix in characteristic two is the square of its Pfaffian, whose reduction modulo two is the parity of the number of perfect matchings. Hence \(A\) is invertible exactly when its graph has an odd number of perfect matchings. Varying \(Q\) by a linear function \(u\cdot x\) multiplies its Gauss sum by \((-1)^{Q(Au)}\). Since a nondegenerate quadratic function takes both values, the two signs occur for each such \(A\).

**4. No lost first-band directions.** For any \(h\ne0\), expanding the two indicators and using the derivative identity above shows
\[
|X_Q\cap(X_Q+h)|=2^{2m-2}+\varepsilon2^{m-1}.
\]
Indeed, the two single Gauss sums each contribute \(\varepsilon2^m\), and the mixed derivative sum vanishes. This intersection count is strictly positive for every \(m\ge2\) and both signs, as well as for \(m=1,\varepsilon=1\). Let \(F(x)=c_0+\sum_{j=1}^n c_j(-1)^{x_j}\) vanish on \(X_Q\). For every coordinate direction \(e_j\), choose \(x,x+e_j\in X_Q\). Subtracting the two vanishing equations gives \(2c_j(-1)^{x_j}=0\). Thus all \(c_j=0\), then \(c_0=0\) because \(X_Q\) is nonempty. If \(m=1,\varepsilon=-1\), the quadric has exactly one point; restriction then has rank one.

**5. Four-coordinate census.** There are three perfect matchings on four labelled vertices. The adjacency matrix is invertible precisely when the graph contains exactly one or all three of these matchings. All three forces \(K_4\). For exactly one chosen matching, each of the two other matching pairs of edges may contain zero or one present edge, giving \(3^2=9\) graphs per chosen matching. The 27 graphs divide into a disjoint pair of edges (three labelled graphs), a four-vertex path (twelve), and a triangle with pendant edge (twelve). Taking the determinant of the explicit five-by-five matrix \(J_5-2\widetilde A\) for one representative of each of these four isomorphism types yields exactly the three polynomial rows stated above: the disjoint-edge and paw polynomials coincide. These cases exhaust all \(28\) invertible graphs. This is an exhaustive finite classification, not an inference from sampling a subset of graphs.

**6. Matched-pair spectrum.** If \(A\) is the union of \(m\) disjoint edges, then on the antisymmetric direction of each pair the Seidel-type matrix \(S_A\) has eigenvalue \(2\). On pair-constant vectors with total pair-sum zero and origin coordinate zero it has eigenvalue \(-2\). The two remaining directions, spanned by the origin vector and the uniform coordinate-vertex vector, are acted on by the two-by-two matrix \(\begin{psmallmatrix}1&2m\\1&2m-2\end{psmallmatrix}\). Its characteristic polynomial is \(z^2-(2m-1)z-2\). This gives the displayed eigenvalues and all multiplicities.

## Verification
The standalone dependency-free checker `artifacts/verify.py` reconstructs both polar inverses and quadratic truth tables over \(\mathbb F_2\). For each invertible four-vertex adjacency graph and every linear refinement, and for tested six-dimensional examples, it compares every entry of the restriction Gram matrix, calculated directly by summation over \(X_Q\), with the claimed signed-Seidel identity using exact integers. It independently checks the difference-set intersection counts and exact rank. It enumerates all \(64\) four-vertex labelled graphs, selects the \(28\) invertible ones, and computes their three characteristic-polynomial multiplicities. The finite enumeration rigorously covers the stated four-vertex census; the all-dimensional result is proved in the preceding algebraic argument.

Run with `python3 artifacts/verify.py`; the expected conclusion begins `VERIFY_OK`. No floating-point tolerance or outside database is used.

## Relationship to prior work
The Walsh flatness of nondegenerate binary quadratic functions, and their connection with Hadamard difference sets and strongly regular Cayley graphs, are established background; see Leopardi (2015) and its cited literature. The global spectra of those Cayley graphs do not by themselves specify the compression to a fixed coordinate first-Walsh band. Leopardi's later classification of extended Cayley equivalence for quadratic bent functions identifies two global classes, while the coordinate-sensitive compressed spectra here have three forms already in dimension four for each sign. The new statement concerns the exact dual-polar graph transfer, realization of odd-perfect-matching graphs, coordinate-sensitive spectra, and universal sampling injectivity, not a new characterization of bentness.

## Limitations
The transfer law applies only to nondegenerate quadratic functions over a binary vector space, with the Walsh band generated by the constant and the specified coordinate characters. It does not describe higher Walsh degrees, degenerate quadrics, arbitrary affine coordinate changes on the sampling band, or sampling with conditional normalization unless the stated rescaling is applied. The graph formula determines the spectrum through a finite real symmetric matrix; it is not a uniform closed-form expression for the eigenvalues of every graph. The standalone checker is finite corroboration and an exhaustive certificate only for the four-vertex graph census, not a replacement for the general proof. A historically equivalent reformulation in punctured Reed--Muller codes or principal Seidel compressions has not been exhaustively ruled out.

## References
1. Paul Leopardi, *Twin bent functions, strongly regular Cayley graphs, and Hurwitz--Radon theory*, arXiv:1504.02827, publicly posted 2015-04-11; especially the bent difference-set background and the graph-theoretic results.
2. Paul Leopardi, *Classifying bent functions by their Cayley graphs*, arXiv:1705.04507, first posted 2017-05-12; especially Section 4, Theorem 4 and Appendix A on quadratic bent functions.
3. Canan Kaşıkcı, *On the spectra of quadratic functions*, doctoral thesis, Sabancı University (2015); public repository record https://research.sabanciuniv.edu/id/eprint/32335 (deposited 2017-06-12). Its Walsh-transform and plateaued-function results supply related background, not the claimed coordinate-compression theorem.
