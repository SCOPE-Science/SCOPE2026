# A sharp Mittag–Leffler quartic crossover for symmetric minimal-walk noise

## Finding

Fix \(0<p<1\), \(0<\delta<1\). In the minimal random walk, let \(I_1=1\), let \(K_n=\sum_{j=1}^n I_j\), and let
\[
\Pr(I_{n+1}=1\mid I_1,\ldots,I_n)=\frac{pK_n}{n}.
\]
Independently take positive step sizes \(Z_j\in\{1-\delta,1+\delta\}\), each with probability \(1/2\). Define the centered self-normalized noise
\[
T_n=\frac{\sum_{j=1}^n I_j(Z_j-1)}{\sqrt{\sum_{j=1}^n I_j(Z_j-1)^2}}.
\]
The denominator is positive almost surely. Let \(\overline\Phi(x)=\Pr(G\ge x)\) for a standard normal \(G\). Let \(W_p\) be the positive Mittag–Leffler movement-count limit characterized by
\[
\frac{K_n}{n^p}\longrightarrow W_p\quad\text{almost surely},\qquad
\mathbb E W_p^r=\frac{r!}{\Gamma(1+pr)}\quad(r=1,2,\ldots).
\]
For **every deterministic** \(x_n\ge0\) with \(x_n/n^{p/4}\to c\in[0,\infty)\),
\[
\boxed{\frac{\Pr(T_n\ge x_n)}{\overline\Phi(x_n)}
\longrightarrow F_p(c):=\mathbb E\exp\!\left(-\frac{c^4}{12W_p}\right).}
\]
The same limit holds for \(\Pr(T_n\le -x_n)\). In particular, for **every** nonnegative \(u_n=o(n^{p/4})\),
\[
\boxed{\sup_{0\le x\le u_n}
\left|\frac{\Pr(T_n\ge x)}{\overline\Phi(x)}-1\right|\longrightarrow0.}
\]
For every \(c>0\), \(0<F_p(c)<1\), and \(F_p\) is continuous and strictly decreasing on \((0,\infty)\), with \(F_p(0)=1\). Hence \(n^{p/4}\) is the **sharp power scale** for uncorrected Gaussian relative-tail approximation in this step-size law: nonzero critical multiples have a strictly subunit asymptotic ratio. The limit is independent of \(\delta\).

## Assumptions and scope

The movement clock is the \(q=0\) minimal walk with deterministic initial movement and fixed \(p\in(0,1)\). The positive step-size noise is independent of the movement clock, identically distributed and exactly symmetric two-point about its mean; \(0<\delta<1\) ensures strict positivity. All limits concern the centered step-size noise \(T_n\), **not** the centered full position. The argument \(c\) is any fixed finite nonnegative real; no relative-tail assertion for \(x_n/n^{p/4}\to\infty\) is made. The limiting movement-count law and its strict positivity are established in the cited minimal-walk literature. The fixed-sample sign-tail estimate below is also reproved here.

## Proof

**1. Reduction to an independently stopped sign sum.** Write \(\varepsilon_j=(Z_j-1)/\delta\), so the \(\varepsilon_j\) are independent fair signs. Since each squared centered step is \(\delta^2\), the conditional random-sum representation gives
\[
\mathcal L(T_n\mid K_n=m)=\mathcal L\left(m^{-1/2}\sum_{j=1}^m\varepsilon_j\right),\qquad m\ge1.
\]
In particular, for \(r_m(x):=\Pr(\sum_{j=1}^m\varepsilon_j\ge x\sqrt m)/\overline\Phi(x)\),
\[
\frac{\Pr(T_n\ge x)}{\overline\Phi(x)}=\mathbb E\,r_{K_n}(x).
\]
The clock limit \(K_n/n^p\to W_p>0\) almost surely follows from the classical \(q=0\) minimal-walk law. Its normalization is fixed by the displayed Mittag–Leffler moment formula; equivalently, the exact rising-factorial identity is
\[
\mathbb E\bigl[K_n(K_n+1)\cdots(K_n+r-1)\bigr]
=r!\prod_{j=1}^{n-1}\left(1+\frac{pr}{j}\right).
\]
The recursion for this identity is immediate from \(\Pr(K_{n+1}=K_n+1\mid K_n=k)=pk/n\); it agrees with the stated moment normalization. We invoke strict positivity of the almost-sure limit from the cited movement-clock theorem, rather than attempting to infer it from moments alone.

**2. A fixed-sample fourth-order lemma.** For any integer sequence \(m\to\infty\) and \(x_m\ge0\) such that \(x_m/m^{1/4}\to d\in[0,\infty)\),
\[
\boxed{r_m(x_m)\longrightarrow e^{-d^4/12}.}
\]
To prove this, put \(y=x/\sqrt m\), \(\theta=\operatorname{arctanh}(y)\), \(v=1-y^2\), and
\[
I(y)=\theta y-\log\cosh\theta
=\frac{(1+y)\log(1+y)+(1-y)\log(1-y)}2.
\]
For \(x=O(m^{1/4})\), eventually \(0\le y<1/2\). Exponentially tilt the signs so that their mean becomes \(y\), their variance becomes \(v\), and their independence is preserved. With \(S_m=\sum_{j=1}^m\varepsilon_j\), define \(U_m=(S_m-my)/\sqrt{mv}\) under that tilted law, and \(a=\theta\sqrt{mv}\). Exact change of measure gives
\[
\Pr(S_m\ge x\sqrt m)=e^{-mI(y)}
\mathbb E_\theta[e^{-aU_m}\mathbf1_{\{U_m\ge0\}}].
\]
Because \(y\to0\), the tilted signs have uniformly bounded third absolute centered moments and variance bounded away from zero. Berry–Esseen therefore gives a Kolmogorov bound \(C m^{-1/2}\) for \(U_m\) against a standard normal. The bounded-variation function \(u\mapsto e^{-au}\mathbf1_{\{u\ge0\}}\) has total variation at most two for every \(a\ge0\). Integration by parts transfers the Kolmogorov estimate to this expectation, yielding
\[
\Pr(S_m\ge x\sqrt m)=e^{-mI(y)}
\left[e^{a^2/2}\overline\Phi(a)+O(m^{-1/2})\right].
\]
Here \(a=x(1+O(x^2/m))\) and \(e^{a^2/2}\overline\Phi(a)\asymp(1+a)^{-1}\). Thus the relative error inside the brackets is \(O((1+x)/\sqrt m)=o(1)\). If \(x\to\infty\), Mills' ratio and \(a/x\to1\) give
\[
 r_m(x)=\exp\left(\frac{x^2}{2}-mI(y)\right)\frac{x}{a}\,[1+o(1)].
\]
The convergent rate expansion
\[
I(y)=\frac{y^2}{2}+\frac{y^4}{12}+O(y^6)
\]
then gives \(mI(y)-x^2/2=x^4/(12m)+O(x^6/m^2)\); the remainder is \(o(1)\) throughout \(x=O(m^{1/4})\). If \(x\) remains bounded, the tilted formula gives \(r_m(x)\to1\). Every sequence has bounded or diverging subsequences, proving the lemma including \(d=0\). A lattice-point equality at the threshold is covered by the Berry–Esseen error; no continuity correction survives.

**3. A uniform integrable Gaussian tail envelope.** For each \(m\ge1\), symmetry and the Gaussian comparison inequality for bounded martingale increments imply, for every \(x>0\),
\[
\Pr(S_m\ge x\sqrt m)
=\tfrac12\Pr(|S_m|\ge x\sqrt m)
\le\frac{2e^3}{9}\overline\Phi(x).
\]
The cited comparison inequality applies to \(S_m\) as a real-valued martingale with increments bounded by one. At \(x=0\), the elementary inequality \(\Pr(S_m\ge0)/\overline\Phi(0)\le2\) suffices. Consequently
\[
0\le r_m(x)\le\max\{2,2e^3/9\}
\quad\text{for every }m\ge1,\;x\ge0.
\]
This **relative** envelope, rather than a Hoeffding estimate with a growing normal-tail prefactor, is what permits mixing over exceptionally small clock values without losing the polynomial range.

**4. Mixing and sharpness.** For almost every movement-clock sample path, \(K_n/n^p\to W_p\in(0,\infty)\), so \(K_n\to\infty\). Whenever \(x_n/n^{p/4}\to c\),
\[
\frac{x_n}{K_n^{1/4}}\longrightarrow\frac{c}{W_p^{1/4}}.
\]
Apply the fixed-sample lemma pathwise at the random integer \(m=K_n\), to obtain
\[
r_{K_n}(x_n)\longrightarrow\exp\left(-\frac{c^4}{12W_p}\right)\quad\text{almost surely}.
\]
The constant envelope in step 3 allows bounded convergence in expectation, proving the stated critical limit. For \(c=0\), the limit equals one. To obtain uniformity on \([0,u_n]\), suppose otherwise; choose a violating deterministic sequence \(0\le x_n\le u_n\). Then \(x_n/n^{p/4}\to0\), contradicting the just-proved sequential result. Symmetry gives the lower-tail assertion. Finally, since \(0<W_p<\infty\) almost surely, \(\exp(-c^4/(12W_p))\) is strictly between zero and one for \(c>0\), and monotone bounded convergence proves the claimed strict and continuous profile. Every positive critical multiple therefore obstructs uniform uncorrected approximation on that scale.

## Verification

The accompanying standard-library program `verify.py` checks the exact finite-clock mass recursion, rising-factorial moments, exact finite-binomial tails, fourth- and sixth-order rate coefficients, finite-instance Gaussian tail comparison, and the approach of fixed-sample ratios toward \(\exp(-c^4/12)\). Run `python3 verify.py` from the directory containing this file. The included `verification_output.txt` is the actual recorded output of that run. These checks do **not** establish the infinite-size limit: steps 2–4, the cited movement-count limit, the cited martingale comparison, and the classical Berry–Esseen theorem provide that proof.

## Relationship to prior work

Liang (2026), Theorems 2.5 and Proposition 2.6, gives a logarithmic sufficient relative-tail range at \(q=0\) and an explicit *nonsymmetric* bounded-step counterexample to a uniform polynomial range across step laws. Liang's Lemma 3.1 supplies the conditional random-sum representation, Lemma 3.2 the movement-count estimates, and the cited classical movement-count limit identifies \(W_p\). The present statement singles out **symmetric positive two-point steps** and supplies the sharp \(n^{p/4}\) scale and a nontrivial Mittag–Leffler quartic crossover; it neither contradicts nor reclaims Liang's general assertion.

Liu, Liu and Lu (2026), introduction (equations (1.1)–(1.4)), explicitly notes the fixed-sample symmetric Rademacher quartic factor \(\exp(-x^4/(12m))\), a classical Cramér–Petrov phenomenon. That fixed-sample factor is **not claimed as new**. The contribution here is its precise transmission through the nonconcentrating minimal-walk clock, including the random critical mixture and uniformity. Juškevičius and Šileikis (2026), Theorem 1, supplies a universal Gaussian tail comparison that controls small-clock contributions. Eichelsbacher and Löwe (2017) address logarithmic moderate-deviation principles for random sums under various scaling assumptions; their displayed results do not provide this self-normalized, relative-normal-tail quartic profile for the minimal walk.

## Limitations

No general result for asymmetric, other symmetric continuous, or unbounded step-size laws is asserted. The starting move is deterministic and \(p\) is fixed in \((0,1)\); there is no uniform assertion in \(p\). The result concerns the noise statistic, not the full position, and only finite critical constants \(c\). The finite verification tests are not an exhaustive test of infinite limits. Priority against all older unindexed random-index Cramér expansions has not been independently established, and the scientific assessment is not independent validation.

## References

1. Shuyuan Liang, *Normal approximation and self-normalized moderate deviations for the minimal random walk with random step sizes*, arXiv:2610.29156v1, first posted 21 October 2026, https://arxiv.org/html/2610.29156v1.
2. Hui-Lin Liu, Song-Hao Liu and Dawei Lu, *Refined Cramér-type moderate deviations by Stein's method under dependence*, arXiv:2610.29078v1, first posted 21 October 2026, https://arxiv.org/html/2610.29078v1.
3. Tomas Juškevičius and Matas Šileikis, *Concentration inequalities for vector-valued martingales*, arXiv:2610.31449v1, first posted 22 October 2026, https://arxiv.org/html/2610.31449v1.
4. Peter Eichelsbacher and Matthias Löwe, *Lindeberg's method for moderate deviations and random summation*, arXiv:1705.03837, first posted 10 May 2017, https://arxiv.org/abs/1705.03837.
