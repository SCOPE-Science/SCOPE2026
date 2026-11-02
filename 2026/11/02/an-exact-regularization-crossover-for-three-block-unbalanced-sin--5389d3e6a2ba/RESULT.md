# An exact regularization crossover for three-block unbalanced Sinkhorn on balanced kernels

## Finding

Fix an integer \(n\ge2\), two positive parameters \(\rho,\varepsilon\), uniform unit-mass marginals \(\alpha_i=\beta_j=1/n\), and a finite cost matrix \(C\). Suppose the strictly positive Gibbs matrix \(K_{ij}=\exp(-C_{ij}/\varepsilon)\) has identical row and column sums \(\kappa>0\). Write
\[
W=K/\kappa,\qquad \tau=\frac{\rho}{\rho+\varepsilon},\qquad s=\left\|W\big|_{\mathbf1^\perp}\right\|_2.
\]
Since \(W\) is strictly positive and doubly stochastic, \(0\le s<1\). For **one complete sweep**, performing first the exact \(g\)-coordinate maximization and then the exact \(f\)-coordinate maximization, denote the usual two-block algorithm by F. Denote by G the alternative three-block algorithm whose third operation maximizes the same dual objective over the common translation \((f,g)\mapsto(f+\delta\mathbf1,g-\delta\mathbf1)\).

At the unique dual optimum, the Jacobian spectral radii of these algorithms, both measured on the *recovered physical dual potentials*, are exactly
\[
\boxed{q_F=\tau^2,\qquad
q_G=\tau^2\max\left\{\frac{\varepsilon}{2\rho},s^2\right\}.}
\]
The F uniform-mode eigenvalue is \(\tau^2\), while the G uniform-mode eigenvalue is \(-\tau(1-\tau)/2\), and their nonuniform nonzero eigenvalues agree: they are \(\tau^2\) times the squared nontrivial singular values of \(W\). The remaining eigenvalues are zero, corresponding to the overwritten coordinate block (and possibly to singularities of \(W\)). In particular, because \(s<1\),
\[
q_G<q_F\iff\varepsilon<2\rho,\quad
q_G=q_F\iff\varepsilon=2\rho,\quad
q_G>q_F\iff\varepsilon>2\rho.
\]
The G dominant-mode identity switches at the separate kernel-dependent threshold \(\varepsilon=2\rho s^2\). These assertions hold for all such positive **nonsymmetric** as well as symmetric kernels.

For example, set \(\rho=1\), and \(W=\begin{pmatrix}3/4&1/4\\1/4&3/4\end{pmatrix}\), with \(K=W\). When \(\varepsilon=1\), the F and G rates are \(1/4\) and \(1/8\); when \(\varepsilon=3\), they are \(1/16\) and \(3/32\), respectively. Thus the method with the extra scalar maximization is strictly slower by the local spectral metric in the latter case.

## Assumptions and scope

The finite-dimensional KL unbalanced-transport dual for the stated unit-mass marginals is
\[
\mathcal D(f,g)=-\rho\sum_i\alpha_i\big(e^{-f_i/\rho}-1\big)
-\rho\sum_j\beta_j\big(e^{-g_j/\rho}-1\big)
-\varepsilon\sum_{ij}\alpha_i\beta_j
\big(e^{(f_i+g_j-C_{ij})/\varepsilon}-1\big).
\]
All potential vectors are real and finite. Strict positivity of the kernel and marginals ensures smoothness and strict concavity of this dual; therefore its optimum is unique. The row-and-column balancing assumption holds, for example, for strictly positive circulant kernels and many translation-invariant periodic costs; symmetry of \(K\) is *not* assumed. Both algorithms use the same ordering of the two full block operations; G adds one exact scalar maximization. The comparison is **local Jacobian spectral radius per complete sweep**, not a claim about finite-iteration error norms or computational time.

## Proof

**1. Fixed point and first two block derivatives.** For any vector \(v\), the exact g-update is
\[
T_g(v)_j=-\varepsilon\tau\log\left(\frac1n\sum_iK_{ij}e^{v_i/\varepsilon}\right),
\]
and the f-update is \(T_f(u)_i=-\varepsilon\tau\log\left(n^{-1}\sum_jK_{ij}e^{u_j/\varepsilon}\right)\). The identical row/column sums force the dual optimum to be constant:
\[
f^*=g^*=c\mathbf1,\qquad
c=-\frac{\varepsilon\rho}{\varepsilon+2\rho}\log(\kappa/n).
\]
Indeed these constants satisfy both first-order optimality equations, and strict concavity excludes other optima. Direct differentiation of the two log-sum-exp functions at this point gives
\[
DT_g(c\mathbf1)=-\tau W^{\mathsf T},\qquad
DT_f(c\mathbf1)=-\tau W.
\]
Thus the F complete-sweep map on pairs \((f,g)\) has, in the coordinate order \((f,g)\), derivative
\[
J_F=\begin{pmatrix}\tau^2WW^{\mathsf T}&0\\-\tau W^{\mathsf T}&0\end{pmatrix}.
\]
Since \(W\) is doubly stochastic, its singular vectors split into the constant vector and the orthogonal complement. The nonzero eigenvalues are those of \(\tau^2WW^{\mathsf T}\), including the constant-mode eigenvalue \(\tau^2\); all others have modulus at most \(\tau^2s^2\). This proves \(q_F=\tau^2\).

**2. Exact translation update.** For any two vectors \((u,v)\), strictly concave maximization of \(\mathcal D(u+\delta\mathbf1,v-\delta\mathbf1)\) gives the unique shift
\[
\delta(u,v)=\frac{\rho}{2}\log\frac{n^{-1}\sum_i e^{-u_i/\rho}}{n^{-1}\sum_j e^{-v_j/\rho}}.
\]
At the constant optimum, the differential is
\[
D\delta[du,dv]=\frac12\big(\overline{dv}-\overline{du}\big),
\qquad \overline{w}=\frac1n\sum_i w_i.
\]
For the first two raw operations, \(du=\tau^2WW^{\mathsf T}df\) and \(dv=-\tau W^{\mathsf T}df\). Hence
\[
D\delta=-\frac{\tau(1+\tau)}2\overline{df}.
\]
On zero-mean variations the shift derivative vanishes. On constant variations \(df=m\mathbf1\), after shifting \(u\) up and \(v\) down, both recovered means equal \(-\tau(1-\tau)m/2\). Consequently the G upper-left Jacobian block acts as \(\tau^2WW^{\mathsf T}\) on \(\mathbf1^\perp\), and by \(-\tau(1-\tau)/2\) on the constant direction. The other input block is overwritten at each sweep. Thus its full Jacobian eigenvalues are the claimed values plus zeros.

**3. Strict singular gap and crossover.** Since each entry of \(W\) is positive and its row and column sums are one, Jensen's inequality gives \(\|Wz\|_2\le\|z\|_2\), with equality only for constant \(z\). Compactness of the unit sphere in \(\mathbf1^\perp\) makes the inequality strict uniformly there, so \(s<1\). The G uniform multiplier has absolute value \(\tau(1-\tau)/2=\tau^2\varepsilon/(2\rho)\). Taking the maximum with its nonuniform eigenvalue moduli yields \(q_G\). Comparing this maximum to \(q_F=\tau^2\), with \(s^2<1\), proves the exact three-way threshold and its equality case.

## Verification

Run `python verify.py` with `numpy` installed (see `requirements.txt`). The executable independently evaluates finite-difference Jacobians of both *nonlinear* full-sweep maps for strictly positive, potentially nonsymmetric doubly stochastic kernels in dimensions two, three, and five, at seven positive regularization ratios each. It compares all 42 measured spectral radii to the formulas and checks a rational two-point example. A successful run ends with `VERIFY_OK: all 42 independent finite-difference Jacobians; exact 2x2 rate; sharp crossover`. The complete all-dimension theorem is established by the proof, not inferred from this finite numerical test.

## Relationship to prior work

Séjourné, Vialard and Peyré (2022, Appendix B.6) introduce precisely the three-block G-Sinkhorn procedure, contrast it experimentally with F-Sinkhorn, and propose an approximate regularization-dependent rule of thumb. Their H-Sinkhorn variant is a different solver. The present calculation identifies the exact local F-versus-G spectral crossover \(\varepsilon=2\rho\) **on the stated balanced-kernel class**, including a negative mass-mode multiplier; it neither reclaims the original solver nor asserts the same rule for arbitrary kernels. The earlier two-block generalized scaling literature of Chizat et al. and the KL unbalanced Sinkhorn convergence analysis of Séjourné et al. establish the underlying update and contraction framework, but the inspected material did not supply this exact three-block spectral comparison. Conventional balanced Sinkhorn spectral facts are not a proof of the negative G uniform mode with positive KL mass penalties.

## Limitations

The condition that every row and every column of the Gibbs matrix sum to the same \(\kappa\) and the uniform-marginal assumption are essential for this simple spectral decomposition. The exact crossover is not asserted for arbitrary nonuniform data, unequal marginal penalties, sparse or zero kernels, or other divergences. Jacobian spectral radius governs local asymptotic linear behavior (subject to standard local differentiability) rather than finite-horizon monotonicity or wall-clock speed. Near a defective/degenerate or zero singular mode, finite-step transients can differ. No independent priority assessment or external audit has been performed.

## References

1. T. Séjourné, F.-X. Vialard and G. Peyré, *Faster Unbalanced Optimal Transport: Translation invariant Sinkhorn and 1-D Frank-Wolfe*, AISTATS 2022, Appendix B.6, https://proceedings.mlr.press/v151/sejourne22a/sejourne22a.pdf ; first preprint 2022-01-03, https://arxiv.org/abs/2201.00730 .
2. T. Séjourné, J. Feydy, F.-X. Vialard, A. Trouvé and G. Peyré, *Sinkhorn Divergences for Unbalanced Optimal Transport*, 2019, https://arxiv.org/abs/1910.12958 .
3. L. Chizat, G. Peyré, B. Schmitzer and F.-X. Vialard, *Scaling Algorithms for Unbalanced Transport Problems*, 2016, https://arxiv.org/abs/1607.05816 .
