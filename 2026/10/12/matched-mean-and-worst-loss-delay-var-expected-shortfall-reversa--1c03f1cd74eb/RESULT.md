# Matched mean and worst loss delay VaR–Expected-Shortfall reversal to two tail masses
## Finding
Fix a confidence level
\[
\alpha\in(0,1)
\]
and let
\[
L_{1:n}\le\cdots\le L_{n:n}
\]
be the sorted values of an equally weighted empirical loss distribution.

Use the left empirical quantile
\[
F^{\leftarrow}(u)
=
\inf\{x:F(x)\ge u\},
\]
so
\[
\mathrm{VaR}_\alpha
=
F^{\leftarrow}(\alpha).
\]

Define Expected Shortfall by the integrated-quantile formula
\[
\mathrm{ES}_\alpha
=
\frac{1}{1-\alpha}
\int_\alpha^1 F^{\leftarrow}(u)\,du.
\]

Compare two empirical loss distributions only when they have:
- the same number \(n\) of equally weighted scenarios;
- the same mean loss;
- the same maximum loss.

Put
\[
p=1-\alpha.
\]

Then strict ranking reversal between \(\mathrm{VaR}_\alpha\) and \(\mathrm{ES}_\alpha\) is impossible whenever
\[
n<
\left\lceil\frac{2}{p}\right\rceil.
\]

This boundary is sharp. Let
\[
n_*=
\left\lceil\frac{2}{p}\right\rceil
\]
and
\[
r=n_*p.
\]
Minimality gives
\[
2\le r<3.
\]

At this first admissible size, consider
\[
A=(0,\ldots,0,1,3,4)
\]
and
\[
B=(0,\ldots,0,2,2,4).
\]
Both vectors have total loss \(8\), hence the same mean
\[
\frac{8}{n_*},
\]
and both have the same maximum loss \(4\).

Nevertheless,
\[
\mathrm{VaR}_\alpha(A)=1
<
2
=
\mathrm{VaR}_\alpha(B),
\]
while
\[
\mathrm{ES}_\alpha(A)
>
\mathrm{ES}_\alpha(B).
\]

More precisely,
\[
\mathrm{ES}_\alpha(A)
=
\frac{r+5}{r},
\qquad
\mathrm{ES}_\alpha(B)
=
\frac{2r+2}{r},
\]
so
\[
\mathrm{ES}_\alpha(A)-\mathrm{ES}_\alpha(B)
=
\frac{3-r}{r}
>
0.
\]

Thus VaR prefers \(A\), because its quantile threshold is lower, while Expected Shortfall prefers \(B\), even though the two empirical portfolios have identical expected loss and identical worst-case loss.

At the common \(95\%\) confidence level,
\[
p=\frac1{20},
\qquad
n_*=40.
\]
The witness then gives
\[
\mathrm{VaR}_{0.95}(A)=1,
\qquad
\mathrm{VaR}_{0.95}(B)=2,
\]
but
\[
\mathrm{ES}_{0.95}(A)=\frac72
>
3
=
\mathrm{ES}_{0.95}(B).
\]

At \(97.5\%\) confidence,
\[
p=\frac1{40},
\qquad
n_*=80,
\]
and the same four nonzero loss levels give the same risk values.

## Assumptions and scope
Losses are nonnegative, equally weighted empirical scenarios.

The theorem uses the generalized-inverse, left-quantile convention for VaR and the integrated-quantile definition of Expected Shortfall. These definitions handle atoms without replacing Expected Shortfall by a naive conditional expectation beyond the VaR threshold.

The two compared empirical distributions must have the same scenario count, same mean loss, and same maximum loss.

The result is an exact finite-support ordering statement. It does not address estimation uncertainty, dependence across time, model error, portfolio optimization, or regulatory backtesting.

Other empirical quantile interpolation conventions can change the integer boundary and require a separate analysis.

## Proof
Let
\[
p=1-\alpha
\]
and put
\[
r=np.
\]

For an equally weighted empirical distribution, the quantile function is constant on intervals of width
\[
\frac1n.
\]

First suppose
\[
r<1.
\]
Then
\[
\alpha>\frac{n-1}{n}.
\]
Both VaR and Expected Shortfall use only the maximum loss:
\[
\mathrm{VaR}_\alpha
=
\mathrm{ES}_\alpha
=
L_{n:n}.
\]
If the two portfolios have the same maximum, both measures tie, so strict reversal is impossible.

Now suppose
\[
1\le r<2.
\]
Then
\[
\mathrm{VaR}_\alpha
=
L_{n-1:n}.
\]
The Expected Shortfall integral contains a fraction
\[
r-1
\]
of the \((n-1)\)-st order-statistic mass and one full maximum-loss mass. Hence
\[
\mathrm{ES}_\alpha
=
\frac{(r-1)L_{n-1:n}+L_{n:n}}{r}.
\]
When the maximum \(L_{n:n}\) is fixed, this is a strictly increasing affine function of
\[
L_{n-1:n}
=
\mathrm{VaR}_\alpha.
\]
Therefore VaR and Expected Shortfall cannot rank two same-maximum portfolios in opposite strict orders whenever
\[
r<2.
\]

The condition
\[
r<2
\]
is exactly
\[
n<
\frac{2}{p}.
\]
For integer \(n\), this is equivalent to
\[
n<
\left\lceil\frac{2}{p}\right\rceil.
\]

At the first remaining integer
\[
n_*=
\left\lceil\frac{2}{p}\right\rceil,
\]
we have
\[
2\le r=n_*p<3.
\]
Thus
\[
\mathrm{VaR}_\alpha
=
L_{n_*-2:n_*},
\]
and
\[
\mathrm{ES}_\alpha
=
\frac{
(r-2)L_{n_*-2:n_*}
+
L_{n_*-1:n_*}
+
L_{n_*:n_*}
}{r}.
\]

For
\[
A=(0,\ldots,0,1,3,4),
\]
this gives
\[
\mathrm{VaR}_\alpha(A)=1
\]
and
\[
\mathrm{ES}_\alpha(A)
=
\frac{(r-2)+3+4}{r}
=
\frac{r+5}{r}.
\]

For
\[
B=(0,\ldots,0,2,2,4),
\]
we obtain
\[
\mathrm{VaR}_\alpha(B)=2
\]
and
\[
\mathrm{ES}_\alpha(B)
=
\frac{2(r-2)+2+4}{r}
=
\frac{2r+2}{r}.
\]

Their Expected-Shortfall difference is
\[
\frac{3-r}{r}>0,
\]
because
\[
r<3.
\]
This proves both sharpness and the equal-mean, equal-maximum witness.

## Verification
The embedded `verify_var_es_same_mean_max_threshold.py` uses exact rational arithmetic.

It implements:
- the left empirical quantile;
- the integrated empirical quantile for Expected Shortfall;
- the sharp threshold
  \[
  \left\lceil\frac{2}{1-\alpha}\right\rceil;
  \]
- the equal-mean, equal-maximum witness.

It replays the theorem over ten exact rational confidence levels, including
\[
\frac{19}{20}
\]
and
\[
\frac{39}{40},
\]
and checks \(2875\) finite ordering comparisons below the corresponding thresholds.

For \(95\%\) confidence it verifies
\[
n_*=40,
\]
with
\[
(\mathrm{VaR},\mathrm{ES})(A)
=
\left(1,\frac72\right)
\]
and
\[
(\mathrm{VaR},\mathrm{ES})(B)
=
(2,3).
\]

For \(97.5\%\) confidence it verifies
\[
n_*=80
\]
with the same score pair.

Run:

`python3 verify_var_es_same_mean_max_threshold.py`

The first output line must be `VERIFY_OK`.

The universal theorem is proved algebraically above; the finite replay is a consistency check rather than a substitute for that proof.

## Relationship to prior work
Acerbi and Tasche give the directly relevant foundation. Their full public preprint defines VaR through a quantile threshold, explains why VaR is insensitive to losses beyond that threshold, derives Expected Shortfall from the average of a fixed worst-case probability mass, and gives the generalized-inverse integral representation of Expected Shortfall.

The same paper also discusses empirical samples and order statistics. Its sample discussion focuses on constructing Expected Shortfall from the worst fraction of observed outcomes and on the subtleties created by atoms and quantile estimation.

Those results fully motivate the present problem and supply the risk-measure definitions. They do not state the constrained finite-order theorem here: when mean loss and worst loss are both matched, VaR and Expected Shortfall must remain order-compatible until the tail contains enough empirical probability mass to reach two observations beyond the VaR order statistic.

Targeted searches for same-mean, same-maximum, fixed-worst-loss, finite-support, historical-simulation, and minimum-scenario VaR/Expected-Shortfall ranking reversals did not locate the threshold
\[
\left\lceil\frac{2}{1-\alpha}\right\rceil
\]
or the displayed witness.

## Limitations
The result depends on the left empirical quantile and integrated-quantile Expected Shortfall convention.

It is a structural statement about empirical loss distributions, not a recommendation for using short historical windows. Practical estimation of tail risk generally requires substantially more data than the minimum mathematical support needed for a ranking reversal.

Matching the mean and maximum loss does not match other moments, drawdown behavior, liquidity effects, or dependence structure.

The proof is elementary once the empirical quantile geometry is isolated, so an unindexed teaching note, implementation test, or practitioner derivation could contain an equivalent boundary even though it was not located in the checked literature.

## References
1. C. Acerbi and D. Tasche, “Expected Shortfall: a natural coherent alternative to Value at Risk,” arXiv:cond-mat/0105191, first submitted 9 May 2001.
2. C. Acerbi and D. Tasche, “Expected Shortfall: A Natural Coherent Alternative to Value at Risk,” *Economic Notes* 31(2), 379–388, 2002. DOI: 10.1111/1468-0300.00091.
