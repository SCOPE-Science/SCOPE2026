# Sharp antiphase exchange-cycle stability in symmetric two-species Ricker competition

## Finding
Consider the symmetric competitive Ricker map
\[
F_{\rho,a}(x,y)=\bigl(x\exp(\rho-x-ay),\ y\exp(\rho-y-ax)\bigr),\qquad (x,y)\in(0,\infty)^2,
\]
with intrinsic log growth \(\rho>0\) and interspecific competition \(a>0\). A **positive exchange two-cycle** means a prime period-two orbit of the form \((X,Y)\mapsto(Y,X)\mapsto(X,Y)\), where \(X>Y>0\).

**Theorem.** A positive exchange two-cycle exists precisely when \(0<a<1\) and \(\rho>2(1+a)/(1-a)\), and then it is unique up to exchanging the two phases. There is a universal constant
\[
a_* = 0.277839040264\ldots,
\]
characterized **exactly** as the unique common value
\[
a_* = \frac{\sinh z_*-z_*}{\sinh z_*+z_*}
      =\frac{1}{1+z_*\coth(z_*/2)},\qquad z_*>0.
\]
For each \(0<a<a_*\), the unique exchange cycle is exponentially attracting exactly in one nonempty open interval \(\rho_-(a)<\rho<\rho_+(a)\), whose endpoints are given below. For \(a\ge a_*\), no exchange cycle is linearly exponentially attracting. This classification concerns exchange two-cycles specifically, not all positive period-two orbits of the map.

Define for \(z>0\)
\[
C(z)=z\coth(z/2),\quad
J(z)=\frac{z^2}{2\sinh^2(z/2)},\quad
A(z)=\frac{\sinh z-z}{\sinh z+z}.
\]
For each \(a\in(0,1)\), there are unique positive \(z_-(a)\), \(z_+(a)\) determined by
\[
A(z_-(a))=a,\qquad
C(z_+(a))-(1+a)J(z_+(a))=1-a.
\]
The exact stability endpoints, when \(a<a_*\), are
\[
\rho_\pm(a)=\frac{1+a}{1-a}C(z_\pm(a)).
\]
The open stability window disappears by an exact collision at \(a=a_*\). At the lower stability boundary the two-step monodromy has a \(+1\) multiplier; at the upper boundary it has conjugate unit-modulus multipliers. No nonlinear behavior at either nonhyperbolic boundary is asserted.

## Assumptions and scope
Time is discrete, and all abundance coordinates and parameters are real. Only \(a>0\), \(\rho>0\), and strictly positive states are considered; the result does not concern species-extinction boundary dynamics. The **exchange** condition fixes a biologically interpretable equal-amplitude antiphase mode: the abundances of the two competing species trade places after one iteration. General asynchronous two-cycles need not satisfy that symmetry.

## Proof
**1. Reduction to one scalar.** Write \(z=\log(X/Y)>0\) and \(S=X+Y\). Requiring \(F(X,Y)=(Y,X)\), and taking logs of both coordinates, yields
\[
\rho-X-aY=-z,\qquad \rho-Y-aX=z.
\]
Subtracting proves \((1-a)(X-Y)=2z\), hence necessarily \(a<1\). Adding proves \(S=2\rho/(1+a)\). Because \((X-Y)/S=\tanh(z/2)\), these identities are equivalent to
\[
S=\frac{2C(z)}{1-a},\quad
\rho=\frac{1+a}{1-a}C(z),\quad
X=\frac{S}{2}\bigl(1+\tanh(z/2)\bigr),\quad
Y=\frac{S}{2}\bigl(1-\tanh(z/2)\bigr).
\]
Conversely these equations reconstruct the two exact swap identities, so there are no extraneous solutions. The function \(C(z)=2u\coth u\) with \(u=z/2\) is strictly increasing: its derivative with respect to \(u\) has numerator \(\sinh u\cosh u-u>0\). Its limits are \(2\) as \(z\downarrow0\) and \(+\infty\) as \(z\to\infty\). Therefore the stated existence and uniqueness follow.

**2. Exact Floquet reduction.** At the exchange orbit the first-step Jacobian is
\[
M=DF(X,Y)=
\begin{pmatrix}
(Y/X)(1-X)&-aY\\
-aX&(X/Y)(1-Y)
\end{pmatrix}.
\]
Let \(P\) interchange the two coordinates. Symmetry implies \(DF(Y,X)=PMP\), so the two-step monodromy is \((PM)^2\). Put \(D=\det M\). Direct multiplication gives
\[
D=1-S+(1-a^2)XY,
\quad \operatorname{tr}(PM)=-aS,\quad\det(PM)=-D.
\]
The characteristic polynomial of \(PM\) is therefore \(\lambda^2+aS\lambda-D\). The Floquet multipliers of the two-cycle are the squares of its two roots. The strict quadratic Jury criterion (for both roots to lie inside the unit disk) reduces here to
\[
1+D>0,\qquad 1-aS-D>0.
\]
(The third Jury condition \(1+aS-D>0\) follows from the second because \(aS>0\).)

**3. The two sharp boundary functions.** Substitute the one-parameter orbit formula. One obtains
\[
D=1-\frac{2}{1-a}\left[C(z)-(1+a)J(z)\right],
\]
and
\[
1-aS-D=(1-a)[S-(1+a)XY].
\]
Since \(S/(XY)=(1-a)\sinh(z)/z\), the second strict Jury inequality is equivalent to
\[
(1-a)\sinh z>(1+a)z,
\]
that is, \(a<A(z)\). The first strict Jury inequality is equivalent to
\[
C(z)-(1+a)J(z)<1-a.
\]
The function \(A\) is strictly increasing from \(0\) to \(1\), because \(z/\sinh z\) strictly decreases. The function \(J(z)=2(u/\sinh u)^2\) is strictly decreasing from \(2\) to \(0\). Thus \(C(z)-(1+a)J(z)\) is strictly increasing from \(-2a\) to \(+\infty\). Exactly one crossing of each inequality exists, and both inequalities hold precisely for
\[
z_-(a)<z<z_+(a).
\]
This also proves that no unexamined stable parameter intervals exist.

**4. A unique universal coupling ceiling.** At the lower boundary \(a=A(z_-(a))\), its defining equation gives \((1+a)z/\sinh z=1-a\). Because \(J(z)=C(z)z/\sinh z\), it follows that
\[
C(z_-)-(1+a)J(z_-)=aC(z_-).
\]
By the strict monotonicity in Step 3, \(z_-<z_+\) if and only if \(aC(z_-)<1-a\), equivalently
\[
a<\frac1{1+C(z_-)}.
\]
The left side of \(A(z)=1/(1+C(z))\) increases strictly from \(0\) to \(1\); the right side decreases strictly from \(1/3\) to \(0\). They cross exactly once at \(z_*>0\). This proves the sharp threshold and the complete classification. At equality the two strict Jury conditions fail together. Throughout, statements of attraction mean exponential local stability; neutral-boundary nonlinear dynamics are not classified.

## Verification
The standalone `verify.py` checks the Jacobian trace/determinant formulas, the swap equations, sample stability windows on both sides of the critical coupling, and numerical critical values. More importantly, it supplies a **rational interval certificate** for an exact attracting orbit:
\[
a=\frac1{10},\quad
(X,Y)=\left(\frac{80\log4}{27},\frac{20\log4}{27}\right),\quad
\rho=\frac{55\log4}{27}.
\]
Indeed \(\rho-X-aY=-\log4\) and \(\rho-Y-aX=\log4\), so the two phases are exchanged exactly. At this orbit,
\[
D=1-\frac{100}{27}\log4+\frac{1584}{729}(\log4)^2,
\quad
1-aS-D=\frac{10}{3}\log4-\frac{1584}{729}(\log4)^2.
\]
The code bounds \(\log4\) from rational truncations of the positive series \(2\sum_{k\ge0}(3/5)^{2k+1}/(2k+1)\), with an explicit positive tail bound; rational inequalities prove \(1+D>0\) and \(1-aS-D>0\). The resulting monodromy multipliers are approximately \(0.34134134\) and \(0.00501291\). The exact completeness and uniqueness are proved above rather than inferred from finite calculations.

## Relationship to prior work
Goldar, Hassan, Pati, Mohsen, and Izadi (2026) study the general two-species Ricker competition map, equilibrium bifurcations, and general two-cycle stability conditions. The exchange-symmetric equal-growth, equal-coupling setting is a specialization of that ecological model. Kulakov, Neverova, and Frisman (2022) already describe antiphase modes, coexistence of phases, and associated bifurcations, chiefly through numerical bifurcation diagrams. Ryashko, Otman, and Bashkirtseva (2025) study multirhythmicity and perturbations of the same symmetric competition class. Hence the existence of antiphase cycles and their qualitative bifurcations are **not new claims**. The specific result here is a complete analytic description of the **exchange** two-cycle's attraction wedge and a universal sharp coupling ceiling expressed by a unique scalar transcendental root. A separate published spectral Floquet reduction for **synchronous** Ricker cycles does not address this antiphase exchange orbit.

## Limitations
The theorem classifies only prime two-cycles whose species abundances swap each step; other attracting cycles, quasiperiodic states, and chaotic dynamics may exist outside this branch or simultaneously with it. At unit-circle boundaries the proof establishes a linear spectral condition, not the direction or existence of nonlinear bifurcating solutions. The statement is local, deterministic and parameter-specific; stochastic and ecological data interpretations are not established. Prior numerical antiphase results are recognized, and a less accessible earlier analytic specialization remains possible.

## References
1. S. Goldar, S. S. Hassan, R. Pati, A. A. Mohsen and M. Izadi, *Dynamics and Bifurcations in a Two-Species Ricker Competition Model With Nonmonotonic Growth*, Discrete Dynamics in Nature and Society (first published 2026-09-16), doi:10.1155/ddns/7255117.
2. M. Kulakov, G. Neverova and E. Frisman, *The Ricker Competition Model of Two Species: Dynamic Modes and Phase Multistability*, Mathematics 10 (2022), article 1076, doi:10.3390/math10071076.
3. L. Ryashko, A. Otman and I. Bashkirtseva, *Multirhythmicity, Synchronization, and Noise-Induced Dynamic Diversity in a Discrete Population Model with Competition*, Mathematics 13 (2025), article 857, doi:10.3390/math13050857.
4. R. Luís, S. Elaydi and H. Oliveira, *Stability of a Ricker-type competition model and the competitive exclusion principle*, Journal of Biological Dynamics 5 (2011), 636–660, doi:10.1080/17513758.2011.581764.
