# A trapezoid disproves parameter-independent \(p\)-critical points

## Finding

Let
\[
K=\operatorname{conv}\{(-1,-1),(1,-1),(1/2,1),(-1/2,1)\}\subset\mathbb R^2.
\]
For \(1<p<\infty\), let \(x_p\) denote the unique \(p\)-critical point of \(K\) for Guo's \(p\)-Minkowski measure of asymmetry.

Then \(x_p\) is not independent of \(p\). More precisely,
\[
x_p=(0,t_p),
\]
and
\[
-\frac{103}{1000}<t_2<-\frac{102}{1000},
\qquad
-\frac{119}{1000}<t_3<-\frac{118}{1000}.
\]
Thus
\[
x_2\ne x_3.
\]
Since reflection symmetry forces every \(x_p\) onto the vertical symmetry axis,
\[
\boxed{\dim\operatorname{conv}\{x_p:1<p<\infty\}=1.}
\]

This gives a negative answer to Problem 5.4 of Lai and Jin, which asks whether the finite-\(p\) critical points of every convex body always coincide.

## Assumptions and scope

For a convex body \(C\subset\mathbb R^n\), a point \(x\in\operatorname{int}C\), and \(1\le p<\infty\), write
\[
h_x(C,u)=h(C,u)-\langle x,u\rangle
\]
and
\[
\alpha_x(C,u)=\frac{h_x(C,-u)}{h_x(C,u)}.
\]
The probability measure used in the \(p\)-measure of asymmetry is
\[
dm_x(C,u)=\frac{h_x(C,u)\,dS(C,u)}{nV(C)}.
\]
Hence
\[
\mu_p(C,x)^p
=
\frac1{nV(C)}
\int_{S^{n-1}}
h_x(C,u)^{1-p}h_x(C,-u)^p\,dS(C,u).
\]
A \(p\)-critical point minimizes \(\mu_p(C,\cdot)\) over the interior.

The published uniqueness theorem states that for every convex body and every \(1<p<\infty\), the \(p\)-critical point is unique. That theorem is used here only for the symmetry reduction from two coordinates to one; the subsequent optimization is explicit.

## Proof

The trapezoid \(K\) is invariant under reflection
\[
R(x,y)=(-x,y).
\]
The functional \(\mu_p(K,\cdot)\) is equivariant under this reflection. Since the \(p\)-critical point is unique for \(1<p<\infty\), it must be fixed by \(R\). Therefore
\[
x_p=(0,t_p)
\]
for some
\[
-1<t_p<1.
\]

The area of \(K\) is \(3\). Its bottom edge has length \(2\), its top edge has length \(1\), and the two sloping edges are congruent.

For \(x=(0,t)\), the bottom edge has
\[
h_x(u)=1+t,
\qquad
h_x(-u)=1-t,
\]
while the top edge has these two quantities reversed.

For either sloping edge, using its unit outer normal and multiplying by its edge length, the two congruent contributions together reduce exactly to
\[
(3-t)^{1-p}(5+t)^p.
\]
Consequently
\[
6\mu_p(K,(0,t))^p
=
B_p(t),
\]
where
\[
B_p(t)
=
2(1+t)^{1-p}(1-t)^p
+
(1-t)^{1-p}(1+t)^p
+
(3-t)^{1-p}(5+t)^p.
\]

For positive affine functions \(a(t)\) and \(b(t)\), set
\[
f(t)=a(t)^{1-p}b(t)^p.
\]
A direct differentiation gives
\[
f''(t)
=
p(p-1)f(t)
\left(
\frac{a'(t)}{a(t)}
-
\frac{b'(t)}{b(t)}
\right)^2.
\]
Thus every summand of \(B_p\) is convex. The bottom-edge summand is strictly convex on \((-1,1)\), so \(B_p\) is strictly convex there. Also \(B_p(t)\to\infty\) as \(t\to\pm1\). Hence \(B_p\) has exactly one minimizer, characterized by
\[
B_p'(t)=0.
\]

For \(p=2\), simplification gives
\[
B_2'(t)
=
\frac{4q_2(t)}
{(3-t)^2(1-t)^2(1+t)^2},
\]
where
\[
q_2(t)
=
15t^4+12t^3-78t^2+60t+7.
\]
Exact rational substitution gives
\[
q_2\!\left(-\frac{103}{1000}\right)
=
-\frac{3785292157}{200000000000}<0
\]
and
\[
q_2\!\left(-\frac{102}{1000}\right)
=
\frac{717214403}{12500000000}>0.
\]
Strict convexity therefore places the unique minimizer in
\[
-\frac{103}{1000}<t_2<-\frac{102}{1000}.
\]

For \(p=3\),
\[
B_3'(t)
=
-\frac{4q_3(t)}
{(3-t)^3(1-t)^3(1+t)^3},
\]
where
\[
q_3(t)
=
45t^7+169t^6-507t^5+681t^4-1153t^3+1155t^2-561t-85.
\]
Exact rational substitution gives
\[
q_3\!\left(-\frac{119}{1000}\right)
=
\frac{41414090584371091849}{200000000000000000000}>0
\]
and
\[
q_3\!\left(-\frac{118}{1000}\right)
=
-\frac{1064519557340180471}{1562500000000000000}<0.
\]
Therefore
\[
-\frac{119}{1000}<t_3<-\frac{118}{1000}.
\]

The two isolating intervals are disjoint, so
\[
x_2\ne x_3.
\]
All finite-\(p\) critical points lie on one line and at least two are distinct, which proves
\[
\dim\operatorname{conv}\{x_p:1<p<\infty\}=1.
\]

## Verification

The accompanying `verify.py` checks the two polynomial sign brackets using exact rational arithmetic, verifies that the intervals are disjoint, evaluates the exact one-variable objective near each isolated minimizer, and rechecks the strict-convexity identity used in the proof.

The replay output is:

`VERIFY_OK p-critical trapezoid counterexample`

The numerical bisections in the checker are only consistency checks. The separation of \(x_2\) and \(x_3\) is certified by exact rational signs together with the analytic strict-convexity proof.

## Relationship to prior work

Guo introduced the \(p\)-measures of asymmetry and their \(p\)-critical points. Huang and Guo later proved continuity of \(p\)-critical points with respect to \(p\) on \((1,\infty)\) and studied their relation to Minkowski-critical points.

Lai and Jin restate the uniqueness theorem for finite \(p>1\), exhibit two special quadrilaterals for which all finite-\(p\) critical points coincide, and then ask in Problem 5.4 whether this coincidence holds for every convex body. Their full text gives the normalized \(L_p\)-mixed-volume formula used above and explicitly states the problem.

The trapezoid here has the opposite behavior: already \(p=2\) and \(p=3\) have disjoint certified critical-point intervals. Targeted searches for the problem number, \(p\)-critical quadrilaterals and trapezoids, finite-\(p\) dependence, and the two derivative polynomials did not locate an equivalent counterexample.

## Limitations

The result answers the coincidence question negatively but does not classify bodies for which all finite-\(p\) critical points coincide.

The 2015 paper devoted specifically to properties of \(p\)-critical points was available through a public PDF endpoint, but the accessible extraction in this run exposed only its opening material and definitions; the remainder could not be fully inspected through that endpoint. Its abstract describes continuity, limiting behavior, and approximation, not a counterexample to parameter independence. This incomplete full-text access is retained as a residual originality risk.

Because the counterexample is elementary after writing the polygonal objective, an equivalent unindexed observation remains possible.

## References

D. Lai and H. Jin, “The \(\phi\)-Brunn–Minkowski inequalities for general convex bodies,” Boletín de la Sociedad Matemática Mexicana 27 (2021), article 78, DOI 10.1007/s40590-021-00387-3.

X. Huang and Q. Guo, “On Properties of \(p\)-Critical Points of Convex Bodies,” Communications in Mathematical Research 31 (2015), 161–170, DOI 10.13447/j.1674-5647.2015.02.07.

Q. Guo, “On \(p\)-measures of asymmetry for convex bodies,” Advances in Geometry 12 (2012), 287–301, DOI 10.1515/ADVGEOM.2011.052.
