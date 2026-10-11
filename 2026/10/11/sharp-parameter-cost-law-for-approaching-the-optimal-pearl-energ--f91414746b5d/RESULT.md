# Sharp parameter-cost law for approaching the optimal Pearl energy coefficient

## Finding

The Pearl ensemble has an expected logarithmic-energy expansion
\[
\mathbb E(E_N)
=
\left(\frac12-\log2\right)N^2
-\frac12N\log N
+
C(A,B)N
+
O(\sqrt N\log N).
\]
The recent source minimizes \(C(A,B)\) in \(B\), proves that the resulting coefficient decreases to
\[
L=\frac{1-\log3}{2},
\]
and uses density of admissible rational-square parameters to obtain coefficients arbitrarily close to \(L\).

The approach to \(L\) has an exact parameter law.

For
\[
B_{\min}(A)
=
\frac{12}{(\pi-2\Phi_0)^2},
\qquad
\cos\Phi_0=1-\frac2A,
\]
put
\[
C_*(A)=C(A,B_{\min}(A)).
\]
Then, for every
\[
A>2,
\]
\[
C_*(A)-L
=
\frac{c_*}{A}
+
\sum_{n=2}^{\infty}
\frac{4n-7}{3n(n-1)}A^{-n},
\]
where
\[
c_*=\frac13+\log\frac34
=
0.0456512608815524\ldots.
\]
Every coefficient is positive. In particular,
\[
\frac{c_*}{A}
<
C_*(A)-L
\le
\frac{c_*}{A}
+
\frac5{18}\frac{A^{-2}}{1-A^{-1}},
\]
and therefore
\[
A(C_*(A)-L)\longrightarrow c_*.
\]

This asymptotic is sharp even after imposing the arithmetic restrictions required by the Pearl construction. Let
\[
\mathcal Q_{\mathrm{odd}}
=
\left\{
(a/b)^2:
a,b\text{ positive odd integers}
\right\}
\]
and define
\[
A_{\mathrm{adm}}(\varepsilon)
=
\inf
\left\{
A>2:
A\in\mathcal Q_{\mathrm{odd}},
\ \exists B\in\mathcal Q_{\mathrm{odd}}
\text{ with }
C(A,B)\le L+\varepsilon
\right\}.
\]
Then
\[
\varepsilon A_{\mathrm{adm}}(\varepsilon)
\longrightarrow
c_*
\qquad
(\varepsilon\downarrow0).
\]

Thus achieving an \(\varepsilon\)-gap from the limiting Pearl coefficient requires, and asymptotically permits, a polar parameter of size
\[
c_*/\varepsilon.
\]

The second optimized parameter converges on a different scale. One has
\[
B_{\min}(A)
=
\frac{12}{\left(\pi-4\arcsin(A^{-1/2})\right)^2}
=
\frac{12}{\pi^2}
+
\frac{96}{\pi^3}A^{-1/2}
+
O(A^{-1}).
\]
If \(A_\varepsilon\) is the continuous threshold defined by
\[
C_*(A_\varepsilon)=L+\varepsilon,
\]
then
\[
A_\varepsilon
=
\frac{c_*}{\varepsilon}+O(1)
\]
and
\[
B_{\min}(A_\varepsilon)
=
\frac{12}{\pi^2}
+
\frac{96}{\pi^3\sqrt{c_*}}\sqrt{\varepsilon}
+
O(\varepsilon).
\]

## Assumptions and scope

The coefficient \(C(A,B)\), the parameters \(A,B\), and the optimized value \(B_{\min}(A)\) are exactly those in Theorem 7 and the proof of Theorem 2 of arXiv:2609.39825v1.

The source requires
\[
A>2,\qquad B>0
\]
at the continuous level. To realize a Pearl ensemble with compatible integer parallel counts, Theorem 2 restricts both parameters to squares of ratios of odd integers. The quantity \(A_{\mathrm{adm}}(\varepsilon)\) measures the smallest possible first parameter within precisely this admissible set, allowing any admissible second parameter.

The result analyzes the parameter cost inside the Pearl family. It does not assert that
\[
L=\frac{1-\log3}{2}
\]
is the true optimal linear coefficient among all point configurations on the sphere.

## Proof

The source gives
\[
\begin{aligned}
C_*(A)
&=
\left(\frac73-\frac1A\right)
\log\frac{A}{A-1}
+
\left(\frac1A-\frac12\right)\log3
\\
&\qquad
-\frac{2\log2}{A}
+\frac12-\frac2A.
\end{aligned}
\]
Set
\[
x=\frac1A.
\]
Since
\[
L=\frac{1-\log3}{2},
\]
subtraction gives
\[
C_*(A)-L
=
\left(\frac73-x\right)(-\log(1-x))
+x\log3-2x\log2-2x.
\]

Because
\[
0<x<\frac12,
\]
the absolutely convergent power series
\[
-\log(1-x)
=
\sum_{n=1}^{\infty}\frac{x^n}{n}
\]
may be substituted directly. The coefficient of \(x\) is
\[
\frac73+\log3-2\log2-2
=
\frac13+\log\frac34
=
c_*.
\]
For every
\[
n\ge2,
\]
the coefficient of \(x^n\) is
\[
\frac7{3n}-\frac1{n-1}
=
\frac{4n-7}{3n(n-1)}.
\]
This proves the exact series.

For
\[
n\ge2,
\]
\[
0<
\frac{4n-7}{3n(n-1)}
\le
\frac5{18}.
\]
The upper inequality is equivalent to
\[
5n^2-29n+42\ge0,
\]
which holds for every integer \(n\ge2\), with equality at \(n=3\). Therefore
\[
0<
\sum_{n=2}^{\infty}
\frac{4n-7}{3n(n-1)}A^{-n}
\le
\frac5{18}
\frac{A^{-2}}{1-A^{-1}}.
\]
The two-sided bound and
\[
A(C_*(A)-L)\to c_*
\]
follow immediately.

The same positive-coefficient series also proves directly that \(C_*(A)\) is strictly decreasing in \(A\).

Now define \(A_\varepsilon\) by
\[
C_*(A_\varepsilon)=L+\varepsilon.
\]
For all sufficiently small positive \(\varepsilon\), existence and uniqueness follow from strict monotonicity and the limiting value \(L\). The two-sided estimate gives
\[
A_\varepsilon
=
\frac{c_*}{\varepsilon}+O(1).
\]

For the arithmetic restriction, any admissible pair satisfies
\[
C(A,B)\ge C_*(A).
\]
Hence
\[
C(A,B)\le L+\varepsilon
\]
forces
\[
A\ge A_\varepsilon,
\]
and therefore
\[
\liminf_{\varepsilon\downarrow0}
\varepsilon A_{\mathrm{adm}}(\varepsilon)
\ge c_*.
\]

Ratios of positive odd integers are dense in
\[
(0,\infty),
\]
so their squares are dense there as well. Choose an admissible \(A>A_\varepsilon\) with
\[
A/A_\varepsilon\to1.
\]
Then
\[
C_*(A)<L+\varepsilon.
\]
Because \(C(A,B)\) is continuous in \(B\) and is minimized at \(B_{\min}(A)\), an admissible \(B\) can be chosen sufficiently close to \(B_{\min}(A)\) so that
\[
C(A,B)\le L+\varepsilon.
\]
This gives
\[
\limsup_{\varepsilon\downarrow0}
\varepsilon A_{\mathrm{adm}}(\varepsilon)
\le c_*,
\]
and proves the sharp admissible-cost law.

Finally, the source relation
\[
\cos\Phi_0=1-\frac2A
\]
is equivalent to
\[
\Phi_0=2\arcsin(A^{-1/2}).
\]
Thus
\[
B_{\min}(A)
=
\frac{12}{\left(\pi-4\arcsin(A^{-1/2})\right)^2}.
\]
Using
\[
\arcsin u=u+O(u^3)
\]
gives
\[
B_{\min}(A)
=
\frac{12}{\pi^2}
+
\frac{96}{\pi^3}A^{-1/2}
+
O(A^{-1}).
\]
Substituting
\[
A_\varepsilon
=
c_*/\varepsilon+O(1)
\]
gives the displayed square-root law.

## Verification

The primary Pearl paper was inspected at its classification data, Theorem 7, the proof of Theorem 2, and the following remark on the optimized number of parallels. The displayed formula for \(C_*(A)\), the exact optimizer \(B_{\min}(A)\), the relation
\[
\cos\Phi_0=1-\frac2A,
\]
the strict decrease of \(C_*(A)\), and the odd-rational-square admissibility condition were checked directly in the full text and on the rendered theorem page.

The expansion above was independently reconstructed from the source formula. The coefficient identity is exact, and all tail coefficients have a proved sign. Numerical evaluation is used only to display the decimal value of \(c_*\).

The full primary Diamond-ensemble paper was also inspected at its main theorem. It gives the earlier fixed linear coefficient
\[
-0.0492220914515784\ldots
\]
for its quasioptimal construction, but it has no Pearl parameter \(A\), no limiting Pearl coefficient, and therefore no implication for the parameter-cost law proved here.

## Relationship to prior work

The Diamond ensemble previously achieved a rigorously computed linear coefficient close to the heuristic value
\[
(1-\log3)/2.
\]
The Pearl ensemble improves this by introducing a two-region construction and proving that its linear coefficient can approach that heuristic value arbitrarily closely.

The fresh source establishes this approach qualitatively: after optimizing \(B\), it states that \(C_*(A)\) decreases to \(L\), then uses density of odd-rational-square parameters to obtain Theorem 2 for every prescribed positive tolerance.

The present result determines the missing quantitative tradeoff. It gives an exact positive all-order expansion of the gap, identifies the sharp first coefficient \(c_*\), and shows that the same \(c_*/\varepsilon\) scale is unavoidable and attainable after the source's arithmetic admissibility constraints are restored.

Targeted searches under the source identifier, the optimized coefficient, the limiting constant, first-correction terminology, and parameter-efficiency formulations did not locate an implication-equivalent statement.

## Limitations

The sharp parameter-cost statement concerns the Pearl family and its parameter \(A\). It is not a lower bound on the computational complexity of generating arbitrary low-energy point configurations.

The square-root expansion for \(B_{\min}\) describes the continuous optimizer. Admissible odd-rational-square values of \(B\) can approximate it arbitrarily well, but no Diophantine denominator bound is claimed.

The result does not improve the
\[
O(\sqrt N\log N)
\]
remainder in the expected energy expansion and does not determine the conjectural universal optimal linear coefficient.

## References

1. B. Gariboldi and G. Gigante, *The Pearl ensemble and the logarithmic energy on the Sphere*, arXiv:2609.39825v1, 2026.
2. C. Beltrán and U. Etayo, *The Diamond ensemble: a constructive set of points with small logarithmic energy*, Journal of Complexity 59 (2020), 101471; arXiv:1809.09416.
3. C. Beltrán, U. Etayo, and P. R. López-Gómez, *Low-energy points on the sphere and the real projective plane*, Journal of Complexity 76 (2023), 101742.
