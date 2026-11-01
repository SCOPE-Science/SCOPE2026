# Sharp rare-event and moment laws for antithetic nested Monte Carlo at a kink

## Finding

Let \(n=2m\to\infty\) be even. In the two-block antithetic estimator of the positive-part payoff, define
\[
\Delta_n=\frac{(A_n)_+ +(B_n)_+}{2}-\left(\frac{A_n+B_n}{2}\right)_+,
\quad z_+=\max\{z,0\}.
\]
Here \(A_n\) and \(B_n\) are independent inner-block averages conditional on the same outer value, as specified below. Convexity implies \(\Delta_n\ge0\). If the outer variable has a bounded density continuous and positive at the kink, then, for every \(r>0\) with the stated moment assumption,
\[
\boxed{\lim_{\substack{n\to\infty\\ n\text{ even}}}
 n^{(r+1)/2}\mathbb E\Delta_n^r
 =\frac{2^{1-r}}{r+1}f(0)\sigma^{r+1}\mathbb E|Z|^{r+1},\quad Z\sim N(0,1).}
\]
In particular, the probability of a nonzero correction has a sharp rare-event law
\[
\boxed{\sqrt n\,\mathbb P(\Delta_n>0)\longrightarrow
 \lambda=2\sigma f(0)\sqrt{2/\pi}.}
\]
For \(M_n\) independent outer replications, the probability that **every** observed antithetic correction is zero tends to \(e^{-c\lambda}\) if \(M_n/\sqrt n\to c\in[0,\infty)\), and to zero if \(M_n/\sqrt n\to\infty\). Thus fewer than order \(\sqrt n\) independent pilot replications are insufficient even to see a nonzero correction with high probability. Under the fifth-plus moment assumption in the next section, the ordinary centered kurtosis obeys
\[
\boxed{\lim_{\substack{n\to\infty\\ n\text{ even}}}\frac{\operatorname{Kurt}(\Delta_n)}{\sqrt n}
 =\frac{9\sqrt{2\pi}}{10\sigma f(0)}.}
\]
A Gaussian subfamily admits the following additional **exact finite-sample distribution**. For independent \(Y\sim N(0,\tau^2)\), \(\epsilon_i\sim N(0,\sigma^2)\), where \(\tau,\sigma>0\), set \(t=\sigma^2/n\), \(w=\tau^2+t\), and \(\theta=\arctan\sqrt{t/w}\). For independent standard normal \(Z_1,Z_2\),
\[
\Delta_n\ \overset{d}=\ \frac12\bigl(\sqrt t\,|Z_1|-\sqrt w\,|Z_2|\bigr)_+.
\]
Consequently,
\[
\boxed{\mathbb P(\Delta_n>0)=\frac{2\theta}{\pi},\quad
\mathbb E\Delta_n=\frac{\sqrt{\tau^2+2t}-\sqrt{\tau^2+t}}{\sqrt{2\pi}},}
\]
\[
\boxed{\mathbb E\Delta_n^2
 =\frac{(\tau^2+2t)\theta-\sqrt{t(\tau^2+t)}}{2\pi}.}
\]
For every real \(r>0\), all Gaussian moments are explicitly represented by
\[
\mathbb E\Delta_n^r=\frac{2^{1-r/2}\Gamma(1+r/2)}{\pi}
\int_0^{\theta}\bigl(\sqrt t\cos\varphi-\sqrt w\sin\varphi\bigr)^r\,d\varphi.
\]
The centered-kurtosis limit in this Gaussian subfamily simplifies to \(9\pi\tau/(5\sigma)\).

## Assumptions and scope

The outer scalar \(Y\) is independent of independent identically distributed centered inner errors \(\epsilon_1,\epsilon_2,\ldots\), each with variance \(\sigma^2\in(0,\infty)\). The distribution of \(Y\) has a bounded density \(f:\mathbb R\to[0,\infty)\), continuous at the threshold zero, with \(f(0)>0\). Define
\[
A_n=Y+\frac1m\sum_{i=1}^{m}\epsilon_i,\qquad
B_n=Y+\frac1m\sum_{i=m+1}^{2m}\epsilon_i,\qquad n=2m.
\]
All limits take place along even positive integers \(n\). The moment limit for a specified real \(r>0\) assumes \(\mathbb E|\epsilon_1|^{r+1+\delta}<\infty\) for some \(\delta>0\); the indicator limit uses only finite positive variance. The simultaneous statements through fourth order, including kurtosis, hold if \(\mathbb E|\epsilon_1|^{5+\delta}<\infty\) for some \(\delta>0\). Replications used for the zero-pilot law are mutually independent copies of both \(Y\) and their inner errors. The displayed Gaussian formulas require the additional normality and independence indicated in the finding; they are not claimed for general error laws.

The correction orientation here is the nonnegative coarse-average-minus-fine Jensen gap; its negative is an equally common multilevel correction convention. Reversing the convention reverses the signed odd moments but does not change the probability, variance or kurtosis.

## Proof

**1. An exact triangular-hat identity.** Conditional on fixed half-sample noise offsets \(a,b\in\mathbb R\), put \(d=|a-b|\) and \(c=(a+b)/2\). Evaluating the piecewise-linear positive-part function on the intervals delimited by \(-a\), \(-b\) and \(-c\) gives the exact identity
\[
\frac{(y+a)_++(y+b)_+}{2}-(y+c)_+
 =\left(\frac d4-\frac{|y+c|}{2}\right)_+.
\]
It follows that the gap is positive precisely on the open interval \(\{|y+c|<d/2\}\), of length \(d\), and has height \(d/4\). For any real \(r>0\), elementary integration on the two halves of its support gives
\[
\int_{\mathbb R}\left(\frac d4-\frac{|y+c|}{2}\right)_+^rdy
 =\frac{d^{r+1}}{4^r(r+1)}.
\]
The formula also holds for \(r=0\) when interpreted as the support-indicator integral (with \(d=0\) contributing zero).

**2. Distribution of the conditional width.** Let \(a_n,b_n\) be the two centered block means. Each has variance \(2\sigma^2/n\), so
\[
D_n=\frac{\sqrt n}{2\sigma}(a_n-b_n)\ \Rightarrow\ Z\sim N(0,1).
\]
Also \(\sqrt n(a_n+b_n)\) is tight. The assumptions ensure uniform integrability of \(|D_n|^{r+1}\): the finite \((r+1+\delta)\)-moment and standard moment bounds for sums of independent centered variables supply bounded corresponding higher moments. For the support probability, uniform integrability of \(|D_n|\) follows already from their unit second moments.

**3. Replacing the outer density by its kink value.** Conditional on \(a_n,b_n\), the \(r\)-moment is the triangular-hat integral weighted by \(f(y)\). Its nonzero support lies within \(|y|\le |(a_n+b_n)/2|+|a_n-b_n|/2\), which vanishes in probability. Boundedness and continuity of \(f\) at zero therefore replace \(f(y)\) by \(f(0)\), with an error \(o(n^{-(r+1)/2})\). To justify that error without an implicit uniformity assumption, fix \(\varepsilon>0\), restrict to the event that both support endpoints lie inside a continuity neighborhood of zero, and bound the integrand by \(\varepsilon d^{r+1}/[4^r(r+1)]\). On the complement, use boundedness of \(f\) and uniform integrability of \(n^{(r+1)/2}d^{r+1}\). Then send \(n\to\infty\) and \(\varepsilon\downarrow0\). The same argument with indicator integrands handles \(r=0\).

Since \(d=2\sigma|D_n|/\sqrt n\), this yields
\[
\lim n^{(r+1)/2}\mathbb E\Delta_n^r
 =\frac{f(0)(2\sigma)^{r+1}}{4^r(r+1)}\mathbb E|Z|^{r+1},
\]
which is the asserted constant, including \(r=0\) for the nonzero probability.

**4. Pilot threshold and kurtosis.** The independent-replication probability that all \(M_n\) corrections vanish is \((1-p_n)^{M_n}\), with \(p_n=\mathbb P(\Delta_n>0)\sim\lambda n^{-1/2}\). The three pilot regimes follow by taking logarithms (or monotonicity when the ratio diverges). The moment limits give \(\mathbb E\Delta_n=O(n^{-1})\), \(\mathbb E\Delta_n^2\sim f(0)\sigma^3\sqrt{2/\pi}\,n^{-3/2}/3\), and \(\mathbb E\Delta_n^4\sim f(0)\sigma^5\sqrt{2/\pi}\,n^{-5/2}/5\). Hence the squared mean is lower order than the second raw moment, and every fourth central-moment cross-term is lower order than the fourth raw moment. Dividing gives the stated sharp centered-kurtosis constant.

**5. Exact Gaussian reduction.** In the Gaussian case, \(a_n-b_n\) and \(a_n+b_n\) are independent jointly normal variables. Thus \(d\) has the law \(2\sqrt t|Z_1|\), whereas \(Y+c\) has law \(\sqrt w Z_2\), independently. Substitution into the triangular-hat identity proves the distribution. In polar coordinates for \((|Z_1|,|Z_2|)\), the nonzero region is the angular wedge \(0<\varphi<\theta\), and a radial gamma integral gives the all-order angular formula. The angular measure gives \(2\theta/\pi\); elementary integration for orders one and two gives the two closed moments. Substituting \(f(0)=1/(\sqrt{2\pi}\tau)\) in the universal kurtosis constant yields \(9\pi\tau/(5\sigma)\).

## Verification

Run `python3 verify.py` with Python 3.9 or later (standard library only). It tests the exact piecewise-linear identity over nontrivial offsets, its integrated powers, finite Gaussian probability/first/second-moment expressions against a separately evaluated polar integral, the predicted limiting moment coefficients, the kurtosis scaling and the independent-pilot threshold. The recorded run passed **593 deterministic checks**. This is supporting finite verification, not a substitute for the asymptotic proof above; neither random sampling nor an exhaustive search over outer distributions is claimed.

## Relationship to prior work

Haji-Ali and Spence's *Nested Multilevel Monte Carlo with Biased and Antithetic Sampling* (arXiv:2308.07835v1, first public August 15, 2023) studies the same nested maximum and antithetic construction, proves general upper-moment rates and reports level-dependent kurtosis growth. The present scope is a centered two-block positive-part specialization, and it does **not** claim that the general rate, antithetic correction or high-level kurtosis phenomenon is new. The precise asymptotic constants for arbitrary positive moments, rare-event/pilot threshold, and exact finite Gaussian correction law are the specific claims compared here. Giles and Goda (arXiv:1708.05531v1) study antithetic nested estimation for decision-making; their complexity results likewise do not by themselves imply these exact statistics.

The 2020 initial-margin multilevel study of Bourgey, De Marco, Gobet and Zhou is particularly relevant to the same positive-part setting; a complete text-level comparison was unavailable for this review. It remains an explicit priority risk, as do earlier specialized Gaussian positive-part and nested simulation identities. The theorem's mathematical proof does not depend on inaccessible literature, but the absence of an independently located prior formula is **not** a proof of publication priority.

## Limitations

This is a scalar, single-kink payoff with independent centered inner noise, one common outer variable per antithetic pair, a positive continuous outer density at the kink, and moment conditions stated above. The exact finite distribution requires Gaussian outer and inner variables. The result concerns the population correction distribution and independent pilot replications; it does not guarantee a given finite pilot will detect the correction, nor does it optimize a complete multilevel allocation or cost, extend to discontinuous payoffs, or address nested models with dependent or biased inner approximations. Finite computations do not prove the all-parameter limits. The result has undergone self-review only; independent scientific audit and full publication-priority verification are not established.

## References

1. A.-L. Haji-Ali and J. Spence, *Nested Multilevel Monte Carlo with Biased and Antithetic Sampling*, arXiv:2308.07835v1 (August 15, 2023), https://arxiv.org/abs/2308.07835 .
2. M. B. Giles and T. Goda, *Decision-making under uncertainty: using MLMC for efficient estimation of EVPPI*, arXiv:1708.05531v1 (August 18, 2017), https://arxiv.org/abs/1708.05531 .
3. F. Bourgey, S. De Marco, E. Gobet and Y. Zhou, *Multilevel Monte-Carlo methods and lower-upper bounds in Initial Margin computations* (2020), https://doi.org/10.1515/mcma-2020-2062 . A full-text priority comparison remains open.
4. J. Spence, *Hierarchical and Adaptive Methods for Accurate and Efficient Risk Estimation*, doctoral thesis (2023), https://www.ros.hw.ac.uk/server/api/core/bitstreams/3d4f5b42-9607-4c5b-8fc2-77fb74717adb/content .
