# Three scenarios are the sharp variance–mean-absolute-deviation ranking split
## Finding
Consider an equally weighted finite return sample
\[
r_1,\ldots,r_n
\]
with mean
\[
\bar r=\frac1n\sum_{i=1}^n r_i.
\]

Use population variance
\[
V=\frac1n\sum_{i=1}^n(r_i-\bar r)^2
\]
and mean absolute deviation about the mean
\[
M=\frac1n\sum_{i=1}^n|r_i-\bar r|.
\]

With one scenario,
\[
V=M=0.
\]

With exactly two scenarios,
\[
V=M^2
\]
identically. Hence variance and mean absolute deviation cannot rank two two-scenario portfolios in opposite strict orders.

Three scenarios are sharp, even when the competing return samples have the same mean. Let
\[
A=(10,20,30)
\]
and
\[
B=(14,15,31).
\]
Both have mean
\[
20.
\]
For \(A\),
\[
M(A)=\frac{20}{3},
\qquad
V(A)=\frac{200}{3}.
\]
For \(B\),
\[
M(B)=\frac{22}{3},
\qquad
V(B)=\frac{182}{3}.
\]
Therefore
\[
M(A)<M(B)
\]
but
\[
V(A)>V(B).
\]

Thus a mean-absolute-deviation investor regards \(A\) as less risky, while a mean-variance investor regards \(B\) as less risky.

There is an exact three-scenario mechanism. Center a nonconstant three-point sample and, after multiplying by \(-1\) if needed, write it as
\[
(-a,-b,a+b),
\qquad
a,b\ge0.
\]
Set
\[
s=a+b,
\qquad
h=|a-b|.
\]
Then
\[
M=\frac{2s}{3}
\]
and
\[
V=\frac{s^2}{2}+\frac{h^2}{6}.
\]
Hence MAD depends only on the total displacement \(s\) on the side with two observations, whereas variance also penalizes how unevenly that displacement is split through \(h\).

The reversal persists for every larger equally weighted scenario count. For every
\[
n\ge3,
\]
define
\[
A_n=(10,20,30,\underbrace{20,\ldots,20}_{n-3})
\]
and
\[
B_n=(14,15,31,\underbrace{20,\ldots,20}_{n-3}).
\]
Then both means remain \(20\), while
\[
M(A_n)=\frac{20}{n}<\frac{22}{n}=M(B_n)
\]
and
\[
V(A_n)=\frac{200}{n}>\frac{182}{n}=V(B_n).
\]

## Assumptions and scope
The scenarios are equally weighted, and both risk measures are centered at each sample's own arithmetic mean.

Variance uses the population normalization \(1/n\). If sample variance with denominator \(n-1\) is used instead, all portfolios being compared at the same scenario count acquire the same positive multiplicative factor, so the ranking and the sharp scenario threshold are unchanged.

The theorem is about risk ordering, not expected return. The witness deliberately fixes the same mean to isolate the difference between quadratic and absolute dispersion penalties.

The result does not claim that three scenarios are statistically adequate for portfolio estimation. It identifies the smallest finite scenario support on which the two classical risk summaries can make opposite deterministic comparisons.

## Proof
For one scenario every deviation from the sample mean is zero, so both risks vanish.

For two observations \(x\) and \(y\), the mean is
\[
\frac{x+y}{2},
\]
and the two centered deviations are
\[
\pm\frac{x-y}{2}.
\]
Therefore
\[
M=\frac{|x-y|}{2}
\]
and
\[
V=\frac{(x-y)^2}{4}=M^2.
\]
Since squaring is strictly increasing on the nonnegative reals, variance and MAD induce exactly the same weak ordering on every collection of two-scenario samples. This proves the lower bound.

For the three-scenario witness, direct centering gives deviations
\[
(-10,0,10)
\]
for \(A\), and
\[
(-6,-5,11)
\]
for \(B\). The displayed MAD and variance values follow immediately, proving a strict reversal.

For the structural identity, consider
\[
(-a,-b,a+b).
\]
Its absolute deviations sum to
\[
2(a+b)=2s,
\]
so
\[
M=\frac{2s}{3}.
\]
Also
\[
V=\frac{a^2+b^2+(a+b)^2}{3}.
\]
Since
\[
a^2+b^2=\frac{s^2+h^2}{2},
\]
we obtain
\[
V=\frac{s^2}{2}+\frac{h^2}{6}.
\]
This proves the exact decomposition.

Finally, appending observations equal to the existing common mean changes neither raw sum of absolute centered deviations nor raw sum of squared centered deviations. Only the divisor changes from \(3\) to \(n\), giving the persistent family formulas above.

## Verification
The embedded `verify_mad_variance_minimal_scenarios.py` uses only the Python standard library and exact rational arithmetic.

It checks:
- every integer two-scenario sample in a symmetric test box, verifying the identity \(M^2=V\);
- the exact witness values for \(A\) and \(B\);
- the three-scenario structural identities for thousands of integer pairs \((a,b)\);
- the padded reversal family for every \(3\le n\le500\).

The finite replay is not the proof of the support-two impossibility or the all-\(n\) family; those statements are proved algebraically above.

Run:

`python3 verify_mad_variance_minimal_scenarios.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Konno and Yamazaki introduced the mean-absolute-deviation portfolio optimization model as an \(L_1\) alternative to Markowitz's standard-deviation or variance model. Their full text defines the mean-absolute-deviation risk functional directly and proves that, under multivariate normal returns, portfolio MAD is exactly
\[
\sqrt{\frac{2}{\pi}}
\]
times portfolio standard deviation. Thus under normality the two models produce the same risk ordering.

The same paper emphasizes that real return distributions need not be normal or symmetric and empirically compares the \(L_1\) and \(L_2\) portfolio frontiers. This establishes the practical importance of understanding when the two risk summaries do and do not agree.

The finding here is a finite-scenario boundary rather than a distributional equivalence theorem: every equally weighted one- or two-scenario sample forces order agreement, while three scenarios already allow a strict reversal at equal mean. Targeted searches using mean absolute deviation, variance, portfolio ranking, finite scenarios, two-point distributions, three-point distributions, and the exact witness values did not locate this support-size statement or the displayed three-point decomposition.

## Limitations
The sharp threshold is for equally weighted scenarios. Unequal scenario probabilities can create a different minimal-support problem.

Only dispersion around the mean is compared. Transaction costs, constraints, estimation error, skewness preferences, and downside-only risk are outside the claim.

Prior work already shows that MAD and standard deviation need not be proportional away from normality, so non-equivalence itself is not claimed as new.

Because the lower-bound proof is elementary, an unindexed exercise, software test, or practitioner note could contain an equivalent three-scenario example even though the sharp support theorem was not located.

## References
1. H. Konno and H. Yamazaki, “Mean-Absolute Deviation Portfolio Optimization Model and Its Applications to Tokyo Stock Market,” *Management Science* 37(5), 519–531, published 1 May 1991. DOI: 10.1287/mnsc.37.5.519.
