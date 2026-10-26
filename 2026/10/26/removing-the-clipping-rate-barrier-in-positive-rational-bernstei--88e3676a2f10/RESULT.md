# Removing the clipping-rate barrier in positive rational Bernstein approximation

## Finding

Let \(b>0\) and let \(f\in C^2([0,b])\) satisfy \(f(x)\ge0\), \(f'(x)\ge0\) for all \(x\in[0,b]\), and \(f'(b)>0\). Write \(p_b(x)=x/(b+x)\) and let
\[
(B_n h)(t)=\sum_{k=0}^n h(k/n)\binom nk t^k(1-t)^{n-k}.
\]

The clipped construction in Minguzzi, Theorem 3.2, uses \(\psi_b(t)=bt/(1-t)\) for \(0\le t\le1/2\) and \(\psi_b(t)=b\) for \(1/2\le t\le1\), with \(h_c=f\circ\psi_b\) and \(R_n^{\mathrm{clip}}(f;x)=(B_nh_c)(p_b(x))\). Its endpoint error has the exact limit
\[
\lim_{n\to\infty}\sqrt n\big(R_n^{\mathrm{clip}}(f;b)-f(b)\big)=-b f'(b)\sqrt{\frac2\pi}.
\]
In particular, this fixed clipped sequence cannot have uniform error \(O(n^{-1})\) when \(f'(b)>0\).

There is a rate-preserving repair. The function \(h_0(t)=f(bt/(1-t))\) on \([0,1/2]\) admits a nonnegative, nondecreasing \(C^2\) extension \(h\) to \([0,1]\) that is constant near \(1\). For this extension set
\[
\widehat R_n(f;x)=\sum_{k=0}^n h(k/n)\binom nk\frac{b^{n-k}x^k}{(b+x)^n}+\frac1n.
\]
Then every \(\widehat R_n\) is a strictly positive, nondecreasing rational function on \([0,\infty)\); its numerator and denominator have degree exactly \(n\) and nonnegative coefficients; and
\[
\sup_{0\le x\le b}|\widehat R_n(f;x)-f(x)|\le\frac{1+\|h''\|_\infty/8}{n}.
\]
The constant depends on the chosen smooth extension, which is allowed to depend on \(f\) and \(b\).

## Assumptions and scope

The interval length satisfies \(b>0\). The target \(f\) is twice continuously differentiable, nonnegative and nondecreasing on \([0,b]\), with a strictly positive left derivative at \(b\). The endpoint asymptotic concerns exactly the clipped sequence defined above. The improved sequence is existential through a smooth monotone extension; it does not claim a universal bound depending only on \(\|f''\|_\infty\), nor does it optimize the extension-dependent constant.

## Proof

**1. Exact endpoint asymptotic for the clipped sequence.** The map \(p_b\) satisfies \(p_b(b)=1/2\), so \(R_n^{\mathrm{clip}}(f;b)=(B_nh_c)(1/2)\). On the left of \(1/2\),
\[
h_c'(1/2-)=4b f'(b)=:L>0,
\]
whereas \(h_c\) is constant to the right. Let \(K_n\) have the binomial distribution \(\mathrm{Bin}(n,1/2)\) and put \(Z_n=(K_n-n/2)/\sqrt n\). Then
\[
\sqrt n\big((B_nh_c)(1/2)-f(b)\big)
=\mathbb E\!\left[\sqrt n\big(h_c(K_n/n)-h_c(1/2)\big)\right].
\]
The function \(h_c\) is Lipschitz on \([0,1]\). Its one-sided first-order expansion at \(1/2\) therefore gives, uniformly on bounded sets of \(z\),
\[
\sqrt n\big(h_c(1/2+z/\sqrt n)-h_c(1/2)\big)\longrightarrow Lz\,\mathbf1_{\{z<0\}}.
\]
The variables \(Z_n\) converge in distribution to \(Z\sim N(0,1/4)\) and have uniformly bounded second moments, so the Lipschitz bound gives uniform integrability of the displayed random variables. Taking expectations yields
\[
\lim_{n\to\infty}\sqrt n\big(R_n^{\mathrm{clip}}(f;b)-f(b)\big)
=L\mathbb E[Z\mathbf1_{\{Z<0\}}]
=-\frac{L}{2\sqrt{2\pi}}
=-b f'(b)\sqrt{\frac2\pi}.
\]
The limit is nonzero. Hence the clipped sequence's uniform error is bounded below by a positive constant times \(n^{-1/2}\) for all sufficiently large \(n\), and cannot be \(O(n^{-1})\).

**2. Constructing a smooth monotone extension.** Put \(h_0(t)=f(bt/(1-t))\) on \([0,1/2]\). It is \(C^2\), nonnegative and nondecreasing, and \(h_0'(1/2)=4bf'(b)>0\). Let \(q_0=h_0'(1/2)>0\) and \(q_1=h_0''(1/2)\). Choose \(\delta>0\) so small that \(q_0+q_1u>0\) for \(0\le u\le2\delta\), and choose a \(C^1\) cutoff \(\chi\) on \([0,1/2]\) with \(0\le\chi\le1\), equal to \(1\) near \(0\), and equal to \(0\) for \(u\ge2\delta\). Set \(q(u)=(q_0+q_1u)\chi(u)\) and, for \(t\ge1/2\), define
\[
h(t)=h_0(1/2)+\int_0^{t-1/2}q(u)\,du.
\]
This joins \(h_0\) with matching value, first derivative and second derivative; it is nondecreasing, nonnegative, \(C^2\), and constant near \(1\). Since \(q_0>0\), it also satisfies \(h(1)>0\).

**3. Coefficients, monotonicity and error.** For \(x\ge0\),
\[
\sum_{k=0}^n h(k/n)\binom nk\frac{b^{n-k}x^k}{(b+x)^n}=(B_nh)(p_b(x)).
\]
All numerator coefficients are nonnegative because \(h\ge0\); the leading coefficient is \(h(1)>0\), so the numerator has degree \(n\). The denominator \((b+x)^n\) has degree \(n\) and positive coefficients. The Bernstein derivative identity
\[
(B_nh)'(t)=n\sum_{k=0}^{n-1}\big(h((k+1)/n)-h(k/n)\big)\binom{n-1}{k}t^k(1-t)^{n-1-k}
\]
shows that \(B_nh\) is nondecreasing. Since \(p_b\) is increasing, the rational function is nondecreasing on \([0,\infty)\); adding \(1/n\) makes it strictly positive without changing monotonicity or degree.

For \(0\le x\le b\), \(p_b(x)\le1/2\) and \(h(p_b(x))=h_0(p_b(x))=f(x)\). If \(K\sim\mathrm{Bin}(n,t)\), Taylor's theorem and \(\mathbb E(K/n-t)=0\) imply
\[
|(B_nh)(t)-h(t)|\le\tfrac12\|h''\|_\infty\operatorname{Var}(K/n)
=\frac{t(1-t)}{2n}\|h''\|_\infty
\le\frac{\|h''\|_\infty}{8n}.
\]
Taking \(t=p_b(x)\) and accounting for the added \(1/n\) proves the stated bound.

## Verification

The endpoint constant is independently checkable from the central limit theorem and the Gaussian negative-part expectation \(\mathbb E[Z\mathbf1_{\{Z<0\}}]=-1/(2\sqrt{2\pi})\) for variance \(1/4\). As a numerical sanity check for \(b=1\) and \(f(x)=x\), the scaled clipped endpoint errors \(\sqrt n(R_n^{\mathrm{clip}}(f;1)-1)\) are approximately \(-0.70934\), \(-0.76757\), and \(-0.78802\) at \(n=100,1000,10000\), respectively, approaching \(-\sqrt{2/\pi}\approx-0.79788456\). This finite check corroborates but does not replace the proof. The improved rate follows from the displayed Taylor estimate and is valid for every integer \(n\ge1\).

## Relationship to prior work

Minguzzi's *A Stone-Weierstrass approximation theorem for monotone functions* proves density of positive isotone rational functions with nonnegative coefficients and gives an explicit rational Bernstein construction in Theorem 3.2. That construction clips the transformed variable at \(1/2\), making the transformed target's derivative jump from \(4bf'(b)\) to \(0\) at the endpoint used when approximating \(x=b\). Its stated bound is \((5/4)\omega_f(4b/\sqrt n)\). The exact endpoint limit above identifies the resulting \(n^{-1/2}\) loss for smooth targets with \(f'(b)>0\). The alternative extension uses the classical Bernstein operator on a \(C^2\) monotone continuation; it retains nonnegative coefficients, global monotonicity and equal numerator/denominator degrees while giving an \(n^{-1}\) rate. The contribution is this specific sharp diagnosis and coefficient-preserving repair, not a new version of the general Bernstein approximation theorem.

## Limitations

The extension is not unique, and the bound depends on \(\|h''\|_\infty\). No optimal constant for the improved family is claimed. The endpoint asymptotic applies to the specified clipped construction and to targets with \(f'(b)>0\); it does not classify the rate when \(f'(b)=0\). The result is a constructive rate improvement, not a best-rational-approximation theorem. The literature search is not exhaustive, and independent review has not been performed.

## References

1. E. Minguzzi, *A Stone-Weierstrass approximation theorem for monotone functions*, arXiv:2512.03633, first submitted 3 December 2025, v2 revised 11 October 2026. Sections 1 and 3, especially Theorem 1.12, Lemma 3.1 and Theorem 3.2. https://arxiv.org/abs/2512.03633
2. B. R. Draganov and I. Gadjev, *Direct and Converse Voronovskaya Estimates for the Bernstein Operator*, Results in Mathematics 73 (2018), article 11. https://doi.org/10.1007/s00025-018-0795-8
