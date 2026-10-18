# A sharp mesh-grading reversal for periodic \(P_1\) BRAS mass preconditioning

## Finding

For a periodic one-dimensional mesh with \(n\geq 3\) cells, let \(M\) be the conforming, consistent \(P_1\) finite-element mass matrix and let \(B\) be the broken-space additive Schwarz (BRAS) inverse approximation formed from **exact two-node element mass inverses and multiplicity averaging**. If one cell has length \(\varepsilon>0\) and all other cells have length one, then, at every fixed \(n\geq3\), precisely two eigenvalues of \(BM\) grow on the scale \(\varepsilon^{-1}\) as \(\varepsilon\downarrow0\), while its other \(n-2\) eigenvalues remain bounded above and below by positive constants. Thus
\[
\kappa(BM)=\Theta(\varepsilon^{-1}),
\qquad
\kappa\bigl(\operatorname{diag}(M)^{-1}M\bigr)\leq3
\]
for every positive cell-length vector, where \(\kappa\) denotes the ratio of the largest to smallest positive eigenvalue.

Three cells are the smallest periodic example exhibiting this failure of grading robustness. For exactly three cells with cyclic lengths \((\varepsilon,1,1)\) and \(0<\varepsilon\leq1\), the complete BRAS and Jacobi spectra are
\[
\operatorname{spec}(BM)
=\left\{1,\;\frac{1}{2\varepsilon}+\frac7{12}+\frac{\varepsilon}{6},\;\frac{1}{6\varepsilon}+\frac7{12}+\frac{\varepsilon}{2}\right\},
\]
\[
\operatorname{spec}\bigl(\operatorname{diag}(M)^{-1}M\bigr)
=\left\{\frac32,\;\frac{2\varepsilon+1}{2(\varepsilon+1)},\;\frac{\varepsilon+2}{2(\varepsilon+1)}\right\}.
\]
Consequently
\[
\boxed{\kappa_{\mathrm B}(\varepsilon)=\frac{1}{2\varepsilon}+\frac7{12}+\frac{\varepsilon}{6}},
\qquad
\boxed{\kappa_{\mathrm J}(\varepsilon)=\frac{3(1+\varepsilon)}{1+2\varepsilon}}.
\]
There is a **unique reversal threshold** \(\varepsilon_*\in(0,1)\), the unique root there of
\[
4\varepsilon^3-20\varepsilon^2-17\varepsilon+6=0,
\qquad \varepsilon_*=0.2711405747281964\ldots .
\]
BRAS has the smaller condition number for \(\varepsilon>\varepsilon_*\), and Jacobi has the smaller condition number for \(0<\varepsilon<\varepsilon_*\). At the uniform mesh \(\varepsilon=1\), the condition numbers are \(5/4\) versus \(2\); for strong grading, their ratio is asymptotic to \(1/(6\varepsilon)\). No assertion is made about actual solve-time ratios.

## Assumptions and scope

Let the periodic domain be a circle of circumference \(\sum_{j=0}^{n-1}h_j\), divided into \(n\geq2\) distinct cells \(K_j\) of positive lengths \(h_j\), with periodic nodal degrees of freedom \(v_0,\ldots,v_{n-1}\) and cell \(K_j\) joining nodes \(j\) and \(j+1\) modulo \(n\). The cell restriction \(R_j\) selects the ordered pair of endpoint values. Define
\[
T=\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad
U=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},
\]
\[
M=\sum_{j=0}^{n-1}\frac{h_j}{6}R_j^{\mathsf T}TR_j,
\qquad
B=\sum_{j=0}^{n-1}\frac{1}{2h_j}R_j^{\mathsf T}UR_j.
\]
The formula for \(B\) is exactly \(D^{-1}P^{\mathsf T}M_{\mathrm{br}}^{-1}PD^{-1}\) with \(D=P^{\mathsf T}P=2I\), because the local mass inverse is \((2/h_j)U\). These definitions retain the two distinct cell contributions when \(n=2\) (both cells have the same two endpoints). Both \(M\) and \(B\) are symmetric positive definite. The spectrum of \(BM\) is real and positive, since \(BM\) is similar to \(M^{1/2}BM^{1/2}\). Here the spectral condition number is the ratio of extremal positive eigenvalues, not the Euclidean singular-value condition number of the nonsymmetric product \(BM\).

The first claim holds for each **fixed** integer \(n\geq3\) as \(h_0=\varepsilon\downarrow0\) and \(h_1=\cdots=h_{n-1}=1\); the implicit comparison constants may depend on \(n\). The exact transition specializes to \(n=3\) and \(0<\varepsilon\leq1\). The preconditioner is not a lumped-mass discretization; \(M\) remains the consistent mass matrix.

## Proof

**Elementwise Jacobi bound.** For each element the diagonal of its local mass matrix is \((h_j/3)I_2\). The eigenvalues of \(T/2\) are \(1/2\) and \(3/2\). Therefore, in quadratic-form order, each local mass contribution lies between one half and three halves of its local diagonal contribution. Summing over elements gives
\[
\frac12\operatorname{diag}(M)\preceq M\preceq\frac32\operatorname{diag}(M).
\]
Thus the eigenvalues of the diagonally preconditioned mass matrix lie in \([1/2,3/2]\), independently of grading, and their ratio is at most three.

**Exactly two divergent BRAS modes.** For \(n\geq3\), write
\[
M(\varepsilon)=M_0+\varepsilon F,
\qquad
B(\varepsilon)=B_0+\varepsilon^{-1}E,
\]
where \(F=R_0^{\mathsf T}TR_0/6\), \(E=R_0^{\mathsf T}UR_0/2\), and \(M_0,B_0\) sum the unit-length contributions from the other \(n-1\) cells. These cells form a connected path touching every node, so both \(M_0\) and \(B_0\) are strictly positive definite: each local two-node matrix is positive definite, and a vector in the common nullspace must vanish at every node of the path. The matrix \(E\) has exactly rank two.

Set \(H_\varepsilon=M(\varepsilon)^{1/2}B(\varepsilon)M(\varepsilon)^{1/2}\). Its decomposition into
\[
S_\varepsilon=M(\varepsilon)^{1/2}B_0M(\varepsilon)^{1/2},
\quad
H_\varepsilon=S_\varepsilon+\varepsilon^{-1}K_\varepsilon,
\quad
K_\varepsilon=M(\varepsilon)^{1/2}EM(\varepsilon)^{1/2}
\]
has the following properties: \(S_\varepsilon\) has eigenvalues uniformly bounded above and below by positive constants; \(K_\varepsilon\) has rank two, and its two positive eigenvalues converge to those of \(M_0^{1/2}EM_0^{1/2}\), which are strictly positive. By monotonicity of ordered eigenvalues under positive-semidefinite addition, the largest two eigenvalues of \(H_\varepsilon\) are bounded below by positive multiples of \(\varepsilon^{-1}\), and the operator norm of \(H_\varepsilon\) is \(O(\varepsilon^{-1})\). On the \((n-2)\)-dimensional nullspace of \(K_\varepsilon\), the Rayleigh quotient of \(H_\varepsilon\) equals that of \(S_\varepsilon\), which is uniformly bounded. The Courant–Fischer principle therefore bounds the first \(n-2\) eigenvalues from above. Their positive uniform lower bound follows from \(H_\varepsilon\succeq S_\varepsilon\). This proves the two-mode dichotomy and \(\kappa(BM)=\Theta(\varepsilon^{-1})\).

**Minimality.** On the two-cell periodic mesh with arbitrary positive lengths \(a,b\), both cell contributions couple the same two degrees of freedom. Since \(UT=3I\),
\[
M=\frac{a+b}{6}T,
\quad
B=\frac12\left(\frac1a+\frac1b\right)U,
\quad
BM=\frac{(a+b)^2}{4ab}I.
\]
Hence \(\kappa(BM)=1\) regardless of the two-cell grading. One-node periodic matrices are scalar, so cannot exhibit a condition-number separation either.

**Three-cell exact spectrum.** Label the short cell as joining nodes \(0,1\). Direct assembly gives
\[
M=\frac16\begin{pmatrix}
2(1+\varepsilon)&\varepsilon&1\\
\varepsilon&2(1+\varepsilon)&1\\
1&1&4
\end{pmatrix},\qquad
B=\begin{pmatrix}
1+\varepsilon^{-1}&-1/(2\varepsilon)&-1/2\\
-1/(2\varepsilon)&1+\varepsilon^{-1}&-1/2\\
-1/2&-1/2&2
\end{pmatrix}.
\]
Their product has characteristic polynomial
\[
(\lambda-1)\left(\lambda-\frac{6+7\varepsilon+2\varepsilon^2}{12\varepsilon}\right)
\left(\lambda-\frac{2+7\varepsilon+6\varepsilon^2}{12\varepsilon}\right).
\]
The corresponding diagonal-preconditioned characteristic polynomial factors with roots \(3/2\), \((2\varepsilon+1)/(2(\varepsilon+1))\), and \((\varepsilon+2)/(2(\varepsilon+1))\). For \(0<\varepsilon\leq1\), the first BRAS factor is the largest eigenvalue because the difference of the two nonunit factors equals \((1-\varepsilon^2)/(3\varepsilon)\). Both nonunit factors exceed one (their respective numerator differences from \(12\varepsilon\) are positive for positive \(\varepsilon\)). The smallest BRAS eigenvalue is therefore one. The smallest Jacobi eigenvalue is \((2\varepsilon+1)/(2(\varepsilon+1))\), and the largest is \(3/2\). This establishes the two exact condition-number formulas.

**Unique reversal.** Subtracting the Jacobi condition number from the BRAS condition number gives
\[
\kappa_{\mathrm B}-\kappa_{\mathrm J}
=\frac{4\varepsilon^3-20\varepsilon^2-17\varepsilon+6}{12\varepsilon(2\varepsilon+1)}.
\]
The numerator equals six at zero and minus twenty-seven at one, with derivative \(12\varepsilon^2-40\varepsilon-17<0\) throughout \([0,1]\). It consequently has exactly one zero in \((0,1)\), with the indicated sign change. The stated asymptotics follow by taking \(\varepsilon\downarrow0\).

## Verification

The accompanying `verify.py` uses only the Python standard library. Run `python3 verify.py` in the directory containing this document; the expected output begins with `PASS 2577 exact-and-assembly checks` and includes the 50-digit bisection value of \(\varepsilon_*\). It reconstructs the elementwise assembled matrices using exact rational arithmetic, checks the scalar two-cell identity on 576 meshes, checks both three-cell characteristic-polynomial factorizations on 401 rational meshes, and checks assembly identities and strict diagonal dominance on 1600 additional short-cell meshes. It also encloses the unique crossover by decimal bisection. The rank-two spectral argument and the universal-in-dimension claims are proved above, not inferred from any finite computation.

As independent decimal spot checks, at \(\varepsilon=1\) the BRAS/Jacobi condition numbers are \(1.25/2\); at \(\varepsilon=0.1\) they are \(5.6/2.75\); and at \(\varepsilon=0.01\) they are \(50.585/2.970588235294\ldots\). All quantities are spectral ratios of symmetric positive-definite pencils.

## Relationship to prior work

Krzysik, Southworth, and Wimmer (2026) introduce BRAS using exactly the broken-space inverse and multiplicity weights used here, prove positivity and a universal eigenvalue lower bound of one, and give an upper bound that scales with element-metric contrast (Section 2, especially Lemma 2/Corollary 2). Their experiments concern two- and three-dimensional finite elements and report improvements over Jacobi. The present calculation is a complementary sharp **necessity result** for contrast dependence: on the smallest nontrivial periodic one-dimensional mesh, BRAS becomes worse than Jacobi at an explicit nonuniformity threshold, and the BRAS spectral condition number grows linearly with inverse short-cell length. The original theorem allows this behavior; it does not state this lower-bound construction, the two divergent modes, or the exact reversal threshold. No contradiction with the paper's proven estimates or numerical reports is claimed.

Wathen's diagonal mass-matrix bounds (1987) and Miller's related analysis (1991) establish the classical robustness of diagonal preconditioning for low-order finite elements; the elementwise \([1/2,3/2]\) inequality above is a direct self-contained proof for this setting and is not claimed as new. Ainsworth and Jiang (2019, 2021) consider specialized high-order mass preconditioners that are different from multiplicity-averaged exact broken-element inverses. Their robustness statements do not provide the asserted BRAS reversal. The novelty asserted here is the explicit minimal grading obstruction and its sharp spectral comparison, not the BRAS definition or the older Jacobi bounds.

## Limitations

The sharp crossover constant pertains to periodic one-dimensional continuous nodal \(P_1\) mass matrices on three cells, with precisely one nonunit length. The \(n\)-cell divergence statement keeps \(n\) fixed as the smallest cell shrinks. No analogous universal statement is proved here for Dirichlet boundaries, nonperiodic meshes, higher polynomial order, vector finite elements, or practical solve time. For a nonnormal product \(BM\), its Euclidean singular-value condition number is not interchangeable with the SPD-pencil spectral condition number. The claimed literature distinction remains subject to unindexed sources, and one older diagonal-preconditioning source was accessible only through its abstract.

## References

1. O. A. Krzysik, B. S. Southworth, G. A. Wimmer, *Broken-space Additive Schwarz Mass Inverse Approximations and (Block) Preconditioning*, arXiv:2607.12138 (first posted 2026-07-13), https://arxiv.org/abs/2607.12138 . Accessible full text: https://academ.us/article/2607.12138/ .
2. A. J. Wathen, *Realistic Eigenvalue Bounds for the Galerkin Mass Matrix*, IMA Journal of Numerical Analysis 7 (1987), 449–457, https://doi.org/10.1093/imanum/7.4.449 .
3. K. Miller, *On the Mass Matrix Spectrum Bounds of Wathen and the Local Moving Finite Elements of Baines*, SIAM Journal on Numerical Analysis 29 (1992), https://doi.org/10.1137/0729006 .
4. M. Ainsworth and S. Jiang, *Preconditioning the Mass Matrix for High Order Finite Element Approximation on Triangles*, SIAM Journal on Numerical Analysis 57 (2019), https://doi.org/10.1137/18M1182450 .
5. M. Ainsworth and S. Jiang, *Preconditioning the Mass Matrix for High Order Finite Element Approximation on Tetrahedra*, SIAM Journal on Scientific Computing 43 (2021), https://doi.org/10.1137/20M1333018 .
