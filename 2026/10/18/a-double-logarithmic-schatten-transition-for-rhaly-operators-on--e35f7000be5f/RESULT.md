# A double logarithmic Schatten transition for Rhaly operators on the critical Dirichlet space

## Finding
Let \(\mathcal D_*\) be the Hilbert space of functions \(f(z)=\sum_{n\ge0}a_nz^n\), holomorphic on the unit disk, with
\[
\|f\|_{\mathcal D_*}^2=\sum_{n=0}^{\infty}(n+1)|a_n|^2.
\]
For every real \(\beta\), define the Rhaly operator initially on polynomials by
\[
\mathcal R_\beta f(z)=\sum_{n=0}^{\infty}\frac{\sum_{k=0}^n a_k}{(n+1)[\log(e+n)]^\beta}\,z^n.
\]
Here \(\mathcal S_p\), for \(p\ge1\), denotes the Schatten ideal on \(\mathcal D_*\).
The complete boundedness and singular-ideal phase classification is
\[
\begin{array}{c|c}
\text{Parameter}&\text{Exact property}\\\hline
\beta<1&\mathcal R_\beta\text{ does not extend boundedly},\\
\beta=1&\mathcal R_\beta\text{ is bounded and noncompact},\\
1<\beta\le2&\mathcal R_\beta\in\bigcap_{p>1}\mathcal S_p\setminus\mathcal S_1,\\
\beta>2&\mathcal R_\beta\in\mathcal S_1.
\end{array}
\]
Thus the boundedness/compactness transition is \(\beta=1\) and the sharp trace-class transition is \(\beta=2\), with an intermediate family belonging to every Schatten \(\mathcal S_p\) for \(p>1\) but not to trace class.

## Assumptions and scope
The scalar field is complex; \(\beta\) is an arbitrary fixed real number. The coefficient weights are exactly \(n+1\), corresponding to a conventional equivalent norm on the classical Dirichlet Hilbert space. The logarithm is natural. The operator is defined on the dense subspace of polynomials; boundedness refers to its unique bounded extension when one exists. The statement concerns this particular monotone, slowly varying family, not arbitrary Rhaly coefficients or arbitrary analytic Hilbert spaces. Schatten ideals are invariant under the bounded isomorphism between the displayed equivalent Dirichlet norm and other standard Dirichlet norms.

## Proof
**1. An exact Hilbert-space matrix.** Let \(e_n(z)=z^n/\sqrt{n+1}\). Relative to this orthonormal basis the operator is the lower-triangular factorable matrix
\[
A_\beta(n,k)=c_nd_k\mathbf1_{\{k\le n\}},\quad
c_n=\frac1{\sqrt{n+1}[\log(e+n)]^\beta},\quad d_k=\frac1{\sqrt{k+1}}.
\tag{1}
\]
All subsequent estimates apply to this exact matrix.

**2. Boundedness at the first threshold.** Put \(\delta_n=\log((n+2)/(n+1))\), \(I_n=[\log(n+1),\log(n+2))\), and define an isometry \(E:\ell_2\to L^2(0,\infty)\) by \(Ee_n=\mathbf1_{I_n}/\sqrt{\delta_n}\). On \(I_n\) let \(a(x)=c_n/\sqrt{\delta_n}\) and \(b(x)=d_n/\sqrt{\delta_n}\). For the weighted Volterra integral
\[
(V_\beta h)(x)=a(x)\int_0^x b(y)h(y)\,dy
\]
direct integration over rectangles and the diagonal triangle gives the **exact** identity
\[
A_\beta=E^*V_\beta E+\tfrac12\operatorname{diag}(c_nd_n).
\tag{2}
\]
For every \(x\ge0\), the step functions satisfy \(b(x)\le C\) and, at \(\beta=1\), \(a(x)\le C/(1+x)\). Classical Hardy's \(L^2\) inequality for \(h\mapsto x^{-1}\int_0^xh\) therefore proves \(V_1\) bounded. The diagonal term is bounded. Hence \(A_1\) is bounded. The exact relation \(A_\beta=\operatorname{diag}([\log(e+n)]^{1-\beta})A_1\) also establishes boundedness for every \(\beta\ge1\).

To prove the converse and noncompactness at equality, let \(R\to\infty\) and choose a unit vector with coordinates
\[
x_k=\frac{(k+1)^{-1/2}}{\sqrt{H_R}}\mathbf1_{\{e^R\le k+1<e^{3R/2}\}},\quad
H_R=\sum_{e^R\le k+1<e^{3R/2}}\frac1{k+1}\asymp R.
\]
For \(e^{3R/2}\le n+1<e^{2R}\) the full preceding support is included, so \((A_\beta x)_n=c_n\sqrt{H_R}\). Thus
\[
\|A_\beta x\|_2^2\ge H_R\sum_{e^{3R/2}\le n+1<e^{2R}}
\frac1{(n+1)[\log(e+n)]^{2\beta}}
\asymp_\beta R^{2-2\beta}.
\tag{3}
\]
For \(\beta<1\) this grows without bound. For \(\beta=1\) it stays bounded below, while these unit vectors converge weakly to zero. Hence \(A_1\) is not compact.

**3. Every \(\beta>1\) belongs to all \(\mathcal S_p\), \(p>1\).** In (2), at infinity \(|a(x)|\le C_\beta(1+x)^{-\beta}\) and \(|b(x)|\le C\). Partition \([0,\infty)\) into \([0,1)\) and \(B_j=[2^j,2^{j+1})\), \(j\ge0\). The Volterra operator is the sum of (i) its restrictions from \(B_j\) into \(B_j\), and (ii) rank-one pieces from the entire earlier interval \([0,2^j)\) into \(B_j\), plus one finite-length initial restriction. The unweighted integration operator on an interval of length \(L\) has singular values
\[
s_k=\frac{2L}{(2k-1)\pi},\qquad k\ge1.
\tag{4}
\]
Its \(\mathcal S_p\) norm is \(C_pL\), finite for every \(p>1\). Multiplication by the bounded weights shows that each same-block piece has \(\mathcal S_p\) norm at most \(C_{p,\beta}2^{j(1-\beta)}\). Every cross-block piece has rank one and trace norm
\[
\|a\mathbf1_{B_j}\|_2\,\|b\mathbf1_{[0,2^j)}\|_2
\le C_\beta2^{j(1-\beta)}.
\]
Because \(\beta>1\), these norms sum geometrically. The initial finite Volterra piece belongs to \(\mathcal S_p\) for \(p>1\). Hence \(V_\beta\in\mathcal S_p\). Also \(\sum_n c_nd_n=\sum_n[(n+1)\log(e+n)^\beta]^{-1}<\infty\), so the diagonal correction is trace class. The ideal property of \(\mathcal S_p\) and (2) prove \(A_\beta\in\mathcal S_p\) for all \(p>1\).

**4. Sharp trace-class necessity.** Let \(D_j=\{n:2^j\le n+1<2^{j+1}\}\), so \(|D_j|=2^j\), and let \(P_j\) project onto its coordinates. On \(D_j\), the diagonal multipliers \(c_n\), \(d_n\) are respectively comparable, above and below, to \(2^{-j/2}(1+j)^{-\beta}\) and \(2^{-j/2}\), with positive constants depending only on \(\beta\). The compressed matrix is \(P_jA_\beta P_j=C_jJ_{2^j}D'_j\), where \(J_N\) is the \(N\)-by-\(N\) lower-triangular all-ones matrix. Inverting \(J_N\) gives a bidiagonal difference matrix. Diagonalizing its tridiagonal Gram matrix yields the exact singular values
\[
s_k(J_N)=\frac1{2\sin\!\left(\frac{(2k-1)\pi}{4N+2}\right)},\quad 1\le k\le N.
\tag{5}
\]
In particular, \(\|J_N\|_1\asymp N\log(N+1)\) for \(N\ge2\), whence
\[
\|P_jA_\beta P_j\|_1\asymp_\beta (1+j)^{1-\beta}\quad(j\ge1).
\tag{6}
\]
The block-diagonal conditional expectation \(T\mapsto\sum_jP_jTP_j\) is contractive on \(\mathcal S_1\), for example by averaging diagonal-block unitary conjugations. Therefore if \(A_\beta\in\mathcal S_1\), then \(\sum_{j\ge1}(1+j)^{1-\beta}<\infty\), forcing \(\beta>2\).

**5. Trace-class sufficiency.** Write the triangular matrix as the sum of its within-block terms \(P_jA_\beta P_j\) and its strictly earlier-block terms \(P_jA_\beta P_{<j}\), where \(P_{<j}=\sum_{i<j}P_i\). Each latter term is rank one, and
\[
\|P_jA_\beta P_{<j}\|_1
=\left(\sum_{n\in D_j}c_n^2\right)^{1/2}
\left(\sum_{k+1<2^j}d_k^2\right)^{1/2}
\lesssim_\beta (1+j)^{1/2-\beta}.
\tag{7}
\]
The diagonal-block trace norms sum when \(\beta>2\) by (6), and the cross-block trace norms sum already for \(\beta>3/2\) by (7). Therefore their operator sum converges absolutely in trace norm to \(A_\beta\), establishing \(A_\beta\in\mathcal S_1\) for \(\beta>2\). Combined with the preceding steps this proves every case of the theorem.

## Verification
Running `python CHECKER.py` with NumPy available checks the exact lower-triangular matrix formula against direct Dirichlet-coefficient action for a range of real parameters, and checks (5) against independently computed singular values for multiple dimensions. The checks concern finite matrices only. Proofs of boundedness, noncompactness and infinite-dimensional Schatten membership are the analytic steps above, not consequences of finite testing.

## Relationship to prior work
Bellavita, Dellepiane, and Stylogiannis (2026) study Rhaly operators on weighted Hardy spaces and Schatten ideals, identifying the classical Dirichlet case as critical; their publicly accessible abstract and an independent article overview do not establish the specific trace-class logarithmic endpoint proved here. Complete preprint text could not be inspected, so priority relative to possible further results in that manuscript is not independently resolved. Their 2025 Rhaly matrix work characterizes \(\mathcal S_q\) on ordinary \(\ell^2\) for \(q>1\), which is a different matrix after the Dirichlet-basis conjugation. Galanopoulos and Girela (2026) investigate boundedness and compactness on Hardy, Bergman and Dirichlet spaces, not the claimed Dirichlet trace threshold. A published result gives a trace-class logarithmic threshold for ordinary monotone Rhaly matrices; although the numerical cutoff can agree, the ordinary \(\ell^2\) operator and the critical Dirichlet operator differ: at the unlogged parameter the former is a bounded Cesàro operator while the latter is unbounded. None of these comparisons alone certifies independent mathematical priority.

## Limitations
The classification covers only \(\eta_n=[(n+1)\log(e+n)^\beta]^{-1}\), not general logarithmically oscillating sequences. No exact asymptotics of individual singular values or optimal constants in ideal norms are claimed. The closest June 2026 preprint was accessible in abstract and overview form but not in full; this is a genuine residual priority risk. Verification of (5) for finitely many dimensions is diagnostic, not an infinite-dimensional certificate. No independent review has been performed.

## References
1. C. Bellavita, E. Dellepiane, G. Stylogiannis, *Rhaly operators on weighted Hardy spaces and factorable matrices*, arXiv:2606.15875v1, initially public June 14, 2026. https://arxiv.org/abs/2606.15875
2. P. Galanopoulos, D. Girela, *Rhaly Operators Acting on Hardy, Bergman, and Dirichlet Spaces*, J. Geom. Anal. 36 (2026), article 115. https://doi.org/10.1007/s12220-026-02361-9
3. C. Bellavita, E. Dellepiane, G. Stylogiannis, *Boundedness, compactness and Schatten class for Rhaly matrices*, J. Lond. Math. Soc. 112 (2025), e70304. https://doi.org/10.1112/jlms.70304
4. Published research record, *The sharp trace-class endpoint for monotone-modulus Rhaly matrices*, October 11, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-sharp-trace-class-endpoint-for-monotone-modulus-rhaly-matric--182bfa9e0a1a
