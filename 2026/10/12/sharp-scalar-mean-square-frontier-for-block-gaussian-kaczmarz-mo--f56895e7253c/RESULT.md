# Sharp scalar mean-square frontier for block Gaussian Kaczmarz momentum

## Finding

For the pseudoinverse-free momentum block Gaussian Kaczmarz (mBGK) update of Han and Xie, a consistent **one-dimensional** linear system has an exact second-moment stability frontier and a sharp global lower bound on its asymptotic second-moment contraction factor. For every integer block width \(p\ge1\), positive fixed stepsize \(\alpha>0\), and constant heavy-ball momentum \(0\le\omega<1\), the source-initialized method is mean-square convergent for every nonoptimal initial value exactly when

\[
0<\alpha<\frac{2p(1-\omega^2)}{p+2+(2-p)\omega}.
\]

At equality the mean-square error does not converge to zero; above equality it diverges exponentially. Comparing with the zero-momentum ceiling, positive momentum actually enlarges the permitted stepsize interval precisely when \(p>2\) and \(0<\omega<(p-2)/(p+2)\), despite its inability to improve the globally best mean-square contraction. Writing \(\mathcal R_p(\alpha,\omega)\) for its asymptotic mean-square rate, defined rigorously below, the **sharp global optimum over both parameters** is

\[
\inf_{\alpha>0,\ 0\le\omega<1}\mathcal R_p(\alpha,\omega)=\frac{2}{p+2},
\]

attained **only** at zero momentum \(\omega=0\) and stepsize \(\alpha=p/(p+2)\). Thus strictly positive heavy-ball momentum cannot improve the optimal asymptotic mean-square rate on this Gaussian multiplicative-noise instance, even though expected iterates can contract quickly.

## Assumptions and scope

Take \(A=[a]\in\mathbb R^{1\times1}\) with \(a\ne0\), \(b\in\mathbb R\), unique solution \(x_*=b/a\), and independent sketch matrices \(S_t\in\mathbb R^{1\times p}\), each with independent standard-normal entries. The **unnormalized** Gaussian block update in Section 5.6 of Han–Xie is

\[
x_{t+1}=x_t-\frac{\alpha A^\top S_tS_t^\top(Ax_t-b)}{p\|A\|_F^2}
 +\omega(x_t-x_{t-1}),\qquad t\ge1.
\]

Fix \(x_1=x_0\ne x_*\), the source's equal-state momentum initialization, and put \(e_t=x_t-x_*\). Then

\[
e_{t+1}=(1+\omega-\alpha G_t)e_t-\omega e_{t-1},\qquad
G_t=\frac1p\sum_{j=1}^pZ_{tj}^2\sim\chi_p^2/p,
\]

where \(\mathbb EG_t=1\), \(\operatorname{Var}(G_t)=2/p\), and \(G_t\) is independent of the earlier iterates. The claim does **not** concern the pseudoinverse-normalized sketch-and-project Gaussian Kaczmarz method, variable steps or momentum, additive gradient noise, or dimension greater than one. Define

\[
\mathcal R_p(\alpha,\omega)=\lim_{t\to\infty}
\left(\frac{\mathbb E[e_t^2]}{e_1^2}\right)^{1/t}.
\]

The proof shows that the limit exists, is independent of the nonzero initial scale, and equals a matrix spectral radius. Mean-square convergence means \(\mathbb E[e_t^2]\to0\).

## Proof

**1. Exact moment dynamics.** Let \(m=1+\omega-\alpha\) and \(v=2/p\), and set

\[
U_t=\mathbb E[e_t^2],\quad V_t=\mathbb E[e_{t-1}^2],
\quad C_t=\mathbb E[e_te_{t-1}].
\]

Independence of \(G_t\) and the history, together with \(\mathbb E[(1+\omega-\alpha G_t)^2]=m^2+v\alpha^2\), yields the **exact**, not upper-bound, recurrence

\[
\begin{pmatrix}U_{t+1}\\V_{t+1}\\C_{t+1}\end{pmatrix}
=M_{p,\alpha,\omega}
\begin{pmatrix}U_t\\V_t\\C_t\end{pmatrix},\qquad
M_{p,\alpha,\omega}=
\begin{pmatrix}
m^2+2\alpha^2/p&\omega^2&-2\omega m\\
1&0&0\\m&0&-\omega
\end{pmatrix}.
\]

In particular, \(U_1=V_1=C_1=e_1^2\). Although this coordinate matrix has negative entries, the corresponding map on symmetric \(2\times2\) covariance matrices is positive: with

\[
B(g)=\begin{pmatrix}1+\omega-\alpha g&-\omega\\1&0\end{pmatrix},
\qquad \mathcal T(Q)=\mathbb E[B(G_t)QB(G_t)^\top],
\]

we have \(\mathcal T(Q)\succeq0\) whenever \(Q\succeq0\).

**2. The asymptotic factor is the Perron spectral radius.** For \(\alpha>0\) and \(\omega>0\), this covariance map is primitive on the PSD cone: if \(u=(u_1,u_2)\ne0\) has \(u_1\ne0\), the random vector \(B(G_t)u\) has nonzero variance in its first coordinate and a nonzero constant second coordinate; hence \(\mathcal T(uu^\top)\) is positive definite. If \(u_1=0\), its image is a positive multiple of the first coordinate projector, and its *second* image is positive definite. By spectral decomposition, \(\mathcal T^2\) maps every nonzero PSD matrix into a positive-definite matrix. Finite-dimensional Perron–Frobenius theory for a primitive cone-preserving map therefore gives a simple strictly dominant positive eigenvalue \(\rho(M_{p,\alpha,\omega})\); the source-initialized rank-one covariance has a strictly positive Perron component, as does the first-coordinate observable. Consequently

\[
\mathcal R_p(\alpha,\omega)=\rho(M_{p,\alpha,\omega}).
\]

For \(\omega=0\), the recurrence directly gives \(U_{t+1}=\big(1-2\alpha+(1+2/p)\alpha^2\big)U_t\), so the same conclusion follows without the cone argument. In particular \(\mathcal R_p>0\) throughout the stated parameter range.

**3. Sharp stability frontier.** An exact determinant expansion yields

\[
\det(I-M_{p,\alpha,\omega})
=\frac{\alpha}{p}\left[2p(1-\omega^2)
 -\alpha\big(p+2+(2-p)\omega\big)\right].
\]

For \(0<\omega<1\), at \(\alpha=0\) the moment eigenvalues are \(1,\omega,\omega^2\), and the derivative of the eigenvalue emanating from \(1\) is \(-2/(1-\omega)<0\). Its positive Perron continuation is therefore below one for all sufficiently small positive \(\alpha\). A Perron eigenvalue can cross one only if \(\det(I-M)=0\); since \(p+2+(2-p)\omega=p(1-\omega)+2(1+\omega)>0\), there is exactly one positive crossing candidate

\[
\alpha_{\rm crit}=\frac{2p(1-\omega^2)}{p+2+(2-p)\omega}.
\]

The Perron root grows without bound as \(\alpha\to\infty\) (the trace of \(M\) grows quadratically). By continuity, uniqueness of the positive unit-eigenvalue crossing, and the initial strict stability, the Perron root is below one exactly for \(0<\alpha<\alpha_{\rm crit}\), equals one at the threshold, and exceeds one afterwards. The endpoint \(\omega=0\) follows from its explicit scalar quadratic multiplier; its stability ceiling is \(2p/(p+2)\). By the positive Perron component from Step 2, these spectral statements also apply to the actual equal-state initialization.

**4. Sharp global no-acceleration bound.** Put \(r=2/(p+2)\). Direct calculation gives

\[
\det M=\omega^3,
\quad f(\alpha):=\det(rI-M),
\quad [\alpha^2]f(\alpha)=-\frac{r\,[2+(2-p)\omega]}p,
\]

and the discriminant, considered as a quadratic in \(\alpha\), is

\[
\operatorname{disc}_\alpha f
=\frac{8p\omega^2\big((p+2)\omega-2\big)
\big((p+2)\omega+2\big)}{(p+2)^4}.
\]

If \(0<\omega<r\), the leading coefficient is negative and the discriminant strictly negative; thus \(f(\alpha)<0\) for every real \(\alpha\). Since \(\det(zI-M)\to+\infty\) as real \(z\to+\infty\), there is a real eigenvalue larger than \(r\), implying \(\rho(M)>r\). At \(\omega=r\), the direct identity

\[
\det(rI-M)=-\frac{16\alpha^2}{p(p+2)^2}<0
\]

again yields \(\rho(M)>r\) for \(\alpha>0\). For \(\omega>r\), \(\rho(M)^3\ge|\det M|=\omega^3\) implies \(\rho(M)\ge\omega>r\). Finally, when \(\omega=0\),

\[
\rho(M)=1-2\alpha+\left(1+\frac2p\right)\alpha^2
=\frac{2}{p+2}+\left(1+\frac2p\right)
\left(\alpha-\frac{p}{p+2}\right)^2.
\]

This proves both the global lower bound and uniqueness of its zero-momentum equality case.

**5. A concrete discrepancy between mean and mean square.** For \(p=1\), \(\omega=1/2\), and \(\alpha=1/2\), the sharp mean-square ceiling is \(\alpha_{\rm crit}=3/7<1/2\), although this stepsize lies below the defining paper's zero-momentum ceiling \(2/3\). The expected error obeys

\[
\mathbb E[e_{t+1}]=\mathbb E[e_t]-\tfrac12\mathbb E[e_{t-1}],
\]

whose roots have modulus \(1/\sqrt2<1\); the mean converges to zero. Nevertheless the second-moment matrix has Perron root approximately \(1.1027847152>1\), so actual mean-squared error grows exponentially. For \(e_0=e_1=1\), the first eight values \(\mathbb E[e_t^2]\), starting at \(t=1\), are exactly \(1,3/4,7/8,1,35/32,77/64,85/64,375/256\).

## Verification

The standalone standard-library script `verify.py` constructs \(M\) with exact rational arithmetic, checks \(\det(I-M)\), \(\det M\), the quadratic coefficient and discriminant of \(\det(rI-M)\) for 1,890 distinct triples of tested rational parameters, and checks the concrete example's threshold, eight second moments, and divergence certificate \(\det(I-M)<0\). Run with `python3 verify.py`; the reproduced result is `PASS`. This finite enumeration checks algebra and selected examples; the proof for all integer \(p\ge1\) and continuum-valued parameters is Steps 1–4, **not** the test suite.

## Relationship to prior work

Han and Xie's pseudoinverse-free mBGK source (arXiv:2208.05437, Section 5.6 and its convergence-theorem prerequisites) defines exactly the Gaussian block update and proves a sufficient linear second-moment bound, while separately studying accelerated convergence of **norms of expected iterates**. The sufficient \(q<1\) bound and its positive-stepsize restriction do not imply either a necessary-and-sufficient scalar mean-square stability frontier or a joint \((\alpha,\omega)\) optimum for actual second moments. Their Section 4.3.2 treats *scalar sampling matrices* rather than establishing this one-dimensional, random-chi-square case.

Loizou and Richtárik (arXiv:1712.09677) provide general stochastic heavy-ball second-moment convergence bounds and mean-iterate acceleration, but their quadratic sketch method uses realization-normalized projector Hessians. On a one-dimensional nonzero Gaussian sketch such a projector is deterministic; it is not the unnormalized \(\chi_p^2/p\) Hessian here. Kidambi, Netrapalli, Jain and Kakade (arXiv:1803.05591) show momentum-related stochastic lower bounds on a different multi-directional regression family, not this exact all-block-width frontier and global minimization. Bollapragada, Chen and Ward (arXiv:2206.07553) analyze minibatch heavy ball in distinct finite-sum regimes. Relevant indexed research on momentum and randomized Kaczmarz was also compared by actual update law and parameter implications, not title alone; none inspected subsumed the stated exact theorem. A failed literature search alone is not proof of priority.

## Limitations

The result is an **exact one-dimensional** obstruction only. It does not assert that momentum cannot improve multidimensional BGK, adaptive algorithms, finite-time error at fixed initialization, expected error rather than expected squared error, almost-sure rates, normalized sketch-and-project Kaczmarz, or all stochastic momentum schemes. The Gaussian block count is fixed and finite; drawing independent fresh blocks and initializing equal states are essential to the stated asymptotic interpretation. The cone-Perron argument is exact but assumes positive momentum; the zero-momentum endpoint is proved separately. The priority comparison cannot exclude inaccessible or unindexed specialized results. No independent validation has been performed.

## References

1. D. Han and J. Xie, *On pseudoinverse-free randomized methods for linear systems: Unified framework and acceleration*, arXiv:2208.05437 (first public submission 2022-08-10), Section 5.6, Theorem 4.7 and proofs. https://arxiv.org/abs/2208.05437
2. N. Loizou and P. Richtárik, *Momentum and Stochastic Momentum for Stochastic Gradient, Newton, Proximal Point and Subspace Descent Methods*, arXiv:1712.09677 (2017), Sections 1.2, 4, 7 and appendices. https://arxiv.org/abs/1712.09677
3. R. Kidambi, P. Netrapalli, P. Jain and S. Kakade, *On the insufficiency of existing momentum schemes for Stochastic Optimization*, arXiv:1803.05591 (2018). https://arxiv.org/abs/1803.05591
4. R. Bollapragada, T. Chen and R. Ward, *On the fast convergence of minibatch heavy ball momentum*, arXiv:2206.07553 (2022). https://arxiv.org/abs/2206.07553
