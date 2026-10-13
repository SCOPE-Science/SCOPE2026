# The TASL model has balanced exponential tails and a finite MGF strip
## Finding
Let \(X\) have the tri-modal alpha-skew logistic (TASL) density
\[
f_\alpha(x)
=
\frac{P_\alpha(x)}{C(\alpha)}
\frac{e^{-x}}{(1+e^{-x})^2},
\qquad x\in\mathbb R,
\]
where
\[
P_\alpha(x)
=
\big((1-\alpha x)^2+1\big)
\big((x^2-1)^2+2\big)
\]
and \(C(\alpha)>0\) is the normalizing constant given in the source.

For every real \(\alpha\), the distribution has exponentially decaying tails. If
\[
\alpha\ne0,
\]
define
\[
A_\alpha=\frac{\alpha^2}{C(\alpha)}.
\]
Then
\[
\boxed{
f_\alpha(x)
\sim
A_\alpha x^6 e^{-x}
\qquad (x\to+\infty)
}
\]
and
\[
\boxed{
f_\alpha(-x)
\sim
A_\alpha x^6 e^{-x}
\qquad (x\to+\infty).
}
\]
Consequently,
\[
\boxed{
\overline F_\alpha(x)
\sim
F_\alpha(-x)
\sim
A_\alpha x^6 e^{-x}.
}
\]

At the special value
\[
\alpha=0,
\]
the degree drops from six to four. Writing
\[
A_0=\frac{2}{C(0)},
\]
one has
\[
\boxed{
f_0(x)
\sim
f_0(-x)
\sim
A_0x^4e^{-x}
}
\]
and
\[
\boxed{
\overline F_0(x)
\sim
F_0(-x)
\sim
A_0x^4e^{-x}.
}
\]

Thus, for every \(\alpha\in\mathbb R\),
\[
\boxed{
\frac{\overline F_\alpha(x)}
{F_\alpha(-x)}
\longrightarrow1.
}
\]
The two extreme tails are asymptotically balanced even when the finite-range density is strongly skewed.

The exact real domain of the moment generating function is
\[
\boxed{
\mathbb E[e^{tX}]<\infty
\quad\Longleftrightarrow\quad
-1<t<1.
}
\]
In particular, the model has positive exponential moments and is light-tailed in the standard exponential-moment sense.

The right hazard and left reversed hazard satisfy
\[
\boxed{
h_\alpha(x)\longrightarrow1
\qquad (x\to+\infty)
}
\]
and
\[
\boxed{
r_\alpha(x)\longrightarrow1
\qquad (x\to-\infty).
}
\]

For the source's location-scale extension
\[
Y=\mu+\beta X,
\qquad
\beta>0,
\]
the exact MGF domain becomes
\[
\boxed{
-\frac1\beta<t<\frac1\beta,
}
\]
and the corresponding far-tail hazard and reversed-hazard limits are
\[
\boxed{\frac1\beta.}
\]

These conclusions sharpen and correct the source's tail interpretation. The shape parameter \(\alpha\) can change skewness, modality, finite quantiles, and polynomial tail corrections, but it cannot change the asymptotic exponential rate or the MGF boundary. In particular, the article's description of the TASL family as a family of heavy-tailed distributions is false under the standard asymptotic exponential-moment definition.

## Assumptions and scope
The shape parameter satisfies
\[
\alpha\in\mathbb R.
\]
For the location-scale extension,
\[
\mu\in\mathbb R,
\qquad
\beta>0.
\]

The term “heavy-tailed” is used in the standard asymptotic probability sense: a right-heavy-tailed law has no finite positive exponential moment. The TASL law fails that criterion because its MGF is finite on a nonempty positive interval.

This does not say that \(\alpha\) has no effect on tail appearance at finite values of \(x\), nor does it deny that a TASL density may be leptokurtic. Kurtosis and asymptotic tail class are different properties.

The result concerns the mathematical tail class and the domain of the MGF integral. It does not reassess the article's numerical maximum-likelihood fits.

## Proof
The logistic kernel is
\[
\ell(x)
=
\frac{e^{-x}}{(1+e^{-x})^2}.
\]
As
\[
x\to+\infty,
\]
one has
\[
\ell(x)\sim e^{-x}.
\]
As
\[
x\to-\infty,
\]
one has
\[
\ell(x)\sim e^x.
\]

For
\[
\alpha\ne0,
\]
the polynomial factor has leading term
\[
P_\alpha(x)
=
\alpha^2x^6+O(x^5),
\]
and the same leading coefficient appears as \(x\to-\infty\). Hence
\[
f_\alpha(x)
\sim
\frac{\alpha^2}{C(\alpha)}x^6e^{-x}
\]
and
\[
f_\alpha(-x)
\sim
\frac{\alpha^2}{C(\alpha)}x^6e^{-x}.
\]

When
\[
\alpha=0,
\]
the first quadratic factor is the constant \(2\), so
\[
P_0(x)
=
2x^4+O(x^2).
\]
This gives the degree-four tail formulas.

For every nonnegative integer \(m\),
\[
\int_x^\infty u^m e^{-u}\,du
\sim
x^m e^{-x}.
\]
Applying this to the density asymptotics gives the survival and left-CDF asymptotics. In particular, their leading constants agree, proving
\[
\overline F_\alpha(x)/F_\alpha(-x)\to1.
\]

Now consider
\[
M_\alpha(t)
=
\int_{-\infty}^{\infty}
e^{tx}f_\alpha(x)\,dx.
\]
At the right endpoint, for either \(m=6\) or \(m=4\),
\[
e^{tx}f_\alpha(x)
\asymp
x^m e^{-(1-t)x}.
\]
The integral over the positive half-line is finite exactly when
\[
t<1.
\]
At the left endpoint, putting
\[
y=-x,
\]
gives
\[
e^{tx}f_\alpha(x)
\asymp
y^m e^{-(1+t)y}.
\]
The negative-half-line integral is finite exactly when
\[
t>-1.
\]
Combining the two conditions proves
\[
M_\alpha(t)<\infty
\quad\Longleftrightarrow\quad
-1<t<1.
\]
At \(t=1\) or \(t=-1\), the exponential damping disappears on one side and a positive polynomial remains, so the integral diverges.

Because
\[
\overline F_\alpha(x)
\sim
A_\alpha x^m e^{-x},
\]
differentiation at the asymptotic scale or direct division by the density gives
\[
h_\alpha(x)
=
\frac{f_\alpha(x)}{\overline F_\alpha(x)}
\to1.
\]
The left-tail argument gives the analogous reversed-hazard limit.

Finally, if
\[
Y=\mu+\beta X,
\]
then
\[
M_Y(t)
=
e^{\mu t}M_X(\beta t).
\]
Thus \(M_Y(t)\) is finite exactly when
\[
|\beta t|<1,
\]
and the exponential tail rate rescales from \(1\) to \(1/\beta\).

## Verification
The included checker evaluates the exact normalization constant and density from the published formula.

For several positive, negative, and zero values of \(\alpha\), it confirms numerically that the right- and left-density ratios approach the proved constants. It also computes right survival and left CDF by direct quadrature and verifies that their ratio approaches one.

For representative values of \(\alpha\), the checker evaluates the hazard and reversed hazard far into the tails and confirms convergence toward \(1\).

The checker also evaluates the MGF numerically at points strictly inside the strip. At the boundary it verifies directly that
\[
e^x f_\alpha(x)
\]
and
\[
e^{-x}f_\alpha(x)
\]
have polynomial rather than decaying asymptotics, which is the mechanism of divergence at \(t=\pm1\).

These numerical checks support reproducibility. The exact MGF domain and tail class are established analytically above.

## Relationship to prior work
Elbarougy et al. define the TASL density as a polynomial tilt of the standard logistic density. Their abstract calls the proposed class heavy-tailed, and the discussion of moments states that small \(|\alpha|\) produces heavy tails based on kurtosis. The paper also says that \(\alpha\) controls tail behavior and, in the location-scale section, assigns tail behavior specifically to \(\alpha\).

The same paper derives an explicit moment generating function involving trigonometric factors but does not state the exact domain of the defining MGF integral. The density itself fixes that domain: its two tails retain the logistic exponential rate.

The earlier flexible alpha skew-logistic model of Das et al. is a related polynomially modified logistic construction and also derives an MGF. It does not state the TASL tail-balance theorem, the exact TASL MGF strip, or the correction to the 2026 heavy-tail interpretation.

General tail literature distinguishes heavy tails from distributions with exponential asymptotic decay. Under that standard distinction, the TASL family is light-tailed for every \(\alpha\).

Focused searches using the exact DOI, TASL name, heavy-tail terminology, MGF-domain language, exponential-tail rate, and hazard-limit aliases did not locate a published correction or a source already stating the TASL result above.

## Limitations
The theorem concerns asymptotic tails. It does not rule out substantial differences in moderate-tail probabilities as \(\alpha\) varies.

A distribution can have high kurtosis while still being exponentially light-tailed; therefore this result does not contradict a purely descriptive use of “heavier” to compare finite-range kurtosis.

The full finite-\(x\) hazard-shape phase diagram is not classified here.

A very recent unindexed correction could exist outside the sources examined.

## References
1. R. Elbarougy, J. Das, P. J. Hazarika, G. G. Hamedani, A. Nandi, and M. S. Eliwa, “A novel one-parameter tri-modal alpha-skew logistic distribution: mathematical and reliability theory with applications to distant astronomical galaxies and biomedical data,” AIMS Mathematics 11 (2026), 7436–7467. DOI: 10.3934/math.2026305.
2. J. Das, P. Hazarika, G. G. Hamedani, M. Alizadeh, and J. E. Contreras-Reyes, “On the Flexible Alpha Skew-logistic Distribution: Properties and Applications,” Austrian Journal of Statistics 54 (2025), 18–43. DOI: 10.17713/ajs.v54i2.1902.
3. B. Merz et al., “Understanding Heavy Tails of Flood Peak Distributions,” Water Resources Research 58 (2022), e2021WR030506. DOI: 10.1029/2021WR030506.
