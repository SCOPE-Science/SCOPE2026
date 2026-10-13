# The SIR tail index saturates at two with a logarithmic critical phase
## Finding
Let
\[
Z=\frac{X}{Y},
\]
where
\[
X\sim\mathrm{IR}(\theta),
\qquad
Y\sim\mathrm{Beta}(q,1),
\qquad
\theta>0,\ q>0,
\]
and \(X\) and \(Y\) are independent. This is the slashed inverse Rayleigh (SIR) model introduced by Gómez et al.

The inverse-Rayleigh parent has
\[
\Pr(X>x)=1-e^{-\theta/x^2}.
\]
The SIR survival therefore has the exact integral representation
\[
\overline F_Z(z)
=
q\int_0^1
y^{q-1}
\left[
1-\exp\!\left(-\frac{\theta}{z^2y^2}\right)
\right]dy.
\]
Put
\[
a=\frac{\theta}{z^2}.
\]
The change of variable \(t=a/y^2\) gives
\[
\overline F_Z(z)
=
\frac q2 a^{q/2}
\int_a^\infty
(1-e^{-t})t^{-q/2-1}\,dt.
\]

This identity yields a sharp three-regime tail classification.

If
\[
0<q<2,
\]
then
\[
\boxed{
\overline F_Z(z)
\sim
\Gamma\!\left(1-\frac q2\right)
\theta^{q/2}z^{-q}.
}
\]

If
\[
q=2,
\]
then
\[
\boxed{
\overline F_Z(z)
\sim
\theta z^{-2}
\log\!\left(\frac{z^2}{\theta}\right).
}
\]

If
\[
q>2,
\]
then
\[
\boxed{
\overline F_Z(z)
\sim
\frac{q\theta}{q-2}z^{-2}.
}
\]

Consequently,
\[
\boxed{
\overline F_Z\in \mathrm{RV}_{-\min(q,2)}.
}
\]
At the critical value \(q=2\), the power index is still \(2\), but the slowly varying factor is logarithmic.

The density and hazard satisfy
\[
f_Z(z)
\sim
\begin{cases}
q\Gamma(1-q/2)\theta^{q/2}z^{-q-1}, & 0<q<2,\\[4pt]
2\theta z^{-3}\log(z^2/\theta), & q=2,\\[4pt]
2q\theta(q-2)^{-1}z^{-3}, & q>2,
\end{cases}
\]
and hence
\[
\boxed{
h_Z(z)\sim\frac{\min(q,2)}{z}.
}
\]

For every real \(r>0\),
\[
\boxed{
\mathbb E[Z^r]<\infty
\quad\Longleftrightarrow\quad
r<\min(q,2).
}
\]
When this condition holds,
\[
\boxed{
\mathbb E[Z^r]
=
\theta^{r/2}
\Gamma\!\left(1-\frac r2\right)
\frac{q}{q-r}.
}
\]
Thus the variance is infinite for every finite \(q\). The first moment exists exactly when \(q>1\), agreeing with the mean-based regression domain used in the source.

The parameter \(q\) genuinely changes the power-law tail exponent only below \(2\). Once \(q>2\), the inverse-Rayleigh parent imposes the exponent \(2\), and \(q\) changes only the leading constant
\[
\frac{q\theta}{q-2}.
\]
As \(q\to\infty\), that constant tends to \(\theta\), which matches convergence back to the inverse-Rayleigh parent.

## Assumptions and scope
The parameter domain is
\[
\theta>0,\qquad q>0.
\]
The inverse-Rayleigh parameterization is the one used by the source, for which
\[
F_X(x)=e^{-\theta/x^2},
\qquad x>0.
\]

The result sharpens the source's regular-variation statement by identifying the exact index and the critical slowly varying factor. It does not dispute that the SIR law is heavy-tailed for every \(q>0\); all three regimes are polynomially heavy.

The moment theorem covers arbitrary positive real orders. At \(r=2\), the inverse-Rayleigh factor already diverges, so no value of \(q\) produces a finite variance.

## Proof
Conditioning on \(Y\) gives
\[
\overline F_Z(z)
=
q\int_0^1
y^{q-1}
\left[
1-e^{-\theta/(z^2y^2)}
\right]dy.
\]
With
\[
a=\theta/z^2,
\qquad
t=a/y^2,
\]
one obtains
\[
\overline F_Z(z)
=
s\,a^s I_s(a),
\qquad
s=\frac q2,
\]
where
\[
I_s(a)
=
\int_a^\infty
(1-e^{-t})t^{-s-1}\,dt.
\]

For \(0<s<1\), integration by parts gives
\[
I_s(0)
=
\frac{\Gamma(1-s)}{s},
\]
so
\[
\overline F_Z(z)
\sim
\Gamma(1-s)a^s.
\]

For \(s=1\), the integrand is
\[
(1-e^{-t})t^{-2}
=
t^{-1}+O(1)
\]
near zero. Therefore
\[
I_1(a)
=
\log(1/a)+O(1),
\]
which gives the critical logarithmic equivalent.

For \(s>1\),
\[
(1-e^{-t})t^{-s-1}
=
t^{-s}(1+o(1))
\]
near zero, and hence
\[
I_s(a)
\sim
\frac{a^{1-s}}{s-1}.
\]
Thus
\[
s a^s I_s(a)
\sim
\frac{s}{s-1}a
=
\frac{q}{q-2}\frac{\theta}{z^2}.
\]

These three equivalents establish the regular-variation index and the critical logarithmic factor.

The density equivalents follow by the source's exact density formula, or equivalently by differentiating the regularly varying survival with its explicit slowly varying factor. Division by the survival yields
\[
h_Z(z)\sim\frac{\min(q,2)}{z}.
\]

For the moments, independence gives
\[
\mathbb E[Z^r]
=
\mathbb E[X^r]\,
\mathbb E[Y^{-r}]
\]
whenever both factors are finite. Direct integration gives
\[
\mathbb E[X^r]
=
\theta^{r/2}
\Gamma\!\left(1-\frac r2\right)
\quad\text{for }r<2,
\]
and divergence for \(r\ge2\). Also,
\[
\mathbb E[Y^{-r}]
=
q\int_0^1 y^{q-r-1}\,dy
=
\frac q{q-r}
\quad\text{for }r<q,
\]
and it diverges for \(r\ge q\). This proves the sharp moment condition and formula.

## Verification
The accompanying checker evaluates the exact survival integral and the exact source density at representative parameter values
\[
q=1,\qquad q=2,\qquad q=3.
\]
It verifies convergence of the normalized survival and density to the constants stated above and verifies
\[
z\,h_Z(z)\to\min(q,2).
\]

It also compares direct numerical integration of fractional moments with the closed formula for orders strictly below the threshold. These calculations are consistency checks only. The phase classification and moment-existence theorem are proved analytically.

## Relationship to prior work
Gómez et al. introduce the SIR distribution, derive its density and CDF, prove convergence to the inverse-Rayleigh parent as \(q\to\infty\), give the first moment for \(q>1\), and state that the survival is regularly varying. Their Proposition 8 writes the regular-variation ratio as a factor \(t^{-q}\) times a quotient of incomplete integrals. The behavior of that quotient changes at \(q=2\): it tends to \(1\) only in the subcritical regime, contributes an additional power when \(q>2\), and produces a logarithmic slowly varying factor at \(q=2\). The theorem above resolves those regimes explicitly.

Rivera et al. study a different scale-mixture/slashed Rayleigh construction. In that model the Rayleigh parent has all positive moments, and the slash component alone creates a cutoff \(r<q\). That does not cover SIR, where the inverse-Rayleigh parent itself has the competing cutoff \(r<2\). The competition between the two mechanisms is exactly what creates the threshold \(\min(q,2)\) and the critical logarithm.

Focused searches using the SIR name and DOI, inverse-Rayleigh tail terminology, moment-threshold aliases, regular-variation index, and the critical value \(q=2\) did not locate the three-regime theorem stated here.

## Limitations
The theorem concerns first-order tail equivalents and positive moments. No second-order regular-variation expansion is claimed.

The source's Proposition 8 correctly identifies the SIR family as regularly varying and therefore heavy-tailed; the refinement here is the exact index, critical logarithmic factor, and consequences for moments and hazard.

The result does not reassess the source's EM algorithm, regression estimation, simulation study, or application fit.

## References
1. H. W. Gómez, D. I. Gallardo, M. Bourguignon, and O. Venegas, “EM algorithm in the slashed inverse Rayleigh regression model with an application,” AIMS Mathematics 11 (2026), 23262–23281. DOI: 10.3934/math.2026938.
2. P. A. Rivera, I. Barranco-Chamorro, D. I. Gallardo, and H. W. Gómez, “Scale Mixture of Rayleigh Distribution,” Mathematics 8 (2020), 1842. DOI: 10.3390/math8101842.
