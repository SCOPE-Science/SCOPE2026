# A sharp critical window for positive singleton–quadrupleton occupancy covariance

## Finding

Throw \(n\) independent uniform balls into \(m\ge3\) labeled boxes, with \(n\ge4\). For every integer \(r\ge0\), let \(Y_r\) denote the number of boxes containing exactly \(r\) balls. Set \(a=1-1/m\) and \(b=1-2/m\).

For \(n\ge5\), the **exact mixed-frequency covariance** is
\[
\operatorname{Cov}(Y_1,Y_4)
=\mathbb E[Y_1]\mathbb E[Y_4](Q_m(n)-1),\qquad
Q_m(n)=\frac{n-4}{n}\frac{b^{n-5}}{a^{2n-6}},
\]
where \(\mathbb E[Y_1]=na^{n-1}\) and \(\mathbb E[Y_4]=\binom n4m^{-3}a^{n-4}\). At \(n=4\) the covariance is strictly negative.

For every \(m\ge3\), the positive-covariance ball counts form one nonempty, consecutive integer interval \([\ell_m,u_m]\), containing \(2m\). Outside that interval and for \(n\ge5\), the covariance is nonpositive. The ratio \(Q_m(n)\) is strictly increasing up to its unique maximum at \(n=2m\) and strictly decreasing afterward. For fixed \(m\), sufficiently large \(n\) give strictly negative covariance.

The **sharp location and width** of the positive window are
\[
\frac{\ell_m-2m}{\sqrt m}\longrightarrow-\sqrt2,\qquad
\frac{u_m-2m}{\sqrt m}\longrightarrow\sqrt2.
\]
More precisely, for any integer sequence \(n_m\) with \((n_m-2m)/\sqrt m\to z\in\mathbb R\),
\[
\lim_{m\to\infty}\operatorname{Cov}(Y_1,Y_4)
=\frac43e^{-4}\left(1-\frac{z^2}{2}\right).
\]
For comparison, at any fixed load \(n/m\to c\in(0,\infty)\),
\[
\lim_{m\to\infty}\frac{\operatorname{Cov}(Y_1,Y_4)}m
=-\frac{c^4(c-2)^2}{24}e^{-2c}.
\]
Thus the leading-order covariance is nonpositive at every fixed load, while a positive covariance of order one survives within an asymptotically sharp \(\sqrt m\)-wide window centered at load two.

## Assumptions and scope

The \(n\) choices are independent and each box has probability \(1/m\). Boxes are labeled. The finite-sample results hold for all integers \(m\ge3\), \(n\ge4\); the ratio \(Q_m(n)\) is defined for \(n\ge5\). The asymptotic statements let \(m\to\infty\), with integer \(n=n_m\) as specified. No Poissonization, independence of frequency counts, or asymptotic normality assumption is made.

## Proof

**Exact covariance.** Distinct boxes cannot simultaneously have occupancy one and occupancy four unless \(n\ge5\). Their joint indicators have probability
\[
\Pr(N_1=1,N_2=4)=\frac{n!}{4!(n-5)!m^5}b^{n-5}.
\]
Summing over ordered pairs of distinct boxes gives
\[
\mathbb E[Y_1Y_4]
=\frac{(m-1)n\binom{n-1}{4}}{m^4}b^{n-5}.
\]
The single-box binomial margins give the stated means, so cancellation yields exactly the formula in the finding. At \(n=4\), \(Y_1Y_4=0\) identically and both means are strictly positive.

**One positive interval.** For integers \(n\ge5\), divide consecutive ratios:
\[
\frac{Q_m(n+1)}{Q_m(n)}
=\frac{m(m-2)}{(m-1)^2}\frac{n(n-3)}{(n+1)(n-4)}.
\]
As \(n(n-3)=(n+1)(n-4)+4\), this ratio exceeds one exactly when
\[
(n+1)(n-4)<4m(m-2).
\]
The inequality holds through \(n=2m-1\) and fails from \(n=2m\), for every \(m\ge3\). Thus \(Q_m\) has the unique integer maximizer \(2m\). It starts at \(Q_m(5)>0\) and tends to zero as \(n\to\infty\). To verify that its maximum is strictly greater than one, put \(k=m-1\ge2\); direct simplification gives
\[
Q_m(2m)=\left(1+\frac1k\right)^2
\left(1-\frac1{k^2}\right)^{2k-2}.
\]
The strict inequalities \(\log(1+x)>x/(1+x)\) for \(x>0\) and \(\log(1-x)>-x/(1-x)\) for \(0<x<1\) imply
\[
\log Q_m(2m)>\frac2{k+1}-\frac{2k-2}{k^2-1}=0.
\]
Therefore the integers satisfying \(Q_m(n)>1\) form a nonempty interval containing \(2m\), and exactly those integers have positive covariance. Equality \(Q_m(n)=1\) is allowed at an exterior integer boundary; the claim does not assert it is impossible.

**Two asymptotic scales.** If \(n/m\to c\in(0,\infty)\), direct expansion yields
\[
 m\log Q_m(n)\longrightarrow 4-c-\frac4c
 =-\frac{(c-2)^2}{c}.
\]
The means satisfy \(\mathbb E[Y_1]/m\to ce^{-c}\) and \(\mathbb E[Y_4]/m\to(c^4/24)e^{-c}\). Since \(Q_m(n)-1\sim\log Q_m(n)\) when the latter is nonzero to first order, and the zero case follows directly from the same expansion, the fixed-load covariance-density limit follows.

Now suppose \(n=2m+z_m\sqrt m\) with bounded \(z_m\to z\). Taylor expansion of the three logarithms defining \(Q_m\), uniform on any bounded set of \(z_m\), gives
\[
\log Q_m(n)=\frac{1-z_m^2/2}{m^2}+O(m^{-5/2}).
\]
Consequently \(m^2(Q_m(n)-1)\to1-z^2/2\), while \(\mathbb E[Y_1]\mathbb E[Y_4]/m^2\to4e^{-4}/3\). This proves the claimed finite-covariance profile. For any fixed \(\varepsilon>0\), the profile is positive at rescaled offsets \(\pm(\sqrt2-\varepsilon)\) and negative at \(\pm(\sqrt2+\varepsilon)\). Strict unimodality and the consecutive positive interval force the asserted two endpoint limits.

## Verification

The accompanying standalone `verify_occupancy.py` uses only the Python standard library. It independently enumerates five small finite occupancy spaces and compares all three moments and the covariance with exact rational formulas. It also checks \(3116\) exact-rational consecutive-ratio conditions and \(15\) finite-size numerical comparisons with the critical-window limiting profile. Running `python3 verify_occupancy.py` reports `PASS`. These computations are consistency checks; the all-size and limiting statements are proved above.

## Relationship to prior work

Joint occupancy-frequency counts and local central limit theorems are classical. Hwang and Janson (arXiv:math/0604397) derive local limits for occupied-urn counts and discuss extensions to other statistics. Gnedin, Hansen and Pitman (arXiv:math/0701718, equation (7)) give a negative cross-frequency covariance for **Poissonized** infinite occupancy, not the fixed-number-of-balls positive critical window. Barbour and Gnedin (arXiv:0809.4387) analyze joint normal approximation of counts in the infinite-frequency occupancy scheme. Eaton, Godbole and Sinclair (arXiv:0806.1007) provide multivariate Poisson approximations for sparse tie counts; their conditions do not cover the linear-loading window here.

Sevast'yanov and Chistyakov, *Asymptotic Normality in the Classical Ball Problem* (1964), establish joint local normality for finite occupancy-frequency vectors at bounded positive loads. Their abstract is directly relevant to the first-order covariance-density context, but the full paper was inaccessible for comparison. The present mathematical claim is the **complete exact sign interval and its second-order square-root critical profile**, not a new joint central limit theorem, not a new general multinomial moment formula, and not a claim of certified historical priority.

## Limitations

The theorem concerns only the pair of exact frequency classes one and four in the uniform fixed-total model; it does not classify all cross-frequency pairs or nonuniform allocations. The covariance within the positive window is of order one, not of order \(m\), so it is not a nonzero limiting correlation claim. The first-order profile vanishes at load two; the critical-window profile resolves that degeneracy. Independent historical verification, especially of the 1964 full text and older joint-moment treatments, remains outstanding.

## References

1. H.-K. Hwang and S. Janson, *Local limit theorems for finite and infinite urn models*, arXiv:math/0604397, first publicly submitted 18 April 2006, https://arxiv.org/abs/math/0604397.
2. A. Gnedin, B. Hansen, and J. Pitman, *Notes on the occupancy problem with infinitely many boxes: general asymptotics and power laws*, arXiv:math/0701718, https://arxiv.org/abs/math/0701718.
3. A. D. Barbour and A. V. Gnedin, *Small counts in the infinite occupancy scheme*, arXiv:0809.4387, https://arxiv.org/abs/0809.4387.
4. J. Eaton, A. P. Godbole, and B. Sinclair, *Competition between Discrete Random Variables, with Applications to Occupancy Problems*, arXiv:0806.1007, https://arxiv.org/abs/0806.1007.
5. B. A. Sevast'yanov and V. P. Chistyakov, *Asymptotic Normality in the Classical Ball Problem*, Theory of Probability and Its Applications 9 (1964), 198–211, https://doi.org/10.1137/1109034.
6. D. Dubhashi and D. Ranjan, *Balls and Bins: A Study in Negative Dependence*, BRICS Research Series RS-96-25 (1996), https://www.brics.dk/RS/96/25/BRICS-RS-96-25.pdf.
