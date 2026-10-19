# Modulo-four spectral-realification thresholds in a nonreciprocal impurity ring

## Finding

Let \(N\ge3\) be an integer. On the \(N\)-site ring, define the real non-Hermitian hopping matrix \(H_{N,g,V}\) by \((H_{N,g,V})_{j+1,j}=e^g\), \((H_{N,g,V})_{j,j+1}=e^{-g}\), with indices modulo \(N\), and add \(V\ge0\) to entry \((0,0)\). Here \(g>0\), and both hopping assignments on each edge are accumulated in the matrix. Define \(V_*(N,g)\) to be the smallest number such that the entire spectrum of \(H_{N,g,V}\) is real for every \(V\ge V_*(N,g)\). Put \(C=\cosh(Ng)\).

For each complete negative-sine lobe
\[
I_j=\left(\frac{(2j+1)\pi}{N},\frac{(2j+2)\pi}{N}\right),\qquad 0\le j<\left\lfloor\frac{N-1}{2}\right\rfloor,
\]
define
\[
M_j=\max_{\theta\in I_j}\frac{-\sin(N\theta)}{\sin\theta},\qquad
R_N=\left(\min_j M_j\right)^{-1}.
\]
These maxima are attained in the interior. For every fixed \(N\ge3\),
\[
\lim_{g\to\infty}\frac{V_*(N,g)}{2\cosh(Ng)}=R_N.
\]
The limiting prefactor has the **exact arithmetic dichotomy**
\[
R_N=1\ \Longleftrightarrow\ N\equiv3\pmod4,
\qquad 0<R_N<1\ \text{otherwise}.
\]
In the exceptional congruence class the first correction is explicit:
\[
V_*(N,g)=2C-\frac{N^2}{(N^2-1)C}+O_N(C^{-3}),\qquad N\equiv3\pmod4.
\]
Thus the finite-size sufficient bound \(2\sinh(Ng)\) is asymptotically sharp to exponentially small absolute error *only* in that congruence class, and
\[
2\sinh(Ng)-V_*(N,g)=\frac{1}{(N^2-1)C}+O_N(C^{-3}).
\]
For comparison, \(R_4=3\sqrt6/8\) and \(R_5=4/5\). Along the four residue classes as \(N\to\infty\),
\[
R_N=1-\frac{d_N^2}{2N^2}+O(N^{-4}),\qquad
d_N=\begin{cases}
0,&N\equiv3\pmod4,\\
\pi/2,&N\text{ even},\\
\pi,&N\equiv1\pmod4.
\end{cases}
\]
The error estimates involving \(C\) are at fixed \(N\); the final error estimate is for the exact \(N\)-dependent prefactors \(R_N\), not a uniform two-parameter limit in \(g\) and \(N\).

## Assumptions and scope

The directed amplitudes are positive reciprocal numbers \(e^g\) and \(e^{-g}\), the impurity is a positive *real on-site* potential, and all matrices are finite. Eigenvalues are counted algebraically, so the spectrum is called real even at a defective exceptional point. No statement is made about diagonalizability, the complex spectrum at all smaller impurity strengths for arbitrary \(g\), nonreal impurities, or a joint limit of \(N\) and \(g\). The strong-nonreciprocity limit holds for every fixed integer \(N\ge3\).

## Proof

**1. Characteristic identity.** Write \(T_N\) and \(U_{N-1}\) for the ordinary Chebyshev polynomials. Deleting the impurity vertex leaves an \((N-1)\)-site path; a diagonal similarity transforms its asymmetric hoppings into symmetric unit hoppings. The matrix determinant lemma along entry \((0,0)\), and the Fourier spectrum of the ring without impurity, give
\[
P_{N,g,V}(E)=\det(EI-H_{N,g,V})=
2\bigl[T_N(E/2)-\cosh(Ng)\bigr]-V U_{N-1}(E/2).
\tag{1}
\]
This identity fixes both the sign and the normalization of the impurity term.

**2. The real-root lobes.** Set \(E=2\cos\theta\) for \(0<\theta<\pi\). Since \(C>1\), equation (1) with \(V>0\) can hold there only when \(\sin(N\theta)<0\). On each full interval \(I_j\), it is equivalent to
\[
V=F_C(\theta):=
\frac{2[C-\cos(N\theta)]\sin\theta}{-\sin(N\theta)}
=\frac{2[C-\cos(N\theta)]}{-U_{N-1}(\cos\theta)}.
\tag{2}
\]
The denominator is positive inside the interval. The function \(F_C\) tends to \(+\infty\) at either endpoint. The polynomial \(U_{N-1}\) has simple zeros at the endpoints of all these intervals, and its derivative has exactly one nondegenerate zero strictly between consecutive zeros (Rolle's theorem plus degree counting). Consequently \(-U_{N-1}(\cos\theta)\) has exactly one nondegenerate maximum in each \(I_j\). For any *fixed* \(N\), sufficiently large \(C\) makes the normalized function \(F_C/(2C)\) a smooth perturbation of \(1/[-U_{N-1}(\cos\theta)]\). Its unique interior minimum persists, and no extra critical points arise because the poles and the derivative signs near the endpoints persist. Write \(V_j(C)=\min_{\theta\in I_j}F_C(\theta)\). Then the interval supplies two real eigenvalues, counted with multiplicity at a tangency, if \(V\ge V_j(C)\), and none if \(V<V_j(C)\).

There is exactly one real eigenvalue \(E>2\): writing \(E=2\cosh\xi\), the positive-\(V\) secular expression is strictly increasing after its zero at \(\xi=g\) and tends to infinity. For odd \(N\), there is no real eigenvalue below \(-2\), and the full intervals account for the remaining \(N-1\) eigenvalues. For even \(N\), there is one additional real eigenvalue, either below \(-2\) or in the terminal interval \(((N-1)\pi/N,\pi)\). Indeed at \(E=-2\) the characteristic value is \(2(1-C)+NV\), and for \(E=-2\cosh\xi\) the characteristic polynomial is \(2(\cosh N\xi-C)+V\sinh(N\xi)/\sinh\xi\), strictly increasing in \(\xi>0\). The crossing occurs at \(V=2(C-1)/N\). In particular the extra root is always real. The fixed-degree root count thus gives, for sufficiently large \(C\),
\[
V_*(N,g)=\max_j V_j(C).
\tag{3}
\]
At equality a double real eigenvalue is allowed. No assumption about any complex eigenvalue's numerical path is needed.

**3. The strong-asymmetry prefactor.** Since \(\lvert\cos(N\theta)\rvert\le1\), formula (2) gives
\[
\frac{2(C-1)}{M_j}\le V_j(C)\le \frac{2(C+1)}{M_j}.
\]
Taking the maximum over \(j\), dividing by \(2C\), and letting \(C\to\infty\) proves the formula for \(R_N\).

At a negative-sine antinode, the numerator of \(M_j\) is \(1\) and \(M_j\ge1/\sin\theta\). Unless an antinode lies exactly at \(\pi/2\), this is strictly greater than \(1\). Such a central negative-sine antinode occurs exactly when \(N\equiv3\pmod4\). For those \(N\), the corresponding central interval is \(\theta=\pi/2+\delta\) with \(\lvert\delta\rvert<\pi/(2N)\), and its ratio satisfies
\[
\frac{-\sin(N\theta)}{\sin\theta}
=\frac{\cos(N\delta)}{\cos\delta}\le1,
\]
with equality at \(\delta=0\). Every other full negative-sine lobe has maximum strictly above \(1\). Thus its central lobe uniquely minimizes \(M_j\), proving the dichotomy.

**4. The exceptional correction.** For \(N\equiv3\pmod4\) and sufficiently large \(C\), the central lobe controls (3), where
\[
\frac12F_C(\pi/2+\delta)=
\frac{[C-\sin(N\delta)]\cos\delta}{\cos(N\delta)}.
\]
Taylor expansion and the implicit-function theorem around its nondegenerate minimum yield
\[
\delta_C=\frac{N}{(N^2-1)C}+O_N(C^{-3}),\qquad
\frac12F_C(\pi/2+\delta_C)=C-\frac{N^2}{2(N^2-1)C}+O_N(C^{-3}).
\]
Multiplying by two proves the correction. Expanding \(\sinh(Ng)=\sqrt{C^2-1}\) gives the stated difference.

**5. The large-\(N\) prefactors.** Translating a full lobe outward by \(2\pi/N\) preserves \(-\sin(N\theta)\) and reduces \(\sin\theta\) on the corresponding side of \(\pi/2\). Therefore the lobes nearest \(\pi/2\) have the smallest maxima \(M_j\). Their negative-sine antinode lies a distance \(d_N/N\) from \(\pi/2\), with \(d_N\) as in the theorem. Writing the nearby angle as \(\theta=\pi/2+(d_N+u)/N\), the maximized ratio has the local form \(\cos u/\cos((d_N+u)/N)\). Its critical point satisfies \(u=d_N/N^2+O(N^{-4})\), giving
\[
\min_j M_j=1+\frac{d_N^2}{2N^2}+O(N^{-4}).
\]
Taking its reciprocal completes the last asymptotic formula. For \(d_N=0\), the exact equality \(R_N=1\) supplies the stronger statement.

## Verification

The included standalone `verify.py` reconstructs the characteristic polynomial symbolically at an exact rational hopping-asymmetry point for \(N=3,\ldots,8\); computes lobe thresholds and independently diagonalizes finite full matrices at both sides of the realification threshold for \(N=3,\ldots,10\) and three asymmetries; checks the explicit Chebyshev extrema at \(N=4,5\); and checks the displayed strong-asymmetry correction in selected dimensions \(N\equiv3\pmod4\). The computations passed. They are finite consistency checks, not proofs of the universal asymptotics.

## Relationship to prior work

Liu, Zeng, Li and Chen (arXiv:2106.03420, initially public 7 June 2021), equations (11)–(13) and Appendix A, derived the same single-real-impurity secular equation and supplied \(2\sinh(Ng)\) as an effective large-system sufficient cutoff, explicitly noting that the actual finite-size threshold is lower. The characteristic equation and realification phenomenon are **prior work**, not new here. The result proved above isolates the previously unspecified fixed-size strong-asymmetry prefactor, shows it has a sharp modulus-four dichotomy, obtains the exceptionally small cutoff deficit, and determines the residue-dependent large-size coefficients. Guo and collaborators (arXiv:2102.03781) solve a *boundary-hopping* perturbation rather than this real on-site defect; Li, Lee and Gong (arXiv:2008.05501) also analyze modified boundary couplings. Their large-size sensitivity results do not imply the stated on-site threshold prefactor. Priority is not independently certified.

## Limitations

The asymptotics take \(g\to\infty\) with \(N\) fixed before examining the independent sequence of prefactors as \(N\to\infty\). The cutoff may be a defective exceptional point; all-real spectrum does not imply a stable Hermitian dynamics, diagonalizability, or positive norm. The theorem does not address higher-dimensional, disordered, interacting or many-body models, and does not assert that a broad literature search proves uniqueness.

## References

1. Y. Liu, Y. Zeng, L. Li and S. Chen, *Exact solution of single impurity problem in non-reciprocal lattices: impurity induced size-dependent non-Hermitian skin effect*, arXiv:2106.03420v1 (7 June 2021), https://arxiv.org/html/2106.03420v1.
2. C.-X. Guo, C.-H. Liu, X.-M. Zhao, Y. Liu and S. Chen, *Exact solution of non-Hermitian systems with generalized boundary conditions*, arXiv:2102.03781v2 (2021), https://arxiv.org/html/2102.03781v2.
3. L. Li, C. H. Lee and J. Gong, *Impurity induced scale-free localization*, arXiv:2008.05501v1 (12 August 2020), https://arxiv.org/html/2008.05501v1.
