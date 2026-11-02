# Exact diagonal condition-number scaling for two-community equicorrelation matrices

## Finding
For every pair of integers \(m,n\geq2\), let \(0<b,c<1\), \(a>0\), and put
\[
r=1+(m-1)b,\quad s=1+(n-1)c,\quad \delta=1-b,\quad\varepsilon=1-c.
\]
Assume \(mn a^2<rs\), and consider the symmetric positive-definite two-community correlation matrix
\[
A=\begin{pmatrix}
\delta I_m+b\mathbf1_m\mathbf1_m^{\mathsf T}&a\mathbf1_m\mathbf1_n^{\mathsf T}\\
a\mathbf1_n\mathbf1_m^{\mathsf T}&\varepsilon I_n+c\mathbf1_n\mathbf1_n^{\mathsf T}
\end{pmatrix}.
\]
Among **all** positive diagonal matrices \(D\) with independently selectable diagonal entries, the spectral condition number \(\kappa_2(DAD)\) has a **unique minimizing scaling up to multiplication by a common positive scalar**, namely
\[
D_*=\operatorname{diag}(\sqrt{x_*}I_m,I_n).
\]
Define the quotient-balancing point \(x_0=s/r\), the fluctuation-balancing point \(x_E=\varepsilon/\delta\), and \(\operatorname{clip}(z;u,v)=\max\{u,\min\{v,z\}\}\) for \(u\le v\). Then
\[
\boxed{x_*=\begin{cases}
\operatorname{clip}\!\left(\dfrac{c(1-c)}{rc-ma^2};\,x_E,x_0\right),&x_E\le x_0,\quad rc>ma^2,\\[5pt]
x_0,&x_E\le x_0,\quad rc\le ma^2,\\[5pt]
\operatorname{clip}\!\left(\dfrac{bs-na^2}{b(1-b)};\,x_0,x_E\right),&x_E\ge x_0.
\end{cases}}
\]
At the shared boundary \(x_E=x_0\), all relevant prescriptions give \(x_*=x_0\). The exact optimal condition number is
\[
\boxed{\kappa_* =\frac{\lambda_+(x_*)}{\min\{\lambda_-(x_*),\delta x_*,\varepsilon\}},\qquad
\lambda_\pm(x)=\frac{rx+s\pm\sqrt{(rx-s)^2+4mna^2x}}2.}
\]
This class exhibits interior balancing against either community's fluctuation eigenvalue, in addition to the two boundary-balancing regimes.

An exact infinite subfamily illustrates why the scale is not merely an unmotivated tuning parameter: fix \(m=3\), \(b=1/10\), \(c=1/2\), and \(a^2=1/10\). For **every** \(n\ge2\),
\[
\boxed{x_*=5/6,\qquad\kappa_*=n+2.}
\]
Thus the optimal first-community scaling is independent of the size of the other community. For \(n=3\), the unit-diagonal Jacobi choice \(x=1\) has condition number \((16+\sqrt{106})/5>5=\kappa_*\).

## Assumptions and scope
All matrices and scalings are real. Each community contains at least two vertices. Within- and between-community correlations are **strictly positive**, the original diagonal entries equal one, and \(mn a^2<rs\) is the exact Schur-complement positive-definiteness condition. No claim is made for negative or zero correlations, singular boundary matrices, general block-diagonal preconditioners, nonlinear or indefinite problems, or noncongruence left/right scalings. The scalar normalization in \(D_*\) is immaterial because the spectral condition number is homogeneous under common multiplication of \(D\).

## Proof
**Step 1: spectral decomposition.** For the block-constant candidate \(D_x=\operatorname{diag}(\sqrt x I_m,I_n)\), the \((m-1)\)-dimensional first-community fluctuation space has eigenvalue \(\delta x\); the \((n-1)\)-dimensional second-community fluctuation space has eigenvalue \(\varepsilon\). On the two-dimensional normalized-community-constant subspace, the matrix is
\[
Q(x)=\begin{pmatrix}rx&a\sqrt{mnx}\\a\sqrt{mnx}&s\end{pmatrix},
\]
with eigenvalues \(\lambda_\pm(x)\) above. The assumptions imply \(Q(x)\succ0\). Since \(r>\delta\), \(s>\varepsilon\), and \(a>0\), its Perron eigenvalue obeys \(\lambda_+(x)>\max\{\delta x,\varepsilon\}\). Consequently
\[
\kappa_2(D_xAD_x)=\max\left\{\frac{\lambda_+(x)}{\lambda_-(x)},\frac{\lambda_+(x)}{\delta x},\frac{\lambda_+(x)}{\varepsilon}\right\}.
\]

**Step 2: global reduction and rigidity, not an imposed symmetry assumption.** The minimization over all positive diagonal \(D\) is equivalent to minimizing \(k\) subject to the existence of a positive diagonal \(H\) with \(H\preceq A\preceq kH\). To see the equivalence, normalize any scaled matrix \(B=DAD\) by its least eigenvalue \(\ell\), and take \(H=\ell D^{-2}\); conversely \(H^{-1/2}AH^{-1/2}\) has eigenvalues in \([1,k]\) whenever the inequalities hold. Average the feasible \(H\)'s diagonal entries over independent coordinate permutations within the two communities. The average \(\bar H\) remains feasible and is constant on each community. This proves that the global optimum is attained in the displayed one-parameter family.

It also proves **unrestricted uniqueness**. At the optimal \(k=\kappa_*\), the averaged scaling is optimal, and its spectrum must attain both endpoints \(1\) and \(k\); otherwise its condition number would be smaller than the optimum. The largest eigenvector of \(\bar H^{-1/2}A\bar H^{-1/2}\) is strictly positive by Perron–Frobenius because all entries of \(A\) are positive. Write \(w>0\) for the corresponding generalized eigenvector, so \((k\bar H-A)w=0\). Every permuted feasible \(H_\pi\) gives \(kH_\pi-A\succeq0\), and their average is \(k\bar H-A\). Hence each nonnegative quadratic form \(w^{\mathsf T}(kH_\pi-A)w\) vanishes; positive semidefiniteness gives \((kH_\pi-A)w=0\). Taking the identity permutation and subtracting the equation for \(\bar H\) yields \((H-\bar H)w=0\). Since \(H-\bar H\) is diagonal and \(w\) has no zero coordinate, \(H=\bar H\). Thus every global optimizer is community-constant, not merely some optimizer. The next step gives a unique ratio.

**Step 3: three monotonic spectral branches.** Put
\[
f_0(x)=\lambda_+(x)/\lambda_-(x),\quad f_1(x)=\lambda_+(x)/(\delta x),\quad f_2(x)=\lambda_+(x)/\varepsilon.
\]
The determinant of \(Q(x)\) is \(x(rs-mna^2)\). Therefore \(f_0\) is strictly decreasing on \((0,x_0)\) and increasing on \((x_0,\infty)\): it is an increasing function of the normalized trace \((r\sqrt x+s/\sqrt x)/\sqrt{rs-mna^2}\), uniquely minimized at \(x_0=s/r\). Meanwhile \(f_1\) is strictly decreasing, because \(\lambda_+(x)/x\) is the Perron eigenvalue of
\[
\begin{pmatrix}r&a\sqrt{mn/x}\\a\sqrt{mn/x}&s/x\end{pmatrix},
\]
whose nonconstant positive entries strictly decrease in \(x\). Similarly \(f_2\) strictly increases because the positive entries of \(Q(x)\) increase in \(x\).

When \(x_E\le x_0\), the maximum of \(f_0,f_1,f_2\) decreases to the interval \([x_E,x_0]\) and increases after it; on that interval the relevant competition is \(\max\{f_0,f_2\}\), with one decreasing and the other increasing. They coincide precisely when \(\lambda_-(x)=\varepsilon\). The determinant identity \(\det(Q(x)-\varepsilon I_2)=0\) gives
\[
x=\frac{\varepsilon(s-\varepsilon)}{r(s-\varepsilon)-mna^2}
=\frac{c(1-c)}{rc-ma^2}.
\]
If \(rc\le ma^2\), this crossing is absent at positive \(x\) and the unique minimum on the interval is \(x_0\). Otherwise clipping the crossing to \([x_E,x_0]\) gives the first two lines of the formula.

When \(x_E\ge x_0\), the optimum lies in \([x_0,x_E]\), where the competition is \(\max\{f_0,f_1\}\). Equality occurs exactly when \(\lambda_-(x)=\delta x\), equivalently \(\det(Q(x)-\delta xI_2)=0\), giving
\[
x=\frac{s-mna^2/(r-\delta)}\delta
=\frac{bs-na^2}{b(1-b)}.
\]
Clipping to \([x_0,x_E]\) gives the final line. Strict monotonicity on either side of the chosen point establishes uniqueness, including at all regime boundaries.

**Step 4: exact subfamily.** For \(m=3\), \(b=1/10\), \(c=1/2\), and \(a^2=1/10\), one has \(r=6/5\), \(s=(n+1)/2\), \(x_E=5/9\), \(x_0=5(n+1)/12\), and \(c(1-c)/(rc-ma^2)=5/6\). For every \(n\ge2\), the latter lies strictly between \(x_E\) and \(x_0\), and \(rs-mna^2>0\). At \(x=5/6\), the quotient eigenvalues are \(1/2\) and \((n+2)/2\), while the fluctuation eigenvalues are \(3/4\) and \(1/2\). Therefore \(\kappa_*=n+2\). At \(n=3,x=1\), the largest quotient eigenvalue is \((16+\sqrt{106})/10\) and the least full eigenvalue is \(1/2\), giving the claimed strict Jacobi gap.

## Verification
Run \(\texttt{python verify.py}\) with Python 3, NumPy, SciPy and SymPy. The attached standalone verifier checks an exact rational six-dimensional instance and the closed-form saturation family; it compares the formula against direct eigenvalues on a structured grid and against randomized scalar and unrestricted diagonal searches. On the packaged source it passed **17,287 assertions**. These finite checks do not replace any of Steps 1–4, and a numerical optimizer result is not an infinity-wide certificate.

## Relationship to prior work
The numerical linear-algebra and control literature establishes general Euclidean condition-number scaling formulations, iterative equilibration heuristics and unrestricted block-diagonal preconditioning theory; see the references. Braatz–Morari's convex formulation allows general scaling to be computed but does not provide the two-community closed-form phase rule in the inspected treatment. Takapoui–Javadi discuss diagonal-equilibration heuristics and graph-projection splitting, not this exact optimum. Kolotilina's block-diagonal congruence results allow arbitrary nonsingular transformations *inside each community*, a strictly larger admissible set than positive diagonal scaling; their block-Jacobi result therefore does not imply the restricted optimum or its three-way fluctuation/quotient balance. A one-hub equicorrelation specialization has only one nontrivial fluctuation subspace, whereas the present theorem has two. This distinction prevents that special case from determining the two-community regime classification. The inaccessible full text of Shapiro's 1985 work remains a specific possible earlier-coverage risk; absence of a matching title or search result does not establish novelty.

## Limitations
The theorem applies only to strictly positive correlations with two exchangeable groups and symmetric positive diagonal congruence. It does not imply a universal rule for generic SPD matrices or for full block preconditioners. All originality comparisons are literature-limited; the full text of Shapiro (1985) and all earlier specialized cases have not been exhaustively verified. Independent mathematical validation has not been performed.

## References
1. R. Takapoui and H. Javadi, *Preconditioning via Diagonal Scaling*, arXiv:1610.03871v1, publicly submitted 2016-10-12, https://arxiv.org/abs/1610.03871.
2. R. D. Braatz and M. Morari, *Minimizing the Euclidean Condition Number*, SIAM Journal on Control and Optimization 32 (1994), 1763–1768, https://doi.org/10.1137/S0363012992238680.
3. A. Shapiro, *Optimal Block Diagonal \(\ell_2\)-Scaling of Matrices*, SIAM Journal on Numerical Analysis 22 (1985), 81–94, https://doi.org/10.1137/0722005.
4. L. Yu. Kolotilina, *A Class of Optimally Conditioned Block \(2\times2\) Matrices*, Journal of Mathematical Sciences 121 (2004), 2474–2480, https://doi.org/10.1023/B:JOTH.0000026285.08558.74.
5. L. Yu. Kolotilina, *Optimally Conditioned Block Matrices*, Linear Algebra and its Applications 340 (2002), 55–67, https://doi.org/10.1016/S0024-3795(01)00412-8.
