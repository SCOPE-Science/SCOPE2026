# CHME and SME share a tail index but have a sharp tail-constant crossover
## Finding
Let the moment exponential baseline have scale \(\beta>0\). The 2026 confluent hypergeometric moment exponential (CHME) model is defined by
\[
X_C=\frac{Y}{2Z_C},
\qquad
Y\sim\mathrm{ME}(\beta),
\qquad
Z_C\sim\mathrm{Beta}(q,q),
\]
with \(q>0\). The earlier slashed moment exponential (SME) model uses
\[
X_S=\frac{Y}{Z_S},
\qquad
Z_S\sim\mathrm{Beta}(q,1),
\]
with the same moment-exponential baseline and the same nominal \(\beta,q\).

The two models have the **same** Pareto survival exponent. Their right tails satisfy
\[
\boxed{
\overline F_C(x)
\sim
K_C x^{-q},
\qquad
K_C=
(q+1)2^{-q}\beta^q\frac{\Gamma(2q)}{\Gamma(q)}
}
\]
and
\[
\boxed{
\overline F_S(x)
\sim
K_S x^{-q},
\qquad
K_S=\beta^q\Gamma(q+2).
}
\]
Hence
\[
\boxed{
\frac{\overline F_C(x)}{\overline F_S(x)}
\longrightarrow
R(q)
=
\frac{2^{-q}\Gamma(2q)}{q\Gamma(q)^2}.
}
\]

The tail-order comparison has a sharp crossover. There is a unique
\[
\boxed{
q_*=2.578543315125812\ldots
}
\]
such that \(R(q_*)=1\). Therefore
\[
R(q)<1\quad(0<q<q_*),
\qquad
R(q)>1\quad(q>q_*).
\]
At representative values,
\[
R(1)=\frac12,
\qquad
R(2)=\frac34,
\qquad
R(3)=\frac54.
\]
Thus, at equal \(\beta,q\), CHME is asymptotically lighter than SME throughout the entire interval \(0<q<q_*\), and becomes asymptotically heavier only for \(q>q_*\).

The case \(q=1\) is stronger than an asymptotic counterexample. Both latent variables are uniform on \((0,1)\), so
\[
\boxed{
X_C\overset{d}{=}\frac12X_S.
}
\]
Hence CHME is exactly a factor-two contraction of SME at equal \(\beta\) when \(q=1\).

The density equivalents are
\[
f_C(x)\sim qK_Cx^{-q-1},
\qquad
f_S(x)\sim qK_Sx^{-q-1},
\]
so both hazards have the same terminal form
\[
\boxed{
h_C(x)\sim h_S(x)\sim\frac qx.}
\]
Likewise, both have the same positive-real-moment cutoff
\[
\boxed{
\mathbb E[X^r]<\infty
\quad\Longleftrightarrow\quad
0<r<q.
}
\]
Finally, their upper quantiles satisfy
\[
\boxed{
\frac{Q_C(1-u)}{Q_S(1-u)}
\longrightarrow
R(q)^{1/q}
}
\qquad(u\downarrow0).
\]

The 2026 source correctly identifies the CHME density as Pareto-type with exponent \(q+1\), but it also motivates the symmetric-Beta construction as producing heavier tails than SME. The comparison above shows that this latter statement is not uniform at equal nominal parameters: the two models share the same Pareto exponent, while only the multiplicative tail constant changes sign relative to SME at \(q_*\).

## Assumptions and scope
The comparison fixes the same \(\beta>0\) and \(q>0\) in both models. This is the natural same-parameter comparison used by the stochastic representations and by the formulas quoted in the 2026 source.

“Heavier” is used in the precise first-order survival sense: if two survival functions have the same regularly varying exponent, the one with larger asymptotic survival constant has the larger extreme-tail probability at a common large threshold.

The result does not claim that CHME cannot have larger kurtosis, a better finite-sample fit, or a more useful body-to-tail transition. Those properties can differ even when the regular-variation exponent is identical. The theorem addresses only the asymptotic right-tail ordering at common \(\beta,q\).

## Proof
The 2026 source derives
\[
f_C(x)
=
\frac{2(q+1)x e^{-2x/\beta}}{\beta^2(2q+1)}
{}_1F_1\!\left(q;2q+2;\frac{2x}{\beta}\right).
\]
Using
\[
{}_1F_1(a;b;t)
\sim
\frac{\Gamma(b)}{\Gamma(a)}e^t t^{a-b},
\]
gives
\[
f_C(x)
\sim
q(q+1)2^{-q}\beta^q
\frac{\Gamma(2q)}{\Gamma(q)}
 x^{-q-1}.
\]
Integrating the two-sided asymptotic bounds for this positive density yields
\[
\overline F_C(x)
\sim
(q+1)2^{-q}\beta^q
\frac{\Gamma(2q)}{\Gamma(q)}x^{-q}.
\]

For SME, the density quoted by the same source from the 2017 construction is
\[
f_S(x)
=
q\beta^q x^{-q-1}
\gamma\!\left(q+2,\frac{x}{\beta}\right),
\]
where \(\gamma\) is the lower incomplete gamma function. Since
\[
\gamma(q+2,x/\beta)\longrightarrow\Gamma(q+2),
\]
we get
\[
f_S(x)
\sim
q\beta^q\Gamma(q+2)x^{-q-1}
\]
and therefore
\[
\overline F_S(x)
\sim
\beta^q\Gamma(q+2)x^{-q}.
\]
Dividing the two survival constants gives
\[
R(q)
=
\frac{2^{-q}\Gamma(2q)}{q\Gamma(q)^2}.
\]

For \(0<q\le1\),
\[
qB(q,q)
=
q\int_0^1t^{q-1}(1-t)^{q-1}\,dt
\ge
q\int_0^1t^{q-1}\,dt
=1,
\]
because \((1-t)^{q-1}\ge1\). Since
\[
R(q)=\frac{2^{-q}}{qB(q,q)},
\]
it follows that \(R(q)<1\) throughout \(0<q\le1\).

For \(q\ge1\), the duplication formula gives
\[
R(q)
=
\frac{2^{q-1}}{q\sqrt\pi}
\frac{\Gamma(q+1/2)}{\Gamma(q)}.
\]
Differentiation yields
\[
\frac{d}{dq}\log R(q)
=
\log2+\psi(q+1/2)-\psi(q)-\frac1q.
\]
The digamma difference has the integral representation
\[
\psi(q+1/2)-\psi(q)
=
\int_0^\infty
\frac{e^{-qt}}{1+e^{-t/2}}\,dt.
\]
Since \(1/q=\int_0^\infty e^{-qt}\,dt\),
\[
\frac{d}{dq}\log R(q)
=
\log2-
\int_0^\infty
\frac{e^{-qt}}{1+e^{t/2}}\,dt
\ge
\log2-\frac{1}{2q}>0
\]
for \(q\ge1\). Thus \(R\) is strictly increasing on \([1,\infty)\). Because
\[
R(2)=\frac34<1,
\qquad
R(3)=\frac54>1,
\]
there is a unique root \(q_*\in(2,3)\). Numerical solution gives
\[
q_*=2.578543315125812\ldots .
\]

The hazard and moment conclusions follow from the common density/survival exponent. The quantile ratio follows by inversion of
\[
\overline F_j(x)\sim K_jx^{-q},
\]
which gives
\[
Q_j(1-u)\sim(K_j/u)^{1/q}.
\]

## Verification
The accompanying checker evaluates the exact CHME survival through its beta-mixture representation and the exact SME survival through its beta-slash representation. At \(q=1,2,3\), it confirms the predicted normalized survival constants and the limiting survival ratios \(1/2\), \(3/4\), and \(5/4\).

It independently solves \(R(q)=1\) at high precision and verifies positivity of the analytic derivative bound on \([1,\infty)\). It also checks that the exact hazard ratios satisfy
\[
xh_C(x)\to q,
\qquad
xh_S(x)\to q.
\]

These calculations are consistency checks only. The crossover theorem is proved analytically above.

## Relationship to prior work
Olmos et al. introduce CHME using the symmetric \(\mathrm{Beta}(q,q)\) slash-type mechanism. Their full paper derives the CHME density and its Pareto-type asymptotic
\[
f_C(x)\propto x^{-q-1},
\]
and explicitly states that the construction is designed to exhibit heavier tails than the earlier SME distribution. The paper does not compare the two first-order tail constants.

Iriarte et al. introduce SME using a \(\mathrm{Beta}(q,1)\) slash factor. The 2026 CHME paper reproduces the SME density formula in its introduction, which is sufficient to determine the SME asymptotic constant. The original SME article confirms the quotient construction and heavy-tail motivation.

Focused searches using the exact CHME DOI, CHME/SME names, same-index language, tail-constant comparisons, beta-mixing aliases, hazard asymptotics, and upper-quantile comparisons did not locate the crossover function \(R(q)\) or the threshold \(q_*\).

## Limitations
The result compares equal nominal \(\beta,q\). A comparison after matching variance, median, kurtosis, or another functional could produce a different ordering and is not addressed here.

The original 2017 SME PDF was not fully retrievable through the available public interface during the final comparison; however, the exact SME density is reproduced as Eq. (1.3) in the fully inspected 2026 CHME source, and the primary 2017 article page confirms the stochastic quotient construction. This access limitation remains a residual literature risk rather than evidence of noncoverage.

No second-order tail expansion is claimed. The body-to-tail transition and finite-threshold survival ordering can differ from the eventual constant-ratio ordering.

## References
1. N. M. Olmos, W. E. Caimanque, Y. M. Gómez, F. Segovia, and O. Venegas, “A flexible moment exponential distribution based on confluent hypergeometric functions: properties, inference, and applications,” AIMS Mathematics 11 (2026), 27706–27727. DOI: 10.3934/math.20261108.
2. Y. A. Iriarte, J. M. Astorga, O. Venegas, and H. W. Gómez, “Slashed Moment Exponential Distribution,” Journal of Statistical Theory and Applications 16 (2017), 354–365. DOI: 10.2991/jsta.2017.16.3.7.
