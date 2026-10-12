# The \(3-\sqrt{3}\) relaxation frontier for shuffle-once and IID equiangular Kaczmarz

## Finding

Let \(u_1=(1,0)^\mathsf T\), \(u_2=(-1/2,\sqrt{3}/2)^\mathsf T\), and \(u_3=(-1/2,-\sqrt{3}/2)^\mathsf T\). For any fixed \(0<\eta<2\), apply the relaxed Kaczmarz update \(e\mapsto P_i e\), where \(P_i=I_2-\eta u_i u_i^\mathsf T\), to the homogeneous consistent system \(u_i^\mathsf T e=0\) for all three rows. Begin with a random \(e_0\), independent of row choices, with \(\mathbb E[e_0e_0^\mathsf T]=I_2/2\). Compare (SS) one uniformly random permutation of the three rows, reused during every epoch, to (IID) independent uniformly selected rows with replacement at each individual update. Let \(S_K=\mathbb E\|e_{3K}^{\mathrm{SS}}\|^2\) and \(I_K=\mathbb E\|e_{3K}^{\mathrm{IID}}\|^2\) for every integer \(K\ge1\).

Write \(a(\eta)=1-\eta+\eta^2/2\), \(\eta_0=4\sqrt3-6\), and \(\eta_\star=3-\sqrt3\). Then \(I_K=a(\eta)^{3K}\) exactly, while

\[
\lim_{K\to\infty} S_K^{1/K}=R(\eta)=
\begin{cases}
(1-\eta)^3,&0<\eta\le\eta_0,\\[3pt]
\displaystyle\left(\frac{(2-\eta)(\eta^2+8\eta-8)+\eta^2\sqrt{\eta^2+12\eta-12}}{16}\right)^2,&\eta_0\le\eta<2.
\end{cases}
\]

The two branches agree at \(\eta_0\). The following trichotomy is **necessary and sufficient**, with no unstated genericity assumption:

\[
R(\eta)<a(\eta)^3\ \Longleftrightarrow\ 0<\eta<\eta_\star,
\qquad
R(\eta)=a(\eta)^3\ \Longleftrightarrow\ \eta=\eta_\star,
\qquad
R(\eta)>a(\eta)^3\ \Longleftrightarrow\ \eta_\star<\eta<2.
\]

In particular, for each \(0<\eta<\eta_\star\), SS has a strictly better exponential expected-squared-error rate and eventually smaller expected error than IID; for each \(\eta_\star<\eta<2\), the **opposite strict comparison** holds for sufficiently large \(K\). At the exact boundary only the exponential rates agree; finite-epoch errors need not agree.

The reversal is visible with no asymptotic approximation: at \(\eta=3/2\), the first epoch gives \(S_1=473/2048<125/512=I_1\), but after the second epoch \(S_2=586697/8388608>15625/262144=I_2\).

## Assumptions and scope

All arithmetic is over the real numbers. The system has three **unit-norm rows in dimension two** with pairwise absolute inner products \(1/2\) and tight-frame matrix \(\sum_{i=1}^3u_i u_i^\mathsf T=3I_2/2\). Its only solution is \(e=0\); the condition number of its normal matrix is one. The initial covariance condition, not any Gaussian assumption, is used to average the SS squared norm. The random permutation is sampled only once and then held fixed; IID sampling is independent at every row update. The assertions concern expected squared Euclidean error at *epoch endpoints* and its exponential rate as the integer epoch count tends to infinity, not a pathwise or finite-epoch uniform comparison. The endpoints \(\eta=0,2\) are excluded.

## Proof

**1. Exact IID law.** The rank-one orthogonal projector \(u_i u_i^\mathsf T\) is idempotent, hence
\[
P_i^\mathsf T P_i=I_2-(2\eta-\eta^2)u_i u_i^\mathsf T.
\]
Averaging uniformly over \(i\in\{1,2,3\}\) and using the tight-frame identity gives
\[
\frac13\sum_{i=1}^3P_i^\mathsf TP_i
=\bigl(1-\eta+\eta^2/2\bigr)I_2=a(\eta)I_2.
\]
Conditional expectation therefore multiplies \(\|e\|^2\) by \(a(\eta)\) at each IID step. Since \(\mathbb E\|e_0\|^2=1\), induction proves \(I_K=a(\eta)^{3K}\) for every \(K\ge1\).

**2. SS reduces to one deterministic product.** The three unoriented normal lines are the equally spaced projective directions \(0,\pi/3,2\pi/3\). Their orthogonal symmetries induce all six permutations of the lines. Because \(P_i\) depends on \(u_i\) only through \(u_i u_i^\mathsf T\), every three-factor epoch product is an orthogonal conjugate of \(T=P_3P_2P_1\). For the isotropic initial covariance,
\[
\mathbb E_{e_0}\|T_\pi^K e_0\|^2=\tfrac12\|T_\pi^K\|_F^2=\tfrac12\|T^K\|_F^2,
\]
where the last equality uses orthogonal conjugacy. Thus \(S_K=\|T^K\|_F^2/2\). By the finite-dimensional spectral-radius formula, \(\lim_{K\to\infty}S_K^{1/K}=\rho(T)^2\), even if \(T\) is nondiagonalizable at one parameter value.

**3. Exact characteristic polynomial.** Multiplying the three matrices, or expanding two-by-two determinants, gives
\[
T=
\begin{pmatrix}
\displaystyle\frac{(\eta-1)[3\eta^2-(\eta-4)^2]}{16}
&\displaystyle\frac{\sqrt3\eta^2}{8}\\[5pt]
\displaystyle\frac{\sqrt3\eta^2(\eta-1)}8
&\displaystyle 1-\frac{3\eta}{2}+\frac{3\eta^2}{8}
\end{pmatrix},
\]
so
\[
t:=\operatorname{tr}T=\frac{(\eta-2)(\eta^2+8\eta-8)}8,\quad
d:=\det T=-(\eta-1)^3,\quad
t^2-4d=\frac{\eta^4(\eta^2+12\eta-12)}{64}.
\]
The discriminant is negative for \(0<\eta<\eta_0\), and then the eigenvalues are complex conjugates with squared modulus \(d=(1-\eta)^3\). For \(\eta\ge\eta_0\), the trace is negative because \(-4+2\sqrt6<\eta_0\), and the dominant eigenvalue is the negative root \((t-\sqrt{t^2-4d})/2\). Substitution gives exactly the piecewise formula \(R(\eta)=\rho(T)^2\) stated above.

**4. Sharp sign comparison.** In the real-eigenvalue regime \(\eta_0\le\eta<2\), set \(b=a(\eta)^{3/2}>0\) and let \(\lambda_-\le\lambda_+\) be the real eigenvalues of \(T\). Since \(t<0\), \(\rho(T)=-\lambda_-\). If \(\eta\ge1\), then \(d\le0\), hence \(\lambda_+\ge0\). If \(\eta<1\), then both eigenvalues are negative, \(|\lambda_+|\le\sqrt d=(1-\eta)^{3/2}<b\), the last inequality following from \(a(\eta)>1-\eta\). Therefore \(b+\lambda_+>0\) throughout, and
\[
 b^2+tb+d=(b-\rho(T))(b+\lambda_+)
\]
has the sign of \(b-\rho(T)\). Moreover \(b^2+d>0\): this is immediate for \(\eta\le1\), while for \(1<\eta<2\) it follows from \(a(\eta)>\eta-1\), equivalently \((2-\eta)^2>0\). Because \(t<0\), the sign of \(b^2+tb+d\) is consequently the sign of \((b^2+d)^2-t^2b^2\). Its exact factorization is
\[
(b^2+d)^2-t^2b^2
=\frac{\eta^4(\eta-2)^2}{512}
(\eta^2-6\eta+6)
\bigl(7\eta^4-32\eta^3+84\eta^2-104\eta+52\bigr).
\]
The quartic \(Q(\eta)\) is positive for every real \(\eta\). Indeed, writing \(z=\eta-1\),
\[
Q(1+z)=z^2(7z^2-4z+1)+(29z^2-4z+7),
\]
where both parenthesized quadratics are strictly positive by completing the square. Therefore the sole comparison sign change for \(0<\eta<2\) occurs at the one root of \(\eta^2-6\eta+6\) in this interval, namely \(3-\sqrt3\). For \(0<\eta<\eta_0\), we already know \(\rho(T)^2=(1-\eta)^3<a(\eta)^3\), because \(a(\eta)=1-\eta+\eta^2/2>1-\eta\). This proves the complete trichotomy, including both boundaries.

**5. Exact two-epoch witness.** At \(\eta=3/2\), direct rational calculation gives \(S_1=473/2048\), \(I_1=125/512\), \(S_2=586697/8388608\), and \(I_2=15625/262144\). In particular \(S_2-I_2=86697/8388608>0\), exhibiting a finite-epoch reversal. All six SS orders yield the same error because of the conjugacy proved in step 2.

## Verification

Run `python verify.py` with SymPy available. The program checks the tight-frame identity; the exact characteristic polynomial, discriminant and comparison factorization; the positive-quartic decomposition; all six orderings for the first four powers at \(\eta=3/2\); and the exact second-epoch rational witness. Successful execution prints `VERIFY_OK exact polynomial, six-order invariance, and two-epoch witness`. The program performs finite symbolic identities and a finite witness check. Global validity of the rate trichotomy is proved analytically above, not inferred from sampled parameters.

## Relationship to prior work

Ahle, Bulatov, De Sa, and Ré (2026) analyze IID, single-shuffle, and flip-flop schemes for isotropic Gaussian high-dimensional data and derive asymptotic constant-factor differences, including relaxation dependence. Their hypotheses and limit regime do not imply a two-dimensional equiangular tight-frame comparison or its unique sharp overrelaxation threshold.

**A close same-object precursor:** Yun, Sra, and Jadbabaie (2021, Appendix A, equation (16)) explicitly introduced the very same three **rank-one equiangular matrices** (up to row relabeling) to compare a norm of the *mean of fixed-permutation powers* against a *fresh-permutation mean raised to a power*, primarily for relaxation at most one. This earlier equiangular construction is not new. Its comparison is between the operators \(\|\mathbb E_\pi T_\pi^K\|\) and \(\|(\mathbb E_\pi T_\pi)^K\|\), not between \(\mathbb E_{\pi,e_0}\|T_\pi^K e_0\|^2\) and independent with-replacement sampling. Its cited formulas do not imply the exact frontier \(3-\sqrt3\) or the finite-epoch mean-square reversal above.

Nguyen, Phan, and Kalagnanam (2026) establish prefix-variance and reversed-order sensitivity identities for structured shuffling, rather than a repeated three-row spectral-rate comparison. Standard IID Kaczmarz convergence results also do not compare against one order reused for every epoch. A distinct prior result on reshuffling of common-Hessian finite-sum quadratics concerns different component Hessians and re-randomizes at each epoch; its conclusion does not specialize to the present heterogeneous rank-one projectors and fixed permutation. These distinctions are about statements and implications, not merely titles. Equivalent work outside inspected sources remains possible.

## Limitations

The theorem is restricted to a three-row planar equiangular tight frame, homogeneous consistent equations, isotropic initial second moment, uniform single-shuffle and uniform IID sampling, and \(0<\eta<2\). It compares limiting exponential expected-squared-error rates, not all finite epochs or individual trajectories. At \(\eta=3-\sqrt3\) only rate equality is asserted. Extension to unequal row weights, noisy inconsistent systems, nonisotropic initial covariance, different frame sizes, random reshuffling at every epoch, and adaptive relaxation remains open here. The bibliographic originality assessment is not an exhaustive search of every unindexed or unavailable manuscript.

## References

1. Thomas Dybdahl Ahle, Yaroslav Bulatov, Christopher De Sa, Christopher Ré, *Stochastic Optimization Under Power-Law Spectra: Tight Bounds and Shuffling Analysis*, arXiv:2609.36271v1, submitted 2026-09-28, https://arxiv.org/html/2609.36271v1 (sections on shuffling schemes, asymptotic test loss, and Appendix F).
2. Chulhee Yun, Suvrit Sra, Ali Jadbabaie, *Can Single-Shuffle SGD be Better than Reshuffling SGD and GD?*, arXiv:2103.07079v1, submitted 2021-03-12, https://arxiv.org/html/2103.07079v1 (Section 3 and Appendix A, especially equation (16)).
3. Lam M. Nguyen, Dzung T. Phan, Jayant Kalagnanam, *Learning to Shuffle: Block Reshuffling and Reversal Schemes for Stochastic Optimization*, arXiv:2604.00260v1, submitted 2026-03-31, https://arxiv.org/html/2604.00260v1 (Sections 2–3 and Appendix A).
4. Robert M. Gower, Peter Richtárik, *Randomized Iterative Methods for Linear Systems*, SIAM Journal on Matrix Analysis and Applications 36 (2015), 1660–1690, https://arxiv.org/abs/1506.03296 (general IID randomized Kaczmarz framework).
