# Sharp third-rank stability of the nuclear envelope for Hardy geometric matrix norms

## Finding

For each integer \(n\ge3\), let \(H_n\) denote the Hardy geometric-mean norm on real \(n\times n\) matrices, as defined below. Put
\[
C_n=\exp\!\left(\frac{\psi(1/2)-\psi(n/2)}{2}\right),\qquad \kappa=3-e>0.
\]
For every real matrix \(A\), with decreasing singular values \(s_1(A)\ge\cdots\ge s_n(A)\ge0\), one has the **sharp, dimension-independent spectral-tail refinement**
\[
\boxed{\ H_n(A)\le C_n\left(\|A\|_*-(3-e)\sum_{j=3}^{n}s_j(A)\right).\ }
\]
The plain nuclear majorant \(H_n(A)\le C_n\|A\|_*\) is an equality **exactly when** \(\operatorname{rank}A\le2\). The coefficient \(3-e\) cannot be increased uniformly in \(n\): equality in the refined inequality occurs for every positive multiple of a rank-three orthogonal projector. The assertion is real, not a claim about complex-unit-sphere averages.

## Assumptions and scope

The normalized rotation-invariant probability measure on \(S^{n-1}\subset\mathbb R^n\) is \(\sigma\). For a nonzero matrix define
\[
H_n(A)=\exp\left(\int_{S^{n-1}}\log\|Ax\|_2\,d\sigma(x)\right),\qquad H_n(0)=0.
\]
The logarithm is integrable for every nonzero finite matrix, even when it has nontrivial kernel. The already-established norm property and orthogonal invariance of \(H_n\) are taken from Kovalev [1]. The nuclear norm is \(\|A\|_* =\sum_{j=1}^{n}s_j(A)\); \(\psi(t)=\Gamma'(t)/\Gamma(t)\) is the digamma function. Empty singular-value tails have sum zero. All quantifiers run over every integer \(n\ge3\) and every real \(n\times n\) matrix.

## Proof

**Step 1: Exact nuclear equality on rank at most two.** By orthogonal invariance it suffices to take a diagonal matrix with only two possibly nonzero singular values \(a,b\ge0\), not both zero. If \(x\) is uniform on the sphere, let \(R=(x_1^2+x_2^2)^{1/2}\). The polar angle of \((x_1,x_2)\) is uniform and independent of \(R\), and \(R^2\) has the beta distribution with parameters \(1\) and \((n-2)/2\). Therefore
\[
\mathbb E\log R=\frac{\psi(1)-\psi(n/2)}2.
\]
The elementary Jensen/Poisson angular integral, valid also at \(a=0\) or \(b=0\) by monotone limiting of its regularization, is
\[
\frac1{2\pi}\int_0^{2\pi}\log\sqrt{a^2\cos^2\theta+b^2\sin^2\theta}\,d\theta
=\log\frac{a+b}2.
\]
Since \(\psi(1/2)=\psi(1)-2\log2\), these identities yield
\[
H_n(A)=\exp\left(\frac{\psi(1)-\psi(n/2)}2\right)\frac{a+b}2
=C_n(a+b)=C_n\|A\|_*.
\]
The zero matrix is immediate. Thus there is an entire rank-two equality locus rather than only the rank-one extreme rays.

**Step 2: Exact projection radii.** For a rank-\(k\) orthogonal projector \(P_k\), \(\|P_kx\|_2^2\) has the beta law with parameters \(k/2\) and \((n-k)/2\), interpreted deterministically when \(k=n\). Hence
\[
H_n(P_k)=\exp\left(\frac{\psi(k/2)-\psi(n/2)}2\right)=C_n r_k,
\qquad r_k=\exp\left(\frac{\psi(k/2)-\psi(1/2)}2\right).
\]
In particular \(r_1=1\), \(r_2=2\), \(r_3=e\), \(r_4=2\sqrt e\), \(r_5=e^{4/3}\), and \(r_6=2e^{3/4}\). These projection values themselves are available in [1], and are treated as prior input.

**Step 3: Strictly diminishing projection increments from the third rank onward.** Extend the normalized numbers smoothly to real \(t>0\) by
\[
r(t)=\exp\left(\frac{\psi(t/2)-\psi(1/2)}2\right).
\]
Writing \(x=t/2\), differentiation gives
\[
\frac{r''(t)}{r(t)}=\frac{\psi_1(x)^2+2\psi_2(x)}{16},
\]
where \(\psi_1\) and \(\psi_2\) are the first two derivatives of \(\psi\). From the convergent series for polygamma functions and the integral test,
\[
0<\psi_1(x)=\sum_{j\ge0}(x+j)^{-2}\le x^{-1}+x^{-2},
\qquad \psi_2(x)=-2\sum_{j\ge0}(x+j)^{-3}\le-x^{-2}.
\]
For \(x\ge5/2\), this implies
\[
\psi_1(x)^2+2\psi_2(x)
\le x^{-2}\big((1+x^{-1})^2-2\big)<0,
\]
so \(r(t)\) is strictly concave for \(t\ge5\). The remaining adjacent increments are verified by the strict inequalities
\[
1=r_2-r_1>r_3-r_2=e-2>r_4-r_3>r_5-r_4>r_6-r_5>0.
\]
These last finite inequalities follow, for example, by exact rational upper/lower Taylor bounds for exponentials; the included standalone checker supplies such bounds rather than relying on printed decimals. Strict concavity propagates the last inequality to all later increments. Consequently
\[
r_1-r_0=1,\quad r_2-r_1=1,\quad
0<r_j-r_{j-1}\le e-2\quad (j\ge3),
\]
where \(r_0=0\).

**Step 4: Majorization by singular-value tails.** Let \(A=U\operatorname{diag}(s_1,\ldots,s_n)V\) be a real singular-value decomposition, with \(s_{n+1}=0\). The nonnegative diagonal has the exact nested-projector decomposition
\[
\operatorname{diag}(s_1,\ldots,s_n)
=\sum_{k=1}^n(s_k-s_{k+1})P_k.
\]
The norm property from [1], orthogonal invariance, and the previous step give
\[
\begin{aligned}
H_n(A)&\le C_n\sum_{k=1}^n(s_k-s_{k+1})r_k\\
&=C_n\sum_{j=1}^n s_j(r_j-r_{j-1})\\
&\le C_n\left(s_1+s_2+(e-2)\sum_{j=3}^n s_j\right)\\
&=C_n\left(\|A\|_*-(3-e)\sum_{j=3}^n s_j\right).
\end{aligned}
\]
For rank at most two, Step 1 gives equality with the nuclear majorant. If the rank is at least three, the tail is positive and \(3-e>0\), so the nuclear majorant is strictly larger. For \(A=tP_3\) with \(t>0\), Step 2 gives \(H_n(A)=teC_n\), whereas the refined right-hand side equals \(C_n(3t-(3-e)t)=teC_n\). Thus its coefficient is sharp, completing the proof.

## Verification

The elementary special-function identities reduce to beta-distribution log moments and the digamma recurrence. In particular, \(\psi(x+1)-\psi(x)=1/x\) gives the displayed six projection values. The concavity estimate in Step 3 is an infinite-dimensional series inequality proved by the integral test, not by experimentation. The file `verify_hardy_rational.py` computes rigorous rational Taylor enclosures for the four exponential values needed for the finitely many remaining increment comparisons; running it prints `EXACT_RATIONAL_CONSECUTIVE_PROJECTION_GAPS_OK` and `POLYGAMMA_COMPARISON_BOUND_OK`. It is auxiliary: no finite sampling is used to infer the all-dimension theorem.

## Relationship to prior work

Kovalev [1] introduced \(H_n\), proved its norm and orthogonal invariance properties, and calculated the norm on projections. Those facts are inputs, not claimed as new. The statement established here is the sharp **full singular-tail stability** of the nuclear upper envelope, its exact rank-two equality set, and the dimension-free optimal coefficient \(3-e\). These require the rank-two angular identity and diminishing normalized projection increments. The original preprint was not accessible in full at verification time; the available mathematical synopsis [2] describes the projection identities and norm proof but does not describe this precise sharp tail inequality, leaving an explicit originality-comparison risk.

## Limitations

The result concerns **real** square finite-dimensional matrices. It makes no claim about complex sphere averages, \(0<p<1\), the dual norm, or optimal bounds involving Schatten norms other than the nuclear norm. The coefficient is sharp for the stated trace-tail inequality, not a claim about all possible refined spectral profiles. A full-text originality check against [1] remains unresolved because the primary PDF was inaccessible through the available permitted routes; this is an access limitation rather than mathematical verification.

## References

[1] L. V. Kovalev, *Hardy-type norms of matrices*, arXiv:2607.17373v1, first public 19 July 2026, https://arxiv.org/abs/2607.17373.

[2] *Hardy-type norms of matrices*, mathematical literature synopsis, https://www.themoonlight.io/en/review/hardy-type-norms-of-matrices (secondary account; not a substitute for the primary full text).
