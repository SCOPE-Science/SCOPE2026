# The \(q\)-deformed Lindley quantile omits the scale parameter
## Finding
For the \(q\)-deformed Lindley distribution of El-Awady, Haj Ahmad, Rabaiah, and Ramadan, the published cumulative distribution function is
\[
F(x;\theta,q)
=
1-
\left[
1+\frac{(2-q)\theta x}{A_\theta}
\right]
\{\exp_q(-\theta x)\}^{2-q},
\]
where
\[
\boxed{
A_\theta=1+(3-2q)\theta.
}
\]

Theorem 1 then gives a Lambert–Tsallis quantile formula, but defines the constant as
\[
\boxed{
A_0=1+(3-2q)=4-2q,
}
\]
with no factor of \(\theta\).

That omission changes the function being inverted. Let
\[
b=(2-q)\theta.
\]
The displayed theorem is the inverse of
\[
\boxed{
\widetilde F(x)
=
1-
\left(
1+\frac{bx}{A_0}
\right)
\{\exp_q(-\theta x)\}^{2-q},
}
\]
rather than the source's stated CDF \(F\).

Consequently, if \(Q_{\rm pub}(u)\) is the positive value returned by the published Eq. (9), then
\[
\boxed{
F(Q_{\rm pub}(u);\theta,q)-u
=
bQ_{\rm pub}(u)
\{\exp_q(-\theta Q_{\rm pub}(u))\}^{2-q}
\left(
\frac1{A_0}-\frac1{A_\theta}
\right).
}
\]
Because
\[
A_\theta-A_0=(3-2q)(\theta-1)
\]
and the admissible model has
\[
q<\frac32,
\]
the residual is nonzero for every interior quantile whenever
\[
\theta\ne1.
\]
Its sign is the sign of \(\theta-1\).

The algebraic correction is to replace \(A_0\) everywhere in Eq. (9) by
\[
A_\theta=1+(3-2q)\theta.
\]
Put
\[
q'=\frac1{2-q},
\qquad
\kappa_\theta=1+(1-q')A_\theta.
\]
Whenever
\[
\kappa_\theta>0,
\]
the corrected Lambert–Tsallis expression is
\[
\boxed{
Q(u;\theta,q)
=
-\frac{
A_\theta
+
\kappa_\theta
W_{q'}\!\left(
-\frac{A_\theta(1-u)}
{\kappa_\theta\exp_{q'}(A_\theta)}
\right)
}{
(2-q)\theta
},
}
\]
using the real lower branch that yields \(Q(u)>0\).

There is a second domain issue. A direct simplification gives
\[
\boxed{
\kappa_\theta
=
\frac{3-2q}{2-q}
\{1-(q-1)\theta\}.
}
\]
Hence for
\[
q<1,
\]
the corrected shifted formula is real throughout the admissible parameter space, but for
\[
1<q<\frac32
\]
it requires
\[
\boxed{
\theta<\frac1{q-1}.
}
\]
At equality the displayed shifted formula divides by zero, and above it \(\exp_{q'}(A_\theta)\) is outside the real domain specified by the paper's own \(q\)-exponential definition. The distribution itself remains well defined; numerical inversion of its correct CDF is still available.

The source states that its Monte Carlo study generates observations by inverse transformation using Eq. (9). Its four parameter pairs are
\[
(1.5,1.1),\qquad
(0.75,0.85),\qquad
(0.4,1.4),\qquad
(0.15,-0.5),
\]
where each ordered pair is \((\theta,q)\). None has \(\theta=1\).

For the median \(u=1/2\), literal inversion of Eq. (9) gives the following mismatch with the true CDF:
\[
\begin{array}{c|c|c|c}
(\theta,q) & Q_{\rm pub}(1/2) & F(Q_{\rm pub}(1/2)) & Q(1/2)\\
\hline
(1.5,1.1) & 0.9931638956\ldots & 0.5388083965\ldots & 0.8914035861\ldots\\
(0.75,0.85) & 1.1355965578\ldots & 0.4754264357\ldots & 1.2037338350\ldots\\
(0.4,1.4) & 30.1776695297\ldots & 0.4523408680\ldots & 38.2575025743\ldots\\
(0.15,-0.5) & 1.7178514545\ldots & 0.3787326582\ldots & 2.1487250311\ldots
\end{array}
\]

Thus the quantile theorem is wrong as printed, and the simulation procedure described in the paper does not generate the stated \(q\)-deformed Lindley law if Eq. (9) is implemented literally.

## Assumptions and scope
The source defines
\[
\exp_q(y)
=
\{1+(1-q)y\}^{1/(1-q)}
\]
on its real positive-base domain.

The admissible \(q\)-deformed Lindley parameter region is
\[
\theta>0,
\]
together with
\[
q<1
\]
for bounded support or
\[
1<q<\frac32
\]
for unbounded support.

The finding concerns the published quantile theorem and the inverse-transform simulation procedure that explicitly cites that theorem. It does not assert that unpublished or unreported simulation code necessarily used the printed constant \(A_0\). If the authors silently used \(A_\theta\) in software, their numerical tables may be unaffected even though the reproducible mathematical specification is wrong.

The maximum-likelihood formula based directly on the PDF is not changed by this correction. CDF-based procedures are valid when they use the stated CDF itself rather than the faulty quantile formula.

## Proof
Set
\[
b=(2-q)\theta,
\qquad
q'=\frac1{2-q},
\qquad
z=-bx.
\]
The elementary \(q\)-exponential identity used by the source gives
\[
\{\exp_q(-\theta x)\}^{2-q}
=
\exp_{q'}(z).
\]

The correct CDF equation
\[
F(x;\theta,q)=u
\]
is equivalent to
\[
1-u
=
\left(
1-\frac{z}{A_\theta}
\right)
\exp_{q'}(z).
\]
Therefore
\[
\boxed{
(z-A_\theta)\exp_{q'}(z)
=
-A_\theta(1-u).
}
\]

By contrast, the paper's Eq. (9) is written with
\[
A=A_0=1+(3-2q).
\]
Reversing the same Lambert–Tsallis algebra therefore gives
\[
(z-A_0)\exp_{q'}(z)
=
-A_0(1-u),
\]
which is exactly
\[
\widetilde F(x)=u.
\]

Subtract the two CDFs:
\[
F(x;\theta,q)-\widetilde F(x)
=
bx
\{\exp_q(-\theta x)\}^{2-q}
\left(
\frac1{A_0}-\frac1{A_\theta}
\right).
\]
At
\[
x=Q_{\rm pub}(u),
\]
one has
\[
\widetilde F(Q_{\rm pub}(u))=u,
\]
so the residual identity follows.

For the corrected closed form, set
\[
\kappa_\theta
=
1+(1-q')A_\theta
\]
and
\[
w=\frac{z-A_\theta}{\kappa_\theta}.
\]
When
\[
\kappa_\theta>0,
\]
the \(q'\)-exponential product identity yields
\[
\exp_{q'}(z)
=
\exp_{q'}(A_\theta)\exp_{q'}(w).
\]
Hence
\[
w\exp_{q'}(w)
=
-\frac{A_\theta(1-u)}
{\kappa_\theta\exp_{q'}(A_\theta)}.
\]
Applying \(W_{q'}\) and then recovering \(z\) gives the corrected formula.

Finally,
\[
1-q'
=
\frac{1-q}{2-q},
\]
so
\[
\kappa_\theta
=
1+
\frac{1-q}{2-q}
\{1+(3-2q)\theta\}
=
\frac{3-2q}{2-q}
\{1-(q-1)\theta\}.
\]
This proves the additional domain restriction.

## Verification
The accompanying checker evaluates the source CDF, the auxiliary CDF actually inverted by Eq. (9), and the corrected CDF inverse at high precision.

It implements the real lower branch of the Lambert–Tsallis equation
\[
w\exp_{q'}(w)=\xi
\]
by monotone bisection on the lower branch and verifies that the published Eq. (9) agrees with \(\widetilde F^{-1}\), not with \(F^{-1}\).

For all four Monte Carlo parameter pairs printed in the source, it checks the median discrepancies listed above and verifies the exact residual identity.

It also verifies that replacing \(A_0\) by \(A_\theta\) restores
\[
F(Q(1/2);\theta,q)=\frac12
\]
for the four simulation designs.

Finally, it tests the legitimate unbounded-support parameter pair
\[
(q,\theta)=(1.4,3).
\]
The distribution is admissible because
\[
1<q<\frac32,
\]
but
\[
\kappa_\theta<0,
\]
so the corrected shifted Lambert–Tsallis representation is not real under the source's own \(q\)-exponential convention.

## Relationship to prior work
The primary source gives the correct CDF in Proposition 2, including the denominator
\[
A_\theta=1+(3-2q)\theta.
\]
Theorem 1 then defines
\[
A=1+(3-2q)
\]
and carries that different quantity into its Lambert–Tsallis quantile. This is not an equivalent reparameterization: it removes the scale parameter from a term where the CDF requires it.

The same article later states that Monte Carlo observations are generated by inverse transformation using Eq. (9), with four parameter pairs whose \(\theta\)-values are
\[
1.5,\quad0.75,\quad0.4,\quad0.15.
\]
Thus every reported simulation design is outside the only slice
\[
\theta=1
\]
on which the printed quantile constant agrees with the stated CDF.

Da Silva and Ramos introduced the Lambert–Tsallis \(W_q\) function as the inverse relation for
\[
w\exp_q(w).
\]
That general theory supplies the inversion device but does not imply the incorrect choice \(A_0\) or cover the source-specific quantile correction.

Focused searches using the exact DOI, model name, quantile terminology, the missing-\(\theta\) constant, CDF-inversion aliases, and simulation language did not locate a corrigendum or an independent source already identifying this correction.

## Limitations
The finding does not reconstruct the authors' private simulation code. It proves that the published algorithm is wrong if Eq. (9) is implemented literally.

For
\[
1<q<\frac32,
\qquad
\theta\ge\frac1{q-1},
\]
the distribution remains valid but the corrected shifted Lambert–Tsallis representation above is not a real formula under the source's convention. Numerical inversion of the monotone CDF remains available.

The raw-moment formulas, likelihood calculations, and empirical data fits are not reassessed here except where their interpretation depends on Monte Carlo samples described as being generated from Eq. (9).

## References
1. M. M. El-Awady, H. Haj Ahmad, Y. Rabaiah, and A. T. Ramadan, “The \(q\)-Deformed Lindley Distribution: Properties, Statistical Inference, and Applications,” Mathematics 14 (2026), 1364. DOI: 10.3390/math14081364.
2. G. B. da Silva and R. V. Ramos, “The Lambert–Tsallis \(W_q\) function,” Physica A 525 (2019), 164–170. DOI: 10.1016/j.physa.2019.03.046.
