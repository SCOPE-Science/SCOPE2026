# Sharp Poisson approximation for one square-root multiset block

## Finding

For each integer \(n\ge 2\), let \(1\le m=m_n\le n\) be an integer. Form a multiset with one symbol appearing \(m\) times and each of the remaining \(n-m\) symbols appearing once. Choose one of its distinct arrangements uniformly, and let \(W_n\) be the number of positions agreeing with the sorted arrangement. Write
\[
\lambda_n=\frac{n-m+m^2}{n},\qquad q_\lambda(j)=e^{-\lambda}\frac{\lambda^j}{j!}\quad(j\ge0),
\]
with \(q_\lambda(j)=0\) for negative integers. Put \(\Delta^2q_\lambda(j)=q_\lambda(j)-2q_\lambda(j-1)+q_\lambda(j-2)\).

**Theorem.** For each pair of fixed constants \(0<a<b<\infty\), uniformly over integers satisfying \(a\sqrt n\le m\le b\sqrt n\), one has the signed, whole-distribution expansion
\[
\sum_{j\ge0}\left|\Pr(W_n=j)-q_{\lambda_n}(j)
+\frac{m^3}{n^2}\Delta^2q_{\lambda_n}(j)\right|=O_{a,b}(n^{-1}). \tag{1}
\]
Consequently, whenever \(m_n/\sqrt n\to c\in(0,\infty)\),
\[
\lim_{n\to\infty}\sqrt n\,d_{\rm TV}(\mathcal L(W_n),\operatorname{Poisson}(\lambda_n))
=\frac{c^3}{2}\sum_{j\ge0}|\Delta^2q_{1+c^2}(j)|>0.\tag{2}
\]
In particular, for the explicit critical multiplicity \(m_n=\lfloor\sqrt n\rfloor\),
\[
\boxed{\lim_{n\to\infty}\sqrt n\,d_{\rm TV}(\mathcal L(W_n),\operatorname{Poisson}(\lambda_n))
=\frac{5}{3}e^{-2}.}\tag{3}
\]
Thus the inverse-square-root upper bound in this natural example has an exact, nonzero leading constant, not merely an upper bound and a logarithmically weaker lower bound.

## Assumptions and scope

All arrangements are equally likely; repeated copies are indistinguishable. An agreement at one of the \(m\) designated positions for the repeated symbol counts as one fixed point. \(d_{\rm TV}(P,Q)=\frac12\sum_{j\ge0}|P\{j\}-Q\{j\}|\). The theorem concerns the law of the total fixed-point count and the Poisson approximation with its **exact finite-sample mean**, not an approximation by a fixed Poisson law. Constants in \(O_{a,b}\) may depend on the displayed compact multiplicity interval.

## Proof

**Step 1: exact mixed factorial transform.** Write \(U_n\) for agreements at singleton positions and \(K_n\) for agreements at positions assigned to the repeated symbol. Set \(t=n-m\), \(\mu=t/n\), and \(\nu=m^2/n\). For any nonnegative integers \(r\le t\), \(s\le m\), prescribing \(r\) different singleton matches and \(s\) repeated-symbol matches has probability \((m)_s/(n)_{r+s}\): the designated singleton values must all occupy their own places and the designated repeated-symbol positions must receive distinct copies of that symbol. Here \((x)_k=x(x-1)\cdots(x-k+1)\) with \((x)_0=1\). Therefore
\[
\mathbb E\binom{U_n}{r}\binom{K_n}{s}
=\frac{\binom tr\binom ms(m)_s}{(n)_{r+s}}.\tag{4}
\]
This is an exact finite counting identity. Summing gives the entire polynomial
\[
F_n(z):=\mathbb E(1+z)^{W_n}
=\sum_{r=0}^{t}\sum_{s=0}^{m}
\frac{\binom tr\binom ms(m)_s}{(n)_{r+s}}z^{r+s}.\tag{5}
\]
The terms with \(r+s=0\) have denominator one; each displayed denominator is positive because \(r+s\le n\).

**Step 2: a uniform analytic expansion.** Divide the coefficient of \(z^{r+s}\) in (5) by \(\mu^r\nu^s/(r!s!)\). The ratio is
\[
R_{r,s}=\frac{(t)_r}{t^r}\left(\frac{(m)_s}{m^s}\right)^2
\frac{n^{r+s}}{(n)_{r+s}}.\tag{6}
\]
When \(0\le r+s\le n^{1/8}\) and \(a\sqrt n\le m\le b\sqrt n\), the falling-factorial product expansions give, uniformly,
\[
R_{r,s}=1-\frac{s(s-1)}m+O_{a,b}\left(\frac{(r+s+1)^4}{n}\right).\tag{7}
\]
Indeed the two copies of \((m)_s/m^s\) each contribute \(-s(s-1)/(2m)\); factors involving \(t\) and \(n\) have relative error \(O((r+s)^2/n)\), and second-order errors in \(1/m\) have magnitude \(O((r+s)^4/m^2)=O_{a,b}((r+s)^4/n)\).

This termwise expansion can be summed **uniformly on every fixed complex disk** \(|z|\le R\). To justify the tail, observe that, for \(r\le n/2\) and all sufficiently large \(n\), the nonnegative coefficient in (5) is at most \(1/r!\) times \((3m^2/n)^s/s!\), because \(\binom tr/(n)_r\le1/r!\) and \((n-r)_s\ge(n/2-m)^s\ge(n/3)^s\). For \(r>n/2\), the same coefficient is at most \(\binom ms/r!\), since \((m)_s/(n-r)_s\le1\) whenever \(r\le t\). Summing over \(s\) bounds this second region by \(2^m\sum_{r>n/2}1/r!\), which decays faster than any power of \(n\). The first region is dominated by a product of two convergent exponential series with bounded parameters. In particular its part where \(r+s>n^{1/8}\) is superpolynomially small, uniformly on \(|z|\le R\). The comparison series in (7), including its polynomial factor, has the same property.

Summing (7) and using \(\sum_{s\ge0}s(s-1)(\nu z)^s/s!=(\nu z)^2e^{\nu z}\), we obtain
\[
F_n(z)=e^{(\mu+\nu)z}
\left(1-\frac{\nu^2}{m}z^2\right)+O_{a,b,R}(n^{-1})
=e^{\lambda_n z}\left(1-\frac{m^3}{n^2}z^2\right)+O_{a,b,R}(n^{-1}).\tag{8}
\]
The error is a bound for the **complex modulus** of the entire function difference, not merely convergence of moments.

**Step 3: pass to all probabilities.** Put \(z=w-1\) in (8). On the circle \(|w|=2\), use (8) with \(R=3\). Cauchy's coefficient bound implies that a function bounded in modulus by \(C/n\) on this circle has Taylor coefficients whose sum of absolute values is at most \(2C/n\). The coefficient of \(w^j\) in \(e^{\lambda_n(w-1)}\) equals \(q_{\lambda_n}(j)\), while that in \((w-1)^2e^{\lambda_n(w-1)}\) is \(\Delta^2q_{\lambda_n}(j)\). This proves (1). It also proves the nonasymptotic uniform absolute-summability assertion needed for (2); pointwise convergence alone would not suffice.

Since \(\lambda_n\to1+c^2\), the Poisson probability sequences and their second differences converge in \(\ell^1\), and \(\sqrt n\,m^3/n^2\to c^3\). Taking half the \(\ell^1\) norm of (1) gives (2).

**Step 4: evaluate the critical constant.** For \(\lambda=2\),
\[
\Delta^2q_2(j)=q_2(j)\frac{(j-1)(j-4)}4\qquad(j\ge0).\tag{9}
\]
It is positive at \(j=0\) and \(j\ge5\), negative at \(j=2,3\), and zero at \(j=1,4\). By telescoping,
\[
\sum_{j\ge0}|\Delta^2q_2(j)|
=2\bigl(q_2(0)+q_2(3)-q_2(4)\bigr)
=\frac{10}{3}e^{-2}.\tag{10}
\]
Substituting \(c=1\) in (2) yields (3).

## Verification

The accompanying standard-library Python script `verification/check.py` independently calculates exact rational fixed-point distributions from (4), verifies nonnegativity, total mass, the exact mean, and the second factorial cumulant, and checks direct arrangement enumeration on small examples. It reports the finite-sample scaled total-variation distances against the limiting constant. These finite evaluations only check the algebra and numerical behavior; the infinite claims follow from Steps 1–4 and the summable analytic remainder.

## Relationship to prior work

Dudley Stark's *Poisson approximations of the number of fixed points in random multiset permutations* (first submitted 1 August 2026, arXiv:2608.00710) defines this fixed-point model and proves a general Stein upper bound. In the specific example with one symbol of order \(\sqrt n\) and the others distinct, its Section 3 yields an upper bound of order \(n^{-1/2}\); its Section 4 derives a lower bound weaker by logarithmic factors. Neither section states the exact coefficient or the signed \(\ell^1\) expansion here. The exact factorial-counting formula (4) and its uniform analytic summation supply the new step. The general Poisson–Charlier expansion framework is classical: the contribution is the particular uniform coefficient calculation and the exact error constant for this multiset model, not the invention of that framework. Diaconis and Fulman (2023) and Barbour, Holst and Janson (1992) provide broad shuffle and Poisson-approximation background. All priority statements are limited to materially inspected sources; unlocated general expansions could subsume the argument.

## Limitations

The parameter \(c\) is fixed and strictly positive, so the expansion is not claimed uniformly across regimes \(m=o(\sqrt n)\) or \(m\gg\sqrt n\). There is only one repeated symbol; adding multiple large blocks may create different first-order terms. The statement concerns fixed-point counts under uniform multiset arrangements, not cycle statistics of a multiset permutation. Independent priority assessment has not been performed. Numerically verified finite samples cannot establish the infinite asymptotics.

## References

1. D. Stark, *Poisson approximations of the number of fixed points in random multiset permutations*, arXiv:2608.00710, first submitted 2026-08-01, https://arxiv.org/abs/2608.00710.
2. A. D. Barbour, L. Holst, and S. Janson, *Poisson Approximation*, Clarendon Press, 1992.
3. P. Diaconis and J. Fulman, *The Mathematics of Shuffling Cards*, American Mathematical Society, 2023.
