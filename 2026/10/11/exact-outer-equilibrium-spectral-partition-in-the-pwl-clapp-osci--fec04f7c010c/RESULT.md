# Exact outer-equilibrium spectral partition in the PWL Clapp oscillator
## Finding
Consider the normalized Case II piecewise-linear Clapp oscillator with accumulation elements scaled to unity, \(y_{11}=1\), \(y_{12}=1/10\), and outer transconductance slope \(a\in[-10,-1]\). The source states that the characteristic polynomial of either outer equilibrium is obtained from its origin polynomial by replacing the inner slope by the outer slope. Hence
\[
q_a(\lambda)=\lambda^4+\lambda^3+\left(3-\frac{a}{10}\right)\lambda^2+\left(a+\frac{21}{10}\right)\lambda-\frac{a}{10}.
\]

Define
\[
P(a)=192a^5-1380360a^4-11138818a^3-29595555a^2-44649090a-24931935.
\]
The discriminant of \(q_a\) is \(P(a)/50000\). In \([-10,-1]\), \(P\) has exactly two simple real zeros,
\[
\alpha=-4.8719648119545760497\ldots,
\qquad
\beta=-1.0090243447763414249\ldots.
\]
The unique imaginary-axis stability crossing in the same interval is
\[
a_H=\frac{-131-\sqrt{100321}}{220}
=-2.0351586587654359853\ldots.
\]
They satisfy \(\alpha<a_H<\beta\).

The complete local spectral partition at either outer equilibrium is:

- For \(-10\le a<\alpha\), two eigenvalues are positive real and the remaining two form a stable complex-conjugate pair.
- For \(\alpha<a<a_H\), there is one unstable complex-conjugate pair and one stable complex-conjugate pair.
- For \(a_H<a<\beta\), there are two stable complex-conjugate pairs.
- For \(\beta<a\le-1\), there is one stable complex-conjugate pair and two negative real eigenvalues.

At \(a=\alpha\), the two positive real eigenvalues coalesce before becoming an unstable complex pair. At \(a=a_H\), the crossing pair is purely imaginary with
\[
\omega^2=\frac{331-\sqrt{100321}}{220},
\qquad
\omega=0.2546396301335752701\ldots.
\]
At \(a=\beta\), a stable complex pair coalesces and becomes two negative real eigenvalues.

Thus the source's two-threshold summary near \(-2\) and \(-1\) omits the earlier real-to-complex transition near \(-4.872\). Its outer-equilibrium discussion can be sharpened to the exact four-regime partition above.

## Assumptions and scope
The statement concerns the normalized Case II model with \(y_{11}=1\), \(y_{12}=1/10\), and the outer-slope range \(a\in[-10,-1]\). The inner PWL slope determines the origin linearization but not the outer-equilibrium polynomial analyzed here. The two symmetry-related outer equilibria have identical spectra.

This is a local linear classification. It does not prove a nonlinear Hopf bifurcation, does not compute basin geometry, and does not identify the mechanism of the source's chaos-hyperchaos transition. The collisions at \(\alpha\) and \(\beta\) are spectral real/complex coalescences, not stability changes. Only \(a_H\) changes unstable dimension.

## Proof
Write
\[
q_a(\lambda)=\lambda^4+A_1\lambda^3+A_2\lambda^2+A_3\lambda+A_4,
\]
where
\[
A_1=1,\qquad
A_2=3-\frac{a}{10},\qquad
A_3=a+\frac{21}{10},\qquad
A_4=-\frac{a}{10}.
\]
On \([-10,-1]\), \(A_1,A_2,A_4>0\). The relevant Routh quantities are
\[
\Delta_2=A_1A_2-A_3=\frac{9-11a}{10}>0
\]
and
\[
\Delta_3=A_1A_2A_3-A_3^2-A_1^2A_4
=-\frac{110a^2+131a-189}{100}.
\]
The quadratic \(110a^2+131a-189\) has exactly one root in \([-10,-1]\), namely \(a_H\). Consequently the Routh first column has two sign changes for \(a<a_H\) and none for \(a>a_H\). Hence the unstable dimension is exactly two before \(a_H\) and zero after it.

At \(a=a_H\), substituting \(\lambda=i\omega\) into \(q_a\) gives \(\omega^2=A_3\), hence the displayed exact frequency. The remaining quadratic factor is strictly stable, so the crossing pair is simple.

To decide whether the two-dimensional blocks are real or complex, compute the quartic discriminant:
\[
\operatorname{disc}_\lambda(q_a)=\frac{P(a)}{50000}.
\]
A Sturm count gives exactly two zeros of \(P\) in \([-10,-1]\): the simple roots \(\alpha\) and \(\beta\) displayed above. There are therefore no other eigenvalue collisions in this parameter interval.

Exact Sturm counts at representative rational parameters give: at \(a=-10\), two positive real roots and no negative real roots; at \(a=-4\), no real roots; at \(a=-2\), no real roots; and at \(a=-1\), two negative real roots and no positive real roots. Combining these real-root counts with the Routh unstable dimensions, and using the absence of any other discriminant or imaginary-axis crossing, yields the four open-regime classifications. Continuity supplies the coalescence descriptions at \(\alpha\) and \(\beta\).

## Verification
The accompanying `verify.py` uses only the Python standard library and exact rational arithmetic. It reconstructs the characteristic polynomial, evaluates its quartic discriminant through exact Sylvester determinants at enough parameter values to identify the degree-bounded polynomial identity, verifies the Routh determinants, uses exact Sturm sequences to isolate the two discriminant roots and the negative Hurwitz crossing, and checks representative real-root and unstable-dimension counts in every regime.

The stored replay ends with `VERIFY_OK`. The exact Routh and Sturm arguments, rather than decimal eigenvalue approximations, establish the classification.

## Relationship to prior work
Petržela's 2022 article introduces the exact PWL Clapp model, gives the outer equilibria, states that their characteristic polynomial is obtained by replacing the inner slope by the outer slope, and then summarizes the outer linear geometry over \(a\in(-10,-1)\) using approximate transitions near \(-2\) and \(-1\). The article does not give the discriminant, the exact Hurwitz crossing, or the additional real-to-complex collision near \(-4.872\).

A previously published same-source result on the cubic Clapp oscillator concerns invariant-measure barycenters and a third-moment identity for Case I. It does not imply the present Case II outer-equilibrium spectral partition. Focused database searches by DOI, exact polynomial, discriminant coefficients, threshold decimals, and equilibrium-stability aliases did not locate a publication containing this three-threshold classification. The closest retrieved stability-partition results concern different vector fields.

## Limitations
The result is confined to the source's normalized outer-equilibrium slice \(y_{11}=1\), \(y_{12}=1/10\). It does not classify arbitrary admittance parameters. It is not a theorem about the existence, persistence, or criticality of periodic, chaotic, or hyperchaotic invariant sets. The literature search cannot exclude every unindexed analysis, and the originality assessment is limited to the inspected primary source and focused comparison searches.

## References
1. J. Petržela, “Chaotic and Hyperchaotic Dynamics of a Clapp Oscillator,” *Mathematics* 10(11), 1868 (2022), DOI: 10.3390/math10111868. Published 30 May 2022. Primary MSC: 37M05.
