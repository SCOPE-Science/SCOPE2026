# The golden-ratio-conditioned two-dimensional safety transition for Gaussian hinted descent

## Finding

Consider one **projected-gradient oracle** step in the Gaussian control-variate zeroth-order method of Ryabchenko, Qian, and Mou [1]. The precise worst-case expected-objective safety threshold for its undiscounted reference step differs qualitatively between two dimensions and higher dimensions. For dimension \(d\ge 2\), an SPD quadratic with spectral condition number \(\kappa\ge1\), and any proper hint subspace, the scaled step \(\alpha=t/(\gamma L)\) is expected-objective nonincreasing **at every nonstationary point** if and only if

\[
\gamma\ge\Gamma_d(\kappa),\qquad
\Gamma_d(\kappa)=\begin{cases}
\frac54-\frac{5-\sqrt5}{8}(1-\kappa^{-1}),&d=2,\\
1+\frac1{2d\kappa},&d\ge3.
\end{cases}
\]

The constants are attained for every \(d\) and \(\kappa\), including equality at the boundary. In particular, the undiscounted step \(\gamma=1\) is universally safe in dimension two precisely for \(\kappa\ge(5+\sqrt5)/2\), while it is not universally safe for any finite \(\kappa\) in dimensions at least three. At positive finite-difference radius, an exact additional nonnegative term reveals an unavoidable noise floor; it is not part of the zero-radius safety assertion.

## Assumptions and scope

Fix an integer \(d\ge2\), real \(\kappa\ge1\), and an SPD matrix \(H\in\mathbb R^{d\times d}\) with \(\lambda_{\max}(H)=L>0\) and \(\lambda_{\min}(H)=L/\kappa\). Let \(f(x)=\tfrac12 x^\top Hx\), let \(g=Hx\ne0\), and choose any proper linear subspace \(S\) (possibly the zero space). Set \(m=P_Sg\), \(r=g-m\), \(s=\|r\|^2/\|g\|^2\). Define \(t_d(s)=\min\{1,1/(ds)\}\) for positive \(s\), with \(t_d(0)=1\), and \(\alpha=t_d(s)/(\gamma L)\) for \(\gamma>0\). The random direction \(u\sim N(0,I_d)\) is independent of the chosen current point and hint. For \(\tau\ge0\), define

\[
G_\tau=m+(u^\top r)u+\frac\tau2(u^\top Hu)u,
\qquad x^+=x-\alpha G_\tau.
\]

For \(\tau>0\), this equals exactly the one-sided finite-difference control-variate estimator \(m+\{f(x+\tau u)-f(x)-\tau m^\top u\}u/\tau\) of [1]. At \(\tau=0\), the displayed polynomial is its **directional-derivative limit**, not a finite-query derivative-free evaluation. This result concerns one conditional expectation, not the practical estimated hint or the log-discounted high-probability algorithm of [1]. Quadratics are not globally Lipschitz as functions, so the theorem does **not** invoke the global bounded-gradient assumptions of [1].

## Proof

**1. Exact Gaussian objective identity.** Gaussian symmetry and Wick's fourth-moment rule give \(\mathbb E G_\tau=g\), since the cubic finite-difference term has zero mean. Writing \(R=uu^\top r\), the fourth-moment identity is

\[
\mathbb E[R^\top HR]=\|r\|^2\operatorname{tr}H+2r^\top Hr.
\]

The mixed quadratic/cubic estimator terms have odd total Gaussian degree and therefore zero expectation. Moreover, the quadratic/cubic term has second energy moment proportional to the sixth Gaussian moment

\[
M_3(H):=\mathbb E(u^\top Hu)^3
=(\operatorname{tr}H)^3+6\operatorname{tr}H\operatorname{tr}(H^2)+8\operatorname{tr}(H^3).
\]

Combining \(g=m+r\) gives the exact identity, **for every real \(\tau\ge0\)**,

\[
\mathbb E[f(x^+)-f(x)]
=-\alpha\|g\|^2+\frac{\alpha^2}{2}
\left[g^\top Hg+\|r\|^2\operatorname{tr}H+r^\top Hr+\frac{\tau^2}4M_3(H)\right]. \tag{1}
\]

In particular, at \(\tau=0\), writing

\[
R(H,g,r)=\frac{g^\top Hg+\|r\|^2\operatorname{tr}H+r^\top Hr}{L\|g\|^2},
\]

expected nonincrease is equivalent to \(\gamma\ge\tfrac12 t_d(s)R(H,g,r)\). Thus the *universal threshold* is the supremum of this explicit expression over the stated spectral matrices, gradients, and hints. The supremum is a maximum in all the cases below.

**2. All dimensions at least three.** Put \(Q=I-H/L\), so \(Q\succeq0\), \(\|Q\|_{\mathrm{op}}=\delta:=1-1/\kappa\), and \(\operatorname{tr}Q\ge\delta\). Orthogonality \(m\perp r\) yields

\[
R=1+(d+1)s-\frac{g^\top Qg+r^\top Qr}{\|g\|^2}-s\operatorname{tr}Q
\le1+(d+1-\delta)s=1+(d+\kappa^{-1})s.
\]

For \(s\le1/d\), the product \(t_d(s)R\) is bounded by an increasing affine function; for \(s\ge1/d\), it is bounded by \(\{1/s+d+\kappa^{-1}\}/d\), which is decreasing. The maximum is therefore \(2+1/(d\kappa)\) at \(s=1/d\). Equality is attained by selecting a single minimum-eigenvalue direction orthogonal to the two-dimensional span of \(m,r\): choose \(H/L=\operatorname{diag}(1,1,\kappa^{-1},1,\ldots,1)\), \(g=\sqrt{1-1/d}\,e_1+\sqrt{1/d}\,e_2\), and \(S=\operatorname{span}\{e_1\}\). Thus \(\Gamma_d(\kappa)=1+1/(2d\kappa)\).

**3. The two-dimensional exception.** When \(d=2\), the extremal spectral defect is \(Q=\delta vv^\top\), for a unit vector \(v\); if \(\kappa=1\), take \(Q=0\). Normalize \(\|g\|=1\) and write \(g=m+r\), \(\|m\|^2=1-s\), \(\|r\|^2=s\), \(m\perp r\). Then

\[
R=1+3s-\delta\big(s+v^\top(gg^\top+rr^\top)v\big).
\]

The positive-semidefinite \(2\times2\) matrix \(K=gg^\top+rr^\top\) has trace \(1+s\), determinant \(s(1-s)\), and smallest eigenvalue

\[
\lambda_-(s)=\frac{1+s-\sqrt{1-2s+5s^2}}2.
\]

Minimizing the Rayleigh quotient over \(v\) therefore yields the *exact*, attainable bound

\[
R\le F(s):=1+(3-\delta)s-\delta\lambda_-(s).
\]

The function \(F\) strictly increases on \(0\le s\le1/2\): indeed \(\lambda'_-(s)\le1\) there (differentiate the square root), and \(F'(s)\ge3-2\delta>0\). On \(s\ge1/2\), \(F(s)/s\) strictly decreases, because

\[
sF'(s)-F(s)=-1+\delta\big(\lambda_-(s)-s\lambda'_-(s)\big),\qquad
\lambda_-(s)-s\lambda'_-(s)=\frac12\left(1-\frac{1-s}{\sqrt{1-2s+5s^2}}\right)\in[0,1/2].
\]

The last inclusion follows from \(1-2s+5s^2\ge(1-s)^2\). Thus \(t_2(s)F(s)\) is maximized at exactly \(s=1/2\), even across the cap switch. Since \(\lambda_-(1/2)=(3-\sqrt5)/4\), the maximum is \(5/2-\delta(5-\sqrt5)/4\), hence

\[
\Gamma_2(\kappa)=\frac54-\frac{5-\sqrt5}{8}(1-1/\kappa).
\]

For sharpness take \(m=e_1/\sqrt2\), \(r=e_2/\sqrt2\), \(g=m+r\), let \(v\) be any unit minimum-eigenvalue eigenvector of \(K=gg^\top+rr^\top\), and define \(H=L(I-\delta vv^\top)\), \(S=\operatorname{span}\{e_1\}\), \(x=H^{-1}g\). When \(\kappa=1\), any such \(v\) works. Every inequality above is an equality. Therefore every \(\gamma<\Gamma_d(\kappa)\) yields a *strict* expected-objective increase in a constructed example, while every \(\gamma\ge\Gamma_d(\kappa)\) yields nonincrease for all admissible examples. Solving \(\Gamma_2(\kappa)\le1\) gives precisely \(\kappa\ge(5+\sqrt5)/2\). For \(d\ge3\), \(\Gamma_d(\kappa)>1\) for every finite \(\kappa\).

**4. Positive smoothing radius.** Formula (1) gives an exact nonnegative extra term \(\alpha^2\tau^2M_3(H)/8\); it cannot be dropped. At the minimizer \(x=0\), the estimator for \(\tau>0\) is \(\tfrac\tau2(u^\top Hu)u\), and any nonzero fixed step yields expected objective increase \(\alpha^2\tau^2M_3(H)/8>0\). This does not contradict [1]'s finite-radius convergence bounds, which include smoothing error terms and do not promise one-step objective monotonicity.

## Verification

A standalone standard-library Python script `verification.py` independently enumerates exact Gaussian moments for a rational two-dimensional forward-difference quadratic and checks (1); it verifies the integer/rational higher-dimensional witness, the two-dimensional eigenvalue identity and golden-ratio threshold numerically at high precision, and sampled dimension/condition-number inequalities. Invoke `python3 verification.py` from a directory containing that script. These finite and exact checks supplement, rather than replace, the proof for all dimensions and spectral matrices.

## Relationship to prior work

Ryabchenko, Qian, and Mou [1, Section 3.3, equation (4)] introduce the projected-gradient oracle step \(L^{-1}\min\{1,(d\sin^2\theta)^{-1}\}\) and recommend a logarithmic discount for their stochastic convergence analysis. Their Lemma 3.3 is a general upper variance bound; neither the condition-number-dependent sharp one-step expected-objective threshold nor the two-dimensional transition is stated in the examined main text and proofs. Their global bounded-gradient and high-probability assumptions are distinct from the quadratic one-step benchmark proved here.

Kozak et al. [2] study orthogonal random-direction zeroth-order steps, including stochastic finite differences and related convergence rates. Their Section 4.2 explicitly identifies tailored quadratic analysis as remaining future work, but [2]'s random-direction scaling and lack of a projected-gradient control variate mean its theorems do not give this threshold. Feng and Wang [3] develop variance-reduced estimators from random orthogonal frames and bias estimates; the inspected formulation is not the Gaussian projected-gradient reference estimator with the oracle step of [1]. These comparisons are about implications of the statements, not a claim of exhaustive novelty across all possible sources.

## Limitations

The theorem is for one **conditional expectation** on an SPD quadratic with a known exact projected-gradient hint and a prescribed spectral condition number. It neither covers the practical estimated-hint scheme nor gives a pathwise monotonicity or full-trajectory convergence theorem. The source's global bounded-gradient hypothesis does not hold for nonconstant quadratics and is not invoked. The sharp guarantee is at the zero-radius directional-derivative limit; at fixed positive radius the additional \(\tau^2\) term remains, with no uniform monotonicity near stationary points. The case \(d=1\) is excluded, as the rank-one proper-hint geometry is different. Other unpublished or unindexed equivalent spectral-moment analyses might exist.

## References

[1] A. Ryabchenko, J. Qian, W. Mou, *Adaptively Incorporating Directional Hints into Zeroth-Order Optimization*, arXiv:2609.08277v1 (8 September 2026), especially Sections 3.1–3.3, Lemma 3.3, equation (4), and Appendix C. https://arxiv.org/html/2609.08277v1

[2] D. Kozak, C. Molinari, L. Rosasco, L. Tenorio, S. Villa, *Zeroth order optimization with orthogonal random directions*, arXiv:2107.03941v2 (2021), especially Sections 2, 4.2–4.3. https://arxiv.org/html/2107.03941v2

[3] Y. Feng, T. Wang, *Stochastic Zeroth Order Gradient and Hessian Estimators: Variance Reduction and Refined Bias Bounds*, arXiv:2205.14737v3 (2023), especially Sections 2–4. https://arxiv.org/html/2205.14737v3
