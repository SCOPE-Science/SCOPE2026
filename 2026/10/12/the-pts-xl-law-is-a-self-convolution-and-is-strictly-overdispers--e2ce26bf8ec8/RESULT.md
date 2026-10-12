# The PTS-XL law is a self-convolution and is strictly overdispersed
## Finding
Let
\[
Y_1,Y_2\stackrel{\mathrm{iid}}{\sim}\mathrm{XLindley}(\theta),
\qquad
\theta>0,
\]
and let the proposed PTS-XL count be defined by
\[
N\mid(Y_1,Y_2)
\sim
\operatorname{Poisson}(Y_1+Y_2).
\]

Introduce conditionally independent counts
\[
N_i\mid Y_i\sim\operatorname{Poisson}(Y_i),
\qquad i=1,2.
\]
Conditional Poisson additivity gives
\[
N_1+N_2\mid(Y_1,Y_2)
\sim
\operatorname{Poisson}(Y_1+Y_2).
\]
Hence
\[
\boxed{
N\overset d=N_1+N_2.
}
\]

Each \(N_i\) is exactly the previously studied Poisson XLindley count model with the same parameter \(\theta\). Therefore
\[
\boxed{
\mathrm{PTS\!-\!XL}(\theta)
=
\mathrm{PXL}(\theta)*\mathrm{PXL}(\theta).
}
\]

The XLindley density used by the source is
\[
f_Y(y)
=
\frac{\theta^2}{(1+\theta)^2}
(2+\theta+y)e^{-\theta y},
\qquad y>0.
\]
For a Poisson mixture,
\[
G_{PXL}(z)
=
E\!\left[e^{(z-1)Y}\right].
\]
Direct integration gives
\[
G_{PXL}(z)
=
\frac{
\theta^2
[\theta^2+3\theta+3-(\theta+2)z]
}{
(1+\theta)^2(1+\theta-z)^2
}.
\]
Consequently
\[
\boxed{
G_{PTS}(z)=G_{PXL}(z)^2.
}
\]
Squaring the preceding expression gives
\[
G_{PTS}(z)
=
\frac{
\theta^4
[\theta^2+3\theta+3-(\theta+2)z]^2
}{
(1+\theta)^4(1+\theta-z)^4
},
\]
which is exactly the PGF displayed for PTS-XL in the source.

The convolution identity has an immediate dispersion consequence. If \(m_{PXL}\) and \(v_{PXL}\) denote the PXL mean and variance, then
\[
E[N]=2m_{PXL},
\qquad
\operatorname{Var}(N)=2v_{PXL},
\]
and therefore
\[
\boxed{
\frac{\operatorname{Var}(N)}{E[N]}
=
\frac{v_{PXL}}{m_{PXL}}.
}
\]
Thus the two-sum construction doubles absolute mean and variance but does not change the Fano factor relative to PXL at the same \(\theta\).

More strongly, PTS-XL is strictly overdispersed for every finite positive parameter. Put
\[
\Lambda=Y_1+Y_2.
\]
The conditional variance identity gives
\[
\operatorname{Var}(N)
=
E[\operatorname{Var}(N\mid\Lambda)]
+
\operatorname{Var}(E[N\mid\Lambda])
=
E[\Lambda]+\operatorname{Var}(\Lambda).
\]
Because the XLindley law is nondegenerate for every finite \(\theta>0\),
\[
\operatorname{Var}(\Lambda)>0.
\]
Hence
\[
\boxed{
\operatorname{Var}(N)>E[N]
\qquad
\text{for every finite }\theta>0.
}
\]

The same fact is visible directly in the source's dispersion-index formula:
\[
DI(\theta)
=
\frac{
\theta^5+5\theta^4+11\theta^3+14\theta^2+10\theta+2
}{
\theta(1+\theta)^2(\theta^2+2\theta+2)
}.
\]
Subtracting one and factoring yields
\[
\boxed{
DI(\theta)-1
=
\frac{
\theta^4+4\theta^3+8\theta^2+8\theta+2
}{
\theta(1+\theta)^2(\theta^2+2\theta+2)
}
>0.
}
\]

The source repeatedly describes the family as capable of modeling equidispersed count data because \(DI(\theta)\) approaches one as \(\theta\) becomes large. The equality
\[
DI(\theta)=1
\]
does not occur at any finite \(\theta>0\).

Furthermore, the approach to one occurs only at a degenerate boundary. The source mean is
\[
E[N]
=
\frac{2(\theta^2+2\theta+2)}
{\theta(1+\theta)^2},
\]
so
\[
E[N]\to0
\qquad(\theta\to\infty).
\]
Indeed,
\[
DI(\theta)-1\sim\frac1\theta,
\qquad
E[N]\sim\frac2\theta.
\]
Thus the equidispersed limit is accompanied by concentration at zero rather than by a nondegenerate finite-mean Poisson regime.

## Assumptions and scope
The parameter domain is
\[
\theta>0.
\]

The term PXL denotes the Poisson XLindley model obtained by mixing a Poisson rate with one XLindley random variable having the same density and parameterization used in the 2026 source.

The strict-overdispersion conclusion concerns exact population dispersion. A finite observed dataset can of course have an empirical variance-to-mean ratio near one.

The finding does not claim that PTS-XL is redundant for every inferential purpose. Its count distribution is a two-fold convolution of PXL, which changes the count law even though it preserves the Fano factor at fixed \(\theta\).

## Proof
For fixed \(Y_1=y_1\) and \(Y_2=y_2\), independent Poisson variables with means \(y_1\) and \(y_2\) satisfy
\[
N_1+N_2
\sim
\operatorname{Poisson}(y_1+y_2).
\]
Mixing over the iid XLindley variables proves
\[
N\overset d=N_1+N_2.
\]

For the PGF, set
\[
s=1-z.
\]
Then
\[
G_{PXL}(z)
=
\frac{\theta^2}{(1+\theta)^2}
\int_0^\infty
(2+\theta+y)e^{-(\theta+s)y}\,dy.
\]
Using
\[
\int_0^\infty e^{-ay}\,dy=\frac1a,
\qquad
\int_0^\infty ye^{-ay}\,dy=\frac1{a^2},
\]
one obtains
\[
G_{PXL}(z)
=
\frac{\theta^2}{(1+\theta)^2}
\left[
\frac{2+\theta}{1+\theta-z}
+
\frac1{(1+\theta-z)^2}
\right],
\]
which simplifies to the expression in the finding. Independence gives the square relation.

For dispersion, the law of total variance gives
\[
\operatorname{Var}(N)
=
E[\Lambda]+\operatorname{Var}(\Lambda)
\]
for every mixed Poisson law. Since
\[
\Lambda=Y_1+Y_2
\]
is nondegenerate,
\[
\operatorname{Var}(\Lambda)>0.
\]
This proves strict overdispersion independently of the source's algebraic moment formulas.

Finally, direct subtraction of one from the displayed \(DI(\theta)\) gives a rational function whose numerator
\[
\theta^4+4\theta^3+8\theta^2+8\theta+2
\]
has strictly positive coefficients. The asymptotic statements follow by comparing leading powers of \(\theta\).

## Verification
The bundled checker performs four independent checks.

First, it symbolically derives the PXL PGF from the XLindley mixing density and verifies that its square equals the PTS-XL PGF printed by the source.

Second, it verifies for several positive parameter values and count values that the closed-form PTS-XL PMF equals the discrete convolution of two PXL PMFs.

Third, it symbolically factors
\[
DI(\theta)-1
\]
and checks the positive numerator stated above.

Fourth, it verifies the leading large-\(\theta\) asymptotics for the mean and dispersion gap.

The computations are reproducibility aids. The convolution and strict-overdispersion statements are proved analytically.

## Relationship to prior work
The primary source explicitly constructs the TS-XL mixing variable as the sum of two iid XLindley variables and later presents a PTS-XL PGF that is a perfect square. It does not identify the resulting count law as the convolution square of the earlier PXL model.

The 2022 PXL paper studies the one-XLindley Poisson mixture. Its model is precisely the component count appearing in the convolution representation above. The present statement compares the two constructions at distribution level and shows that the PTS-XL Fano factor is inherited unchanged from PXL at the same parameter.

General mixed-Poisson theory gives
\[
\operatorname{Var}(N)=E[\Lambda]+\operatorname{Var}(\Lambda).
\]
That general identity implies strict overdispersion for any nondegenerate mixing law, but it does not by itself identify the PTS-XL self-convolution or the exact equivalence to two iid PXL counts.

Focused searches using the exact source DOI, PTS-XL and PXL names, Poisson-mixture additivity, self-convolution terminology, PGF-square terminology, and equidispersion aliases did not locate a published statement of this combined structural result.

## Limitations
The result does not compare likelihood efficiency or predictive performance of PTS-XL and PXL after their parameters are separately fitted.

The convolution identity uses equal XLindley parameters, exactly as in the source definition.

Equidispersion may be used informally for a dispersion index numerically close to one; the correction here concerns exact probabilistic classification at finite parameter values.

A recent or unindexed source may contain the same structural observation outside the material examined.

## References
1. H. Haj Ahmad and M. M. El-Awady, “The Poisson two-sum XLindley distribution: Statistical properties, estimation, regression modeling, and applications,” AIMS Mathematics 11 (2026), 28121–28160. DOI: 10.3934/math.20261122.
2. M. Ahsan-ul-Haq, A. Al-Bossly, M. El-Morshedy, and M. S. Eliwa, “Poisson XLindley Distribution for Count Data: Statistical and Reliability Properties with Estimation Techniques and Inference,” Computational Intelligence and Neuroscience 2022 (2022), Article 6503670. DOI: 10.1155/2022/6503670.
3. D. Karlis and E. Xekalaki, “Mixed Poisson Distributions,” International Statistical Review 73 (2005), 35–58. DOI: 10.1111/j.1751-5823.2005.tb00250.x.
