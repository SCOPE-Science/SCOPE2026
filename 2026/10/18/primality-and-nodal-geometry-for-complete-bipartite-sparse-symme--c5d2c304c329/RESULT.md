# Primality and nodal geometry for complete-bipartite sparse symmetric rank-defect varieties

## Finding
Let \(k\) be algebraically closed of characteristic zero, and let \(m\ge 3\). In the standard-graded polynomial ring
\[
R_m=k[a,c,z_1,\ldots,z_m,b_1,\ldots,b_m,d_1,\ldots,d_m],
\]
consider the symmetric \((m+2)\)-square matrix
\[
A_m=\begin{pmatrix}
 a&0&b_1&\cdots&b_m\\
 0&c&d_1&\cdots&d_m\\
 b_1&d_1&z_1&&0\\
 \vdots&\vdots&&\ddots&\\
 b_m&d_m&0&&z_m
\end{pmatrix}.
\]
Write \(I_m=I_{m+1}(A_m)\) for the ideal of **all** submaximal minors and \(Y_m=\operatorname{Proj}(R_m/I_m)\). Then \(I_m\) is **prime for every \(m\ge3\)**. In particular, \(Y_m\) is integral, rational, and of dimension \(3m-2\) and degree \(\binom{m+3}{3}\).

This gives a uniform positive instance, including all \(m\ge5\) beyond the computational sizes reported in the original question, of the two-vertex-connected graph primality problem of Deng and Kretschmer: the nonzero off-diagonal pattern of \(A_m\) is the graph \(K_{2,m}\).

The projective determinant hypersurface \(H_m=V(\det A_m)\subset\mathbb P^{3m+1}\) is integral and normal. Its entire reduced singular locus is \(Y_m\). A general point of \(Y_m\) has, transverse to \(Y_m\) in \(H_m\), the ordinary surface-double-point equation \(uv-w^2=0\).

## Assumptions and scope
The coefficient field is algebraically closed of characteristic zero; \(m\) is any integer at least three. All minors of size \(m+1\), including nonprincipal minors, are used. Coordinates have degree one. Projective dimension is computed in \(\mathbb P^{3m+1}\), not the ambient full symmetric-matrix space. The assertion is ideal-theoretic primality, rather than merely set-theoretic irreducibility. The earlier general radicality/unmixedness theorem for connected graph patterns is explicitly used below.

## Proof
**1. An irreducible dense torus-diagonal chart.** Work first in the affine rank-defect scheme \(V(I_m)\). Invert \(z_1\cdots z_m\) and take the Schur complement of the invertible leaf diagonal. Congruence by invertible matrices gives the block sum of \(\operatorname{diag}(z_i)\) and
\[
S=\begin{pmatrix}u&w\\w&v\end{pmatrix},\qquad
u=a-\sum_{i=1}^m\frac{b_i^2}{z_i},\quad
v=c-\sum_{i=1}^m\frac{d_i^2}{z_i},\quad
w=-\sum_{i=1}^m\frac{b_id_i}{z_i}.
\]
Consequently the rank bound \(\operatorname{rank}(A_m)\le m\) is equivalent, scheme-theoretically on this chart, to \(u=v=w=0\). Eliminating \(a,c\), its coordinate ring is
\[
k[z_1^{\pm1},\ldots,z_m^{\pm1},b_1,\ldots,b_m,d_1,\ldots,d_m]
\Big/\left(\sum_{i=1}^m b_id_i/z_i\right).
\]
The defining bilinear polynomial is irreducible: over \(k(z_1,\ldots,z_m)\) it has matrix rank \(m\ge2\), whereas a reducible homogeneous polynomial of total degree two and bidegree \((1,1)\) would be a product of one linear form in the \(b_i\) and one in the \(d_i\), hence have rank one. It is primitive over the Laurent polynomial coefficient ring because its coefficients are units. By Gauss's lemma the displayed ring is a domain. This open subset is thus irreducible, nonempty and of affine dimension \(3m-1\).

**2. No codimension-three component lies on the deleted leaf-diagonal boundary.** Stratify the boundary according to the exact set \(T\) of vanishing \(z_i\), with \(t=|T|\ge1\), and invert the other leaf diagonals. Taking their Schur complement reduces the rank bound to
\[
\operatorname{rank}M\le t,\qquad M=\begin{pmatrix}C&B\\ B^{\mathsf T}&0_{t\times t}\end{pmatrix},
\]
where \(C\) is symmetric of size two and \(B\) is the \(2\)-by-\(t\) matrix whose columns are \((b_i,d_i)^{\mathsf T}\) for \(i\in T\). The diagonal entries of \(C\) remain independent affine-linear parameters through \(a,c\); its off-diagonal entry is determined by the inverted leaves.

For \(t=1\), rank at most one forces \(B=0\) and \(\det C=0\). These impose two independent linear conditions and one genuine further equation in \(a,c\), in addition to \(z_i=0\): ambient codimension at least four.

For \(t=2\), rank at most two forces \(\operatorname{rank}B\le1\), a determinantal hypersurface condition. On the dense rank-one part write \(B=r s^{\mathsf T}\) with \(r\ne0\). Congruence brings \(M\) to a block with an invertible hyperbolic \(2\)-square pivot plus the scalar restriction of \(C\) to \(\ker B^{\mathsf T}\); hence rank at most two requires that scalar to vanish. It is a nontrivial equation in the independent diagonal parameters \(a,c\). The rank-zero part of \(B\) has codimension four in \(B\)-space. Thus the residual rank condition has codimension at least two, and the two vanished \(z_i\) give ambient codimension at least four.

For \(t=3\), \(\operatorname{rank}B=2\) forces \(\operatorname{rank}M=4>3\), hence \(\operatorname{rank}B\le1\). This is a determinantal condition of codimension two on a \(2\)-by-\(3\) matrix; including the three vanished leaf diagonals gives codimension at least five.

For \(t\ge4\), the equations \(z_i=0\) alone give ambient codimension at least four (indeed \(\operatorname{rank}M\le4\le t\)). Since there are finitely many strata, the entire boundary in \(V(I_m)\) has ambient codimension at least four.

**3. From dense irreducibility to primality.** Deng and Kretschmer's Theorem 1 (arXiv:2211.07020) proves that for every connected graph, the corresponding sparse symmetric submaximal-minor ideal is radical and its quotient is Cohen--Macaulay of height three. The graph \(K_{2,m}\) is connected. The cited paper keeps additional indeterminates for positions set to zero; dropping those unused variables is a polynomial-extension descent and does not alter these ideal properties. Thus every irreducible component of \(V(I_m)\) has ambient codimension three. Step 2 excludes any component supported in the omitted boundary; step 1 says that the remaining open subset is irreducible. Therefore \(V(I_m)\) is irreducible. Radicality now implies that \(I_m\) is prime.

**4. Dimensions, rationality and degree.** The polynomial ring has \(3m+2\) variables, so \(\dim Y_m=3m-2\). On the chart from step 1, if some \(b_j\ne0\), the single bilinear equation solves uniquely for \(d_j\), while \(a,c\) are already determined. This exhibits a dense rational parametrization; hence \(Y_m\) is rational. By the established sparse-symmetric Betti resolution (same Theorem 1), with \(n=m+2\) and \(D_G=0\), the Hilbert numerator before removing the codimension-three factor is
\[
1-\binom{n+1}{2}t^{n-1}+(n^2-1)t^n-\binom n2t^{n+1}.
\]
Its third derivative at one gives degree \(n(n^2-1)/6=\binom{m+3}{3}\). This degree is a consequence of the **known** resolution, not an independently claimed new numerical theorem.

**5. The determinant hypersurface and its generic transverse germ.** Deng and Kretschmer's Proposition 15 establishes irreducibility of the determinant for any connected graph, so \(H_m\) is integral. At a corank-one symmetric matrix, the adjugate is a nonzero scalar multiple of \(qq^{\mathsf T}\) for a nonzero kernel vector \(q\). Some diagonal adjugate entry is nonzero in characteristic zero, hence a derivative with respect to a present diagonal variable is nonzero. All points of rank at most \(m\), on the other hand, have zero adjugate. Thus \(\operatorname{Sing}(H_m)_{\mathrm{red}}=Y_m\). This has codimension two in the hypersurface, which is Cohen--Macaulay and therefore satisfies Serre's \(S_2\); the hypersurface is also \(R_1\), hence normal. Finally, on the dense chart the determinant is the unit \(\prod z_i\) times \(uv-w^2\). At a general point of \(Y_m\), the differential of \(w=-\sum b_i d_i/z_i\) is nonzero; together with the independent differentials of \(u,v\), this makes \(u,v,w\) part of a regular system of local parameters. The completed transverse equation is exactly \(uv-w^2=0\).

## Verification
The standalone script `verify.py` performs exact rational Gaussian elimination and determinant arithmetic, checking both sides of the Schur-complement rank and determinant identities for \(3\le m\le7\). It independently checks the four boundary-rank criteria for \(1\le t\le8\) on deterministic test families, and gives a nontrivial exact smooth rank-defect witness at \(m=5\). Run `python3 verify.py` from this file's directory; successful execution prints `VERIFY_OK`. The script is an executable consistency check, not an exhaustive infinite-parameter proof; the quantifiers above are established by the symbolic rank and dimension arguments and the cited general radicality theorem.

## Relationship to prior work
Boocher, *Free Resolutions and Sparse Determinantal Ideals*, first publicly available on 2011-11-01, supplies the historical sparse-determinantal-pruning context, **for matrices with independent nonzero entries**, not the symmetric theorem here. Conca and Welker, *Lovász--Saks--Schrijver Ideals and Coordinate Sections of Determinantal Varieties*, study sparse symmetric determinantal ideals (2018); the forest zero-pattern primality criterion of their Theorem 7.8 does not apply because the zero graph here is the disjoint union of a clique on \(m\ge3\) leaves and the edge joining the two hubs, so it contains a triangle. Deng and Kretschmer (2022) supply radicality, Cohen--Macaulayness, Hilbert resolution, and connected-graph determinant irreducibility; their Question 16 asks whether submaximal-minor ideals are prime for every two-connected graph and notes computations only through six vertices. The present proof establishes the graph family \(K_{2,m}\) for all \(m\), without answering that full question.

## Limitations
Primality beyond the indicated complete-bipartite family is not addressed. The proof imports the general radicality/Cohen--Macaulayness theorem, which must be understood as prior work. The assertion about an ordinary transverse node is generic only; no classification of special germs along the rank-defect boundary is claimed. The unreduced Jacobian singular scheme is not computed. Novelty is assessed relative to the inspected sources and mathematical-record queries, not by an exhaustive literature theorem; an undiscovered equivalent specialization remains possible. There is no independent audit.

## References
1. A. Boocher, *Free Resolutions and Sparse Determinantal Ideals*, arXiv:1111.0279 (initial public version: 2011-11-01), https://arxiv.org/abs/1111.0279.
2. A. Conca and V. Welker, *Lovász--Saks--Schrijver Ideals and Coordinate Sections of Determinantal Varieties*, arXiv:1801.07916 (initial public version: 2018-01-24), https://arxiv.org/abs/1801.07916.
3. J. Deng and A. Kretschmer, *Ideals of Submaximal Minors of Sparse Symmetric Matrices*, arXiv:2211.07020 (initial public version: 2022-11-13), https://arxiv.org/abs/2211.07020, particularly Theorem 1, Proposition 15, and Question 16.
