# Sharp factorial saturation of common Zak zeros by compactly supported windows

## Finding
For every integer \(d\geq 1\) there is an explicit, continuously parameterized family of \(d\) windows \(g_1,\ldots,g_d\in C_c^\infty(\mathbb R^d)\), each supported in \([-1/2,1]^d\), such that their simultaneous Zak-zero set modulo the integer phase-space lattice consists of **exactly \(d!\) points**. Every zero is nondegenerate with **positive local index**. The real Jacobian determinant is explicit and has the same strictly positive value at every zero. More generally, the construction works for any \(d\) distinct parameters in \(\mathbb C\setminus[0,\infty)\); the zero locations are exactly the permutations of their uniquely determined one-coordinate preimages.

This count is sharp: for any smooth \(d\)-tuple of Zak-quasiperiodic functions on \(\mathbb R^{2d}\) having only transverse common zeros, there are at least \(d!\) such zeros on the torus. The lower bound is the classical Chern/Euler index count already implicit in the preceding existence theorem; **the new assertion is its explicit, all-positive, compactly supported saturation and the full parameterized zero/Jacobian formula**.

## Assumptions and scope
Let \(\eta(t)=e^{-1/t}\) for \(t>0\) and \(\eta(t)=0\) for \(t\leq0\). Set
\[
\phi(t)=\eta(t+1/2)\eta(1/2-t),\qquad
\psi(t)=\eta(t)\eta(1-t).
\]
For \(f\in C_c^\infty(\mathbb R^d)\), use the unit-scale Zak transform
\[
(Z_df)(u,v)=\sum_{n\in\mathbb Z^d}f(u-n)e^{2\pi i n\cdot v},\qquad (u,v)\in\mathbb R^{2d}.
\]
Write \(A=Z_1\phi\), \(B=Z_1\psi\), and \(A_j=A(u_j,v_j)\), \(B_j=B(u_j,v_j)\). Fix any pairwise distinct \(\rho_1,\ldots,\rho_d\in\mathbb C\setminus[0,\infty)\), and let \(e_k(\rho)\) denote the elementary symmetric polynomial of degree \(k\), with \(e_0=1\). For \(1\leq k\leq d\), define
\[
S_k(u,v)=\sum_{\substack{J\subseteq\{1,\ldots,d\}\\|J|=k}}
\prod_{j\in J}A_j\prod_{j\notin J}B_j
-e_k(\rho)\prod_{j=1}^d B_j.
\]
Each \(S_k\) is exactly \(Z_dg_k\), where
\[
g_k(x)=\sum_{\substack{J\subseteq\{1,\ldots,d\}\\|J|=k}}
\prod_{j\in J}\phi(x_j)\prod_{j\notin J}\psi(x_j)
-e_k(\rho)\prod_{j=1}^d\psi(x_j).
\]
The torus is \(\mathbb T^{2d}=\mathbb R^{2d}/\mathbb Z^{2d}\), oriented by \(du_1\wedge dv_1\wedge\cdots\wedge du_d\wedge dv_d\). A transverse common zero means that the real derivative of \((\operatorname{Re}S_1,\operatorname{Im}S_1,\ldots,\operatorname{Re}S_d,\operatorname{Im}S_d)\) is invertible.

## Proof
**1. Exact one-coordinate preimages.** On the open strip \(0<u<1\), the second Zak factor equals \(B(u,v)=\psi(u)>0\). For \(0<u<1/2\), \(A(u,v)=\phi(u)>0\), so \(A/B\) lies on the positive real ray. At \(u=1/2\), \(A=0\). For \(1/2<u<1\), only the shifted \(n=1\) term of \(A\) survives and
\[
\frac{A(u,v)}{B(u,v)}=R(u)e^{2\pi i v},\qquad
R(u)=\frac{\phi(u-1)}{\psi(u)}.
\]
The logarithm of the radial factor is
\[
L(u):=\log R(u)=-\frac1{u-1/2}-\frac1{3/2-u}+\frac1u+\frac1{1-u},
\]
so
\[
L'(u)=\left(\frac1{(u-1/2)^2}-\frac1{u^2}\right)
+\left(\frac1{(1-u)^2}-\frac1{(3/2-u)^2}\right)>0.
\]
Both parentheses are strictly positive for \(1/2<u<1\), and \(R\) increases continuously from \(0\) to \(+\infty\). If \(B=0\) at an integer \(u\), then \(A\ne0\). Thus each \(\rho\in\mathbb C\setminus[0,\infty)\) has **one and only one** torus preimage \((u_\rho,v_\rho)\) under \(A/B\): \(u_\rho\in(1/2,1)\) solves \(R(u_\rho)=|\rho|\) and \(e^{2\pi i v_\rho}=\rho/|\rho|\). Its oriented real Jacobian is
\[
J_\rho=2\pi R(u_\rho)R'(u_\rho)
=2\pi|\rho|^2 L'(u_\rho)>0.
\]

**2. Exclusion of spurious zeros at the poles.** Introduce \(H=\prod_{j=1}^dB_j\) and the polynomial
\[
P_{u,v}(t)=\prod_{j=1}^d(B_jt-A_j).
\]
Its coefficient of \(t^{d-k}\) is \((-1)^k\) times the first sum in \(S_k\), for \(0\leq k\leq d\). Consequently \(S_1=\cdots=S_d=0\) is equivalent to
\[
P_{u,v}(t)=H\prod_{j=1}^d(t-\rho_j)
\quad\text{as polynomials in }t.
\]
For every \((u,v)\), the pair \((A_j,B_j)\ne(0,0)\), since the supports of \(\phi\) and \(\psi\) complement each other in the elementary way shown in Step 1. Thus every factor \(B_jt-A_j\) is a nonzero polynomial. If \(H=0\), the right-hand side would vanish identically while the left would not. Hence each common zero has \(H\ne0\), and we can divide by \(H\) to obtain
\[
\prod_{j=1}^d(t-A_j/B_j)=\prod_{j=1}^d(t-\rho_j).
\]
The two multisets of roots coincide. Since the \(\rho_j\) are pairwise distinct and have unique coordinate preimages, precisely the \(d!\) permutations of \(((u_{\rho_1},v_{\rho_1}),\ldots,(u_{\rho_d},v_{\rho_d}))\) are common zeros. There are no others, including on cell boundaries.

**3. Exact positive Jacobian.** At a common zero, write \(z_j=A_j/B_j\) and \(H=\prod B_j\). Derivatives of \(H\) disappear because \(e_k(z)-e_k(\rho)=0\), leaving
\[
dS=H\,D(e_1,\ldots,e_d)(z)\,D(z_1,\ldots,z_d).
\]
The complex determinant of the elementary-symmetric map is, up to sign, the Vandermonde \(\prod_{i<j}(z_i-z_j)\), so its real determinant is \(\prod_{i<j}|\rho_i-\rho_j|^2\). The coordinate quotient maps have positive real determinants from Step 1. Consequently the exact real Jacobian at **each** of the \(d!\) zeros is
\[
\boxed{\ 
\left(\prod_{j=1}^d\psi(u_{\rho_j})^{2d}\right)
\left(\prod_{1\leq i<j\leq d}|\rho_i-\rho_j|^2\right)
\left(\prod_{j=1}^d 2\pi|\rho_j|^2 L'(u_{\rho_j})\right)>0.
\ }
\]
All terms are independent of the permutation and strictly positive. Every common zero is therefore transverse and has index \(+1\).

**4. Sharp universal lower bound.** Any Zak-quasiperiodic smooth \(d\)-tuple defines a section of \(E=L_\mathrm{Zak}^{\oplus d}\) over \(\mathbb T^{2d}\), where the Zak line bundle has \(c_1(L_\mathrm{Zak})=\sum_{j=1}^d[du_j\wedge dv_j]\). By the Whitney formula,
\[
\int_{\mathbb T^{2d}}c_d(E)=
\int_{\mathbb T^{2d}}\left(\sum_{j=1}^d[du_j\wedge dv_j]\right)^d=d!.
\]
This last Chern-number calculation is present in the cited preceding work. The standard zero-counting theorem for the Euler class identifies it with the sum of local indices of any transverse section. Each index is \(+1\) or \(-1\), so there are at least \(d!\) distinct zeros. The explicit family above attains exactly \(d!\), all positively oriented. \(\square\)

## Verification
The accompanying self-contained `check.py` evaluates the explicit one-dimensional inverse function, computes elementary symmetric residuals for every permutation and checks the Vandermonde and positive-Jacobian expressions for \(d=1,2,3,4,5\), yielding counts \(1,2,6,24,120\). These finite tests are auxiliary; the unrestricted all-dimensional result follows from the preceding analytic proof. All necessary computations and function definitions are included above.

## Relationship to prior work
De Dios Pont, Liehr and Taylor (2026), Theorem 1.3, prove a common-zero obstruction for \(N\leq d\), calculate the nonzero top Chern class, and introduce the compactly supported one-dimensional pair \((\phi,\psi)\) together with a \((d+1)\)-coefficient product polynomial to build a zero-free collection. In particular their Chern calculation already gives the signed factorial count by the standard Euler zero theorem; **neither the lower bound by itself nor the coefficient basis is presented as new here**. The additional step proved here is a family of \(d\) coefficient constraints with arbitrary distinct prescribed roots in the slit plane, an exact global exclusion of extra or boundary solutions, and complete, sharp, all-positive transversality with a quantified Jacobian. Classical generic-section and Segre-degree arguments provide nearby abstract existence heuristics, but do not themselves provide the stated explicit compactly supported Zak windows and complete fiber formula.

## Limitations
The lower bound concerns *transverse* common zeros; a singular isolated zero can carry index greater than one, so this is **not** a universal cardinality bound for arbitrary nongeneric sections. The formula makes no claim about lower frame bounds at a lattice admitting common Zak zeros, global perturbation robustness without a quantified topology, or holomorphic Zak sections. The construction relies on smooth compactly supported windows and does not assert positivity or Gaussian shape of those windows. It gives an exact zero set for its specific \(d\)-tuple, not a classification of all minimizing tuples. Existing general intersection theory may yield alternative proofs of abstract attainability.

## References
1. J. de Dios Pont, L. Liehr, M. A. Taylor, *On the existence problem of regular Gabor frames*, arXiv:2606.26052, first posted 24 June 2026, especially Theorem 1.3, Section 3.1 (Chern class), and Section 3.2 (compactly supported coefficient construction). https://arxiv.org/abs/2606.26052 .
2. D. Auroux, *Symplectic Geometry*, Lecture 11, Section 1: transverse zero loci represent the top Chern/Euler class. https://studylib.net/doc/13664186/symplectic--geometry---lecture--11-%E2%86%92-let-e .
3. A. Horst, J. Lemvig, A. E. Videbeck, *On the non-frame property of Gabor systems with Hermite generators and the frame set conjecture*, *Applied and Computational Harmonic Analysis* 76 (2025), 101747, Section 4 (one-window Zak zero techniques). https://doi.org/10.1016/j.acha.2025.101747 .
