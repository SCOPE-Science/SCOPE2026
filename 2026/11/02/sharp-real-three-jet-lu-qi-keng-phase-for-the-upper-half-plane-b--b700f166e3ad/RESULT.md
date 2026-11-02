# Sharp real three-jet Lu Qi-Keng phase for the upper-half-plane Bergman Gram kernel

## Finding

Let \(\mathbb H=\{z\in\mathbb C:\operatorname{Im}z>0\}\). For real \(a,b\), form the differential evaluation
\[
\Lambda_{a,b;z}f=f(z)+a f'(z)+\frac b2 f''(z)
\]
on the unweighted Bergman space \(A^2(\mathbb H)\), with norm \(\int_{\mathbb H}|f|^2\,dx\,dy\). Let \(B_{a,b}(z,w)\) be the canonical Hermitian Gram kernel of the Riesz representatives of these functionals.

**Theorem.** The kernel \(B_{a,b}\) has no zero in \(\mathbb H\times\mathbb H\) if and only if
\[
\boxed{\ a^2\ge b+\sqrt{10/3}\,|b|.\ }
\]
This includes the entire line \(b=0\). If \(b\ne0\) and the strict reverse inequality holds, the kernel has exactly **two distinct attainable scalar zero fibres** in the variable \(t=(z-\overline w)^{-1}\), both simple. On the sharp equality boundary with \(b\ne0\), its auxiliary polynomial has precisely two distinct real roots of multiplicity two; these boundary roots are not attained by interior pairs, so the kernel remains zero-free.

Equivalently, for any fixed \(b>0\), zero-freeness holds exactly when \(a^2\ge(1+\sqrt{10/3})b\); for \(b<0\), it holds exactly when \(a^2\ge(\sqrt{10/3}-1)|b|\). Thus the first-derivative term can restore zero-freeness in the presence of a nonzero second-derivative term, and the restoration threshold depends sharply on the sign of that term.

## Assumptions and scope

The coefficient pair \((a,b)\) is **real**, and the zeroth-order coefficient is normalized to one. The second-order functional is \(bf''/2\), not \(bf''\). For arbitrary complex coefficients or sequences supported beyond order two, no classification is asserted. The kernel is the **positive-definite Riesz-family Gram kernel**, not the generally different off-diagonal extremal kernel.

We count distinct values of \(t=(z-\overline w)^{-1}\) that arise as zeros for some interior pair \((z,w)\). This is not a claim about the number of zeros on a fixed \(w\)-slice. The value \(t=0\) is not attained at finite points of \(\mathbb H\times\mathbb H\).

## Proof

**1. Reproducing-kernel normalization and the quartic.** The standard Bergman kernel of \(\mathbb H\), with unnormalized area measure, is
\[
K(z,w)=-\frac1{\pi(z-\overline w)^2}.
\]
Writing \(u=z-\overline w\), direct differentiation, for every pair of nonnegative integers \(j,k\), gives
\[
\partial_z^j\partial_{\overline w}^{k}K(z,w)
=\frac{(-1)^{j+1}(j+k+1)!}{\pi u^{j+k+2}}.
\]
The Riesz Gram construction applies \(\Lambda_{a,b;z}\) and its conjugate in \(w\) to \(K\). As \(a,b\) are real, the two coefficient lists are identical. Put \(\xi=(1,a,b)\); the normalized factorials in the functional give
\[
B_{a,b}(z,w)=K(z,w)F_{a,b}(u^{-1}),
\qquad
F_{a,b}(t)=\sum_{j,k=0}^2
\frac{(-1)^j(j+k+1)!\xi_j\xi_k}{j!k!}\,t^{j+k}.
\]
The terms of odd total degree cancel pairwise. The degree-two coefficient is \(3b-6a^2+3b\), and the top coefficient is \(30b^2\). Hence the **exact polynomial** is
\[
\boxed{F_{a,b}(t)=1+6(b-a^2)t^2+30b^2t^4.}
\]
This expression can also be obtained directly by applying the two differential operators to the displayed Bergman kernel. Its prefactor \(K(z,w)\) never vanishes in the stated domain.

**2. Precise reachable region.** For \(z,w\in\mathbb H\), the difference \(u=z-\overline w\) has strictly positive imaginary part, so its reciprocal \(t=u^{-1}\) lies in \(\mathbb C_-:=\{t:\operatorname{Im}t<0\}\). Conversely, if \(t\in\mathbb C_-\), then \(u=t^{-1}=p+iq\) with \(q>0\). Choosing
\[
z=\frac p2+i\frac q2,\qquad w=-\frac p2+i\frac q2
\]
gives \(z,w\in\mathbb H\) and \(t=(z-\overline w)^{-1}\). Therefore **every** lower-half-plane zero of \(F_{a,b}\), and only such a zero, yields a zero of \(B_{a,b}\) for an interior pair.

**3. The full real-coefficient classification.** When \(b=0\),
\[
F_{a,0}(t)=1-6a^2t^2.
\]
It is constant if \(a=0\); otherwise its two roots are real. In either case it has no lower-half-plane root.

Now take \(b\ne0\) and set \(x=t^2\). The reduced polynomial is
\[
P_{a,b}(x)=30b^2x^2+6(b-a^2)x+1,
\]
whose discriminant is
\[
\Delta=36\left((a^2-b)^2-\frac{10}{3}b^2\right).
\]
Set \(h=\sqrt{10/3}>1\). The alternative \(a^2-b\le-h|b|\) is impossible, because it would imply \(a^2\le b-h|b|<0\). Consequently, \(\Delta\ge0\) is **equivalent** to \(a^2-b\ge h|b|\), exactly the displayed sharp inequality.

If \(\Delta>0\), the two roots \(x_\pm\) are distinct and positive: their product is \(1/(30b^2)>0\), and their sum is \((a^2-b)/(5b^2)>0\). Therefore all four roots \(t=\pm\sqrt{x_\pm}\) are distinct and real, and none can be attained in \(\mathbb C_-\).

If \(\Delta=0\), the reduced polynomial has the double positive root \(x_0=1/(\sqrt{30}|b|)\). The roots of \(F_{a,b}\) are exactly
\[
t=\pm(30b^2)^{-1/4},
\]
each of multiplicity two and both real. They are excluded from the open attainable region, proving zero-freeness at equality.

If \(\Delta<0\), then \(P_{a,b}\) has two distinct nonreal conjugate roots. Each has one square root strictly below, and one strictly above, the real axis. Therefore \(F_{a,b}\) has exactly two distinct simple roots in \(\mathbb C_-\). These can be described explicitly by
\[
x_\pm=\frac{a^2-b\pm i\sqrt{(10/3)b^2-(a^2-b)^2}}{10b^2},
\]
and taking the two square roots with negative imaginary part. They are nonzero and distinct because the product of the roots of \(P_{a,b}\) is nonzero. The realizability in Step 2 supplies interior zero pairs for both.

The three cases exhaust all real \((a,b)\), proving the theorem and all multiplicity assertions. At an interior scalar zero the \(z\)-derivative is nonzero because \(F'_{a,b}(t)\ne0\) and \(\partial_z t=-t^2\ne0\).

## Verification

The coefficients were checked independently by symbolic differentiation of the classical Bergman kernel and by exact factorial expansion; both give precisely \(1+6(b-a^2)t^2+30b^2t^4\). The discriminant and the case division are exact identities, not numerically inferred.

Run `python CHECK.py` from the extracted package using Python's standard library. It checks exact rational coefficient identities and a finite grid of complex roots, realizable zero pairs, Hermitian symmetry, positive diagonals, two-point Gram positivity, and the double-root transition. The original run completed with `CHECK_OK 4313`. These tests are supplementary; the universal classification follows from Steps 1–3.

## Relationship to prior work

Gehlawat, Jain and Sarkar introduce the canonical positive-definite Riesz-family Gram kernel for differential evaluations. Their upper-half-plane representation supplies the general derivative formula and auxiliary entire function; their Lu Qi-Keng examples treat single-index and factorially supported sequences. The **new claim here is not that general representation** but the sharp two-real-parameter zero-free/zero-fibre phase diagram for the first complete three-jet \((1,a,b)\).

The published two-jet classification for support \(\{0,1\}\) concerns an adjacent two-term functional; for real coefficients it is zero-free, but it has no second-derivative term and does not imply the threshold here. A published parity law for separated derivative orders \(\{p,q\}\) with \(q-p\ge2\) shows all such two-term kernels have zeros; its scope explicitly excludes three nonzero derivatives. In contrast, \((1,0,b)\) with \(b\ne0\) has zeros here, while inclusion of a sufficiently strong first-derivative coefficient can remove them. That restoration mechanism cannot follow merely by substituting parameters into either two-term classification.

Bao, Guan and Sun study extremal and higher-order \(p\)-Bergman kernels; their inspected results do not classify zeros of the canonical two-variable Riesz Gram kernel. Standard Lu Qi-Keng classifications for domain Bergman kernels concern different objects.

## Limitations

Only real coefficients normalized by a nonzero constant zeroth jet are covered. The theorem does not classify complex three-jet phases, arbitrary longer sequences, other domains, or the zero count on a fixed fibre \(w=\text{constant}\). At equality, the auxiliary real roots are **boundary roots**, not interior zeros. No independent validation is implied by the accompanying reproducibility checks. A pre-existing unindexed equivalent calculation of this real three-jet case cannot be excluded by literature searching alone.

## References

1. S. Gehlawat, A. Jain and A. D. Sarkar, *A Canonical Positive Definite Kernel Associated with the \(\xi\)-Bergman Kernel*, arXiv:2608.13193v1, first posted 2026-08-13; especially Theorem 4.1, formula (4.6), and Theorem 4.11. https://arxiv.org/abs/2608.13193
2. *Exact two-jet Lu Qi-Keng phase for the canonical \(\xi\)-Bergman Gram kernel*, 2026, publicly indexed research result, identifier `2026/10/11/SCOPE-exact-two-jet-lu-qi-keng-phase-for-the-canonical-bergman-gram-ke--364c00673845`.
3. *Parity law for zeros of separated weighted Bergman jet Gram kernels*, 2026, publicly indexed research result, identifier `2026/10/11/SCOPE-parity-law-for-zeros-of-separated-weighted-bergman-jet-gram-kern--48a4d84c1cc7`.
4. S. Bao, Q. Guan and X. Sun, *On the \(p\)-Bergman kernel with respect to a functional \(\xi\)*, arXiv:2510.13144v2, 2025. https://arxiv.org/abs/2510.13144
