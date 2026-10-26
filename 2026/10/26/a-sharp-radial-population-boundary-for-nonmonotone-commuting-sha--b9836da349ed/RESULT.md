# A sharp radial-population boundary for nonmonotone commuting shares in the finite radiation model

## Finding

Consider a finite, strictly distance-ordered collection of destinations in the radiation model of commuting. Fix one destination with opportunity mass \(n>0\), total opportunity mass \(a\geq0\) strictly nearer to the origin, and total mass \(c\geq0\) strictly farther away. Put \(S=a+n+c\). The originating population/aspiration mass \(m>0\) varies, while these external masses and the radial ordering remain fixed. The conditional share of all outward trips allocated to the selected destination by the **finite-normalized** radiation rule is
\[
P(m)=\frac{n\,m(m+S)}{S(m+a)(m+a+n)}.
\]

For an intermediate destination (\(a>0\)) there is a **sharp trichotomy**:

1. If \(c\leq a\), then \(P(m)\) is strictly increasing on \((0,\infty)\), and it approaches \(n/S\) from below. No finite maximum occurs.
2. If \(c>a\), then \(P(m)\) increases strictly to a unique finite strict global maximum at
\[
m_* = \frac{a(a+n)+\sqrt{a(a+n)c(n+c)}}{c-a},
\]
then decreases strictly to \(n/S\) from above. More precisely, \(P(m)>n/S\) if and only if
\[
m>\frac{a(a+n)}{c-a}.
\]
The exact peak enrichment relative to the large-origin share is
\[
\frac{P(m_*)}{n/S}=\frac{\bigl(\sqrt{(a+n)(n+c)}-\sqrt{ac}\bigr)^2}{n^2}>1.
\]
3. At the critical boundary \(c=a>0\), no finite peak exists; approaching it from above with \(\varepsilon=c-a\downarrow0\) and \(a,n\) fixed produces the singular onset
\[
m_*\sim\frac{2a(a+n)}{\varepsilon},\qquad
\frac{P(m_*)}{n/S}-1\sim\frac{\varepsilon^2}{4a(a+n)}.
\]

The criterion \(c>a\) is independent of the selected destination's own mass \(n\): the emergence of a finite source-size peak is governed solely by whether the population beyond the destination exceeds that before it.

For the nearest destination (\(a=0\)), \(P(m)\) is strictly decreasing whenever \(c>0\); if this is the only destination (\(a=c=0\)), its share is identically one. For the farthest destination (\(c=0<a\)), its share is strictly increasing. These cases complete the boundary classification.

An exact three-destination example has masses \((1,1,8)\) ordered by distance; for the middle destination,
\[
P(m)=\frac{m(m+10)}{10(m+1)(m+2)}.
\]
The unique maximum is attained at \(m=2\), with \(P(2)=1/5\), twice its large-origin limit \(1/10\). The normalized three shares at this origin mass are exactly \((2/5,1/5,2/5)\).

## Assumptions and scope

There is one origin and a finite number \(J\geq1\) of destination sites, all at distinct distances from it and all carrying strictly positive opportunity masses \(n_1,\ldots,n_J\). They comprise **all** external destinations over which the outward flux is normalized. Their opportunity masses do not change as the origin mass \(m\) varies. Let \(s_j=\sum_{k<j} n_k\), in distance order, and \(S=\sum_j n_j\).

The original radiation model assigns an unnormalized destination weight
\[
w_j(m)=\frac{m n_j}{(m+s_j)(m+s_j+n_j)}.
\]
The finite-system rule divides each weight by \(\sum_jw_j(m)\). The resulting shares are conditional on an outward trip and therefore do not assume any fixed total commuter volume; the total may depend on \(m\). The theorem treats \(m\) as a continuous positive scale variable, as is appropriate to comparative statics of the analytic mobility law. It does not assert that every continuous maximizer is realizable by an integer-valued census.

The theorem is a property of this specified production-normalized law, not of all radiation variants, empirically calibrated models, or actual commuting responses. Equal-distance ties, changes to opportunity masses, and partially observed destination sets are not included.

## Proof

**Finite normalization.** The elementary identity
\[
w_j(m)=\frac{m}{m+s_j}-\frac{m}{m+s_j+n_j}
\]
telescopes over the full strictly ordered destination set, giving
\[
\sum_{j=1}^J w_j(m)=1-\frac{m}{m+S}=\frac{S}{m+S}.
\]
Thus for a target preceded by total mass \(a\), carrying mass \(n\), and followed by mass \(c\), the conditional destination share is exactly the stated \(P(m)\). In particular \(0<P(m)\leq1\) and \(P(m)\to n/S\) as \(m\to\infty\).

**Derivative and strict classification.** Assume first \(a>0\), and abbreviate \(b=a+n\), so \(S=b+c\). Differentiating gives
\[
P'(m)=\frac{n}{S}\,
\frac{(a-c)m^2+2abm+Sab}{(m+a)^2(m+b)^2}.
\]
If \(c\leq a\), the numerator is positive for every \(m>0\), proving strict increase. Furthermore
\[
\frac{P(m)}{n/S}-1
=\frac{(c-a)m-ab}{(m+a)(m+b)},
\]
which is negative in this case. If \(c>a\), the derivative numerator is a strictly concave quadratic with positive constant coefficient and negative leading coefficient. Its two real roots have opposite signs, so it has exactly one positive root. Solving gives
\[
m_* =\frac{ab+\sqrt{a b\,[ab+S(c-a)]}}{c-a}
=\frac{ab+\sqrt{abc(n+c)}}{c-a},
\]
where \(ab+S(c-a)=c(n+c)\). The derivative is positive before and negative after this point. Hence \(m_*\) is the unique finite strict global maximizer. The displayed difference from the asymptotic share yields the exact above-baseline criterion.

**Peak enrichment.** Write \(\Lambda=P(m_*)/(n/S)\). For arbitrary \(m>0\), the equation \(P(m)/(n/S)=\lambda\) is equivalent to
\[
(\lambda-1)m^2+[\lambda(a+b)-S]m+\lambda ab=0.
\]
At a stationary value the positive solution is double, so the discriminant vanishes. Its two possible values are
\[
\lambda_\pm=\frac{\bigl(\sqrt{b(S-a)}\pm\sqrt{a(S-b)}\bigr)^2}{(b-a)^2}.
\]
Only the smaller value \(\lambda_-\) has a positive double root in the case \(c>a\); the larger corresponds to a negative double root. Substituting \(S-a=n+c\), \(S-b=c\), and \(b-a=n\) proves the peak formula. Its strict inequality follows also from the previously proved above-baseline interval.

**Critical onset.** Write \(c=a+\varepsilon\) with \(a,n>0\) fixed. The exact maximizer satisfies
\[
m_* =\frac{ab+\sqrt{ab(a+\varepsilon)(b+\varepsilon)}}{\varepsilon}
\sim\frac{2ab}{\varepsilon}.
\]
At the maximum, the exact baseline difference is
\[
\frac{P(m_*)}{n/S}-1
=\frac{\varepsilon m_*-ab}{(m_*+a)(m_*+b)}.
\]
Inserting the preceding asymptotic relation yields \(\varepsilon^2/(4ab)\) as the leading term. At \(\varepsilon=0\) the derivative remains strictly positive at every finite \(m\), so the peak truly emerges from infinity rather than from a finite stationary point.

**Nearest and farthest boundaries.** If \(a=0\), then \(P(m)=n(m+S)/(S(m+n))\). Its derivative is \(n(n-S)/(S(m+n)^2)\), which is negative for \(c=S-n>0\) and zero if \(c=0\). If \(c=0<a\), the strictly positive derivative argument for \(c\leq a\) applies. This exhausts the nonnegative boundary masses.

## Verification

The accompanying self-contained `verify.py` uses Python 3 with no third-party dependencies. Run `python verify.py` in the same directory as this document. It confirms the exact rational three-destination example, telescoping finite normalization, the exact baseline crossing, 4,200 randomized parameter configurations against the analytical derivative and peak equations, and numerical critical-onset checks. It prints `ALL CHECKS PASSED` when successful.

The exact argument above, not the numerical sample, proves the theorem over the full continuous positive parameter ranges.

## Relationship to prior work

Simini, González, Maritan and Barabási introduced the radiation mobility law; their 2011 preprint and supplementary Section 2 derive the basic unnormalized destination weight and discuss its large-origin limits. Masucci, Serras, Johansson and Batty's arXiv preprint of 25 June 2012 and its 2013 publication explicitly provide the finite-population normalization used here. Those model equations, their original derivations, and their associated saturation interpretations are established prior work and are not novelty claims.

Hilton, Sood and Evans (2020) study empirical predictive limitations and variations in mappings of site data to radiation-model parameters, explicitly describing source mass as a mobility-aspiration parameter. The present result instead classifies the conditional share of one fixed destination **as that source mass varies**, including the exact inner-versus-outer threshold, unique finite maximum, and singular quadratic onset. Kang, Liu, Guo and Qin (2015) generalize the model by a scaling exponent and trip constraints; those generalizations are distinct from the fixed finite-normalized base law analyzed here.

The stated formulas may follow from more general mathematical comparative-statics results not found in the sources inspected. No claim of independent priority, empirical validation, or universal applicability is made.

## Limitations

All conclusions depend on fixed outward opportunity masses, strict radial ordering, complete production normalization, and continuous variation of one origin mass. The critical criterion says nothing about actual urban population growth if the opportunity landscape, individual preferences, spatial scale, attractiveness proxies, or departure rates co-evolve. The model may fit observed commuting data poorly in some settings. The result does not identify causal effects and should not be used as a forecasting guarantee. An external audit has not been performed, and incomplete access to some model-variant publications leaves a residual historical-coverage risk.

## References

1. F. Simini, M. C. González, A. Maritan, and A.-L. Barabási, “A universal model for mobility and migration patterns,” arXiv:1111.0586, first submitted 2 November 2011; *Nature* **484** (2012), 96–100. https://arxiv.org/abs/1111.0586
2. A. P. Masucci, J. Serras, A. Johansson, and M. Batty, “Gravity vs radiation model: on the importance of scale and heterogeneity in commuting flows,” arXiv:1206.5735, first submitted 25 June 2012; *Physical Review E* **88** (2013), 022812. https://arxiv.org/abs/1206.5735
3. C. Kang, Y. Liu, D. Guo, and K. Qin, “A generalized radiation model for human mobility: spatial scale, searching direction and trip constraint,” *PLOS ONE* **10** (2015), e0143500. https://doi.org/10.1371/journal.pone.0143500
4. B. Hilton, A. P. Sood, and T. S. Evans, “Predictive limitations of spatial interaction models: a non-Gaussian analysis,” *Scientific Reports* **10** (2020), 17474. https://doi.org/10.1038/s41598-020-74601-z
