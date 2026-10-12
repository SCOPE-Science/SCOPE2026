# Sharp moment phase diagram for DPITL invalidates four published summary rows
## Finding
For the discrete power inverted Topp-Leone (DPITL) distribution, let
\[
S_n=
\left[
\frac{1+2n^\eta}{(1+n^\eta)^2}
\right]^\kappa,
\qquad
n=0,1,2,\ldots,
\qquad
\kappa,\eta>0,
\]
and
\[
p_n=S_n-S_{n+1}.
\]
Write
\[
a=\kappa\eta.
\]

Then the exact tail orders are
\[
S_n\sim2^\kappa n^{-a}
\]
and
\[
p_n\sim2^\kappa a\,n^{-a-1}.
\]
Therefore, for every real \(r>0\),
\[
\boxed{
\mathbb E[X^r]<\infty
\quad\Longleftrightarrow\quad
r<\kappa\eta .
}
\]

In particular,
\[
\mathbb E[X]<\infty
\quad\Longleftrightarrow\quad
\kappa\eta>1,
\]
\[
\operatorname{Var}(X)<\infty
\quad\Longleftrightarrow\quad
\kappa\eta>2,
\]
finite third moments require
\[
\kappa\eta>3,
\]
and finite fourth moments require
\[
\kappa\eta>4.
\]

There is also no ordinary moment-generating function around the origin:
\[
\boxed{
\mathbb E[e^{tX}]=\infty
\quad\text{for every }t>0.
}
\]
For \(t\le0\), the transform is finite. Thus any formula presented as an MGF must be interpreted only on its Laplace-transform side unless an additional analytic continuation is explicitly distinguished from a probabilistic moment-generating function.

These thresholds invalidate finite summary statistics in four of the six parameter rows displayed in Table 1 of the 2026 source. The relevant products \(a=\kappa\eta\) are
\[
\begin{array}{c|c|c}
(\kappa,\eta) & a & \text{finite moments available}\\
\hline
(1.5,0.5) & 0.75 & \text{no positive integer moment}\\
(1.5,1.5) & 2.25 & \text{first and second only}\\
(1.5,3) & 4.5 & \text{first through fourth}\\
(2.5,0.5) & 1.25 & \text{first only}\\
(2.5,1.5) & 3.75 & \text{first through third}\\
(2.5,3) & 7.5 & \text{first through fourth}.
\end{array}
\]

Hence the rows \((1.5,0.5)\), \((1.5,1.5)\), \((2.5,0.5)\), and \((2.5,1.5)\) each print at least one finite quantity whose defining population moment diverges. The source's statement that under- and over-dispersion occur across the full parameter space likewise needs qualification: a finite variance-to-mean dispersion index is defined only after the stronger condition \(\kappa\eta>2\).

## Assumptions and scope
The parameter domain is
\[
\kappa>0,\qquad \eta>0,
\]
and the DPITL law is the survival-function discretization printed by the source.

The result concerns existence of population moments and positive exponential moments. It does not claim that the source's finite-sample maximum-likelihood procedures fail, and it does not reassess its applications or goodness-of-fit comparisons.

Skewness is treated through the third central moment and kurtosis through the fourth central moment. Whenever the corresponding raw moment diverges, the usual finite standardized population quantity is not available. Coefficient of variation and index of dispersion require finite variance.

## Proof
For real \(x>0\), define the continuous interpolation
\[
S(x)=
\left[
\frac{1+2x^\eta}{(1+x^\eta)^2}
\right]^\kappa.
\]
As \(x\to\infty\),
\[
\frac{1+2x^\eta}{(1+x^\eta)^2}
=
2x^{-\eta}(1+o(1)),
\]
hence
\[
S(x)\sim2^\kappa x^{-\kappa\eta}.
\]
This proves the survival asymptotic.

Differentiate:
\[
\frac{d}{dx}\log S(x)
=
-\frac{2\kappa\eta\,x^{2\eta-1}}
{(1+2x^\eta)(1+x^\eta)}
\sim
-\frac{\kappa\eta}{x}.
\]
By the mean-value theorem,
\[
p_n=S(n)-S(n+1)=-S'(\xi_n)
\]
for some \(\xi_n\in(n,n+1)\). Since \(\xi_n/n\to1\), the two asymptotics above give
\[
p_n
\sim
\frac{\kappa\eta}{n}S(n)
\sim
2^\kappa\kappa\eta\,n^{-\kappa\eta-1}.
\]

For \(r>0\),
\[
\mathbb E[X^r]
=
\sum_{n\ge1}n^r p_n.
\]
The summand is asymptotic to a positive constant times
\[
n^{r-\kappa\eta-1}.
\]
The \(p\)-series criterion therefore yields
\[
\mathbb E[X^r]<\infty
\quad\Longleftrightarrow\quad
r<\kappa\eta.
\]
At equality the series is harmonic to first order and diverges.

For \(t>0\),
\[
e^{tn}p_n
\sim
2^\kappa\kappa\eta\,
e^{tn}n^{-\kappa\eta-1},
\]
which does not even converge to zero. Hence
\[
\sum_{n\ge0}e^{tn}p_n=\infty.
\]
For \(t\le0\), \(e^{tX}\le1\), so the expectation is finite.

The table consequences follow by substituting each displayed pair \((\kappa,\eta)\) into the sharp threshold \(r<\kappa\eta\).

## Verification
The bundled checker evaluates the exact survival and PMF for representative parameter values, including the slowest-decaying table case. It verifies numerically that
\[
n^{\kappa\eta}S_n\to2^\kappa
\]
and
\[
n^{\kappa\eta+1}p_n\to2^\kappa\kappa\eta.
\]
It also compares large finite partial sums on opposite sides of the moment threshold and verifies that positive-MGF summands eventually grow rather than vanish.

These computations are consistency checks only. The infinite-domain phase diagram is proved by the asymptotic comparison above.

## Relationship to prior work
The 2026 DPITL article introduces the discrete law by survival-function discretization of the power inverted Topp-Leone distribution. Its mathematical-properties section gives a probability generating function, an expression labeled as a moment-generating function, and formulas for noncentral and factorial moments. Table 1 then reports finite means, variances, skewnesses, kurtoses, coefficients of variation, and dispersion indices for six parameter pairs, followed by a statement that under- and over-dispersion occur across the full parameter space.

The continuous power inverted Topp-Leone precursor develops the parent distribution and gives moment and MGF expressions. In the inspected full text, no explicit tail-order phase diagram or discrete moment-existence theorem was found. The discrete inverted Topp-Leone literature supplies an earlier survival-discretization special case, but the focused searches did not locate the DPITL threshold \(\kappa\eta\) or a correction to the 2026 table.

Focused searches using the target DOI, DPITL name, moment-existence aliases, positive-MGF terminology, and the parameter product \(\kappa\eta\) did not locate a published correction or a statement covering the sharp discrete threshold.

## Limitations
The result classifies existence, not closed-form values, of finite moments below the threshold.

It does not determine the sign of the finite dispersion index throughout the restricted region \(\kappa\eta>2\); it only shows that a finite variance-to-mean comparison is unavailable outside that region.

The continuous precursor's displayed special-function moment formulas may encode their own convergence restrictions implicitly. The present claim is specifically about the discrete 2026 law, its published finite summary table, and its ordinary probabilistic MGF.

## References
1. A. S. Hassan, E. A. Seyam, A. A. Alzahrani, and O. A. Saudi, “An innovative discrete distribution for modeling genotoxicity data: Applications in pharmacology and environmental health,” AIMS Mathematics 11 (2026), 1145–1174. DOI: 10.3934/math.2026049.
2. T. A. Abushal, A. S. Hassan, E. A. Amin, and M. G. Khalil, “Power Inverted Topp–Leone Distribution in Acceptance Sampling Plans,” Computers, Materials & Continua 67 (2021), 991–1011. DOI: 10.32604/cmc.2021.014620.
3. M. A. El-Morshedy, A. S. Eliwa, and M. S. El-Gohary, “A discrete analog of inverted Topp-Leone distribution: Properties, estimation and applications,” Journal of Applied Mathematics and Computational Mechanics (2021). DOI: 10.28924/2291-8639-19-2021-695.
