# A sharp offset-contrast threshold for reentrant apparent Omori decay

## Finding

Consider a two-component coeval inverse-time aftershock intensity
\[
\lambda(t)=\frac{A}{t+a}+\frac{B}{t+b},\qquad 0<a<b,\quad A,B>0,\quad t\ge0.
\]
Define the instantaneous *apparent exponent* by the local logarithmic slope
\[
E(t)=-\frac{d\log\lambda(t)}{d\log t}=-\frac{t\lambda'(t)}{\lambda(t)},\qquad t>0.
\]
Thus \(E(t)\) is not the intrinsic power exponent of either component: both intrinsic exponents equal one.

**Sharp uniform classification.** Let \(R=b/a\) and \(R_c=17+12\sqrt2=(3+2\sqrt2)^2\).

1. If \(1<R\le R_c\), the apparent exponent \(E(t)\) is strictly increasing on \((0,\infty)\) for *every* positive amplitude ratio \(A/B\). For \(R<R_c\), its derivative is strictly positive everywhere. At equality, the derivative can vanish only at \(t=\sqrt{ab}\), and only when \(A/B=\sqrt{a/b}\); this is a horizontal tangency without a reversal.
2. If \(R>R_c\), the explicit amplitude ratio \(A/B=\sqrt{a/b}\) produces *exactly two* positive stationary points of \(E\): first a strict local maximum and then a strict local minimum. Therefore the apparent exponent increases, decreases, and increases again, although each of the two component laws has fixed intrinsic exponent one.
3. For *every* \(R>1\) and positive amplitude ratio, \(E'\) has at most two positive zeros counted with multiplicity. In particular, no two-component model in this family has more than two strict apparent-exponent turning points.

The fixed-contrast threshold \(R_c\) is necessary and sufficient for *existence of an amplitude mixture with a decreasing apparent-exponent interval*. It is not a claim that every amplitude mixture above the threshold reverses.

## Assumptions and scope

The two constituent processes start at the same reference time and their deterministic intensities add. Their initial regularization times \(a,b\) are positive and distinct; their amplitudes are positive. Equivalently, these can be two independently superposed nonhomogeneous Poisson processes, but the result concerns only the deterministic mean intensity, not realization-wise slope estimates. Background seismicity, time-varying detection, secondary-event branching, and any intrinsic exponent unequal to one are excluded.

The local exponent \(E\) uses natural logarithms and is defined on strictly positive times. Direct differentiation gives \(0<E(t)<1\), \(E(0+)=0\), and \(E(t)\to1\) as \(t\to\infty\). These endpoints do not imply monotonicity.

## Proof

**Step 1: derivative as a competition between intrinsic saturation and shifting weights.** Define
\[
\pi(t)=\frac{A/(t+a)}{\lambda(t)}\in(0,1),\quad
X(t)=\frac{a}{(t+a)^2},\quad
Y(t)=\frac{b}{(t+b)^2},\quad
Z(t)=\frac{t(b-a)^2}{(t+a)^2(t+b)^2}.
\]
Then
\[
E(t)=t\left(\frac{\pi(t)}{t+a}+\frac{1-\pi(t)}{t+b}\right),\qquad
\pi'(t)=-\frac{(b-a)\pi(t)(1-\pi(t))}{(t+a)(t+b)},
\]
so the exact derivative identity is
\[
\boxed{E'(t)=\pi(t)X(t)+(1-\pi(t))Y(t)-Z(t)\pi(t)(1-\pi(t)).}
\]
The first terms are positive component-saturation effects; the last term reflects the progressive loss of weight on the shorter-offset component.

**Step 2: a necessary-and-sufficient local sign test.** At each fixed \(t>0\), varying \(A/B\) through positive values varies \(\pi\) through all \((0,1)\). Since
\[
\frac{\pi X+(1-\pi)Y}{\pi(1-\pi)}
=\frac{X}{1-\pi}+\frac{Y}{\pi}
\ge(\sqrt X+\sqrt Y)^2,
\]
with equality at \(\pi=\sqrt Y/(\sqrt X+\sqrt Y)\), a negative derivative is achievable at that time **if and only if**
\[
Z>(\sqrt X+\sqrt Y)^2.
\]
Taking positive square roots and multiplying denominators, this is equivalent to
\[
\sqrt t\,(b-a)>\sqrt a\,(t+b)+\sqrt b\,(t+a).
\]
Put \(r=\sqrt{b/a}>1\) and \(y=\sqrt{t/a}>0\). Division by the positive factor \(a^{3/2}(r+1)\) reduces the inequality precisely to
\[
\boxed{y(r-1)>y^2+r.}
\]
The upward quadratic \(y^2-(r-1)y+r\) takes a negative value at a positive \(y\) exactly when its discriminant is positive:
\[
(r-1)^2-4r=r^2-6r+1>0.
\]
Since \(r>1\), this means \(r>3+2\sqrt2\), equivalently \(b/a>17+12\sqrt2\). Below this contrast the derivative is everywhere positive for all amplitudes. At equality, the sole possible zero is \(y=\sqrt r\), i.e. \(t=\sqrt{ab}\), with \(\pi=1/2\). The latter condition is equivalent to \(A/B=\sqrt{a/b}\). A derivative that is positive except possibly at one isolated point yields a strictly increasing function, proving the first assertion.

**Step 3: the explicit reversal above the threshold.** At \(t=\sqrt{ab}\), the two component terms satisfy \(X=Y\); the choice \(A/B=\sqrt{a/b}\) makes \(\pi=1/2\). The derivative at this point has the explicit form
\[
\boxed{E'(\sqrt{ab})=\frac{-r^2+6r-1}{4r(r+1)^2\,a},\qquad r=\sqrt{b/a}.
\]
For supercritical contrast its numerator is negative. On the other hand, the exact derivative formula has positive limits near \(0\) and positive leading behavior near infinity: 
\[
E'(0+)=\frac{A/a^2+B/b^2}{A/a+B/b}>0,
\qquad
E'(t)=\frac{Aa+Bb}{A+B}\,t^{-2}+O(t^{-3})>0
\]
for all sufficiently large \(t\). Hence at least two positive critical points exist, one on either side of \(\sqrt{ab}\).

**Step 4: no more than two positive critical points.** Rescale to \(z=t/a>0\), \(R=b/a>1\), \(w=A/B>0\). The derivative with respect to \(z\) has a strictly positive denominator and the numerator
\[
P(z)=c_4z^4+c_3z^3+c_2z^2+c_1z+c_0,
\]
where
\[
\begin{aligned}
c_4&=Rw+R+w^2+w,\\
c_3&=4R(w+1)^2,\\
c_2&=-R^3w+6R^2w^2+7R^2w+7Rw+6R-w,\\
c_1&=4R^3w^2+8R^2w+4R,\\
c_0&=R^4w^2+R^3w+R^2w+R.
\end{aligned}
\]
Indeed
\[
\frac{dE}{dz}=\frac{P(z)}{(R+z)^2(z+1)^2[Rw+zw+z+1]^2}.
\]
The coefficients \(c_4,c_3,c_1,c_0\) are strictly positive, while only \(c_2\) can be negative. Descartes' sign rule therefore gives at most two positive zeros counted with multiplicity. Combined with Step 3 and the signs at the endpoints, the supercritical witness has exactly two simple zeros with the claimed max/min order. The proof does not use numerical root finding.

**Exact numerical witness.** For \(a=1\), \(b=100\), \(A=1/10\), \(B=1\), one has
\[
E(10)=\tfrac12,\qquad E'(10)=-\frac{41}{4840}<0.
\]
The two critical times are approximately \(3.816457666758\) and \(26.202308195642\), and the corresponding apparent exponents are approximately \(0.552914639494\) and \(0.447085360506\). Only the exact rational sign and analytic root-count theorem are used to certify the reversal; approximations are illustrative.

## Verification

Run `python3 verify.py` from the same directory as this document. The standalone Python-3 checker uses only the standard library. It verifies the derivative identity against an independent differentiation of the original intensity, checks the normalized quartic numerator against the derivative, tests the rational witness exactly using `fractions.Fraction`, numerically brackets its two stationary points, and samples the nonreversal regime below the sharp contrast. Its randomized and grid checks are finite diagnostics, not an infinite proof; the proof above establishes the universal results.

## Relationship to prior work

The Omori inverse-time rate and modified \((t+c)^{-p}\) kernels are established, notably in Utsu, Ogata and Matsu'ura (1995) and the full mathematical ETAS analysis of Helmstetter and Sornette (2001). Shcherbakov, Turcotte and Rundle (2004) show that the empirical offset may vary with magnitude cutoff, motivating scrutiny of multiple offsets, but do not establish this two-component logarithmic-slope contrast criterion. Lolli, Boschi and Gasperini (2009) compare distinct single-component aftershock decay models; Omi, Ogata, Hirata and Aihara (2014) estimate additive triggering intensities involving shifted event times; Hainzl (2016) analyzes apparent rates due to imperfect detection. Their inspected model formulas and results do not state the sharp \(17+12\sqrt2\) two-offset threshold or the global bound of two turning points under this restricted no-background, coeval two-component setting.

This result is not a theorem about the entire ETAS branching process; its apparent-exponent reversal can be produced without branching, variable intrinsic exponent, or observational incompleteness. Conversely, those other mechanisms may produce their own changes in observed slopes. The elementary rational-function reductions could overlap with broader results on Stieltjes transforms or elasticity of mixtures not located in the checked sources; historical novelty is not independently certified.

## Limitations

Both component exponents must be exactly one. The two components have a common reference start time, fixed positive offsets and amplitudes, and no additive background. The sharp cutoff guarantees existence of some reversing amplitude above it, not reversal for every positive amplitude. The result neither identifies seismic mechanisms from data nor proves a statistical estimator can resolve the two extrema from a noisy and incomplete catalog. Generalizations to three or more components, varying offsets, ETAS feedback, finite observational windows, and exponent heterogeneity are not established.

## References

1. Helmstetter, A. and Sornette, D. (2001), *Sub-critical and Super-critical Regimes in Epidemic Models of Earthquake Aftershocks*, arXiv:cond-mat/0109318, first submitted 2001-09-18, https://arxiv.org/abs/cond-mat/0109318 .
2. Utsu, T., Ogata, Y. and Matsu'ura, R. S. (1995), *The Centenary of the Omori Formula for a Decay Law of Aftershock Activity*, Journal of Physics of the Earth 43, 1–33, DOI:10.4294/jpe1952.43.1 (publication source records year only; public J-STAGE release dated 2009-04-30).
3. Shcherbakov, R., Turcotte, D. L. and Rundle, J. B. (2004), *A generalized Omori's law for earthquake aftershock decay*, Geophysical Research Letters 31, DOI:10.1029/2004GL019808, first published 2004-06-12.
4. Lolli, B., Boschi, E. and Gasperini, P. (2009), *A comparative analysis of different models of aftershock rate decay by maximum likelihood estimation of simulated sequences*, Journal of Geophysical Research, DOI:10.1029/2008JB005614, first published 2009-01-17.
5. Omi, T., Ogata, Y., Hirata, Y. and Aihara, K. (2014), *Estimating the ETAS model from an early aftershock sequence*, Geophysical Research Letters 41, 850–857, DOI:10.1002/2013GL058958, first published 2014-01-20.
6. Hainzl, S. (2016), *Apparent triggering function of aftershocks resulting from rate-dependent incompleteness of earthquake catalogs*, Journal of Geophysical Research 121, 6499–6509, DOI:10.1002/2016JB013319, first published 2016-08-20.
