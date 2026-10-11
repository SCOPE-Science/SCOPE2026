# Smooth phase-chirp obstruction and sharp phase-variation cost in Toeplitz minimum-attainment approximation

## Finding
Let \(H^2\) be the complex Hardy space on the unit circle \(\mathbb T\), and let \(T_h=P_{H^2}M_h|_{H^2}\) denote the Toeplitz operator with symbol \(h\in L^\infty(\mathbb T)\). Write \(\mathfrak A\) for all absolutely minimum-attaining Toeplitz operators on \(H^2\), and \(\mathfrak A_c=\{T_h\in\mathfrak A:h\in C(\mathbb T)\}\). Every member of \(\mathfrak A_c\) has continuous constant-modulus symbol, and conversely every continuous constant-modulus symbol induces an operator in \(\mathfrak A_c\).

For every complex-valued \(h\in C(\mathbb T)\), put \(M=\max_{\mathbb T}|h|\) and \(m=\min_{\mathbb T}|h|\). Then
\[
\operatorname{dist}(T_h,\mathfrak A)=\operatorname{dist}(T_h,\mathfrak A_c)=\frac{M-m}{2}.
\]
If \(m>0\), the symbol \(r h/|h|\), where \(r=(M+m)/2\), realizes the distance in both classes.

There nevertheless exists a nonzero \(C^\infty\) symbol \(f\) for which no nearest operator in \(\mathfrak A_c\) exists. An explicit choice is
\[
f(e^{it})=\begin{cases}\exp(1-\csc^2(t/2))\exp(i/t),&0<t<2\pi,\\0,&t=0.\end{cases}
\]
For this \(f\), the distance to each of \(\mathfrak A\) and \(\mathfrak A_c\) is \(1/2\), and the continuous-symbol distance is not attained. Moreover, with the precise phase-variation quantity defined below, the near-best phase complexity is
\[
\lim_{\varepsilon\downarrow0}\frac{V_f(\varepsilon)}{\sqrt{\log(1/\varepsilon)}}=\frac12.
\]

## Assumptions and scope
A bounded operator \(A\) on a Hilbert space is *absolutely minimum attaining* when, for every nonzero closed subspace \(E\), the restriction \(A|_E\) attains its minimum modulus. For \(u\in C(\mathbb T)\) taking values in the unit circle and \(\nu\ge0\), a symbol \(\nu u\) belongs to the continuous-symbol class \(\mathfrak A_c\). The zero symbol also belongs to that class. These facts follow from the Toeplitz classification of Ramesh--Sequeira (2022, Theorem 2.7), or directly for continuous \(u\) because \(T_u^*T_u=I-H_u^*H_u\) with compact Hankel operator \(H_u\).

For \(0<\varepsilon<1/4\), define
\[
V_f(\varepsilon)=\inf\big\{\operatorname{Var}_{[0,2\pi]}\beta:\ \nu\ge0,\ u\in C(\mathbb T,\mathbb T),\ u(e^{it})=e^{i\beta(t)},\ \beta\in C([0,2\pi],\mathbb R),\ \|T_f-T_{\nu u}\|\le\tfrac12+\varepsilon\big\}.
\]
The total variation is the usual (possibly infinite) total variation of a real function. A lift \(\beta\) exists for every continuous \(u\), and its variation is independent of adding a constant integer multiple of \(2\pi\). We make no assertion about best approximants or phase costs among *discontinuous*-symbol members of \(\mathfrak A\).

## Proof
**Toeplitz norms and the constant-modulus class.** For any \(h\in L^\infty\), \(\|T_h\|=\|h\|_\infty\): one inequality follows by compression of multiplication, and the opposite follows by evaluating \(\langle T_hk_z,k_z\rangle\) on normalized reproducing kernels and taking radial limits at Lebesgue points of \(h\). The primary characterization says an absolutely minimum-attaining Toeplitz symbol has constant modulus almost everywhere. Therefore, for any \(T_\varphi\in\mathfrak A\), with \(|\varphi|=\nu\) almost everywhere, the reverse triangle inequality gives
\[
\|T_h-T_\varphi\|=\|h-\varphi\|_\infty\ge\max(M-\nu,\nu-m)\ge\frac{M-m}{2}.
\]
For any \(\delta>0\), approximate \(h\) uniformly by a nowhere-zero continuous \(g\), with \(\|h-g\|_\infty<\delta\). To justify this elementary approximation without a topological dimension theorem, first approximate \(h\) by a complex-valued piecewise linear function on a sufficiently fine finite subdivision of the circle; its image is a finite union of line segments, so arbitrarily small constant complex translations move its image away from the origin. Then set \(u=g/|g|\), a continuous unimodular symbol, and \(\nu=(M+m)/2\). Pointwise \(|h-\nu u|\le||h|-\nu|+2\delta\), hence \(\|T_h-T_{\nu u}\|\le(M-m)/2+2\delta\). Let \(\delta\downarrow0\). If \(m>0\), take \(u=h/|h|\) directly. The case \(h=0\) is included.

**Smoothness and nonproximinality.** Put \(a(t)=\exp(1-\csc^2(t/2))\). Its extension by zero at both endpoints has all derivatives zero, since its logarithm behaves as \(-4/t^2\) near zero and as \(-4/(2\pi-t)^2\) near the opposite endpoint. Every derivative of \(e^{i/t}\) grows at most polynomially in \(1/t\), so \(a(t)e^{i/t}\) gives a smooth periodic circle function. Its modulus equals one at \(t=\pi\) and zero at \(t=0\), yielding the distance \(1/2\).

Assume \(\|T_f-T_{\nu u}\|\le1/2\) with \(\nu\ge0\) and continuous unimodular \(u\). At the zero, \(\nu\le1/2\), and at \(t=\pi\) the reverse triangle inequality gives \(\nu\ge1/2\); therefore \(\nu=1/2\). Squaring the pointwise error inequality at any \(0<t<2\pi\) gives
\[
\operatorname{Re}\big(e^{i/t}\overline{u(e^{it})}\big)\ge a(t)>0.
\]
But continuity forces \(u(e^{it})\to u(1)\) as \(t\downarrow0\), whereas along a sequence \(t_j\downarrow0\) with \(e^{i/t_j}=-u(1)\), the left side tends to \(-1\), a contradiction. Thus the distance to \(\mathfrak A_c\) has no minimizer. This argument does not exclude discontinuous-symbol minimizers in \(\mathfrak A\).

**Quantitative upper bound.** Write \(L=\log(1/\varepsilon)\) and \(s=2\arcsin((1+L)^{-1/2})\). Then \(a(s)=a(2\pi-s)=\varepsilon\), and \(a(t)\le\varepsilon\) on both arcs adjacent to the seam. On the central arc \([s,2\pi-s]\), choose \(u(e^{it})=e^{i/t}\); on the remaining arc choose a shortest constant-speed circle interpolation between its endpoint phases, so the phase lift adds at most \(\pi\) variation. With \(\nu=1/2\), the approximation error on the central arc is \(|a-1/2|\le1/2\) and on the complement is at most \(1/2+\varepsilon\). This gives
\[
V_f(\varepsilon)\le\frac1s-\frac1{2\pi-s}+\pi.
\]
Since \(s\sqrt L\to2\), \(\limsup V_f(\varepsilon)/\sqrt L\le1/2\).

**Quantitative lower bound.** For any admissible \(\nu,u,\beta\), the points \(t=0\) and \(t=\pi\) force \(1/2-\varepsilon\le\nu\le1/2+\varepsilon\). Fix \(0<\alpha<1\), and set \(s_\alpha=2\arcsin((1+\alpha L)^{-1/2})\). On \([s_\alpha,\pi]\), \(a(t)\ge\varepsilon^\alpha\). Squaring the error inequality gives
\[
\cos(\beta(t)-1/t)\ge\frac{a(t)^2+\nu^2-(1/2+\varepsilon)^2}{2a(t)\nu}\ge -\frac{\varepsilon}{a(t)\nu}\ge-\frac{\varepsilon^{1-\alpha}}{1/2-\varepsilon}.
\]
For sufficiently small \(\varepsilon\), the final quantity exceeds \(-1/2\). Consequently the continuous angle difference \(\beta(t)-1/t\) must remain in a *single* connected interval \((2\pi k-2\pi/3,2\pi k+2\pi/3)\); it cannot change the integer \(k\) on the connected arc. Its endpoint variation is bounded by \(4\pi/3\), so
\[
\operatorname{Var}\beta\ge\frac1{s_\alpha}-\frac1\pi-\frac{4\pi}{3}.
\]
Since \(s_\alpha\sqrt L\to2/\sqrt\alpha\), this proves \(\liminf V_f(\varepsilon)/\sqrt L\ge\sqrt\alpha/2\). Let \(\alpha\uparrow1\) and combine with the upper bound. The asserted limit is exactly \(1/2\).

## Verification
The proof relies on four explicit analytic checks: the Toeplitz operator norm identity; the primary constant-modulus characterization and continuous-symbol sufficiency; flatness at both endpoints of the chirped bump; and matching upper/lower phase-variation asymptotics. The phase bound uses continuous lifts and cannot be inferred from finite sampling. All constants, exponent ranges, and endpoint cases are included in the proof. A direct numerical sanity check of \(1/[2\arcsin((1+L)^{-1/2})\sqrt L]\) approaches \(1/2\) for increasing \(L\), but no numerical experiment is used as an infinite proof.

## Relationship to prior work
Ramesh--Sequeira's primary characterization (first public version 2022-09-13, Theorem 2.7) supplies the absolute minimum-attainment membership test for Toeplitz operators and is **not** claimed as new. Their separate 2022 paper gives norm-closure descriptions of absolutely norm- and minimum-attaining operators in the full operator algebra, which do not imply best approximation or phase regularity for the continuous Toeplitz subclass. Here the added phenomenon is an explicit \(C^\infty\) Toeplitz symbol for which the natural continuous-symbol minimum-attainment class is closed yet has no nearest point, together with an exact logarithmic square-root law measuring the compulsory winding of all almost-best continuous phases. Exact distance alone is an elementary consequence of the cited classification and is incorporated to normalize the genuine approximation phenomenon.

## Limitations
Only complex Hardy-space Toeplitz operators and continuous symbols are treated. The nonproximinality and phase-variation assertions concern \(\mathfrak A_c\), *not* every possibly discontinuous-symbol absolutely minimum-attaining Toeplitz operator. This does not determine best approximation in the ambient algebra of all bounded operators. The primary preprint and publication have been inspected, but mathematically equivalent results might occur in unindexed literature on unimodular approximation or phase selection. No independent audit has been performed.

## References
1. G. Ramesh and S. S. Sequeira, *Absolutely minimum attaining Toeplitz and absolutely norm attaining Hankel operators*, arXiv:2209.05841v1 (first public 2022-09-13); *Comptes Rendus Mathématique* 361 (2023), 973--977, doi:10.5802/crmath.457. Relevant material: Theorem 2.7 and Remark 2.8.
2. G. Ramesh and S. S. Sequeira, *On the closure of Absolutely Norm attaining Operators*, arXiv:2204.05912v1 (2022). Relevant material: the general operator-norm closure theorem and analogous minimum-attainment closure result.
