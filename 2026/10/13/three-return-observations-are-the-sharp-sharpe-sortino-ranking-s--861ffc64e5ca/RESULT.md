# Three return observations are the sharp Sharpe–Sortino ranking split
## Finding
Fix a zero benchmark and zero minimum acceptable return. For an equally weighted finite return sample
\[
r_1,\ldots,r_n,
\]
write
\[
\mu=\frac1n\sum_{i=1}^n r_i.
\]

Use the population-standard-deviation Sharpe ratio
\[
S=\frac{\mu}{\sigma},
\qquad
\sigma^2=\frac1n\sum_{i=1}^n(r_i-\mu)^2,
\]
and the lower-partial-second-moment Sortino ratio
\[
Q=\frac{\mu}{\delta},
\qquad
\delta^2=\frac1n\sum_{i=1}^n\min(r_i,0)^2.
\]

Restrict to samples with
\[
\mu>0
\]
and
\[
\delta>0,
\]
so both performance ratios are finite and positive.

With one or two observations, no two admissible samples can be ranked in opposite strict orders by \(S\) and \(Q\).

Three observations are sharp. Consider
\[
A=(-1,1,9)
\]
and
\[
B=(-2,5,6).
\]
Both have mean
\[
\mu=3.
\]

For \(A\),
\[
\sigma_A^2=\frac{56}{3},
\qquad
S(A)^2=\frac{27}{56},
\qquad
\delta_A^2=\frac13,
\qquad
Q(A)^2=27.
\]

For \(B\),
\[
\sigma_B^2=\frac{38}{3},
\qquad
S(B)^2=\frac{27}{38},
\qquad
\delta_B^2=\frac43,
\qquad
Q(B)^2=\frac{27}{4}.
\]

Therefore
\[
S(A)<S(B)
\]
but
\[
Q(A)>Q(B).
\]

The mechanism has an exact three-outcome description. Let
\[
R=(-a,b,c),
\qquad
a>0,
\]
have fixed positive mean \(\mu\), and put
\[
h=|b-c|.
\]
Then
\[
b+c=3\mu+a,
\]
and direct algebra gives
\[
\delta^2=\frac{a^2}{3},
\]
while
\[
\sigma^2
=
\frac{(a+\mu)^2}{2}
+
\frac{h^2}{6}.
\]
Thus, at a fixed mean, Sortino ordering depends only on the loss magnitude \(a\), whereas Sharpe ordering also penalizes imbalance between the two nonnegative outcomes through \(h\). A smaller loss can therefore improve Sortino while sufficiently greater upside dispersion worsens Sharpe.

The disagreement persists at every larger sample size. For
\[
n\ge3,
\]
define
\[
A_n=(-1,1,9,\underbrace{3,\ldots,3}_{n-3})
\]
and
\[
B_n=(-2,5,6,\underbrace{3,\ldots,3}_{n-3}).
\]
Both samples still have mean \(3\), and
\[
\sigma^2(A_n)=\frac{56}{n},
\qquad
\sigma^2(B_n)=\frac{38}{n},
\]
while
\[
\delta^2(A_n)=\frac1n,
\qquad
\delta^2(B_n)=\frac4n.
\]
Hence
\[
S(A_n)<S(B_n)
\]
and
\[
Q(A_n)>Q(B_n)
\]
for every \(n\ge3\).

## Assumptions and scope
Returns are equally weighted observations of differential return relative to the same zero benchmark. Translating a common nonzero benchmark to zero gives the same algebra on differential returns.

The main Sortino convention uses the lower partial second moment divided by the total number of observations. This is the probability-weighted downside-deviation convention.

Some empirical implementations divide the downside sum only by the number of below-target observations. The sharp threshold and displayed family are unchanged under that alternative convention because every relevant two-outcome sample and every displayed witness has exactly one below-target observation.

The Sharpe denominator uses population standard deviation. For two portfolios compared with the same number of observations, using sample standard deviation instead multiplies every Sharpe ratio by the same positive factor, so all rankings and the sharp support threshold are unchanged.

The result concerns finite empirical return samples and ordinal comparison of two performance ratios. It does not claim that three observations are statistically sufficient for investment evaluation.

## Proof
There is no admissible one-observation sample. A positive one-point return has zero downside deviation, while a negative one-point return has negative mean.

For two equally likely observations, positive mean and nonzero downside force the sample to have the form
\[
(-a,b),
\qquad
a>0,
\qquad
b>a.
\]
Put
\[
r=\frac ba>1.
\]
Then
\[
\mu=\frac{b-a}{2}
\]
and
\[
\sigma=\frac{a+b}{2},
\]
so
\[
S
=
\frac{r-1}{r+1}.
\]
Also
\[
\delta=\frac{a}{\sqrt2},
\]
hence
\[
Q
=
\frac{r-1}{\sqrt2}.
\]
Both are strictly increasing functions of the same scalar \(r\). Therefore two-outcome Sharpe and Sortino rankings can never reverse.

Under the alternative downside normalization using only below-target observations,
\[
Q_{\mathrm{neg}}
=
\frac{r-1}{2},
\]
which is again strictly increasing in \(r\). Thus the two-outcome obstruction does not depend on the denominator convention.

For three outcomes, the exact calculations for \(A\) and \(B\) displayed in the finding give
\[
S(A)^2=\frac{27}{56}
<
\frac{27}{38}
=
S(B)^2
\]
and
\[
Q(A)^2=27
>
\frac{27}{4}
=
Q(B)^2.
\]
Because both ratios are positive, comparison of their squares preserves the ordering. This proves sharpness.

For the structural formula, let
\[
(-a,b,c)
\]
have mean \(\mu\). Then
\[
b+c=3\mu+a.
\]
Writing
\[
h=|b-c|,
\]
one has
\[
b^2+c^2
=
\frac{(b+c)^2+h^2}{2}.
\]
Substitution into
\[
\sigma^2=\frac{a^2+b^2+c^2}{3}-\mu^2
\]
gives
\[
\sigma^2
=
\frac{(a+\mu)^2}{2}
+
\frac{h^2}{6}.
\]
The downside formula
\[
\delta^2=\frac{a^2}{3}
\]
is immediate when there is exactly one loss.

Finally, padding with observations equal to the common mean changes neither mean nor the raw sums of squared deviations in the original three coordinates. The exact formulas for \(A_n\) and \(B_n\) follow, proving persistence for every \(n\ge3\).

## Verification
The embedded `verify_sharpe_sortino_minimal_support.py` uses only the Python standard library and exact rational arithmetic.

It checks the two-outcome formulas on thousands of integer representatives
\[
(-a,b),
\qquad
1\le a<b,
\]
and verifies monotonicity on the resulting rational ratios \(b/a\).

For the three-outcome witness it independently recomputes:
\[
\mu(A)=\mu(B)=3,
\]
\[
\sigma_A^2=\frac{56}{3},
\qquad
\sigma_B^2=\frac{38}{3},
\]
\[
S(A)^2=\frac{27}{56},
\qquad
S(B)^2=\frac{27}{38},
\]
\[
Q(A)^2=27,
\qquad
Q(B)^2=\frac{27}{4}.
\]

It also checks the negative-observation-only downside convention and the padded reversal family for every
\[
3\le n\le500.
\]

The finite replay is not the proof of the two-outcome impossibility or all-\(n\) persistence; those statements follow from the algebra above.

Run:

`python3 verify_sharpe_sortino_minimal_support.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Sharpe's performance ratio summarizes mean differential return per unit of total standard deviation. His later full exposition explicitly defines the ex post ratio from historical differential returns and notes that, when all funds use the same number of observations, population or sample standard-deviation conventions preserve their relative rankings.

Sortino and van der Meer developed a downside-risk framework in which shortfalls below a target are treated as risk rather than symmetric total volatility. This is the conceptual source of the Sortino denominator used here.

The closest located theoretical comparison is Lien's 2002 paper on relationships among risk-adjusted performance measures. It proves that, under normally distributed returns, Sortino is a monotonically increasing function of Sharpe and therefore gives the same ranking, while under other distributional regimes opposite rankings can occur. Thus the existence of Sharpe–Sortino ranking disagreement is prior work and is not claimed as new.

The finding here is narrower and finite: among equally weighted empirical return samples with positive mean and nonzero downside risk, two observations force exact ranking agreement, three observations are sufficient for reversal, and the same explicit mechanism persists at every larger sample size. The inspected literature and targeted searches did not state this support-size boundary, the displayed exact witness, or the equal-mean three-outcome variance decomposition.

## Limitations
The theorem fixes a common target and benchmark and compares equally weighted empirical returns.

The lower-partial-second-moment downside convention must be stated because empirical Sortino implementations are not completely uniform. The sharp threshold and witness are robust to the two common denominator choices addressed here, but other modifications of Sortino need separate analysis.

The theorem is about mathematical ranking possibility, not estimation reliability. Three observations are far too few to justify practical portfolio selection from noisy data.

Prior literature already establishes that Sharpe and Sortino can disagree for non-Gaussian return distributions. The new claim is only the sharp finite-support boundary and its exact mechanism.

An unindexed exercise, implementation test, or practitioner example could contain the same three-return witness even if the sharp minimality statement is absent.

## References
1. W. F. Sharpe, “Mutual Fund Performance,” *The Journal of Business* 39, 119–138, January 1966. DOI: 10.1086/294846.
2. W. F. Sharpe, “The Sharpe Ratio,” *The Journal of Portfolio Management* 21, 49–58, Fall 1994. Public author reprint at Stanford University.
3. F. A. Sortino and R. van der Meer, “Downside Risk: Capturing What's at Stake in Investment Situations,” *The Journal of Portfolio Management* 17(4), 27–31, 1991. DOI: 10.3905/jpm.1991.409343.
4. D. Lien, “A note on the relationships between some risk-adjusted performance measures,” *Journal of Futures Markets* 22(5), 483–495, first published 7 March 2002. DOI: 10.1002/fut.10024.
