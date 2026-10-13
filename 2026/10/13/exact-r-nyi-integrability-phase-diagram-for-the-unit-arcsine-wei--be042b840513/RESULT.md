# Exact Rényi-integrability phase diagram for the unit arcsine–Weibull law
## Finding

Let \(Y\) have the unit arcsine–Weibull density
\[
g(y)=\frac{k}{\pi\lambda y}
\left(\frac{-\log y}{\lambda}\right)^{k-1}
\frac{\exp\!\left[-\frac12\left(\frac{-\log y}{\lambda}\right)^k\right]}
{\sqrt{1-\exp\!\left[-\left(\frac{-\log y}{\lambda}\right)^k\right]}},
\qquad 0<y<1,
\]
with \(k>0\) and \(\lambda>0\). For Rényi order \(p>0\), \(p\ne1\), write
\[
J_p=\int_0^1 g(y)^p\,dy.
\]
Then \(J_p<\infty\) exactly in the following cases:

1. \(0<p<1\);
2. \(p>1\) and \(k>\max\{1,2-2/p\}\);
3. \(1<p<2\), \(k=1\), and \(\lambda<p/[2(p-1)]\).

In every other case with \(p>1\), \(J_p=\infty\). Consequently the Rényi entropy
\[
R_p(Y)=\frac{1}{1-p}\log J_p
\]
has extended value \(-\infty\), rather than a finite value, outside the displayed finiteness region.

The recent source introduces the same \(J_p\) and derives a double-series expression for all \(p>0\), \(p\ne1\), without stating this existence region. The restriction is consequential for its own fitted example: its reported maximum-likelihood estimates are \(k=0.9952\) and \(\lambda=0.9716\). Since \(k<1\), the fitted density has \(J_p=\infty\) for every \(p>1\).

## Assumptions and scope

The result uses exactly the two-parameter unit arcsine–Weibull density defined in Alghufily, Sultan, Mansour, and Mohamed (2026), with \(k>0\), \(\lambda>0\), and support \((0,1)\). The Rényi order satisfies \(p>0\) and \(p\ne1\).

The claim classifies finiteness of the defining integral \(J_p\). It does not assess the Shannon limit \(p\to1\), other entropy measures, moment formulas, estimation procedures, or goodness of fit.

## Proof

Set
\[
t=\left(\frac{-\log y}{\lambda}\right)^k.
\]
Then
\[
y=\exp\!\left(-\lambda t^{1/k}\right),
\qquad
|dy|=\frac{\lambda}{k}t^{1/k-1}
\exp\!\left(-\lambda t^{1/k}\right)dt.
\]
Substitution into \(J_p\) gives
\[
J_p=C_{p,k,\lambda}
\int_0^\infty
t^{a}
\exp\!\left((p-1)\lambda t^{1/k}-\frac p2t\right)
(1-e^{-t})^{-p/2}\,dt,
\]
where
\[
C_{p,k,\lambda}=\left(\frac{k}{\pi\lambda}\right)^p\frac{\lambda}{k}>0,
\qquad
a=\frac{(p-1)(k-1)}{k}.
\]
This is the transformed integral printed in the source, with the constant prefactor restored.

As \(t\downarrow0\),
\[
1-e^{-t}\sim t
\]
and the exponential factor tends to one. Hence the integrand is asymptotic, up to a positive constant, to
\[
t^{a-p/2}.
\]
Local integrability at zero is therefore equivalent to
\[
a-\frac p2>-1.
\]
After simplification,
\[
a-\frac p2+1
=\frac{p(k-2)+2}{2k},
\]
so the exact zero-end condition is
\[
k>2-\frac2p.
\]
For \(0<p<1\) this condition is automatic because its right-hand side is negative.

As \(t\to\infty\), the factor \((1-e^{-t})^{-p/2}\) tends to one and the logarithm of the remaining non-polynomial part is
\[
(p-1)\lambda t^{1/k}-\frac p2t.
\]
If \(0<p<1\), both terms are nonpositive and the linear term gives exponential decay, so the tail is integrable for every \(k>0\) and \(\lambda>0\).

Now let \(p>1\). If \(k>1\), then \(t^{1/k}=o(t)\), so \(-pt/2\) dominates and the tail is integrable. Combining this with the zero-end condition yields
\[
k>\max\left\{1,2-\frac2p\right\}.
\]
If \(k<1\), then \(t^{1/k}\) grows faster than \(t\), the positive term \((p-1)\lambda t^{1/k}\) dominates, and the tail integral diverges.

It remains to treat \(k=1\). Then the polynomial exponent is \(a=0\), and the tail exponential is
\[
\exp\!\left(\left[(p-1)\lambda-\frac p2\right]t\right).
\]
It is integrable exactly when
\[
\lambda<\frac{p}{2(p-1)}.
\]
The zero-end condition at \(k=1\) is equivalent to \(p<2\). Therefore the boundary case is finite exactly for
\[
1<p<2,
\qquad
\lambda<\frac{p}{2(p-1)}.
\]
At equality in either endpoint condition the corresponding integral has logarithmic or constant-order divergence, so all inequalities above are strict. These cases exhaust \(p>0\), \(p\ne1\), and prove the classification.

A simple check is \(p=2\), \(k=1\). As \(y\uparrow1\),
\[
g(y)\sim \frac{1}{\pi\sqrt{\lambda}}(1-y)^{-1/2},
\]
so
\[
g(y)^2\sim \frac{1}{\pi^2\lambda}(1-y)^{-1},
\]
which gives the predicted logarithmic divergence.

## Verification

The classification uses only two endpoint asymptotics of an exact change of variables. The critical exponents are independently recovered from the original density in the test case \(p=2\), \(k=1\), where the singularity at \(y=1\) is exactly of non-integrable square-density order.

For the source's maximum-likelihood estimates \(k=0.9952\), \(\lambda=0.9716\), the case \(k<1\) applies. For every \(p>1\), the transformed exponent contains a positive superlinear term \((p-1)\lambda t^{1/k}\), proving divergence at \(t=\infty\) without numerical truncation.

No finite numerical experiment is used to establish any infinite-range conclusion.

## Relationship to prior work

Alghufily, Sultan, Mansour, and Mohamed (2026) define the unit arcsine–Weibull model and, in their Section 3.4, define Rényi entropy for \(p>0\), \(p\ne1\), transform its defining integral, and then derive a double series. The transformed integral is precisely the one analyzed above, but no parameter-dependent finiteness condition is stated there.

A closely related unit arcsine–exponential model was published earlier in 2026. Its entropy section explicitly restricts the Rényi-order range to \(0<\delta<2\), showing that endpoint integrability is already recognized as a substantive issue in this nearby model. That one-parameter distribution is different and does not imply the \((p,k,\lambda)\) phase diagram above.

A separate 2026 unit arcsine–Rayleigh model also develops Rényi entropy on \((0,1)\). Its Rayleigh-based transformation produces a different density and does not subsume the Weibull shape parameter \(k\), so its formulas do not imply this classification.

Focused searches for the target DOI, the model acronym, Rényi integrability, endpoint divergence, \(L^p\) density integrability, and corrigendum language did not locate a published correction or an equivalent phase diagram.

## Limitations

The result classifies existence of the Rényi integral, not convergence of every formal double-series manipulation inside the finite region. In particular, no claim is made here that every interchange of sums and integrals in the source is justified whenever \(J_p<\infty\).

The Shannon case \(p=1\) is excluded, as in the Rényi definition. The finding does not invalidate the probability model itself, its ordinary moments, its maximum-likelihood estimator, or its reported goodness-of-fit calculations.

An unindexed correction or an equivalent endpoint analysis under different notation may exist; none was located in the checked sources.

## References

1. N. Alghufily, K. S. Sultan, M. M. M. Mansour, and N. M. Mohamed, “Statistical properties and inference for a new bounded lifetime model with application,” AIMS Mathematics 11 (2026), 14121–14140. DOI: 10.3934/math.2026580.
2. A. S. Al-Moisheer, K. S. Sultan, M. N. Mousa, and M. M. Mansour, “The Unit Arcsine–Exponential Distribution and Its Statistical Properties with Inference and Application to Reliability Data,” Axioms 15 (2026), 218. DOI: 10.3390/axioms15030218.
3. “A Novel Version of the Arcsine–Rayleigh Distribution with Entropy Measures, Statistical Inference, and Applications,” Entropy 28 (2026), 464. DOI: 10.3390/e28040464.
