# Two simple negative Alexander roots for the residual exceptional pretzel family
## Finding
For every odd integer \(m\ge3\), put \(a=2m-1\) and \(P_a=P(a,-a-2,-(a+1)^2/2)\). For the monic degree-\(2a\) Alexander representative
\[
\Delta_a(t)=\frac{(t^{a+2}+1)(t^a+1)}{(t+1)^2}-m^2t^{a-1}(t-1)^2,
\]
the negative real zeros are exactly the simple reciprocal pair \(t_m^\pm=-e^{\pm x_m}\), where \(x_m>0\) is uniquely determined by
\[
\left(\frac{\sinh(mx)}{m\sinh x}\right)^2=1+\frac{1}{4m^2\cosh^2(x/2)}.
\]
Moreover,
\[
x_m=\frac{\sqrt3}{2m^2}+\frac{9\sqrt3}{40m^4}+O(m^{-6})
\]
as \(m\to\infty\) through odd integers. Thus the pair converges to \(-1\) at the sharp logarithmic scale \(m^{-2}\).

## Assumptions and scope
The parameter range is the residual exceptional three-strand pretzel family with \(a\equiv1\pmod4\), equivalently \(a=2m-1\) for odd \(m\ge3\). The displayed polynomial is the monic degree-\(2a\) representative from the cited source; multiplying by a Laurent unit does not change any nonzero root. The claim concerns only negative real roots.

## Proof
Set \(t=-e^x\) with \(x\in\mathbb R\). Direct substitution into the displayed polynomial gives
\[
-e^{-ax}\Delta_a(-e^x)=\left(\frac{\sinh(mx)}{\sinh(x/2)}\right)^2-1-4m^2\cosh^2(x/2).
\]
At \(x=0\) the right side has limiting value \(-1\), so \(t=-1\) is not a root. For \(x\ne0\), division by \(4m^2\cosh^2(x/2)\), together with \(\sinh x=2\sinh(x/2)\cosh(x/2)\), shows that roots are equivalent to
\[
A_m(x)^2=B_m(x),\qquad
A_m(x)=\frac{\sinh(mx)}{m\sinh x},\qquad
B_m(x)=1+\frac{1}{4m^2\cosh^2(x/2)}.
\]
Both sides are even. On \(x>0\), \(B_m\) is strictly decreasing from \(1+1/(4m^2)\) to \(1\). Also \(A_m\) increases strictly from \(1\) to infinity, because
\[
\frac{d}{dx}\log A_m(x)=m\coth(mx)-\coth x>0,
\]
and the last inequality is equivalent to \(m\tanh x>\tanh(mx)\), which follows strictly for every integer \(m>1\) from the addition formula for \(\tanh\) by induction. Hence there is exactly one solution \(x_m>0\). Evenness gives exactly \(\pm x_m\), and the strict crossing makes both roots simple. The map \(x\mapsto-e^x\) is a bijection from \(\mathbb R\) to the negative real axis, so these are all negative real roots; the two are reciprocal because the parameters are \(\pm x_m\).

For the asymptotic, write \(\varepsilon=m^{-2}\) and \(z=m^2x/2\). Uniform Taylor expansion for bounded \(z\) gives
\[
A_m(x)^2=1+\frac{4z^2}{3}\varepsilon+\left(\frac{32z^4}{45}-\frac{4z^2}{3}\right)\varepsilon^2+O(\varepsilon^3),
\]
while
\[
B_m(x)=1+\frac14\varepsilon+O(\varepsilon^3).
\]
After division by \(\varepsilon\), the limiting positive equation is \(4z^2/3=1/4\), with simple root \(z_0=\sqrt3/4\). The implicit-function theorem therefore yields
\[
z=\frac{\sqrt3}{4}+\frac{9\sqrt3}{80}\varepsilon+O(\varepsilon^2),
\]
and substituting back gives the stated expansion for \(x_m\).

## Verification
The proof is analytic and does not infer an infinite statement from finite experiments. Independent symbolic expansion of the two sides through the required order reproduces the coefficients above. Numerical evaluations at several odd values of \(m\) were used only as sanity checks for the unique positive solution and the predicted scaling.

## Relationship to prior work
Saurabh isolates this residual exceptional pretzel family, gives the displayed Alexander polynomial, and proves failure of the Fox--Milnor factorization condition; that argument does not classify the polynomial's real roots or their asymptotic location. Lecuona's earlier treatment identifies the same exceptional family as determinant one and records the Alexander-polynomial computation in the context of sliceness obstructions, without a negative-root classification. Searches for the same family under its parameterization, Alexander polynomial, real-root terminology, reciprocal roots, and asymptotic root location did not locate a statement implying the result above.

## Limitations
No claim is made about positive real roots, nonreal roots, or exceptional pretzel families outside the stated branch. The literature comparison cannot exclude an older equivalent observation expressed under unrelated terminology, although the two most directly relevant sources and targeted searches were inspected.

## References
S. Saurabh, *Exceptional pretzel knots are not algebraically slice*, arXiv:2609.34522v1 (2026).

A. G. Lecuona, *On the slice-ribbon conjecture for pretzel knots*, Algebraic & Geometric Topology 15 (2015), 2133--2173, doi:10.2140/agt.2015.15.2133.
