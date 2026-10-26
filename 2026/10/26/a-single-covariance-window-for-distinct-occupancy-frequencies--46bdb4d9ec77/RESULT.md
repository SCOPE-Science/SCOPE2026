# A single covariance window for distinct occupancy frequencies

## Finding

Throw \(n\) labeled balls independently and uniformly into \(m\) labeled boxes. Let \(N_r\) count boxes receiving exactly \(r\) balls, and define \(N_s\) similarly. For each \(m\ge3\), distinct positive integers \(r,s\), and integer \(n\ge r+s\), set

\[
T_n=\frac{\mathbb E[N_rN_s]}{\mathbb E[N_r]\,\mathbb E[N_s]}.
\]

With the falling factorial \((u)_{\underline{k}}=u(u-1)\cdots(u-k+1)\), the exact formula is

\[
T_n=\frac{(n-r)_{\underline{s}}}{(n)_{\underline{s}}}
\frac{m^{n-1}(m-2)^{n-r-s}}{(m-1)^{2n-r-s-1}}.
\tag{1}
\]

Its adjacent-sample-size ratio has the exact form

\[
\frac{T_{n+1}}{T_n}
=\frac{m(m-2)}{(m-1)^2}
\left(1+\frac{rs}{(n+1)(n+1-r-s)}\right).
\tag{2}
\]

The right side strictly decreases with \(n\). Hence \((T_n)_{n\ge r+s}\) is strictly log-concave and unimodal; moreover \(T_n\to0\) as \(n\to\infty\). As the ball count increases with the number of boxes and the two positive occupancy sizes fixed, **positive covariance occurs on at most one contiguous interval of integers**, possibly empty. The complete sign classification is the exact comparison \(\operatorname{sgn}\operatorname{Cov}(N_r,N_s)=\operatorname{sgn}(T_n-1)\) using (1). In particular the covariance cannot alternate repeatedly between signs.

Both sign reversals really occur. For \(m=10\), \(r=1\), \(s=8\), exact integer comparisons show

\[
\operatorname{Cov}(N_1,N_8)
\begin{cases}<0,&n=9,\\>0,&n=20,\\<0,&n=70.\end{cases}
\tag{3}
\]

There is also a limiting phase diagram. For fixed distinct positive \(r,s\), if \(m\to\infty\) and \(n/m\to\lambda\in(0,\infty)\), then

\[
\frac1m\operatorname{Cov}(N_r,N_s)
\longrightarrow
-\frac{e^{-2\lambda}\lambda^{r+s}}{r!s!}
\left(1+\frac{(r-\lambda)(s-\lambda)}{\lambda}\right).
\tag{4}
\]

Put \(\Delta=(r+s-1)^2-4rs\). If \(\Delta>0\), the limit in (4) is positive precisely on

\[
\frac{r+s-1-\sqrt\Delta}{2}<\lambda<
\frac{r+s-1+\sqrt\Delta}{2},
\tag{5}
\]

and strictly negative outside the *closed* interval. If \(\Delta<0\), it is strictly negative for every positive \(\lambda\). If \(\Delta=0\), it is negative away from the single root and zero at that root; (4) alone does not determine the finite-sample sign at a zero of the limiting expression.

## Assumptions and scope

The number of boxes \(m\) is a fixed integer at least three for (1)--(3), the two required cell loads \(r,s\) are distinct and positive, and \(n\ge r+s\). All balls independently choose a box with probability \(1/m\). Only the asymptotic statement (4)--(5) lets the number of boxes vary. The sequence \((T_n)\) means the sequence under fixed \(m,r,s\), not under a varying number of boxes.

The term 'single window' means that the strictly positive covariance indices form one contiguous (possibly empty) set of integers; equality to zero at its boundary is permitted. No claim is made about diagonally repeated load sizes or unequal allocation probabilities.

## Proof

For \(a=(m-1)/m\) and \(b=(m-2)/m\), count the possibilities for a fixed box and for an ordered pair of distinct boxes:

\[
\begin{aligned}
\mathbb E N_r&=m\binom nr m^{-r}a^{n-r},\\
\mathbb E N_s&=m\binom ns m^{-s}a^{n-s},\\
\mathbb E[N_rN_s]&=m(m-1)\binom nr\binom{n-r}s
 m^{-r-s}b^{n-r-s}.
\end{aligned}
\tag{6}
\]

The last equality uses \(r\ne s\): the same box cannot contribute to both counts. Dividing the third expression by the product of the first two, canceling factorials, and collecting powers of \(m\), \(m-1\), and \(m-2\) gives (1). In particular both means are positive and the covariance has the sign of \(T_n-1\).

Taking the ratio of (1) for consecutive \(n\) yields

\[
\frac{(n+1-r)_{\underline{s}}/(n+1)_{\underline{s}}}
{(n-r)_{\underline{s}}/(n)_{\underline{s}}}
=\frac{(n+1-r)(n+1-s)}{(n+1)(n+1-r-s)}
=1+\frac{rs}{(n+1)(n+1-r-s)}.
\tag{7}
\]

The remaining factor is \(m(m-2)/(m-1)^2\), proving (2). Since \(r,s>0\) and \((n+1)(n+1-r-s)\) strictly increases, consecutive ratios strictly decrease. This proves strict log-concavity at every interior index. The ratio eventually approaches a number strictly below one, and the formula (1), whose polynomial factor is bounded by one, implies \(T_n\to0\). Consequently the superlevel set \(\{n:T_n>1\}\) is an interval of integers and is bounded above. This proves the exact sign-window classification. The three rational comparisons in (3) are independently reproducible by the accompanying verifier; no floating-point inequalities are needed.

For (4), take logarithms in (1). With \(n/m\to\lambda>0\) and fixed \(r,s\), the three contributions satisfy

\[
\begin{aligned}
(1-r-s)\log(1-1/m)&=\frac{r+s-1}{m}+O(m^{-2}),\\
(n-r-s)\log\left(1-\frac1{(m-1)^2}\right)&=-\frac\lambda m+o(m^{-1}),\\
\log\frac{(n-r)_{\underline{s}}}{(n)_{\underline{s}}}&=-\frac{rs}{\lambda m}+o(m^{-1}).
\end{aligned}
\]

Hence

\[
T_n-1=\frac{r+s-1-\lambda-rs/\lambda}{m}+o(m^{-1}).
\tag{8}
\]

The binomial expression for each mean in (6) gives \(\mathbb E N_j/m\to e^{-\lambda}\lambda^j/j!\) for \(j=r,s\). Multiplying these limits by (8) gives (4). The sign of its bracket is the sign of \(-[\lambda^2-(r+s-1)\lambda+rs]\); the quadratic formula gives (5) and the remaining cases. All limits are for fixed \(r,s\) and positive finite \(\lambda\).

## Verification

Run `python verify.py` using a standard Python interpreter. The file independently enumerates labeled assignments for three, four, and five boxes with sample sizes up to seven, then compares three separately computed moments with (6) using exact rational arithmetic. It separately checks (2) and strict log-concavity across wider parameter grids, and verifies all three signs in (3) with exact integers. It reports 13,383 passed exact assertions. The universal theorem and the asymptotic statement rest on the proof, not on finite enumeration.

## Relationship to prior work

The factorial-moment and occupancy-profile distributions are classical. Harris and Park (1971) explicitly give a multinomial occupancy-profile probability formula and derive univariate moment asymptotics; the present finding does **not** claim novelty for that counting identity. Sevast'yanov and Chistyakov (1964) prove a multivariate occupancy normal limit, which may already imply the limiting covariance in (4) after specialization; (4) is supplied to interpret the new finite-size sign-window result rather than claimed as a separate priority result. Barbour and Gnedin's 2008 preprint analyzes correlations of occupancy-size counts in infinite, generally nonuniform box-frequency schemes, a different asymptotic regime. The finite strictly log-concave *sample-size profile* (2), its one-interval positive-covariance classification, and the explicit two-reversal example were not found as statements in the primary texts inspected.

## Limitations

This gives neither a general negative-association law nor stochastic monotonicity of the counts. The two-reversal example is exact but does not describe the full joint distribution. The full text of Sevast'yanov--Chistyakov (1964) and Harris--Park's companion article on linear combinations (1971) could not be inspected here; an implicit or earlier equivalent derivation remains a genuine priority risk. At the limiting roots in (5) the sign of the first-order limit is zero, so finer asymptotics are required to decide sign there. The result is not extended to unequal box probabilities.

## References

1. B. Harris and C. J. Park, *The limiting distribution of the sample occupancy numbers from the multinomial distribution with equal cell probabilities*, Annals of the Institute of Statistical Mathematics 23 (1971), 125--133. Full-text historical article: https://www.ism.ac.jp/editsec/aism/pdf/023_1_0125.pdf .
2. B. A. Sevast'yanov and V. P. Chistyakov, *Asymptotic Normality in the Classical Ball Problem*, Theory of Probability and Its Applications 9 (1964), 198--211, https://doi.org/10.1137/1109034 .
3. A. D. Barbour and A. V. Gnedin, *Small counts in the infinite occupancy scheme*, arXiv:0809.4387v1, posted 2008-09-25, https://arxiv.org/abs/0809.4387 .
4. B. Harris and C. J. Park, *The distribution of linear combinations of the sample occupancy numbers*, Indagationes Mathematicae 33 (1971), 121--134 (historical comparison; full text not inspected).
