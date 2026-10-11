# Logarithmic spectral edge of higher singular values of finite Cesàro matrices

## Finding

For each integer \(n\ge2\), define the real or complex Euclidean Cesàro averaging operator
\[
(C_nx)_i=\frac1i\sum_{r=1}^{i}x_r,\qquad 1\le i\le n.
\]
Write its singular values in decreasing order as \(\sigma_1(C_n)\ge\cdots\ge\sigma_n(C_n)>0\). **For every fixed integer \(j\ge2\)**, as integers \(n\ge j\) tend to infinity,
\[
\lim_{n\to\infty}(\log n)^2\bigl(2-\sigma_j(C_n)\bigr)=4\pi^2j^2.
\tag{1}
\]
Consequently, for every fixed \(j\ge2\), the consecutive higher-level singular-value gap obeys
\[
\lim_{n\to\infty}(\log n)^2\bigl(\sigma_j(C_n)-\sigma_{j+1}(C_n)\bigr)=4\pi^2(2j+1).
\tag{2}
\]
The top singular value case \(j=1\) has independently been treated in sharper form in the finite Hardy-constant literature; the higher levels and their gaps are the subject here.

## Assumptions and scope

All logarithms are natural. Each rank \(j\ge2\) is held fixed as \(n\to\infty\); no estimate uniform for growing ranks is asserted. The real proof applies unchanged over complex scalars because the relevant quadratic forms and their eigenvalues are real. The finite Cesàro matrix is invertible for every \(n\), with positive singular values. Its spectral edge is analyzed via the inverse operator, not the algebraic spectrum of the triangular matrix \(C_n\).

## Proof

**1. Exact inverse variational problem.** Introduce \(z_i=i x_i\) and \(z_0=0\). The inverse of \(C_n\) is the first-difference map \((C_n^{-1}x)_i=i x_i-(i-1)x_{i-1}=z_i-z_{i-1}\). Therefore the eigenvalues \(\lambda_{1,n}\le\cdots\le\lambda_{n,n}\) of \((C_n^{-1})^*C_n^{-1}\) are the generalized eigenvalues of
\[
Q_n(z)=\sum_{i=1}^n|z_i-z_{i-1}|^2,\qquad
M_n(z)=\sum_{i=1}^n\frac{|z_i|^2}{i^2},
\qquad \lambda_{j,n}=\sigma_j(C_n)^{-2}.
\tag{3}
\]
The Courant--Fischer principle applies to \(Q_n/M_n\). Put \(E_n=Q_n-\frac14M_n\), and denote its generalized eigenvalues by \(\mu_{j,n}=\lambda_{j,n}-\frac14\).

**2. Ground-state identity and endpoint control.** Set \(z_i=\sqrt i\,u_i\), \(1\le i\le n\), and \(a_i=\sqrt{i(i-1)}\) for \(i\ge2\). Completing the discrete square gives the *exact identity*
\[
E_n(z)=\sum_{i=2}^n a_i|u_i-u_{i-1}|^2
  +\sum_{i=1}^{n-1}V_i|u_i|^2+V_n|u_n|^2,
\tag{4}
\]
where
\[
V_i=i\left(2-\sqrt{1-1/i}-\sqrt{1+1/i}-\frac1{4i^2}\right)
\quad(1\le i<n),
\]
\[
V_n=n\left(1-\sqrt{1-1/n}\right)-\frac1{4n}.
\tag{5}
\]
For \(0\le t\le1\), differentiating \(\sqrt{1+t}+\sqrt{1-t}\) twice shows \(\sqrt{1+t}+\sqrt{1-t}\le2-t^2/4\). Thus all interior coefficients are nonnegative. Specifically, \(V_1=2-\sqrt2-\frac14>0\), while \(V_n\ge\frac12-\frac1{4n}\ge\frac38\) for \(n\ge2\). Hence for the absolute constant \(c=2-\sqrt2-\frac14>0\),
\[
E_n(z)\ge K_n(u)+c\bigl(|u_1|^2+|u_n|^2\bigr),
\qquad K_n(u)=\sum_{i=2}^n a_i|u_i-u_{i-1}|^2.
\tag{6}
\]
Also \(V_i=O(i^{-3})\) for \(i\ge2\), with an absolute implied constant; this follows by expanding both square roots to fourth order, or Taylor's theorem with bounded derivatives for \(i\ge2\).

**3. Logarithmic interpolation.** Let \(L=\log n\), \(t_i=\log i\), and \(h_i=t_i-t_{i-1}=\log(i/(i-1))\) for \(i\ge2\). Let \(U\) be piecewise affine on \([0,L]\), with \(U(t_i)=u_i\), and define \(f_n(s)=\sqrt L\,U(Ls)\), \(0\le s\le1\). Since \(a_i h_i\ge1/\sqrt2\) and \(a_i h_i\to1\) as \(i\to\infty\),
\[
\int_0^1|f_n'(s)|^2\,ds
=L^2\sum_{i=2}^n\frac{|u_i-u_{i-1}|^2}{h_i}
\le\sqrt2\,L^2 K_n(u).
\tag{7}
\]
Whenever \(M_n(z)=1\) and \(E_n(z)\le C/L^2\) for a fixed \(C\), (6) and \(\sum_{i=2}^n a_i^{-1}=O(L)\) give
\[
|u_1|+|u_n|=O(L^{-1}),\qquad
\max_{1\le i\le n}|u_i|=O(L^{-1/2}).
\tag{8}
\]
To compare mass with the interpolation, write
\[
\int_0^1|f_n|^2ds=\int_0^L|U|^2dt,
\qquad M_n(z)=\sum_{i=1}^n\frac{|u_i|^2}{i}.
\]
The difference between \(\sum_{i=2}^n h_i|u_i|^2\) and \(M_n\) is at most
\[
|u_1|^2+\bigl(\max_i|u_i|^2\bigr)
\sum_{i=2}^\infty\left|\log\frac{i}{i-1}-\frac1i\right|=O(L^{-1}),
\]
since the displayed scalar series converges. On each affine interval the difference from its right endpoint mass is bounded by \(h_i(2\max|u||u_i-u_{i-1}|+|u_i-u_{i-1}|^2)\). Cauchy--Schwarz, (6), and \(\sum_{i=2}^\infty h_i^2/a_i<\infty\) show that the sum of these differences is \(O(L^{-3/2})+O(L^{-2})\). Thus
\[
\int_0^1|f_n|^2\,ds=M_n(z)+o(1)
\tag{9}
\]
uniformly among all vectors normalized as above. Furthermore (6) and (8) imply \(f_n(0)\to0\), \(f_n(1)\to0\).

If the normalized low-energy vectors form any sequence, (7)--(9) make their interpolants bounded in \(H^1(0,1)\), with unit limiting \(L^2\) norm and zero endpoint traces. Rellich compactness yields a subsequence converging strongly in \(L^2\), weakly in \(H^1\), to an element of \(H^1_0(0,1)\). For each \(0<\delta<1\), all interpolation cells meeting \([\delta,1]\) have \(i\ge n^\delta\), up to one cell, and \(a_i h_i=1+o(1)\) uniformly on them. Thus, from (4) and weak lower semicontinuity,
\[
\liminf_{n\to\infty}L^2E_n(z)
\ge\int_\delta^1|f'(s)|^2ds.
\]
Letting \(\delta\downarrow0\) yields the *liminf inequality*
\[
\liminf_{n\to\infty}L^2E_n(z)\ge\int_0^1|f'(s)|^2ds.
\tag{10}
\]
(The omitted single cell at \(\delta\) has nonnegative energy; a slightly smaller cutoff removes it.)

**4. Matching test functions.** Conversely, take any fixed \(g\in C_c^\infty(0,1)\) and set \(u_i=L^{-1/2}g(t_i/L)\). Then the logarithmic-mesh Riemann sums and \(a_i h_i\to1\) uniformly on the support give
\[
M_n(z)\longrightarrow\int_0^1|g|^2ds,
\qquad L^2K_n(u)\longrightarrow\int_0^1|g'|^2ds.
\]
The endpoint potentials are zero, and (5) plus \(V_i=O(i^{-3})\) make \(L^2\sum V_i|u_i|^2\to0\): the support is confined to indices at least \(n^\alpha\) for some \(\alpha>0\). Hence
\[
L^2E_n(z)\longrightarrow\int_0^1|g'|^2ds.
\tag{11}
\]
Polarization extends (11) uniformly to each fixed finite-dimensional space of such test functions.

**5. All fixed spectral levels.** Let \(\nu_j=\pi^2j^2\) be the \(j\)-th Dirichlet eigenvalue of \(-d^2/ds^2\) on \((0,1)\). Approximate the first \(j\) Dirichlet eigenfunctions by smooth compactly supported test functions and use (11) with finite-dimensional Courant--Fischer to get \(\limsup L^2\mu_{j,n}\le\nu_j\). For the reverse inequality, take a subsequence realizing \(\liminf L^2\mu_{j,n}\) and choose \(M_n\)-orthonormal generalized eigenvectors spanning the first \(j\) levels. The previous upper estimate bounds their individual energies by \(C/L^2\). By (7)--(10), after a common subsequence their logarithmic interpolants converge strongly in \(L^2(0,1)\) to \(j\) orthonormal vectors in \(H_0^1(0,1)\); preservation of inner products follows from (9) by polarization, since every bounded-coefficient linear combination satisfies the same energy bound. For each coefficient vector, (10) bounds its limiting Dirichlet energy by the same limiting upper spectral level. The continuum Courant--Fischer principle then forces \(\liminf L^2\mu_{j,n}\ge\nu_j\). Thus for every fixed \(j\ge1\),
\[
\lambda_{j,n}=\frac14+\frac{\pi^2j^2}{(\log n)^2}+o((\log n)^{-2}).
\tag{12}
\]
Finally, \(\sigma_j(C_n)=\lambda_{j,n}^{-1/2}\), and Taylor expansion at \(\lambda=1/4\) has derivative \(-4\). Applying it to (12) proves (1) for every \(j\ge2\), and subtracting neighboring ranks proves (2).

## Verification

The algebraic inverse, quadratic-form identification, and ground-state completion of squares were checked directly and through the accompanying exact rational finite-dimensional checker; all finite checks passed. Independent calculations of the smallest generalized eigenvalues at several dimensions agree with the predicted slowly convergent logarithmic scaling. The universal limit is established by the analytical compactness and min--max proof above, *not* by extrapolating finite numerical data. The checker uses only Python's standard library and deliberately does not represent a proof of the infinite limit.

## Relationship to prior work

Brown--Halmos--Shields' foundational study treats the infinite Cesàro operator and its norm and spectrum; the finite-matrix norm question and its inverse tridiagonal reduction appear explicitly in the 2011--2013 MathOverflow discussion. Lacruz--León-Saavedra--Petrović--Zabeti (first arXiv version 19 March 2014) classify extended eigenvalues of infinite discrete and continuous Cesàro operators, not fixed-rank singular asymptotics of their finite sections. Huang's preprint (first posted 7 September 2026) treats sharp finite Hardy constants, yielding considerably finer information for the *largest* singular value, not a stated higher-singular-value spectral law. The present statement deliberately claims only fixed higher ranks \(j\ge2\) and their spacings. The shift from a single norm to the complete fixed-rank edge is not a corollary of a sharp norm estimate: two matrices can have the same largest singular value and different second or subsequent singular values. A public semantic literature search found no indexed assertion covering (1) for \(j\ge2\). This does not certify global novelty.

## Limitations

The result is for Hilbert exponent two and the canonical unweighted finite Cesàro sections. It is a fixed-rank limit, not uniform in \(j\); it gives only the leading logarithmic correction and no finite-\(n\) exact closed formula or quantitative convergence rate. The 2026 Hardy preprint's full text was not available in the sources inspected, so a stronger unpublished or unindexed formulation could overlap. Other historical finite-section treatments may have been missed; publication-level novelty requires a separate thorough literature review. 
## References

1. A. Brown, P. R. Halmos, A. L. Shields, *Cesàro operators*, Acta Sci. Math. 26 (1965), 125--137; bibliographic entry https://acta.bibl.u-szeged.hu/14062/ .
2. *Norm of Cesaro matrix*, MathOverflow question 72416, posted 9 August 2011, with responses in 2011 and 2013: https://mathoverflow.net/questions/72416/norm-of-cesaro-matrix .
3. M. Lacruz, F. León-Saavedra, S. Petrovic, O. Zabeti, *Extended eigenvalues for Cesàro operators*, first public arXiv version 19 March 2014, https://arxiv.org/abs/1403.4844 .
4. Tianchi Huang, *Finite Hardy Phase Theory for Power Means: An exact analytic shooting family through the Carleman parameter*, first public preprint 7 September 2026, https://arxiv.org/abs/2609.10598 .
