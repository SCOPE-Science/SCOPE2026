# A sign error invalidates the printed SCHI reliability and hazard formulas
## Finding
Let
\[
Z=\frac{X}{Y},
\]
where
\[
X\sim\mathrm{CHI}(\sigma,\alpha),
\qquad
Y\sim\mathrm{Beta}(q,1),
\]
independently, with
\[
\sigma>0,\qquad \alpha>0,\qquad q>0.
\]
Write
\[
a=\frac{\alpha}{2}
\]
and let
\[
G(u;a,1)
\]
denote the Gamma distribution function with shape \(a\) and rate \(1\).

The source's Proposition 2.4 gives
\[
F_Z(t)
=
G\!\left(\frac{t}{2\sigma};a,1\right)
-
\left(\frac{2\sigma}{t}\right)^q
\frac{\Gamma(a+q)}{\Gamma(a)}
G\!\left(\frac{t}{2\sigma};a+q,1\right).
\]
Hence its survival function must be
\[
\boxed{
S_Z(t)
=
1-
G\!\left(\frac{t}{2\sigma};a,1\right)
+
\left(\frac{2\sigma}{t}\right)^q
\frac{\Gamma(a+q)}{\Gamma(a)}
G\!\left(\frac{t}{2\sigma};a+q,1\right).
}
\]

Corollary 2.1 instead prints a minus sign before the second term. The hazard denominator repeats the same sign error.

Using the source's density,
\[
f_Z(t)
=
q(2\sigma)^q
\frac{\Gamma(a+q)}{\Gamma(a)}
t^{-q-1}
G\!\left(\frac{t}{2\sigma};a+q,1\right),
\]
the corrected hazard is
\[
\boxed{
h_Z(t)
=
\frac{
q(2\sigma)^q t^{-1}\Gamma(a+q)
G\!\left(\frac{t}{2\sigma};a+q,1\right)
}{
t^q\Gamma(a)
\left[
1-G\!\left(\frac{t}{2\sigma};a,1\right)
\right]
+
(2\sigma)^q\Gamma(a+q)
G\!\left(\frac{t}{2\sigma};a+q,1\right)
}.
}
\]

The sign error is mathematically substantive. Define
\[
C=(2\sigma)^q\frac{\Gamma(a+q)}{\Gamma(a)}.
\]
Then
\[
\boxed{
S_Z(t)\sim Ct^{-q},
\qquad
h_Z(t)\sim\frac{q}{t}
\qquad(t\to\infty).
}
\]
By contrast, the printed formulas satisfy
\[
S_{\mathrm{printed}}(t)\sim-Ct^{-q}
\]
and
\[
h_{\mathrm{printed}}(t)\sim-\frac{q}{t},
\]
so they eventually become negative and cannot be a survival function or hazard.

For the article's parameter choice
\[
(\sigma,\alpha,q)=(1,3,1),
\]
at \(t=8\) the corrected survival is
\[
\boxed{
S_Z(8)=0.3624233453475855\ldots,
}
\]
which agrees with the \(0.362\) value in Table 1. The printed formula instead gives
\[
S_{\mathrm{printed}}(8)
=
-0.270399933969123\ldots.
\]
At the same point,
\[
h_Z(8)=0.109130538816041\ldots,
\]
whereas the printed hazard formula gives
\[
h_{\mathrm{printed}}(8)
=
-0.146270209377384\ldots.
\]

The printed survival crosses zero at
\[
t=3.48777992428691\ldots
\]
for this example. Therefore the positive black hazard curve shown over the interval extending to \(t=20\) in Figure 2 cannot be generated from Corollary 2.1 as printed.

## Assumptions and scope
The parameters satisfy
\[
\sigma,\alpha,q>0
\]
and
\[
t>0.
\]

The result corrects the survival and hazard formulas in Corollary 2.1. The density in Proposition 2.1 and the CDF in Proposition 2.4 are used as stated.

The tail-probability values in Table 1 are consistent with the corrected survival formula. The result therefore does not claim that the table itself is wrong.

The heavy-tail conclusion of Proposition 2.5 also remains true, but its proof must use the corrected positive survival function.

## Proof
Starting from the published CDF,
\[
F_Z(t)
=
G_a(t)-R_q(t),
\]
where
\[
G_a(t)
=
G\!\left(\frac{t}{2\sigma};a,1\right)
\]
and
\[
R_q(t)
=
\left(\frac{2\sigma}{t}\right)^q
\frac{\Gamma(a+q)}{\Gamma(a)}
G\!\left(\frac{t}{2\sigma};a+q,1\right),
\]
one obtains
\[
1-F_Z(t)=1-G_a(t)+R_q(t).
\]
Thus the plus sign is forced directly by the source's own CDF.

There is also an independent derivation from the stochastic representation. Conditional on \(X=x\),
\[
\Pr(Z>t\mid X=x)
=
\Pr\!\left(Y<\frac{x}{t}\right).
\]
Since \(Y\sim\mathrm{Beta}(q,1)\),
\[
\Pr(Y<u)=u^q
\qquad(0\le u\le1).
\]
Therefore
\[
\Pr(Z>t)
=
\Pr(X>t)
+
t^{-q}\operatorname{E}
\left[
X^q\mathbf 1_{\{X\le t\}}
\right].
\]
For the Gamma-form \(X\),
\[
\Pr(X>t)
=
1-G\!\left(\frac{t}{2\sigma};a,1\right)
\]
and
\[
\operatorname{E}
\left[
X^q\mathbf 1_{\{X\le t\}}
\right]
=
(2\sigma)^q
\frac{\Gamma(a+q)}{\Gamma(a)}
G\!\left(\frac{t}{2\sigma};a+q,1\right),
\]
which reproduces the corrected survival formula exactly.

Since the Gamma upper tail is exponentially small while
\[
G\!\left(\frac{t}{2\sigma};a+q,1\right)\to1,
\]
the corrected survival obeys
\[
S_Z(t)\sim Ct^{-q}.
\]
The source density obeys
\[
f_Z(t)\sim qCt^{-q-1}.
\]
Dividing gives
\[
h_Z(t)\sim q/t.
\]

Replacing the required plus sign by the printed minus sign reverses the dominant polynomial term, yielding the negative asymptotics stated above.

## Verification
The accompanying checker evaluates the published CDF, density, the printed Corollary 2.1 formulas, and the corrected formulas.

It verifies numerically that
\[
1-F_Z(t)=S_Z(t)
\]
and that numerical differentiation of the published CDF agrees with the published density.

For the three \(q\)-values in Table 1, the checker reproduces all nine displayed tail probabilities after rounding to three decimals using the corrected survival formula.

For
\[
(\sigma,\alpha,q)=(1,3,1),
\]
it confirms the sign change of the printed survival, the negative printed hazard at \(t=8\), and the positive corrected values stated above.

It also checks the asymptotic ratios
\[
\frac{t^qS_Z(t)}{C}\to1
\]
and
\[
\frac{t\,h_Z(t)}{q}\to1.
\]

## Relationship to prior work
The primary article introduces the SCHI model through the quotient
\[
Z=X/Y
\]
and gives its density, CDF, reliability function, hazard, heavy-tail property, moments, and an applied wind-speed analysis.

The correction is internal to those displayed formulas: Proposition 2.4 contains a negative correction term in the CDF, so the complement must contain the corresponding positive term. The quotient representation independently gives the same sign.

The article's Table 1 is consistent with the corrected survival formula, while the printed Corollary 2.1 is not. Figure 2 likewise shows a positive hazard throughout its displayed range, whereas the printed hazard becomes negative inside that range for the black parameter setting.

Targeted searches using the DOI, model name, reliability and hazard terminology, the corollary number, and correction terminology did not locate a published correction or an equivalent model-specific repair.

## Limitations
The result corrects the printed reliability and hazard formulas and the tail argument that depends on them. It does not reassess the EM estimation procedure or the fitted wind-speed model.

The table and plotted hazard appear consistent with a corrected implementation, but the numerical code used by the authors is not available here, so no claim is made about the exact implementation.

A very recent or unindexed author correction could exist outside the sources examined.

## References
1. E. Martínez, E. Gómez-Déniz, D. I. Gallardo, O. Venegas, and H. W. Gómez, “The heavy-tailed chi-square model: properties, estimation and application to wind speed data,” AIMS Mathematics 10 (2025), 23849–23868. DOI: 10.3934/math.20251060.
