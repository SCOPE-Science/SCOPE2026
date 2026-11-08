# A boundary-to-bulk transition in high-power weighted Bergman Hankel norms

## Finding

For each real \(\alpha>-1\), let \(H_{m,\alpha}\) be the big Hankel operator with symbol \(\overline z^{\,m}\) on the standard probability-normalized weighted Bergman space of the unit disk, where \(m\) ranges over positive integers. Put \(p=\alpha+1>0\) and define
\[
F_p(t)=\begin{cases}
(t/(t+1))^p,&0\leq t\leq1,\\
(t/(t+1))^p-((t-1)/t)^p,&t\geq1.
\end{cases}
\]
The squared operator norms converge, as the symbol degree grows, to
\[
\lim_{m\to\infty}\|H_{m,\alpha}\|^2=C_p:=\max_{t\geq0}F_p(t).
\]
The maximizer \(t_p\) is unique and satisfies the sharp dichotomy
\[
(t_p,C_p)=\begin{cases}
(1,2^{-p}),&0<p\leq1,\\
(1/x_p,F_p(1/x_p)),&p>1,
\end{cases}
\]
where \(x_p\in(0,1)\) is the unique nonzero solution of
\[
(1-x_p)^{p-1}(1+x_p)^{p+1}=1.
\]
For \(p>1\), the root lies in \((1/p,1)\). Every sequence of maximizing input monomial degrees \(n_m\) satisfies \(n_m/m\to t_p\).

The transition at the unweighted value is nonanalytic: writing \(\delta_\alpha=t_{1+\alpha}-1\), for \(\alpha\downarrow0\),
\[
\delta_\alpha\sim\frac12\,4^{-1/\alpha}.
\]
At \(\alpha=0\) the *finite-degree* norm is exactly \(\|H_{m,0}\|=1/\sqrt2\) for every \(m\geq1\), and its unique maximizing input monomial is \(z^{m-1}\) after normalization.

## Assumptions and scope

Let \(\mathbb D\subset\mathbb C\) be the open unit disk and
\[
d\mu_\alpha(z)=\frac{\alpha+1}{\pi}(1-|z|^2)^\alpha\,dA(z),\qquad \alpha>-1.
\]
Here \(dA\) denotes planar Lebesgue area measure. Let \(A_\alpha^2\) be the holomorphic subspace of \(L^2(d\mu_\alpha)\), \(P_\alpha\) its orthogonal projection, and
\[
H_{m,\alpha}f=(I-P_\alpha)(\overline z^{\,m}f).
\]
No normalization is imposed on the symbol beyond its literal value \(\overline z^{\,m}\). The operator norm is from \(A_\alpha^2\) to \(L^2(d\mu_\alpha)\). The limit holds with \(\alpha\) fixed first, followed separately by the \(\alpha\downarrow0\) limit for the optimizing scale. No claim of uniformity in a simultaneous \((m,\alpha)\) limit is made.

## Proof

**Step 1: exact diagonalization.** Let
\[
 w_n=\|z^n\|^2=\frac{\Gamma(n+1)\Gamma(\alpha+2)}{\Gamma(n+\alpha+2)},\qquad e_n=z^n/\sqrt{w_n}.
\]
Orthogonality of angular frequencies gives
\[
P_\alpha(\overline z^{\,m}e_n)=\begin{cases}
0,&n<m,\\
(\sqrt{w_n}/\sqrt{w_{n-m}})e_{n-m},&n\geq m.
\end{cases}
\]
The outputs \(H_{m,\alpha}e_n\) for different \(n\) are mutually orthogonal because they lie in different angular-frequency subspaces. Subtracting the projection norm therefore gives the *full* squared singular-value multiset
\[
 s_{n,m,\alpha}^2=\begin{cases}
\dfrac{w_{n+m}}{w_n},&0\leq n<m,\\[3pt]
\dfrac{w_{n+m}}{w_n}-\dfrac{w_n}{w_{n-m}},&n\geq m.
\end{cases}
\]
For fixed \(m\), the two moment ratios tend to one as \(n\to\infty\), so \(s_{n,m,\alpha}^2\to0\); hence the operator is compact and the maximum is attained at some integer \(n\geq0\).

**Step 2: moving-index scaling and control of escaping indices.** Stirling's ratio formula gives \(w_n\sim\Gamma(p+1)n^{-p}\) as \(n\to\infty\). If \(n_m/m\to t\in(0,1)\), the first ratio tends to \((t/(t+1))^p\). If \(n_m/m\to t>1\), the two terms tend to \((t/(t+1))^p\) and \(((t-1)/t)^p\). At \(t=1\), the second term tends to zero even when \(n_m-m\) stays bounded: the numerator \(w_{n_m}\) tends to zero while \(w_{n_m-m}\geq w_{n_m}\) and is asymptotically larger in every such regime. Thus the limit is continuous and equals \(F_p(1)=2^{-p}\). If \(n_m/m\to0\), then \(w_{n_m+m}/w_{n_m}\to0\) (uniformly because \(w_n\asymp(n+1)^{-p}\)); the limit is zero. If \(n_m/m\to\infty\), both ratios tend to one and their difference vanishes. Consequently every possible subsequential scaled-degree limit, including the endpoints zero and infinity, has the prescribed limiting value \(F_p(t)\). Choosing degrees closest to any fixed positive \(tm\) proves the lower bound for the supremum; taking a convergent subsequence of scaled maximizers in the compactified half-line proves the upper bound. Strict positivity of \(\max F_p\) excludes escaping maximizers.

**Step 3: unique limiting maximizer.** On \((0,1)\), \(F_p\) strictly increases. For \(t>1\),
\[
F_p'(t)=p\left[\frac{t^{p-1}}{(t+1)^{p+1}}-\frac{(t-1)^{p-1}}{t^{p+1}}\right].
\]
With \(x=1/t\), the derivative is negative exactly when
\[
\Phi_p(x):=(p-1)\log(1-x)+(p+1)\log(1+x)>0.
\]
Moreover \(\Phi_p'(x)=2(1-px)/(1-x^2)\), and \(\Phi_p(0)=0\). For \(0<p\leq1\), \(\Phi_p(x)>0\) on \((0,1)\), hence \(F_p'(t)<0\) for every \(t>1\). For \(p>1\), \(\Phi_p\) first increases on \((0,1/p)\), then decreases to \(-\infty\) as \(x\uparrow1\). There is exactly one nonzero root \(x_p\in(1/p,1)\); thus \(F_p\) increases for \(1<t<1/x_p\) and decreases thereafter. This proves both uniqueness claims. The scaled maximizing degrees converge because every subsequential limit must maximize the unique \(F_p\).

**Step 4: essential-singularity displacement.** Put \(p=1+\alpha\) and \(t_p=1+\delta_\alpha\). The crossing equation becomes
\[
\delta_\alpha^{\alpha}(2+\delta_\alpha)^{2+\alpha}=(1+\delta_\alpha)^{2+2\alpha}.
\]
The unique positive solution tends to zero as \(\alpha\downarrow0\): otherwise a limit of the equation would give \((2+\delta)^2=(1+\delta)^2\) for some \(\delta>0\), impossible. Taking logarithms gives
\[
\log\delta_\alpha=-\left(\frac2\alpha+1\right)\log2+O(\delta_\alpha/\alpha).
\]
The same logarithmic equation first yields \(\delta_\alpha\leq\exp(-c/\alpha)\) for some constant \(c>0\) and all sufficiently small \(\alpha\), so the error term is \(o(1)\). Exponentiation gives the stated \(\frac12 4^{-1/\alpha}\) asymptotic.

**Step 5: an exact finite-degree check at the transition.** When \(\alpha=0\), \(w_n=1/(n+1)\). Hence
\[
s_{n,m,0}^2=\begin{cases}
(n+1)/(n+m+1),&n<m,\\
m^2/((n+1)(n+m+1)),&n\geq m.
\end{cases}
\]
The first branch strictly increases and ends at \(n=m-1\) with value \(1/2\); the second strictly decreases and starts below \(1/2\). This proves the claimed exact norm and its unique norming monomial.

## Verification

Run `python3 check_hankel.py` with Python's standard library. The self-contained checker independently evaluates finite moment integrals and orthogonal projections, verifies exact unweighted rational identities, and compares discrete maxima with the continuum optimizer across representative weights and symbol degrees. Its passing output is `WEIGHTED_HANKEL_CHECKS_PASS 10717`. These finite tests are corroboration, not a substitute for the all-parameter proof in this document.

## Relationship to prior work

Keshavarzi and Wu's October 13, 2022 preprint treats general Schatten-class characterizations of big Hankel operators on regular-weight Bergman spaces. Bourass, El-Fallah, Marrhich and Naqos (February 2, 2021) treat singular-value decay as the *singular-value index* tends to infinity for a *fixed* anti-analytic symbol; their Section 8 gives the monomial moment-difference method for the degree-one symbol. Consequently the diagonalization in Step 1 is standard background, not a novelty claim. The new claim is the *symbol-degree* asymptotic optimum and the weight-dependent boundary-to-bulk transition, including its exponentially small displacement. Hardy-space finite-rank Hankel norms and weighted Bergman circle-trace results do not imply this theorem by a simple parameter identification.

## Limitations

The analysis fixes \(\alpha>-1\) before sending the symbol exponent \(m\) to infinity; it does not cover a joint critical scaling. The maximizing input degree is asymptotically characterized, not exactly classified at finite \(m\) when \(\alpha\ne0\). The operator is the *big* (not the small) Hankel operator on the disk; the norm is not a Schatten norm. The exact diagonal expression alone is elementary and its derivation should not be regarded as a separate new finding. A full historical priority guarantee is not claimed; earlier explicit monomial norm papers could contain an equivalent asymptotic classification.

## References

1. H. Keshavarzi and F. Wu, *Schatten Class Hankel Operators on Weighted Bergman Spaces induced by regular weights*, arXiv:2210.06896v1 (first public October 13, 2022), https://arxiv.org/abs/2210.06896 ; published in Bulletin des Sciences Mathématiques 191 (2024), article 103402.
2. M. Bourass, O. El-Fallah, I. Marrhich and H. Naqos, *On singular values of Hankel operators on Bergman spaces*, arXiv:2102.01743v1 (February 2, 2021), https://arxiv.org/html/2102.01743v1 .
