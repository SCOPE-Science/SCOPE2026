# The APT-DUSL family is exponentially light-tailed for every parameter value
## Finding
Consider the alpha-power transformed DUS-Lindley distribution with
\[
\alpha>0,
\qquad
\xi>0.
\]
Let the Lindley survival be
\[
S_L(x)
=
\left(
1+\frac{\xi x}{1+\xi}
\right)e^{-\xi x},
\]
so its CDF is
\[
G_L(x)=1-S_L(x).
\]
The DUS-Lindley CDF is
\[
H(x)
=
\frac{e^{G_L(x)}-1}{e-1}.
\]
The alpha-power transformation then gives
\[
F(x)
=
\frac{\alpha^{H(x)}-1}{\alpha-1},
\qquad
\alpha\ne1,
\]
with the continuous limiting case
\[
F(x)=H(x)
\]
when \(\alpha=1\).

Define
\[
c(\alpha)
=
\begin{cases}
\dfrac{\alpha\log\alpha}{\alpha-1},&\alpha\ne1,\\[6pt]
1,&\alpha=1.
\end{cases}
\]
Then
\[
c(\alpha)>0
\]
for every \(\alpha>0\).

The exact right-tail asymptotics are
\[
\boxed{
1-F(x)
\sim
K_{\alpha,\xi}\,x e^{-\xi x},
}
\]
and
\[
\boxed{
f(x)
\sim
\xi K_{\alpha,\xi}\,x e^{-\xi x},
}
\]
where
\[
\boxed{
K_{\alpha,\xi}
=
c(\alpha)
\frac{e}{e-1}
\frac{\xi}{1+\xi}.
}
\]

Therefore the hazard satisfies
\[
\boxed{
h(x)\longrightarrow \xi
\qquad
(x\to\infty),
}
\]
independently of \(\alpha\).

The moment-generating function has the exact real domain
\[
\boxed{
\mathbb E[e^{tX}]<\infty
\quad\Longleftrightarrow\quad
t<\xi.
}
\]
Consequently the moment power series
\[
\sum_{r=0}^{\infty}
\frac{\mathbb E[X^r]}{r!}t^r
\]
has radius of convergence exactly
\[
\boxed{\xi.}
\]

Thus the APT-DUSL distribution is exponentially light-tailed for every admissible parameter pair. The alpha-power parameter \(\alpha\) changes the leading multiplicative tail constant and can change finite-sample or pre-asymptotic shape, but it does not change the asymptotic exponential rate, the MGF boundary, or the limiting hazard.

This contradicts the source's explicit statement that \(\alpha\) allows the model to handle heavy-tailed behavior and its interpretation that \(\alpha\) controls the long-run tail pattern.

## Assumptions and scope
The parameter domain is exactly
\[
\alpha>0,
\qquad
\xi>0,
\]
with support
\[
x>0.
\]

The phrase “heavy-tailed” is used in the standard asymptotic probability sense: a nonnegative law is heavy-tailed if every positive exponential moment is infinite. Under this definition, the APT-DUSL family is not heavy-tailed because it has finite positive exponential moments for all
\[
0<t<\xi.
\]

The finding does not claim that \(\alpha\) has no effect on the distribution. It can alter the body, skewness, finite quantiles, and the multiplicative constant in the far tail. The claim is specifically that \(\alpha\) cannot alter the asymptotic exponential decay exponent.

The result also does not challenge the normalization, CDF, PDF, or quantile formula in the source.

## Proof
Write
\[
s=S_L(x).
\]
Then
\[
s
=
\left(
1+\frac{\xi x}{1+\xi}
\right)e^{-\xi x}
\sim
\frac{\xi}{1+\xi}x e^{-\xi x}.
\]

Since
\[
G_L(x)=1-s,
\]
the DUS-Lindley survival is
\[
1-H(x)
=
1-
\frac{e^{1-s}-1}{e-1}
=
\frac{e(1-e^{-s})}{e-1}.
\]
As \(s\downarrow0\),
\[
1-e^{-s}\sim s,
\]
so
\[
1-H(x)
\sim
\frac{e}{e-1}s.
\]

Put
\[
\delta=1-H(x).
\]
For \(\alpha\ne1\),
\[
1-F(x)
=
\frac{\alpha-\alpha^{H(x)}}{\alpha-1}
=
\frac{\alpha\{1-e^{-\delta\log\alpha}\}}{\alpha-1}.
\]
As \(\delta\downarrow0\),
\[
1-e^{-\delta\log\alpha}
\sim
\delta\log\alpha,
\]
and hence
\[
1-F(x)
\sim
\frac{\alpha\log\alpha}{\alpha-1}\delta.
\]
At \(\alpha=1\), one simply has
\[
1-F(x)=\delta.
\]
Combining the two cases gives
\[
1-F(x)
\sim
c(\alpha)\frac{e}{e-1}
\frac{\xi}{1+\xi}
x e^{-\xi x}.
\]

For the density, the DUS-Lindley density is
\[
h_D(x)
=
\frac{e^{G_L(x)}}{e-1}
\frac{\xi^2}{1+\xi}(1+x)e^{-\xi x}.
\]
For \(\alpha\ne1\),
\[
f(x)
=
\frac{\log\alpha}{\alpha-1}
h_D(x)\alpha^{H(x)}.
\]
As \(x\to\infty\),
\[
G_L(x)\to1,
\qquad
H(x)\to1,
\]
and therefore
\[
f(x)
\sim
c(\alpha)\frac{e}{e-1}
\frac{\xi^2}{1+\xi}
x e^{-\xi x}.
\]
The same limit follows directly at \(\alpha=1\).

Dividing the density asymptotic by the survival asymptotic yields
\[
h(x)=\frac{f(x)}{1-F(x)}
\longrightarrow\xi.
\]

For \(t>0\), the nonnegative tail identity gives
\[
\mathbb E[e^{tX}]
=
1+t\int_0^\infty e^{tx}\{1-F(x)\}\,dx.
\]
The tail equivalence shows that the integrand is asymptotic to
\[
tK_{\alpha,\xi}x e^{-(\xi-t)x}.
\]
The integral is finite when
\[
t<\xi
\]
and diverges when
\[
t\ge\xi.
\]
For \(t\le0\), finiteness is automatic because \(X\ge0\). Therefore the MGF domain is exactly
\[
(-\infty,\xi).
\]

Since all moment coefficients are nonnegative, the power series of the MGF converges for
\[
|t|<\xi
\]
and diverges at the positive point
\[
t=\xi.
\]
Its radius is therefore exactly \(\xi\).

## Verification
The accompanying checker evaluates the exact CDF, survival, PDF, and hazard from the published transformations.

For several parameter pairs on both sides of
\[
\alpha=1,
\]
it verifies numerically that
\[
\frac{1-F(x)}
{K_{\alpha,\xi}x e^{-\xi x}}
\longrightarrow1,
\]
that
\[
\frac{f(x)}
{\xi K_{\alpha,\xi}x e^{-\xi x}}
\longrightarrow1,
\]
and that
\[
h(x)\longrightarrow\xi.
\]

It also checks the boundary mechanism for the exponential moment by verifying that
\[
\frac{e^{\xi x}f(x)}
{\xi K_{\alpha,\xi}x}
\longrightarrow1.
\]
Thus the MGF integrand at
\[
t=\xi
\]
has linear growth and cannot be integrable.

The finite numerical evaluations are consistency checks. The tail equivalence and exact MGF domain are established analytically in the proof.

## Relationship to prior work
Jamil et al. define the APT-DUSL family by applying the alpha-power transformation to the DUS-Lindley distribution. Their formulas for the Lindley baseline, DUS transformation, APT transformation, and resulting APT-DUSL CDF provide all ingredients used above.

The source repeatedly attributes tail control to \(\alpha\). It states that \(\alpha\) controls tail behavior and skewness, says that \(\alpha\) allows the model to handle heavy-tailed behavior, and later describes adaptation to heavy-tailed datasets as a practical advantage. The article also develops a moment-generating series but does not identify its exact finite domain.

The exact asymptotics show a sharper distinction. The parameter \(\alpha\) can change a finite multiplicative tail constant, but the exponential decay exponent is always \(\xi\). In particular, every APT-DUSL law has a nonempty interval of positive exponential moments.

The standard probability definition of a heavy-tailed nonnegative law is failure of every positive exponential moment to exist. Under that definition, the family is light-tailed.

Focused searches using the exact DOI, APT-DUSL name, heavy-tail terminology, MGF boundary, exponential-tail rate, and hazard-limit aliases did not locate a published corrigendum or a model-specific result already stating this correction.

## Limitations
The result is asymptotic. It does not deny that \(\alpha\) can materially alter finite quantiles, skewness, kurtosis, or empirical fit over observed ranges.

No claim is made that a light-tailed model cannot fit a finite dataset whose empirical sample contains large observations. The correction concerns the mathematical asymptotic tail class.

The full finite-\(x\) hazard-shape phase diagram is not classified here.

A very recent unindexed correction could exist outside the records examined.

## References
1. R. Jamil, M. Mominkhan, L. Alamoudi, and L. Baharith, “Modeling Lifetime Data with a Novel Alpha-Power DUS Lindley Distribution,” Mathematics 14 (2026), 2469. DOI: 10.3390/math14142469.
2. B. Merz et al., “Understanding Heavy Tails of Flood Peak Distributions,” Water Resources Research 58 (2022), e2021WR030506. DOI: 10.1029/2021WR030506.
