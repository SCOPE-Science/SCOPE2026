# A two-frequency Schoenberg test for cosine-modulated geodesic exponentials on the two-sphere

## Finding
For real \(a>0\), \(b\in\mathbb R\), and \(x,y\in\mathbb S^2\), put \(\theta(x,y)=\arccos(x\cdot y)\) and
\[
K_{a,b}(x,y)=e^{-a\theta(x,y)}\bigl(1+b\cos\theta(x,y)\bigr).
\]
There is an explicit positive threshold \(B(a)\), computable from **two Legendre degrees**, such that \(K_{a,b}\) is positive semidefinite on every finite set if and only if \(b\ge -B(a)\). Moreover, all admissible kernels, including the boundary, are strictly positive definite on every finite set of pairwise distinct points.

Specifically, set \(s(a)=(\sqrt{165+84a^2}-9)/6\). Let \(p(a)\) be the smallest odd integer at least \(1\) and at least \(s(a)\); let \(q(a)\) be the smallest even integer at least \(2\) and at least \(s(a)\). Define
\[
A_0(a)=\frac{1+e^{-\pi a}}{1+a^2},\qquad A_1(a)=\frac{1-e^{-\pi a}}{4+a^2},\qquad
A_{n+2}(a)=\frac{a^2+n^2}{a^2+(n+3)^2}A_n(a)\quad(n\ge0),
\]
\[
T_n(a)=\frac{A_n(a)\bigl(a^2+(n+2)^2\bigr)}{A_{n-1}(a)\bigl(a^2+n^2+n+1\bigr)}\quad(n\ge1),
\qquad B(a)=\min\{T_{p(a)}(a),T_{q(a)}(a)\}.
\]
Every quantity is explicit, and neither infinite minimization nor truncation is required. As \(a\) increases, the controlling candidate degree can grow without bound.

## Assumptions and scope
The kernel is real and continuous, \(a>0\), and positive semidefiniteness means nonnegative quadratic forms for every finite set of points of the unit **two**-sphere. The kernel is not presumed normalized: \(K_{a,b}(x,x)=1+b>0\) in the admitted region. Indeed, \(b=-1\) gives a zero diagonal but nonzero off-diagonal, so it cannot be positive semidefinite; the sharp criterion then implies \(B(a)<1\). No assertion is made for other sphere dimensions or non-geodesic distance.

## Proof
Let \(P_n\) be the Legendre polynomial with \(P_n(1)=1\), and define the unnormalized Legendre moment
\[
A_n=\int_0^\pi e^{-a\theta}P_n(\cos\theta)\sin\theta\,d\theta.
\]
The displayed values for \(A_0,A_1\) follow by elementary integration. For \(n\ge1\), put \(E_n=\int_0^\pi e^{-a\theta}P_n(\cos\theta)\,d\theta\). The Legendre derivative identity and integration by parts give
\[
a(E_{n-1}-E_{n+1})=(2n+1)A_n.
\]
The Legendre differential equation, integrated against \(e^{-a\theta}\), and the three-term Legendre recurrence give
\[
a\bigl(nE_{n-1}+(n+1)E_{n+1}\bigr)=(2n+1)\bigl(a^2+n(n+1)\bigr)A_n.
\]
Solving these two linear equations gives \(E_{n+1}=(a^2+n^2)A_n/a\) and \(E_{n-1}=(a^2+(n+1)^2)A_n/a\). Comparison at consecutive indices establishes \(A_{n+2}/A_n=(a^2+n^2)/(a^2+(n+3)^2)\) for \(n\ge1\); the \(n=0\) case follows directly from \(E_1=aA_0\) and the \(n=2\) formula. Consequently **every** \(A_n>0\).

Put \(C_n=\int_0^\pi e^{-a\theta}\cos\theta\,P_n(\cos\theta)\sin\theta\,d\theta\). The three-term recurrence gives, for \(n\ge1\),
\[
C_n=\frac{nA_{n-1}+(n+1)A_{n+1}}{2n+1}
=A_{n-1}\frac{a^2+n^2+n+1}{a^2+(n+2)^2}>0,
\]
and \(C_0=A_1>0\). Thus the ratio \(A_n/C_n=T_n\) for \(n\ge1\), and \(A_0/C_0=A_0/A_1\). A direct identity shows
\[
\frac{T_2}{A_0/A_1}=
\frac{a^2(a^2+16)}{(a^2+9)(a^2+7)}<1.
\]
Hence harmonic degree zero cannot control the smallest positive ratio. For \(n\ge1\), the exact positive-denominator identity is
\[
\frac{T_{n+2}}{T_n}=
\frac{(a^2+n^2)(a^2+(n+4)^2)(a^2+n^2+n+1)}
{(a^2+(n+3)^2)(a^2+(n-1)^2)(a^2+n^2+5n+7)}.
\]
Subtracting its denominator from its numerator simplifies to
\[
3(2n+3)\bigl(3n^2+9n-7-7a^2\bigr).
\]
Therefore along either parity \(T_n\) decreases strictly while \(n<s(a)\), increases strictly while \(n>s(a)\), and may tie at equality. This proves the two-candidate minimum formula in the finding, including every boundary and integer-switch case. In particular, \(B(a)>0\).

Schoenberg's theorem on \(\mathbb S^2\) identifies positive definiteness with nonnegativity of every Legendre coefficient. These coefficients have the sign of \(A_n+bC_n\), since their usual normalization is a positive multiplier. Since every \(C_n>0\), simultaneous nonnegativity is exactly \(b\ge-\inf_{n\ge0}A_n/C_n=b\ge-B(a)\). For \(b<-B(a)\), a controlling coefficient is negative, proving necessity. At the sharp boundary at most two consecutive-in-parity degrees can tie for each of two parities, so only finitely many coefficients vanish. All sufficiently large even and odd degrees have strictly positive coefficients; the Chen--Menegatto--Sun strictness criterion for spheres of dimension at least two therefore proves strict positive definiteness, including at equality. Larger \(b\) gives every coefficient strictly positive.

## Verification
The Legendre recurrence, the full rational comparison, and the polynomial numerator difference admit exact symbolic checking. With \(a=1\), the candidates are \(p=3\) and \(q=2\), and the threshold is approximately \(B(1)=0.579238561949\); with \(a=2\), they are \(p=3\) and \(q=4\), and the threshold is approximately \(B(2)=0.8630389999\). The optional standalone `check.py` reproduces symbolic algebra and compares a finite sample of numerical Legendre moments to the infinite analytic recurrence. Those computations are **not** used as an infinite proof.

## Relationship to prior work
Gneiting, *Strictly and non-strictly positive definite functions on spheres* (first arXiv release 2011-11-30, arXiv:1111.7077), treats the powered exponential and general Gegenbauer/Legendre criteria, but its examined sections do not present the sharp cosine-modulated exponential parameter region or its two-degree selection rule. Beatson, zu Castell and Xu, *A Pólya criterion for (strict) positive definiteness on the sphere* (first arXiv release 2011-10-11, arXiv:1110.2437), establishes integral-positivity criteria, not this necessary-and-sufficient parameter classification. The result is confined to \(\mathbb S^2\), and neither the corresponding circle problem nor a mixture of two geodesic exponentials implies this coefficient calculation. A possible equivalent result in unindexed literature remains a priority risk.

## Limitations
The criterion concerns only the unit two-sphere and the stated two-parameter family. It has an analytic proof but no independent audit or independent validation; the literature search is bounded and is not a proof of publication priority. Strict positivity applies to matrices on pairwise distinct points, not to duplicated points.

## References
1. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077 (first version 2011-11-30), https://arxiv.org/abs/1111.7077.
2. R. K. Beatson, W. zu Castell and Y. Xu, *A Pólya criterion for (strict) positive definiteness on the sphere*, arXiv:1110.2437 (first version 2011-10-11), https://arxiv.org/abs/1110.2437.
3. I. J. Schoenberg, *Positive definite functions on spheres*, Duke Mathematical Journal 9 (1942), 96–108.
4. D. Chen, V. A. Menegatto and X. Sun, *A necessary and sufficient condition for strictly positive definite functions on spheres*, Proceedings of the American Mathematical Society 131 (2003), 2733–2740.
