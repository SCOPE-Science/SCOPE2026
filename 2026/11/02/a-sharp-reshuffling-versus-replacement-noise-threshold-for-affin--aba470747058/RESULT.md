# A sharp reshuffling-versus-replacement noise threshold for affine stochastic extragradient

## Finding

For two affine monotone saddle-point operators with equal skew part and opposite nonzero offsets, the same-sample stochastic extragradient (SEG) algorithm admits an exact finite-epoch comparison between uniform with-replacement sampling and independent random reshuffling. Although each stochastic SEG step is contractive, reshuffling is not uniformly preferable. Its mean-square noise is no larger than with replacement for **every** offset and **every** positive epoch exactly when the maximum nondimensional frequency is at or below an explicit threshold. A mode strictly above that threshold gives strictly more modal noise under reshuffling whenever its offset projection is nonzero.

Let \(J\in\mathbb R^{2m\times2m}\) be an invertible real skew-symmetric matrix. Choose an orthogonal decomposition into invariant two-dimensional rotation planes \(E_j\), with positive rotation frequencies \(\omega_j\). Fix \(\kappa>1\), step \(\eta>0\), and \(v\in\mathbb R^{2m}\). Set \(F_{+}(z)=Jz+v\), \(F_{-}(z)=Jz-v\). These monotone, affine, Lipschitz operators average to \(Jz\), whose unique zero is the origin.

Write \(t_j=\eta\omega_j\) and assume
\[
0<t_j<\frac{\sqrt{2\kappa-1}}{\kappa}\qquad(1\le j\le m).
\]
For \(P_j\) the orthogonal projection onto \(E_j\), define
\[
r_j^2=(1-\kappa t_j^2)^2+t_j^2,\quad
 g_j=\eta^2(1+\kappa^2t_j^2)\|P_jv\|^2,\quad
 q_j=\frac{t_j^2(1+\kappa^2t_j^2)}{1+r_j^2}.
\]
Every \(r_j\) lies strictly between zero and one. Starting both methods at the same deterministic \(z_0\), with an independent fair reshuffle in every two-step epoch, for each integer \(k\ge1\) their exact endpoint errors are
\[
\begin{aligned}
\mathbb E\|Z^{\mathrm{iid}}_{2k}\|^2
 &=\|M^{2k}z_0\|^2+\sum_{j=1}^m g_j\frac{1-r_j^{4k}}{1-r_j^2},\\
\mathbb E\|Z^{\mathrm{RR}}_{2k}\|^2
 &=\|M^{2k}z_0\|^2+\sum_{j=1}^m g_j\frac{1-r_j^{4k}}{1-r_j^2}q_j,
\end{aligned}
\]
where \(M=I-\eta J+\kappa\eta^2J^2\). The same formulas with \(r_j^{4k}\) set to zero give the stationary mean-square errors of the epoch-end chains.

For each fixed \(J,\eta,\kappa\) satisfying the strict stability assumption, the following criterion is necessary and sufficient:
\[
\mathbb E\|Z^{\mathrm{RR}}_{2k}\|^2\le\mathbb E\|Z^{\mathrm{iid}}_{2k}\|^2
\quad\text{for every }z_0,v\text{ and every }k\ge1
\quad\Longleftrightarrow\quad
\eta\max_j\omega_j\le\frac1{\sqrt\kappa}.
\]
For any mode with \(1/\sqrt\kappa<t_j<\sqrt{2\kappa-1}/\kappa\), taking \(v\ne0\) entirely in that plane makes the reshuffling mean-square error strictly larger at **every** positive epoch and at stationarity. The exact modal noise ratio satisfies
\[
q_j-1=\frac{2(\kappa t_j^2-1)}{1+r_j^2}.
\]
Thus the crossover lies strictly inside the individually contractive step range for every \(\kappa>1\).

In particular, the affine step ratio \(\kappa=4\) used by Emmanouilidis, Vidal, and Loizou has contraction range \(0<t<\sqrt7/4\) and crossover \(t=1/2\). On a single standard rotation plane with \(\eta=3/5\) and \(\|v\|=1\), the exact stationary errors are
\[
V_{\mathrm{iid}}=\frac{169}{31},\qquad
V_{\mathrm{RR}}=\frac{257049}{30101},\qquad
\frac{V_{\mathrm{RR}}}{V_{\mathrm{iid}}}=\frac{1521}{971}>1.
\]
The modal ratio tends to \(2-1/\kappa\) from below as the contractive upper step boundary is approached. This is a **noise-floor** distinction, not a failure of the deterministic SEG step to contract.

## Assumptions and scope

The update is the **same-sample** SEG stage \(z^+=z-\eta F_{\epsilon}(z-\kappa\eta F_{\epsilon}(z))\), so both evaluations in a stage use the same component. For with-replacement sampling, signs for the \(2k\) stages are independent fair \(\pm1\). For reshuffling, each two-stage epoch uses signs \((\epsilon_k,-\epsilon_k)\), where the \(\epsilon_k\) are independent fair signs. Both schemes use the same number of component-gradient evaluations per epoch. All expectations are over the indicated sampling; the initial state and parameters are deterministic.

A real skew-symmetric matrix is orthogonally block-diagonalizable into planar rotation blocks; invertibility rules out zero frequencies. Each affine component is monotone because \(\langle J(z-w),z-w\rangle=0\). In the canonical variables \(z=(x_1,y_1,\ldots,x_m,y_m)\), the two components also arise from convex-concave bilinear-plus-linear games, for example \(f_{\pm}(x,y)=-\sum_j\omega_jx_jy_j\pm\sum_j(v_{x,j}x_j-v_{y,j}y_j)\). The expected iterates converge to zero. For nonzero \(v\), the iterates themselves do not converge to zero in \(L^1\) or \(L^2\) even at epoch endpoints: the displayed limiting second moments are positive, and the update \(z^+=Mz+\epsilon d\) with \(\|M\|_2<1\) bounds the entire trajectory uniformly.

## Proof

**1. Exact one-stage recurrence.** For \(F_{\epsilon}(z)=Jz+\epsilon v\), expand the extrapolation and evaluate with the **same** sign:
\[
\begin{split}
z^+&=z-\eta\big[J(z-\kappa\eta(Jz+\epsilon v))+\epsilon v\big]\\
&=(I-\eta J+\kappa\eta^2J^2)z-\epsilon\eta(I-\kappa\eta J)v\\
&=Mz+\epsilon d,
\end{split}
\]
where \(d=-\eta(I-\kappa\eta J)v\). Both algorithms have the same linear part \(M\).

**2. Spectral contraction and noise factors.** On a rotation plane \(E_j\), write \(J=\omega_jR\) with \(R^{\mathsf T}=-R\) and \(R^2=-I\). Then
\[
M_j=(1-\kappa t_j^2)I-t_jR,
\quad M_j^{\mathsf T}M_j=r_j^2I,
\quad (M_j-I)^{\mathsf T}(M_j-I)=t_j^2(1+\kappa^2t_j^2)I.
\]
Similarly \(\|P_jd\|^2=g_j\). Expansion gives \(1-r_j^2=t_j^2(2\kappa-1-\kappa^2t_j^2)>0\). Invertibility and positive step give \(r_j>0\).

**3. With-replacement moments.** Independent centered signs in \(Z_{n+1}=MZ_n+\epsilon_nd\) eliminate all cross terms against other signs and the deterministic term. Orthogonality of rotation planes and \(\|M_j^\ell w\|^2=r_j^{2\ell}\|w\|^2\) yield, at time \(n=2k\),
\[
\mathbb E\|Z^{\mathrm{iid}}_{2k}\|^2
=\|M^{2k}z_0\|^2+\sum_jg_j\sum_{\ell=0}^{2k-1}r_j^{2\ell}
=\|M^{2k}z_0\|^2+\sum_jg_j\frac{1-r_j^{4k}}{1-r_j^2}.
\]

**4. Reshuffling moments.** One random permutation of two components produces the pair \((\epsilon_k,-\epsilon_k)\), hence exactly
\[
Z_{2(k+1)}^{\mathrm{RR}}=M^2Z_{2k}^{\mathrm{RR}}+\epsilon_k(M-I)d.
\]
The \(\epsilon_k\) are independent and centered between epochs. Repeating the preceding calculation, now with \(k\) pairs and pair multiplier \(M^2\), yields
\[
\mathbb E\|Z^{\mathrm{RR}}_{2k}\|^2
=\|M^{2k}z_0\|^2+
\sum_jg_jh_j\frac{1-r_j^{4k}}{1-r_j^4},
\quad h_j=t_j^2(1+\kappa^2t_j^2).
\]
Since \(1-r_j^4=(1-r_j^2)(1+r_j^2)\), this is the claimed \(q_j\)-weighted formula.

**5. Sharp threshold.** Direct subtraction gives
\[
h_j-(1+r_j^2)=2(\kappa t_j^2-1).
\]
Each modal summand multiplying \(q_j-1\) has nonnegative weight, and is strictly positive when \(P_jv\ne0\), for all \(k\ge1\). Hence the reshuffling error is no larger than the with-replacement error for all offsets if and only if every \(t_j\le1/\sqrt\kappa\). If a mode violates the bound, choose \(v\) entirely in it to reverse the inequality at every epoch. Conversely the nonpositive sign of every difference term proves the universal assertion. The two boundaries obey \(1/\sqrt\kappa<\sqrt{2\kappa-1}/\kappa\) precisely because \(\kappa>1\). This establishes sharpness without limiting or simulation arguments.

**6. Stationary limit and example.** As \(\|M\|_2<1\), both epoch-end recurrences are affine contractions driven by independent, bounded epoch innovations. The stationary distribution is the law of the convergent sum of the past innovations weighted by successive powers of \(M^2\). Starting from any fixed initialization gives the same limiting law since the deterministic initial-state term tends to zero. Set \(\kappa=4\), \(\omega=1\), \(\eta=3/5\), \(\|v\|=1\). Substitution gives \(r^2=346/625\), \(g=1521/625\), \(1-r^2=279/625\), and \(q=1521/971\), yielding the exact fractions stated. To check the limiting ratio from below, put \(u=t^2\) and \(u_b=(2\kappa-1)/\kappa^2\). The difference \((2-1/\kappa)-q\) equals \((u_b-u)\kappa[2-(\kappa-1)u]/(1+r^2)\), positive for \(u<u_b\) and zero at \(u_b\).

## Verification

Run the accompanying standalone Python 3 standard-library program `verify.py`. It reconstructs the two function evaluations of each stage rather than applying the claimed matrix recurrence as the test oracle. With `fractions.Fraction`, it exhaustively enumerates every sign history through four epochs for four exact rational test families (32 uniform-history expectations). It compares the enumerations to the closed formulas, including one mixed-frequency four-dimensional case straddling the threshold, and validates the planar rational stationary example. Its expected message is:

`VERIFY_OK 32 exact uniform-history moments; source-ratio threshold; mixed-frequency and rational stationary witness`

These finite exact computations are supporting checks only. The proof above, not enumeration, establishes the assertions for arbitrary dimensions, frequencies, offsets and positive epoch counts.

## Relationship to prior work

Emmanouilidis, Vidal and Loizou (2024), Algorithm 1 and the affine analysis surrounding Theorem 2.2, introduce and study SEG with independent random reshuffling each epoch; their affine step-size choice includes \(\gamma_2=4\gamma_1\), the special case \(\kappa=4\) here. They give convergence bounds and examples where reshuffling improves on uniform with replacement. They do not state the exact finite-epoch noise-risk crossover proved here for equal-skew opposite-offset clients.

De Sa (2020) already establishes that random reshuffling need not be uniformly better than with-replacement sampling in a different learning and positive-semidefinite matrix-product setting. Thus generic reshuffling inferiority is **not** a new principle. Chae, Yun and Kim (arXiv:2501.00511), Theorem 4.1 and Appendix H.1, independently show divergence of several SEG sampling schemes on a different finite-sum monotone bilinear counterexample. Their instability phenomenon differs from the present **individually stable** affine-offset setup and does not give these exact stochastic noise-floor ratios or the spectral threshold. The contribution here is a specific sharp comparison and its complete spectral characterization, not a first counterexample to reshuffling improvement.

The two-sign pairing mechanism is shared with common-Hessian quadratic SGD, whose terminal-risk comparison has a crossover at \(\eta\lambda=1\) in a Hessian mode [4]. In a common affine recurrence the two-step innovation comparison is governed by \(\|(M-I)d\|^2-\|Md\|^2-\|d\|^2=-2\langle Md,d\rangle\). The result here identifies the sign change of that quadratic form and its exact noise penalty for the contractive rotation planes of same-sample SEG, where the transition occurs at \(\kappa(\eta\omega)^2=1\).

## Limitations

Only unconstrained affine skew-symmetric two-component operators sharing the same linear part, same-sample SEG, uniform component probabilities, constant unequal positive stage steps with \(\kappa>1\), exact arithmetic, and independent epoch reshuffles are treated. The proof does not establish an analogous threshold for heterogeneous component Jacobians, nonlinear games, minibatches of more than two components, general monotone mappings, or the source's global convergence guarantees. The threshold can lie outside the conservative sufficient step bounds used in earlier convergence theorems; this is not a contradiction. The claimed stationary quantity is the squared distance to the averaged operator's root, not the individual component's solution. Previously known reshuffling counterexamples and general sign-anti-correlation heuristics remain pertinent priority risks, and independent scientific review is outstanding.

## References

1. K. Emmanouilidis, R. Vidal and N. Loizou, *Stochastic Extragradient with Random Reshuffling: Improved Convergence for Variational Inequalities*, arXiv:2403.07148, initially public 2024-03-11, https://arxiv.org/abs/2403.07148 (Algorithm 1; Theorem 2.2 and Appendix B.2).
2. C. De Sa, *Random Reshuffling is Not Always Better*, Advances in Neural Information Processing Systems 33 (2020), https://papers.neurips.cc/paper_files/paper/2020/file/42299f06ee419aa5d9d07798b56779e2-Paper.pdf.
3. J. Chae, C. Yun and D. Kim, *Stochastic Extragradient with Flip-Flop Shuffling & Anchoring: Provable Improvements*, arXiv:2501.00511, https://arxiv.org/abs/2501.00511 (Theorem 4.1 and Appendix H.1).
4. *A sharp overshoot boundary for terminal random reshuffling on common-Hessian quadratics*, https://github.com/Resultary/2026/tree/main/2026/10/13/SCOPE-a-sharp-overshoot-boundary-for-terminal-random-reshuffling-on-co--4354fb22c6bf (Finding, equations (1)–(2)).
