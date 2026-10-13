# The UMg mean-residual-life series diverges for every parameter
## Finding
Let \(Y\) have the 2026 unit Mgamma distribution with parameter
\[
\theta>0,
\qquad
0<Y<1.
\]
The model is obtained from a positive Mgamma variable \(X\) by
\[
Y=\frac{X}{1+X}.
\]
Put
\[
\xi=\frac{y}{1-y},
\qquad
0<y<1.
\]
The Mgamma survival function appearing in the source can be written as
\[
S_X(u)
=
\left(
1+\theta u+
\frac{\theta^2u^2}{2(1+\theta)}
\right)e^{-\theta u}.
\]

The UMg mean residual life is
\[
m_Y(y)
=
\frac{I(y)}{S_Y(y)},
\qquad
I(y)=\int_y^1S_Y(t)\,dt.
\]
After the transformation
\[
u=\frac{t}{1-t},
\]
one has
\[
I(y)
=
\int_\xi^\infty
\left(
1+\theta u+
\frac{\theta^2u^2}{2(1+\theta)}
\right)
\frac{e^{-\theta u}}{(1+u)^2}\,du.
\]

The source derives its Eq. (3.5) by substituting
\[
\frac1{(1+u)^2}
=
\sum_{k=0}^\infty
(k+1)(-1)^ku^k,
\]
while explicitly noting that this expansion is valid for
\[
|u|<1.
\]
The integration interval, however, extends from \(\xi\) to infinity.

The resulting series is not just unsupported by that local expansion. Its terms cannot converge to zero. In the source's final incomplete-gamma notation, the \(k\)-th signed numerator term is
\[
a_k
=
\frac{(k+1)(-1)^k}{\theta^{k+1}}
\left[
\Gamma(k+1,\theta\xi)
+
\Gamma(k+2,\theta\xi)
+
\frac{\Gamma(k+3,\theta\xi)}{2(1+\theta)}
\right].
\]
For every fixed
\[
\theta>0,\qquad \xi>0,
\]
one has
\[
\boxed{|a_k|\longrightarrow\infty.}
\]
Therefore the series in Eq. (3.5) diverges for every admissible parameter and every interior threshold.

There is nevertheless a short exact replacement. Define the exponential integral
\[
E_1(z)
=
\int_z^\infty \frac{e^{-t}}{t}\,dt,
\qquad z>0.
\]
Then
\[
\boxed{
I(y)
=
\frac{e^{-\theta\xi}}{2(1+\theta)}
\left[
\theta+(2-\theta^2)(1-y)
\right]
+
\frac{\theta^3e^\theta}{2(1+\theta)}
E_1\!\left(\frac{\theta}{1-y}\right).
}
\]
Since
\[
S_Y(y)=S_X(\xi)
=
\left(
1+\theta\xi+
\frac{\theta^2\xi^2}{2(1+\theta)}
\right)e^{-\theta\xi},
\]
the mean residual life is exactly
\[
\boxed{
m_Y(y)
=
\frac{
\dfrac{e^{-\theta\xi}}{2(1+\theta)}
\left[
\theta+(2-\theta^2)(1-y)
\right]
+
\dfrac{\theta^3e^\theta}{2(1+\theta)}
E_1\!\left(\dfrac{\theta}{1-y}\right)
}{
\left(
1+\theta\xi+
\dfrac{\theta^2\xi^2}{2(1+\theta)}
\right)e^{-\theta\xi}
}.
}
\]

At
\[
(\theta,y)=(1,0.4),
\]
direct numerical integration and the exact formula agree at
\[
\boxed{
m_Y(0.4)=0.2833221886367211247\ldots.
}
\]
By contrast, the first eight signed numerator terms of the source series have magnitudes approximately
\[
1.85,\ 8.58,\ 41.7,\ 240,\ 1620,\ 12600,\ 110880,\ 1088640.
\]
Thus the source series cannot provide the numerical evaluation claimed for it.

## Assumptions and scope
The parameter and threshold domains are
\[
\theta>0,
\qquad
0<y<1.
\]
The result concerns the UMg mean-residual-life representation in Eq. (3.5). It does not challenge the defining transformation, PDF, CDF, or the MRL definition in Eq. (3.4).

The upper incomplete gamma function is
\[
\Gamma(s,z)
=
\int_z^\infty t^{s-1}e^{-t}\,dt.
\]
The exponential integral \(E_1\) is the standard positive-real function defined above.

The divergence statement concerns the infinite series actually obtained after the source's termwise integration. It is stronger than observing that the geometric-type expansion was used outside its disk of convergence.

No claim is made here about the source's stress-strength reliability, extropy, estimation procedures, or empirical fits.

## Proof
Start from
\[
I(y)
=
\int_\xi^\infty
\left(
1+\theta u+
\frac{\theta^2u^2}{2(1+\theta)}
\right)
\frac{e^{-\theta u}}{(1+u)^2}\,du.
\]

First, consider the source series. Its absolute \(k\)-th term is at least
\[
\frac{k+1}{2(1+\theta)\theta^{k+1}}
\Gamma(k+3,\theta\xi).
\]
For all sufficiently large \(k\),
\[
k+2>\theta\xi.
\]
Therefore
\[
\Gamma(k+3,\theta\xi)
=
\int_{\theta\xi}^{\infty}
t^{k+2}e^{-t}\,dt
\ge
\int_{k+2}^{k+3}
t^{k+2}e^{-t}\,dt.
\]
On this unit interval,
\[
t^{k+2}\ge(k+2)^{k+2}
\]
and
\[
e^{-t}\ge e^{-(k+3)}.
\]
Hence
\[
\Gamma(k+3,\theta\xi)
\ge
(k+2)^{k+2}e^{-(k+3)}.
\]
It follows that
\[
|a_k|
\ge
\frac{k+1}{2(1+\theta)\theta^{k+1}}
(k+2)^{k+2}e^{-(k+3)},
\]
whose logarithm grows like
\[
k\log k-k\log\theta-k.
\]
Thus
\[
|a_k|\to\infty.
\]
The term test proves divergence for every admissible \(\theta\) and \(y\).

For the exact replacement, put
\[
A=\frac{\theta^2}{2(1+\theta)},
\qquad
B=\frac{\theta}{1+\theta},
\qquad
C=\frac{2-\theta^2}{2(1+\theta)}.
\]
A direct algebraic decomposition gives
\[
\frac{
1+\theta u+
\dfrac{\theta^2u^2}{2(1+\theta)}
}{
(1+u)^2
}
=
A+\frac{B}{1+u}+\frac{C}{(1+u)^2}.
\]

The three needed integrals are
\[
\int_\xi^\infty e^{-\theta u}\,du
=
\frac{e^{-\theta\xi}}{\theta},
\]
\[
\int_\xi^\infty
\frac{e^{-\theta u}}{1+u}\,du
=
e^\theta E_1\!\big(\theta(1+\xi)\big),
\]
and, by differentiating \(e^{-\theta u}/(1+u)\),
\[
\int_\xi^\infty
\frac{e^{-\theta u}}{(1+u)^2}\,du
=
\frac{e^{-\theta\xi}}{1+\xi}
-
\theta e^\theta
E_1\!\big(\theta(1+\xi)\big).
\]

Substitution yields
\[
I(y)
=
\frac{\theta e^{-\theta\xi}}{2(1+\theta)}
+
\frac{(2-\theta^2)e^{-\theta\xi}}{2(1+\theta)(1+\xi)}
+
\frac{\theta^3e^\theta}{2(1+\theta)}
E_1\!\big(\theta(1+\xi)\big).
\]
Finally,
\[
\frac1{1+\xi}=1-y
\]
and
\[
\theta(1+\xi)=\frac{\theta}{1-y},
\]
which gives the stated closed form.

## Verification
The accompanying checker evaluates the MRL numerator in three independent ways:

1. direct quadrature of the transformed defining integral;
2. the exact \(E_1\)-based formula derived above;
3. the terms of the source's Eq. (3.5).

For multiple parameter-threshold pairs, direct quadrature and the exact formula agree to high precision.

At
\[
(\theta,y)=(1,0.4),
\]
both valid methods give
\[
m_Y(y)
=
0.2833221886367211246550\ldots.
\]

The checker also evaluates source-series terms for several admissible pairs and confirms their rapidly increasing magnitude. These finite evaluations illustrate the proved divergence; the proof itself is the term-test lower bound above.

## Relationship to prior work
Ruidas, Aljeddani, and Khan introduce the UMg distribution by applying the transformation
\[
Y=\frac{X}{1+X}
\]
to the Mgamma model. Their Section 3.4 defines the MRL correctly and transforms its numerator to an integral over
\[
[\xi,\infty).
\]
The next step inserts the Taylor series for \((1+u)^{-2}\), while explicitly recording its restriction \(|u|<1\), and then integrates that series over the entire unbounded interval. Equation (3.5) is the resulting incomplete-gamma series and is presented as an analytical form suitable for numerical evaluation.

The 2025 parent Mgamma paper derives a closed-form MRL for the untransformed positive variable. That formula does not provide the unit-transformed MRL above because the unit transformation introduces the factor
\[
(1+u)^{-2}
\]
inside the residual-life integral. The parent paper therefore does not cover this correction.

Focused searches using the exact DOI, UMg name, mean-residual-life terminology, incomplete-gamma series language, the \((1+u)^{-2}\) expansion, and exponential-integral formulations did not locate a published corrigendum or an equivalent UMg-specific correction.

## Limitations
The result corrects one reliability representation. It does not reassess every structural or inferential formula in the article.

The exact formula uses the standard special function \(E_1\), rather than elementary functions.

A very recent unindexed author correction could exist outside the records examined.

## References
1. M. K. Ruidas, S. M. Aljeddani, and M. I. Khan, “Modelling bounded data over interval (0, 1) using a novel unit Mgamma (UMg) distribution and its statistical properties,” AIMS Mathematics 11 (2026), 18746–18771. DOI: 10.3934/math.2026762.
2. M. I. Khan and M. K. Ruidas, “The Mgamma Distribution: Statistical Properties and Application to Real-Life Data,” European Journal of Pure and Applied Mathematics 18 (2025), Article 6653. DOI: 10.29020/nybg.ejpam.v18i4.6653.
