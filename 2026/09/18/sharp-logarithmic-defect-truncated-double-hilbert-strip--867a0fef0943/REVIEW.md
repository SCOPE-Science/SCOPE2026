# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The Fourier normalization and all constants were checked from the defining
strip. With
\[
\widehat f(\xi)=\frac1{2\pi}\int_{\mathbb R^2}f(x)e^{-ix\cdot\xi}\,dx,
\]
the indicator factors after the change of variables
\(u=x_1-x_2,\ y=x_2\), giving
\[
\widehat{\chi_{V_\varepsilon}}
=
\frac2\pi
\frac{\sin(\varepsilon\xi_1)}{\xi_1}
\frac{\sin(\xi_1+\xi_2)}{\xi_1+\xi_2}.
\]
The double Hilbert multiplier is \(-1\) on equal-sign quadrants and \(+1\) on
opposite-sign quadrants, so the squared defect is four times the Fourier energy
in the first and third quadrants. This yields
\[
R(\varepsilon)^2=\frac8{\pi^2\varepsilon}J(\varepsilon).
\]

The integral identity for \(J''\) was checked independently by reversing the
tail integral defining \(K(t)\). The key scalar derivative
\[
A'(\varepsilon)
=
\frac12\log\frac{1-\varepsilon^2}{\varepsilon^2}
\]
follows from two applications of the cosine Frullani identity. Integration gives
the displayed closed formula for \(J''\). Expanding
\[
\frac{(1+\varepsilon)\log(1+\varepsilon)
-(1-\varepsilon)\log(1-\varepsilon)}{2\varepsilon}
\]
produces
\[
1-\frac{\varepsilon^2}{6}-\frac{\varepsilon^4}{20}
-\frac{\varepsilon^6}{42}-\cdots,
\]
with general coefficient
\(-1/[2k(2k+1)]\). Two integrations give the stated convergent series for
\(J\), including the coefficient \(-1/72\) of \(\varepsilon^4\), and hence the
coefficient \(-1/(9\pi^2)\) of \(\varepsilon^3\) in \(R^2\).

The differentiations of the conditionally convergent oscillatory integral can
be justified by Abel damping \(e^{-\eta t}\), performing the absolutely
convergent manipulations for \(\eta>0\), and then passing to
\(\eta\downarrow0\) by standard Dirichlet estimates. Near zero,
\(-\log\varepsilon\) is locally integrable, so the conditions
\(J(0)=J'(0)=0\) determine the twice-integrated formula.

The positive-slope extension was checked by the change of variables
\((x,y)=(aLX,LY)\). Positive coordinate dilations preserve the signs of the
Fourier variables and therefore commute with the double-Hilbert multiplier,
while the Jacobian cancels in the normalized \(L^2\) ratio.

## Originality

**PASS, to the best of our knowledge.**

The full HTML of arXiv:2609.15155v1 was inspected around the truncated-strip
calculation. The paper explicitly says that it estimates the relevant
first-quadrant integral from above and obtains
\[
R(\varepsilon)\lesssim\sqrt{\varepsilon|\log\varepsilon|}.
\]
It gives an exact dyadic defect \(2\sqrt{2^{-n}}\) and remarks that the dyadic
answer has no logarithmic term. Later it describes the continuous truncation as
having analytic cost \(\sqrt{\varepsilon|\log\varepsilon|}\), but no matching
lower bound, exact leading constant, or convergent expansion was located.

Literature searches combined the exact source title and arXiv identifier with
variants of `sharp`, `asymptotic constant`, `diagonal strip`, `approximate
eigenvector`, `epsilon log epsilon`, `Fourier quadrant energy`, and `double
Hilbert transform`. The located older double-Hilbert-transform literature
concerns operator bounds along surfaces or numerical evaluation, not this 2026
indicator quasi-eigenvector or its defect asymptotic. No prior statement of
\[
R(\varepsilon)\sim\frac2\pi
\sqrt{\varepsilon\log(1/\varepsilon)}
\]
was found.

The current SCOPE archive was also searched by the source arXiv identifier and
by `double Hilbert transform`; no overlapping record was found.

The main residual originality risk is temporal: arXiv:2609.15155v1 is only a
few days old, so a contemporaneous observation may not yet be indexed. No
inaccessible paper was identified whose available title or abstract gives
specific reason to expect this exact strip-defect asymptotic.

## Value

**PASS.**

The source paper explicitly highlights the difference between the continuous
and dyadic truncations but proves only an upper bound in the continuous case.
The exact asymptotic settles whether its logarithm is genuine: it is, with
leading constant \(2/\pi\). The convergent expansion gives more than a matching
order estimate and isolates the first lower-order corrections.

This matters for the paper's quantitative-stability perspective. Its truncated
strip is the model approximate invariant set, and the new formula fixes the
actual analytic cost of creating the two truncation endpoints. At matched width,
the continuous-to-dyadic defect ratio grows like
\[
\pi^{-1}\sqrt{\log(1/\delta)},
\]
so the continuous/dyadic separation is asymptotically real rather than a
difference between proof techniques.

## Limitations and residual risks

This is an exact analysis of one natural family, not a general quantitative
stability theorem and not an optimization over all finite-measure approximate
eigenvectors. The affine extension covers positive-slope strips obtained by
coordinate dilation, not arbitrary curved or non-diagonal invariant sets.

The source preprint is very recent, and unindexed contemporaneous work remains
the main originality risk. No independent validation is asserted.
