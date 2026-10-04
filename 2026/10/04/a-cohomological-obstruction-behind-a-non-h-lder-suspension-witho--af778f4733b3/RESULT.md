# A cohomological obstruction behind a non-Hölder suspension without local product structure
## Finding
Let \(\Sigma=\{0,1\}^{\mathbb Z}\) be the two-sided full shift, let \(\sigma\) be the left shift, and equip \(\Sigma\) with the metric used by Wen,
\[
d(a,b)=\frac13\sum_{i\in\mathbb Z}\frac{|a_i-b_i|}{2^{|i|}}.
\]
Write \(\underline 0\) for the all-zero sequence. Wen's counterexample uses the positive continuous roof
\[
\tau(a)=1+\frac{1}{1-\ln d(a,\underline 0)}\quad(a\ne\underline 0),
\qquad \tau(\underline 0)=1.
\]
The roof \(\tau\) is not continuously cohomologous over \(\sigma\) to any Hölder roof. More precisely, there do not exist a continuous \(u:\Sigma\to\mathbb R\) and a Hölder \(h:\Sigma\to(0,\infty)\) such that
\[
\tau=h+u-u\circ\sigma.
\]

This obstruction is strictly stronger than failure of Hölder regularity. For every \(0<c<1\), define
\[
u_c(a)=\begin{cases}
\dfrac{c}{1-\ln d(a,\underline 0)},&a\ne\underline 0,\\[4pt]
0,&a=\underline 0,
\end{cases}
\qquad
r_c=1+u_c-u_c\circ\sigma.
\]
Then \(r_c\) is positive and is not Hölder for any positive exponent, but its suspension flow has local product structure. Indeed, \(r_c\) is continuously cohomologous to the constant roof \(1\), so its special flow is time-preservingly topologically conjugate to the constant-roof suspension.

## Assumptions and scope
The statement concerns continuous cohomology over the same two-sided full shift: two roofs are cohomologous when their difference is a continuous coboundary. The local product structure is the topological flow property used in arXiv:2608.26561v1. No converse characterization of all roofs with local product structure is asserted.

The parameter in the explicit family satisfies \(0<c<1\). This restriction guarantees positivity because \(0\le u_c\le c\), hence
\[
r_c\ge 1-c>0.
\]

## Proof
First consider Wen's roof. Let \(a\in\Sigma\) have its only nonzero coordinate at index \(-1\). Then
\[
d(a,\underline 0)=\frac16,
\qquad
d(\sigma^k a,\underline 0)=\frac{2^{-k}}6
\quad(k\ge0).
\]
Therefore the stable-orbit roof drift is
\[
\sum_{k=0}^{n-1}\bigl(\tau(\sigma^k a)-\tau(\underline 0)\bigr)
=
\sum_{k=0}^{n-1}\frac{1}{1+\ln 6+k\ln 2}.
\]
The right-hand side diverges as \(n\to\infty\).

Suppose, toward a contradiction, that \(\tau=h+u-u\circ\sigma\) with \(u\) continuous and \(h\) Hölder. Since \(\underline 0\) is fixed, \(h(\underline 0)=\tau(\underline 0)=1\). Telescoping gives
\[
\sum_{k=0}^{n-1}\bigl(\tau(\sigma^k a)-\tau(\underline 0)\bigr)
=
\sum_{k=0}^{n-1}\bigl(h(\sigma^k a)-h(\underline 0)\bigr)
+u(a)-u(\sigma^n a).
\]
If \(h\) has Hölder exponent \(\alpha>0\), then for some \(C>0\),
\[
|h(\sigma^k a)-h(\underline 0)|
\le C\,d(\sigma^k a,\underline 0)^\alpha
=C\,6^{-\alpha}2^{-\alpha k}.
\]
Thus the series involving \(h\) converges absolutely. Also \(\sigma^n a\to\underline 0\), so continuity gives \(u(\sigma^n a)\to u(\underline 0)\). The displayed right-hand side must therefore converge, contradicting the divergent harmonic-type drift. Hence Wen's roof has no continuous Hölder representative in its cohomology class.

Now fix \(0<c<1\). The function \(u_c\) is continuous: away from \(\underline 0\) this is immediate, while \(u_c(a)\to0\) whenever \(d(a,\underline 0)\to0\). The roof \(r_c\) is continuous and positive, and by construction it is continuously cohomologous to the constant roof \(1\).

It remains to verify that \(r_c\) itself is genuinely non-Hölder. Let \(x^{(n)}\) have its only nonzero coordinate at index \(n\ge2\). Put \(A=1+\ln3\) and \(\ell=\ln2\). Then
\[
d(x^{(n)},\underline 0)=\frac{1}{3\cdot2^n},
\qquad
d(\sigma x^{(n)},\underline 0)=\frac{1}{3\cdot2^{n-1}},
\]
and hence
\[
|r_c(x^{(n)})-r_c(\underline 0)|
=
\frac{c\ell}{(A+n\ell)(A+(n-1)\ell)}.
\]
This decays on the order of \(n^{-2}\). For every \(\alpha>0\), however,
\[
d(x^{(n)},\underline 0)^\alpha=3^{-\alpha}2^{-\alpha n},
\]
so the quotient of the preceding two quantities tends to infinity. Thus \(r_c\) is not Hölder for any positive exponent.

Cohomologous positive roofs over an invertible base define topologically conjugate special flows by a vertical coordinate change. Here the conjugacy is continuous and time preserving. The constant roof is Hölder, so Wen's Hölder-roof theorem gives local product structure for the constant-roof suspension. A time-preserving topological conjugacy carries local stable and unstable sets, their local intersections, and the bounded local time displacement to the corresponding objects in the conjugate flow; compactness supplies the required uniform neighborhood transfer. Hence the suspension under \(r_c\) has local product structure.

## Verification
The contradiction for \(\tau\) uses an exact orbit: a single symbol at index \(-1\) moves one step farther into the negative tail at each forward iterate, so its distance to \(\underline 0\) is multiplied by \(1/2\) each time. Substituting that distance into Wen's roof gives the displayed divergent series. The hypothetical Hölder contribution is dominated by a geometric series, while the continuous coboundary contribution telescopes to a convergent endpoint term.

For the positive family, the only quantitative constraints needed are \(0\le u_c\le c<1\) and the exact one-symbol calculation above. No finite computation, asymptotic numerical experiment, or unproved certificate is used.

## Relationship to prior work
Wen, arXiv:2608.26561v1, constructs the logarithmic roof \(\tau\), proves that its suspension lacks local product structure, and proves local product structure for Hölder roofs over the full shift. The paper's proof already exhibits divergent accumulated time drift along a stable pair; the result here turns that phenomenon into a continuous-cohomology obstruction: the same drift rules out every Hölder representative in the entire continuous cohomology class of \(\tau\).

The standard special-flow conjugacy theorem states that positive cohomologous roofs over an invertible base yield topologically conjugate special flows. Applied to the explicit family \(r_c\), this makes the contrast concrete: non-Hölder roofs can still have local product structure when their roughness is a continuous coboundary. The standard conjugacy fact supplies this implication but does not establish the source-specific noncohomology of Wen's logarithmic roof.

## Limitations
The result does not characterize all continuous roofs whose suspensions have local product structure, and it does not claim that continuous cohomology to a Hölder roof is necessary for local product structure. It proves only the stated obstruction for Wen's particular logarithmic roof and gives an explicit non-Hölder family on the opposite side of that obstruction.

A residual literature risk remains that an older symbolic-cohomology or Livšic-type result packages the stable-orbit convergence obstruction in a more general theorem. No inspected source was found that applies such a theorem to Wen's 2026 logarithmic roof or states the resulting cohomological diagnosis.

## References
1. X. Wen, *Local Product Structure of Expansive Flows with Shadowing Property*, arXiv:2608.26561v1, first posted 2026-08-27. Primary MSC 37B10 and 37B65.
2. T. Fisher and B. Hasselblatt, *Hyperbolic Flows*, European Mathematical Society, 2019, Proposition 1.3.19 (cohomologous positive roofs define conjugate special flows).
