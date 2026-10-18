# A sharp ultra-log-concavity obstruction for trimmed Poisson order-statistic sums

## Finding
Let \(X_1,\ldots,X_m\) be independent Poisson observations, each of intensity \(\lambda>0\), with ordered values \(X_{(1)}\le\cdots\le X_{(m)}\). For \(1\le r\le m\), define the upper trimmed sum
\[
Y_{m,r}=\sum_{i=m-r+1}^{m}X_{(i)}.
\]
The **complete ultra-log-concavity preservation boundary** is: \(Y_{m,r}\) is ultra-log-concave precisely for \(r=1\) (one maximum) and \(r=m\) (the full sum). Every intermediate trimmed sum, \(2\le r<m\), violates the defining inequality, for every \(\lambda>0\).

For those intermediate values, write \(q_k=\Pr(Y_{m,r}=k)\), \(t=m\lambda\), and
\[
B_{m,r}(\lambda)=\sum_{j=r+1}^{m}\binom mj\lambda^j.
\]
Then the complete low tail through the first exceptional index is
\[
q_k=e^{-t}\frac{t^k}{k!}\quad (0\le k<r),\qquad
q_r=e^{-t}\left(\frac{t^r}{r!}+B_{m,r}(\lambda)\right).
\]
In particular, for \(2\le r<m\),
\[
(r-1)q_{r-1}^{2}-r q_{r-2}q_r
=-\frac{r e^{-2t}t^{r-2}}{(r-2)!}B_{m,r}(\lambda)<0.
\]

The same first exceptional index has an **exact ordinary-log-concavity crossover**. There is a unique \(\lambda_{m,r}^{*}>0\) such that
\[
\sum_{j=r+1}^{m}\binom mj(\lambda_{m,r}^{*})^{j-r}
=\frac{m^r}{r!(r-1)}.
\]
The ordinary log-concavity inequality \(q_{r-1}^2\ge q_{r-2}q_r\) holds exactly for \(0<\lambda\le\lambda_{m,r}^{*}\), and reverses strictly above that threshold. For fixed \(r\ge2\), the numbers \(m\lambda_{m,r}^{*}\) strictly decrease as \(m\ge r+1\) increases, and converge to the unique positive solution \(\tau_r\) of
\[
\sum_{j=r+1}^{\infty}\frac{\tau_r^{j-r}}{j!}
=\frac{1}{r!(r-1)}.
\]
The crossover describes a single local inequality, not global ordinary log-concavity of every coefficient.

## Assumptions and scope
Here \(m\) and \(r\) are integers satisfying \(m\ge2\), \(1\le r\le m\), and \(\lambda>0\) is arbitrary. All \(X_i\) are independent, identically distributed nonnegative integer counts with mass \(e^{-\lambda}\lambda^k/k!\). Ties in the order statistics are retained with their multiplicity. For a full-support count mass function \((q_k)_{k\ge0}\), ultra-log-concavity means
\[
kq_k^2\ge(k+1)q_{k-1}q_{k+1}\quad(k\ge1).
\]
Ordinary log-concavity replaces the left coefficient \(k\) and the right coefficient \(k+1\) by \(1\). The result does not concern a sum of independent order statistics: the summands in the trimmed sum are dependent.

## Proof
**Low-tail rigidity.** Put \(T=\sum_{i=1}^{m}X_i\), so \(T\sim\operatorname{Poisson}(m\lambda)\). If \(Y_{m,r}<r\), there can be at most \(r-1\) positive observations. All positive observations then belong to the retained \(r\), so \(Y_{m,r}=T\). Conversely \(T<r\) implies \(Y_{m,r}=T\). Hence \(\Pr(Y_{m,r}=k)=\Pr(T=k)\) for \(k<r\).

**The first excess mass.** If \(Y_{m,r}=r\) but \(T>r\), more than \(r\) observations must be positive; otherwise the retained sum would equal \(T\). Each of the largest \(r\) is at least one, so they must all equal one. It follows that every positive observation is exactly one. Conversely, configurations with exactly \(j\ge r+1\) singleton observations and all remaining observations zero have \(Y_{m,r}=r<T=j\). Each such configuration has probability \(\binom mj\lambda^j e^{-m\lambda}\). Adding the disjoint event \(T=r\) gives the displayed formula for \(q_r\) and the strict positivity of \(B_{m,r}(\lambda)\) when \(m>r\).

**Failure and sharp preservation boundary.** For the Poisson mass \(p_k=e^{-t}t^k/k!\), the identity \((r-1)p_{r-1}^2=rp_{r-2}p_r\) holds. Since \(q_{r-2}=p_{r-2}\), \(q_{r-1}=p_{r-1}\), and \(q_r=p_r+e^{-t}B_{m,r}(\lambda)\), the displayed strict negative ultra-log-concavity defect follows. When \(r=m\), the statistic equals \(T\), which is Poisson and satisfies ultra-log-concavity with equality. When \(r=1\), it is the sample maximum, whose ultra-log-concavity follows from the discrete-order-statistic preservation theorem of Badiella, del Castillo and Puig (2023), applicable to the Poisson parent. Those are the only two preserving ranks.

**Ordinary-log-concavity crossover.** Substitute the low-tail masses into the unweighted difference. Exactly,
\[
q_{r-1}^{2}-q_{r-2}q_r
=\frac{e^{-2t}t^{r-2}}{(r-2)!}
\left[\frac{t^r}{r!(r-1)}-B_{m,r}(\lambda)\right].
\]
For \(\lambda>0\), the bracket has the sign of
\[
\frac{m^r}{r!(r-1)}-\sum_{j=r+1}^{m}\binom mj\lambda^{j-r}.
\]
The sum is continuous and strictly increasing from zero to infinity, establishing existence, uniqueness, and the exact sign orientation.

**Sharp rescaled limit.** Set \(s_m=m\lambda_{m,r}^{*}\). Its defining equation is
\[
\sum_{j=r+1}^{m}\frac{(m)_j}{m^j}\frac{s_m^{j-r}}{j!}
=\frac{1}{r!(r-1)},
\]
where \((m)_j=m(m-1)\cdots(m-j+1)\). For each fixed integer \(j\ge r+1\), the coefficient \((m)_j/m^j\) increases strictly toward one with \(m\); additional positive terms appear as \(m\) increases. Thus the positive root \(s_m\) decreases strictly with \(m\). On compact intervals of \(s\ge0\), the series converges uniformly to \(\sum_{j=r+1}^{\infty}s^{j-r}/j!\), dominated by the exponential series. This limit increases continuously from zero to infinity, so its unique positive root \(\tau_r\) is the decreasing limit of \(s_m\).

## Verification
The accompanying dependency-free Python program `verify.py` enumerates ordered Poisson count vectors as finite exact factorial-weight polynomials whenever the trimmed sum is at most \(r\). It verifies the full low-tail identity, the signed ultra-log-concavity defect, and the ordinary local threshold signs for \(3\le m\le6\) and every \(2\le r<m\). It also checks finitely many mass-function inequalities for Poisson maxima at rational intensities. Running `python3 verify.py` gives `PASS: 346 exact checks on polynomial coefficients, ULC defects, and local LC signs`. These checks are finite consistency tests; the preceding argument supplies the all-parameter proof. The \(r=1\) boundary uses the cited published theorem, not numerical extrapolation.

For \(m=3,r=2\), the three masses are \(q_0=e^{-3\lambda}\), \(q_1=3\lambda e^{-3\lambda}\), and \(q_2=(9\lambda^2/2+\lambda^3)e^{-3\lambda}\). Their strict ultra-log-concavity defect is \(-2\lambda^3e^{-6\lambda}\), and the first ordinary-log-concavity inequality changes sign exactly at \(\lambda=9/2\).

## Relationship to prior work
Badiella, del Castillo and Puig (2023) establish ultra-log-concavity of each individual order statistic of a discrete ultra-log-concave parent. Their theorem supplies the positive \(r=1\) endpoint; it neither asserts preservation under *sums* of dependent order statistics nor gives the negative interior-rank classification here. Jakimiuk, Murawski, Nayar and Słobodianiuk (2022) develop the structure of ultra-log-concave probability laws, including Poisson comparisons. Johnson and Goldschmidt (2006) give sufficient conditions under which some sums of dependent log-concave variables remain ordinarily log-concave; no such condition can assert ordinary log-concavity for these trimmed Poisson sums at every intensity, because the explicit local inequality reverses. The result isolates a sharp boundary between single-order-statistic preservation, untrimmed independent convolution, and genuinely dependent intermediate trimming.

## Limitations
The theorem does not classify global ordinary log-concavity of the entire trimmed-sum distribution below the stated local threshold. The asymptotic assertion fixes \(r\) and lets \(m\) grow; it does not cover jointly growing ranks. No claim is made about arbitrary non-Poisson parents or about the full tail beyond the first deviation. Earlier sources could contain an equivalent special-purpose trimmed-sum observation; the directly retrievable full-text copy of the 2023 order-statistics paper was unavailable, although its theorem and proof exposition were accessible through indexed material. No independent historical-priority audit has been performed.

## References
1. L. Badiella, J. del Castillo, P. Puig, *Ultra log-concavity of discrete order statistics*, Statistics & Probability Letters 201 (2023), 109900. DOI: 10.1016/j.spl.2023.109900. First publicly available online 26 June 2023.
2. J. Jakimiuk, D. Murawski, P. Nayar, S. Słobodianiuk, *Log-concavity and discrete degrees of freedom*, preprint arXiv:2205.04069 (9 May 2022), primary MSC 60E15.
3. O. Johnson and C. Goldschmidt, *Preservation of log-concavity on summation*, ESAIM: Probability and Statistics 10 (2006), 206–215; preprint arXiv:math/0502548 (25 February 2005).
