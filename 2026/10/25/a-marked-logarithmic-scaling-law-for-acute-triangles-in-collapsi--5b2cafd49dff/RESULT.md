# A marked logarithmic scaling law for acute triangles in collapsing rectangles

## Finding

Let \(0<h<1\). Independently sample three points uniformly from the **interior** of the Euclidean rectangle \([0,1]\times[0,h]\). Order the points by horizontal coordinate, writing them \(P_i=(X_i,hY_i)\) with \(X_1<X_2<X_3\), and put \(U=X_2-X_1\), \(V=X_3-X_2\). Denote by \(A_h\) the event that all three angles of the resulting triangle are acute. Define its logarithmic horizontal gap coordinate by

\[
Z_h=\frac{\log(U/h)}{\log(1/h)}.
\]

**Marked limit theorem.** As \(h\downarrow0\), conditional on \(A_h\), the vector \((Z_h,Y_1,Y_2,Y_3)\) converges weakly to an explicitly given probability law. For \(y=(y_1,y_2,y_3)\in(0,1)^3\) with \(y_2\) strictly above both other ordinates, write \(a=y_2-y_1>0\) and \(b=y_2-y_3>0\); for \(y_2\) strictly below both, write \(a=y_1-y_2>0\) and \(b=y_3-y_2>0\). In both cases define

\[
w_+(y)=ab-b(a-b)_+ ,\qquad w_-(y)=ab-a(b-a)_+ ,\qquad (t)_+=\max(t,0).
\]

The limiting joint density with respect to \(dz\,dy_1\,dy_2\,dy_3\) is

\[
g(z,y)=6\mathbf 1_{\{y_2\text{ is a strict vertical extreme}\}}
\bigl[\mathbf 1_{(-1,0)}(z)w_-(y)+\mathbf 1_{(0,1)}(z)w_+(y)\bigr].
\]

Outside the displayed region the limiting density is zero. In particular,

\[
\boxed{\Pr(A_h)\sim h^2\log(1/h)}.
\]

Moreover, \(Z_h\), conditional on \(A_h\), converges to the uniform distribution on \((-1,1)\); **the limiting logarithmic gap is independent of the middle point's normalized height** \(Y_2\). That height has limiting density

\[
\boxed{f(t)=\frac52\bigl(t^4+(1-t)^4\bigr),\qquad 0<t<1.}
\]

These conditional geometric statements are the main contribution; the unmarked rectangle obtusity probability is already covered by earlier literature.

## Assumptions and scope

Uniform sampling means three independent two-dimensional Lebesgue-uniform points. The height coordinates \(Y_i\) are divided by the rectangle height after ordering by \(X_i\); they are not original point labels. Collinearity and right angles have probability zero for every positive \(h\). The convergence concerns the full conditional probability law and exact population probabilities, not noisy sampled estimates. All limit symbols refer to \(h\downarrow0\).

## Proof

**1. Horizontal spacing and the exact acute event.** The ordered horizontal gaps \(u=U\), \(v=V\) have joint density \(6(1-u-v)\) on \(u>0,v>0,u+v<1\), independent of the three independent uniform ordinates. The dot product at the middle point is

\[
-uv+h^2(y_2-y_1)(y_2-y_3).
\]

Thus acuteness forces \(y_2\) to be a strict vertical extreme. In either extreme case use the positive differences \(a,b\) in the finding. The three necessary and sufficient strict inequalities for an acute triangle are

\[
uv<h^2ab,\quad
u(u+v)+h^2a(a-b)>0,\quad
v(u+v)+h^2b(b-a)>0.
\]

The formulas for the lower and upper vertical extreme coincide because the vertical coordinate changes sign in both relevant vectors.

**2. Logarithmic change of variables.** Set \(L_h=\log(1/h)\), \(z=\log(u/h)/L_h\), and \(s=uv/h^2\). Then

\[
u=h^{1-z},\qquad v=h^{1+z}s,\qquad du\,dv=h^2L_h\,dz\,ds.
\]

By the middle-angle inequality, for an acute triangle \(0<s<ab\le1\). For each fixed \(-1<z<0\), as \(h\downarrow0\), \(u/h\to0\) and \(v/h\to\infty\); the other-angle conditions reduce respectively to \(s>a(b-a)_+\) and an automatic strict inequality. Consequently the admissible \(s\)-interval has limiting length \(w_-(y)\). For each fixed \(0<z<1\), the roles reverse, giving limiting length \(w_+(y)\). In both cases \(u+v\to0\).

For any bounded continuous test function supported in a compact subset of \((-1,0)\cup(0,1)\) in the logarithmic variable, dominated convergence (integrating \(0<s<1\) and \(0<y_i<1\)) yields

\[
\lim_{h\downarrow0}\frac{\mathbb E[\mathbf 1_{A_h}\varphi(Z_h,Y_1,Y_2,Y_3)]}{h^2L_h}
=\int\varphi(z,y)g(z,y)\,dz\,dy.
\]

No finite simulation is used in this argument.

**3. Excluding all logarithmic boundary scales.** The first acute inequality implies \(uv<h^2\). Fix \(0<\delta<1\). The complement of \(-1+\delta<Z_h<1-\delta\) lies in \(u<h^{2-\delta}\) or \(u>h^\delta\). Integrating the upper bound \(6\mathbf 1_{\{uv<h^2\}}\) against \(du\,dv\), and using \(0<v<\min(1,h^2/u)\), gives

\[
\Pr\bigl(A_h,\,Z_h\notin(-1+\delta,1-\delta)\bigr)
\le6h^2\bigl(1+2\delta L_h\bigr).
\]

After normalization, the upper bound tends to \(12\delta\). Letting \(\delta\downarrow0\) proves tightness on the interior logarithmic interval and rules out endpoint atoms or mass escaping beyond it.

**4. Exact normalization and marginal laws.** For \(y_2=t\) a vertical maximum, set \(a=t-y_1\), \(b=t-y_3\). Direct integration on \([0,t]^2\), with the analogous calculation for a minimum, gives

\[
\int_{[0,t]^2}w_+\,da\,db=\int_{[0,t]^2}w_-\,da\,db=\frac{5t^4}{24}.
\]

Indeed, \(w_++w_-=(a+b)\min(a,b)\); integrating over \(0<b<a<t\) and reflecting across the diagonal yields \(5t^4/12\), split equally by exchange of \(a\) and \(b\). Integrating over the two vertical extremes and \(0<t<1\) shows

\[
\int g(z,y)\,dz\,dy
=6\cdot 2\cdot2\cdot\frac5{24}\cdot\frac15=1.
\]

Thus the coefficient of \(h^2L_h\) in \(\Pr(A_h)\) is exactly one, and dividing the previously proved finite measures by this probability gives the asserted conditional weak convergence. At each \(-1<z<0\) or \(0<z<1\), integrating \(g\) over all ordinates gives \(1/2\): the logarithmic coordinate is uniform on \((-1,1)\). Integrating \(g\) over \(y_1,y_3\), at a fixed \(z\), yields

\[
\frac54\bigl(t^4+(1-t)^4\bigr)
=\frac12\, f(t),
\]

which proves both the stated vertical marginal and the limiting independence of \(z\) and \(Y_2\).

## Verification

The standalone Python 3 script `verify.py` checks the rational integral \(5/24\), both logarithmic half-masses, and exact density normalization, using rational arithmetic. It also performs deterministic-seed weighted sampling of the *exact finite-\(h\)* dot-product conditions with the correct Jacobian, for six heights ranging from \(0.05\) to \(10^{-9}\). The weighted estimates of the normalized rare-event probability approach one, the right logarithmic half approaches probability \(1/2\), and the middle-point height distribution agrees with the exact limiting distribution function \(\bigl(t^5+1-(1-t)^5\bigr)/2\) at four grid points. Numerical agreement is diagnostic only; the weak-convergence theorem follows from Steps 1–4.

## Relationship to prior work

Langford (1969) evaluated the probability that a triangle from three independently uniform **interior** points in a rectangle is obtuse for arbitrary aspect ratio. That is a stronger prior result for the **unmarked scalar probability**; the scalar leading-order asymptotic is **not claimed as an independent discovery**. The present theorem instead reconstructs the joint conditional *location geometry* of rare acute triangles, a property not determined by Langford's scalar probability alone. Khan (2017/2019) proves geometric-probability extremal results and bounds for slender convex bodies, but neither those bounds nor disk optimality specify this marked conditional limit. Beck (2025/2026) derives the scalar obtusity probability for uniform interior points of a three-dimensional cube and discusses Langford's distribution, not the collapsing-rectangle conditional spatial law. The difference between this interior-sampling problem and boundary-uniform rectangle triples is essential: those are distinct probability spaces with different coefficients and singular phenomena.

## Limitations

This theorem is restricted to rectangles with one side exactly one and other side tending to zero, and to three independent interior-uniform points. It does not give a uniform finite-\(h\) error estimate, does not extend the conditional density to arbitrary collapsing convex domains, and does not claim any characterization of the full triangle shape beyond the displayed marks. The 1969 Langford source was accessible only through bibliographic metadata and its abstract, not a readable full manuscript; an unlocated earlier marked theorem cannot be excluded. The established scalar probability formula is prior work and is not independently novel here.

## References

1. E. Langford, *The probability that a random triangle is obtuse*, Biometrika **56** (1969), 689–690, DOI: 10.1093/biomet/56.3.689, first published 1969-12-01. Available abstract and journal record: https://academic.oup.com/biomet/article-abstract/56/3/689/233941.
2. G. Khan, *Hall's Conjecture on Extremal Sets for Random Triangles*, arXiv:1704.05913, first submitted 2017-04-19, in particular Introduction, Theorems 1–4 and Sections 5–6. https://arxiv.org/abs/1704.05913.
3. D. Beck, *The Probability that a Random Triangle in a Cube is Obtuse*, arXiv:2501.11611, first submitted 2025-01-20; Journal of Applied Probability **63** (2026), 1263–1280, DOI: 10.1017/jpr.2026.10075, notably Sections 1 and 2. https://arxiv.org/abs/2501.11611.
