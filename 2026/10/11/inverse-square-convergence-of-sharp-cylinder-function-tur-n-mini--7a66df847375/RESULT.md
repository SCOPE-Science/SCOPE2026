# Inverse-square convergence of sharp cylinder-function Turán minima

## Finding

Fix
\\[
\\mu>0,
\\qquad
0\\le\\alpha<\\pi,
\\]
and define the cylinder function
\\[
C_\\mu(x)
=
(\\cos\\alpha)J_\\mu(x)-(\\sin\\alpha)Y_\\mu(x).
\\]
Its normalized Turánian is
\\[
\\Phi_{\\mu,\\alpha}(x)
=
1-
\\frac{C_{\\mu-1}(x)C_{\\mu+1}(x)}{C_\\mu(x)^2}.
\\]

Let \\(c_{\\mu,n}\\) be the positive zeros of \\(C_\\mu\\). The recent sharp Turán theorem shows that on every nodal interval
\\[
(c_{\\mu,n},c_{\\mu,n+1})
\\]
there is a unique minimizer \\(a_{\\mu,n}\\), and that the minimum
\\[
b_{\\mu,n}
=
\\Phi_{\\mu,\\alpha}(a_{\\mu,n})
\\]
increases to \\(1\\).

The convergence has the quantitative asymptotic
\\[
1-b_{\\mu,n}
=
\\frac{\\mu^2}{\\pi^2n^2}
+
O_{\\mu,\\alpha}(n^{-3}).
\\]
Equivalently,
\\[
\\lim_{n\\to\\infty}
n^2(1-b_{\\mu,n})
=
\\frac{\\mu^2}{\\pi^2}.
\\]

The leading coefficient is independent of the cylinder phase \\(\\alpha\\). Thus the sharp nodal constants for every fixed real combination of \\(J_\\mu\\) and \\(Y_\\mu\\) approach the limiting value \\(1\\) at the same inverse-square scale.

## Assumptions and scope

The order \\(\\mu>0\\) and phase \\(\\alpha\\in[0,\\pi)\\) are fixed while \\(n\\to\\infty\\).

The definitions of \\(a_{\\mu,n}\\) and \\(b_{\\mu,n}\\), their uniqueness, and the qualitative limit \\(b_{\\mu,n}\\to1\\) are those of the recent cylinder-function Turán theorem.

The remainder constant may depend on \\(\\mu\\) and \\(\\alpha\\). No uniformity is asserted as these parameters vary.

## Proof

Introduce the logarithmic-derivative variable used in the recent proof,
\\[
y_{\\mu,\\alpha}(x)
=
x\\frac{C_\\mu'(x)}{C_\\mu(x)},
\\]
and at the \\(n\\)-th minimizer set
\\[
\\varsigma_{\\mu,n}
=
y_{\\mu,\\alpha}(a_{\\mu,n}).
\\]
The source proves the two exact relations
\\[
b_{\\mu,n}(1+\\varsigma_{\\mu,n})=1
\\]
and
\\[
a_{\\mu,n}^2
=
\\frac{(1+\\varsigma_{\\mu,n})(\\mu^2-\\varsigma_{\\mu,n}^2)}{\\varsigma_{\\mu,n}}.
\\]

From the first relation,
\\[
1-b_{\\mu,n}
=
\\frac{\\varsigma_{\\mu,n}}{1+\\varsigma_{\\mu,n}}.
\\]
Multiplying the second relation by this quantity gives the exact identity
\\[
a_{\\mu,n}^2(1-b_{\\mu,n})
=
\\mu^2-\\varsigma_{\\mu,n}^2.
\\]
Using again
\\[
\\varsigma_{\\mu,n}
=
\\frac{1-b_{\\mu,n}}{b_{\\mu,n}},
\\]
we obtain
\\[
a_{\\mu,n}^2(1-b_{\\mu,n})
+
\\left(
\\frac{1-b_{\\mu,n}}{b_{\\mu,n}}
\\right)^2
=
\\mu^2.
\\]

The recent theorem gives
\\[
b_{\\mu,n}\\longrightarrow1,
\\]
so \\(\\varsigma_{\\mu,n}\\to0\\). The preceding identity then shows first that
\\[
1-b_{\\mu,n}
=
\\frac{\\mu^2}{a_{\\mu,n}^2}
+
O(a_{\\mu,n}^{-6}).
\\]
Indeed, the stationarity relation gives
\\[
\\varsigma_{\\mu,n}=O(a_{\\mu,n}^{-2}),
\\]
and hence the correction \\(\\varsigma_{\\mu,n}^2/a_{\\mu,n}^2\\) is \\(O(a_{\\mu,n}^{-6})\\).

It remains to locate the minimizer at leading order. Fixed-order large-argument asymptotics for cylinder functions give
\\[
c_{\\mu,n}
=
\\pi n+O_{\\mu,\\alpha}(1),
\\qquad
c_{\\mu,n+1}
=
\\pi(n+1)+O_{\\mu,\\alpha}(1).
\\]
Because
\\[
a_{\\mu,n}
\\in
(c_{\\mu,n},c_{\\mu,n+1}),
\\]
it follows that
\\[
a_{\\mu,n}
=
\\pi n+O_{\\mu,\\alpha}(1).
\\]
Therefore
\\[
\\frac1{a_{\\mu,n}^2}
=
\\frac1{\\pi^2n^2}
+
O_{\\mu,\\alpha}(n^{-3}).
\\]
Combining the last two displays gives
\\[
1-b_{\\mu,n}
=
\\frac{\\mu^2}{\\pi^2n^2}
+
O_{\\mu,\\alpha}(n^{-3}),
\\]
as claimed.

## Verification

The recent primary paper was checked at the definition of the normalized cylinder Turánian, the uniqueness of the nodal minimizer, the monotone convergence of its minimum to \\(1\\), and the exact stationarity relations used above.

The only external asymptotic input is the classical fixed-order large-zero law for Bessel and cylinder functions. The NIST Digital Library of Mathematical Functions records McMahon-type large-zero expansions in §10.21, which in particular imply
\\[
c_{\\mu,n}=\\pi n+O(1)
\\]
for fixed order and phase.

No finite numerical experiment, truncation, or asymptotic extrapolation is used as proof.

## Relationship to prior work

The recent paper proves that the sharp minimum values \\(b_{\\mu,n}\\) increase to \\(1\\), but it does not state a convergence rate. Its proof contains the exact critical-point identity that makes the rate accessible once combined with classical large-zero asymptotics.

Earlier Bessel Turán literature supplies inequalities and qualitative bounds for normalized Turánians. The targeted searches did not locate a statement identifying the exact limit
\\[
\\lim_{n\\to\\infty}n^2(1-b_{\\mu,n})
=
\\frac{\\mu^2}{\\pi^2}
\\]
for the successive nodal minima, nor the phase independence across the full cylinder family.

The result is also distinct from asymptotics of the zeros themselves: it converts zero spacing and the nonlinear stationarity relation into a sharp asymptotic for the best Turán constant on each nodal interval.

## Limitations

The result is for fixed \\(\\mu\\) and fixed \\(\\alpha\\). It does not address simultaneous large-order and large-index regimes.

Only the leading inverse-square coefficient is identified uniformly at the statement level; no phase-dependent next coefficient is asserted.

The result concerns the normalized oscillatory cylinder Turánian and does not transfer automatically to modified-Bessel or imaginary-order families.

## References

1. I. Aktaş and Á. Baricz, *Turán type inequalities for oscillatory special functions*, arXiv:2609.39008v1, 2026.
2. NIST Digital Library of Mathematical Functions, §10.21, *Zeros of Bessel and Hankel Functions*, especially the McMahon large-zero expansions.
3. G. N. Watson, *A Treatise on the Theory of Bessel Functions*, 2nd ed., Cambridge University Press, 1944.
