# Closed-form high-soundness optimization of the exact product-test QMA conversion bound
## Finding
Beckey, Granha Jeronimo, and Wu give in Remark 7.3 of *An Optimal Analysis of the Product Test* a sharpened but unoptimized two-parameter upper bound on the soundness of their Harrow--Montanaro two-Merlin conversion. Write
\[
a=1-\sigma,
\]
where \(\sigma\) is the original \(k\)-Merlin soundness, and define the exact product-test rejection function
\[
R(\varepsilon)
=
1-\mathrm{PT}^{\le}_k(1-\varepsilon)
=
\frac{1-s(1-\varepsilon)}{2}.
\]
Their bound is
\[
\sigma_{\mathrm{ex}}
\le
\max_{0\le\varepsilon_1,\varepsilon_2\le1}
\frac12\left(
1-\frac{R(\varepsilon_1)+R(\varepsilon_2)}2
+
\min\left\{
1,\,
\sigma+\frac{\sqrt{\varepsilon_1}+\sqrt{\varepsilon_2}}2
\right\}
\right).
\]

For
\[
1-\frac1{2\sqrt2}\le\sigma<1,
\]
this maximization can be evaluated exactly:
\[
\boxed{
\sigma_{\mathrm{ex}}
\le
1-\frac{(1-\sigma)^2-(1-\sigma)^4}{2}
}.
\]
The maximizing point of the displayed Remark 7.3 expression is
\[
\boxed{
\varepsilon_1=\varepsilon_2=(1-\sigma)^2
}.
\]

The result strictly improves the source's uniform Proposition 7.1 bound
\[
1-\frac{(1-\sigma)^2}{4}
\]
throughout the stated interval. In particular, if
\[
\sigma=1-\frac1q
\qquad(q\ge3),
\]
then
\[
\sigma_{\mathrm{ex}}
\le
1-\frac1{2q^2}+\frac1{2q^4}.
\]
Thus the leading rejection probability improves from
\[
\frac1{4q^2}
\]
to
\[
\frac1{2q^2}-\frac1{2q^4},
\]
doubling the leading constant in the high-soundness regime.

## Assumptions and scope
The statement evaluates the explicit upper-bound maximization written in Remark 7.3 of arXiv:2607.21477v1. It does not claim that this upper bound is the exact operational soundness of every converted protocol.

The result applies when
\[
0<a=1-\sigma\le\frac1{2\sqrt2}.
\]
This restriction is chosen so that every point relevant to the optimizing boundary lies inside the first branch
\[
0\le\varepsilon\le\frac12
\]
of the exact product-test curve, where
\[
R(\varepsilon)=\varepsilon-\varepsilon^2.
\]
No formula is claimed here for lower values of \(\sigma\), where additional pieces of the exact product-test curve can enter the optimization.

## Proof
Put
\[
x=\sqrt{\varepsilon_1},
\qquad
y=\sqrt{\varepsilon_2}.
\]
The source's upper-bound objective becomes
\[
F(x,y)
=
\frac12\left(
1-\frac{R(x^2)+R(y^2)}2
+
\min\left\{
1,\,
1-a+\frac{x+y}{2}
\right\}
\right).
\]

First consider the unsaturated region
\[
x+y\le2a.
\]
Because
\[
2a\le\frac1{\sqrt2},
\]
both \(x\) and \(y\) lie in the first branch of the exact curve, so
\[
R(x^2)=x^2-x^4.
\]
In this region,
\[
F(x,y)
=
1-\frac a2
+
\frac14\left[
x-R(x^2)+y-R(y^2)
\right].
\]
Define
\[
h(x)=x-R(x^2)=x-x^2+x^4.
\]
Then
\[
h'(x)=1-2x+4x^3.
\]
The derivative is strictly positive on
\[
0\le x\le\frac1{\sqrt2}.
\]
Indeed its unique interior minimum occurs at \(x=1/\sqrt6\), where
\[
h'(1/\sqrt6)=1-\frac{4}{3\sqrt6}>0.
\]
Hence increasing either coordinate while staying in the unsaturated region strictly increases \(F\). Therefore no maximizer can satisfy
\[
x+y<2a.
\]

Now consider the saturated region
\[
x+y\ge2a.
\]
There
\[
F(x,y)=1-\frac{R(x^2)+R(y^2)}4.
\]
The function \(R\) is nondecreasing because \(\mathrm{PT}^{\le}_k(1-\varepsilon)\) is nonincreasing in \(\varepsilon\). Therefore a minimizer of
\[
R(x^2)+R(y^2)
\]
under \(x+y\ge2a\) can be moved coordinatewise down to the boundary
\[
x+y=2a.
\]
Thus every global maximizer of \(F\) lies on that boundary.

On
\[
x+y=2a
\]
we again have \(x,y\le2a\le1/\sqrt2\), so
\[
R(x^2)=x^2-x^4.
\]
Write
\[
x=a+z,\qquad y=a-z,\qquad |z|\le a.
\]
A direct expansion gives
\[
R(x^2)+R(y^2)-2R(a^2)
=
2z^2\left(1-6a^2-z^2\right).
\]
Since
\[
a^2\le\frac18
\quad\text{and}\quad
z^2\le a^2,
\]
the factor obeys
\[
1-6a^2-z^2
\ge
1-7a^2
\ge
\frac18>0.
\]
Consequently the boundary sum is uniquely minimized at
\[
z=0,
\]
that is,
\[
x=y=a.
\]
Equivalently,
\[
\varepsilon_1=\varepsilon_2=a^2.
\]

Substituting gives
\[
R(a^2)=a^2-a^4
\]
and therefore
\[
F(a,a)
=
1-\frac{a^2-a^4}{2}.
\]
Restoring \(a=1-\sigma\) proves
\[
\sigma_{\mathrm{ex}}
\le
1-\frac{(1-\sigma)^2-(1-\sigma)^4}{2}.
\]

To compare with Proposition 7.1, subtract the new bound from the source's uniform bound:
\[
\left(1-\frac{a^2}{4}\right)
-
\left(1-\frac{a^2-a^4}{2}\right)
=
\frac{a^2(1-2a^2)}4>0
\]
for the entire stated interval. Finally, setting \(a=1/q\) yields
\[
1-\frac1{2q^2}+\frac1{2q^4}.
\]

## Verification
The proof is symbolic and covers the full stated soundness interval. The only source-specific input is the exact Remark 7.3 objective and the first branch of the product-test rejection curve
\[
R(\varepsilon)=\varepsilon-\varepsilon^2
\qquad
(0\le\varepsilon\le1/2),
\]
which follows directly from Theorem 1.1.

The bundled checker verifies the algebraic boundary identity, the strict comparison with Proposition 7.1, and numerically maximizes the full piecewise Remark 7.3 objective on deterministic grids for representative soundness values. The finite grid is corroborative only; the universal result follows from the monotonicity and factorization arguments above.

## Relationship to prior work
Harrow and Montanaro introduced the product test and used it to prove the structural collapse
\[
\mathsf{QMA}(k)=\mathsf{QMA}(2)
\]
for \(k\ge2\). Their product-test analysis supplied an all-regimes linear rejection estimate sufficient for the complexity reduction.

Beckey, Granha Jeronimo, and Wu determine the exact product-test curve in every overlap regime. Proposition 7.1 uses only the optimal global linear consequence of that curve and obtains
\[
1-\frac{(1-\sigma)^2}{4}.
\]
Their Remark 7.3 explicitly retains the full curve and records the sharper two-parameter maximization used here, but leaves it in maximized form rather than evaluating it. The present theorem gives an analytic closed form for that expression throughout the high-soundness interval that includes every
\[
\sigma=1-\frac1q
\]
with integer \(q\ge3\).

A prior result for the same 2026 anchor analyzed a different question: the fixed-local-dimension product-test frontier inside the generalized three-qubit W family. It neither concerns the Section 7 QMA conversion nor implies the soundness optimization here.

## Limitations
The theorem evaluates the source's upper-bound expression; it does not prove matching adversarial witnesses for the converted QMA protocol. The soundness range is restricted to
\[
\sigma\ge1-\frac1{2\sqrt2}.
\]
Below that threshold, other pieces of the exact product-test curve can enter the optimization and a different piecewise analysis may be needed.

The source's continuity estimate on the verification branch is retained unchanged. Therefore any improvement requiring a sharper verification-branch continuity theorem is outside this result.

## References
1. J. Beckey, F. Granha Jeronimo, and P. Wu, *An Optimal Analysis of the Product Test*, arXiv:2607.21477v1, first public 2026-07-23.
2. A. W. Harrow and A. Montanaro, *Testing Product States, Quantum Merlin-Arthur Games and Tensor Optimization*, Journal of the ACM 60 (2013), Article 3, DOI 10.1145/2432622.2432625.
