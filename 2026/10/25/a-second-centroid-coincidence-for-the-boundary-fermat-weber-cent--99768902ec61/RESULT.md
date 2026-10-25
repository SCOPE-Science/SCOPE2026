# A second centroid coincidence for the boundary Fermat–Weber center of an isosceles triangle

## Finding
For the Euclidean isosceles triangle with vertices \((-1,0)\), \((1,0)\), and \((0,h)\), let \(M_h\) minimize the total Euclidean distance to its boundary, integrated with respect to arclength. There is a **non-equilateral** height
\[
\frac1{10}<h_*<\frac18
\]
for which \(M_{h_*}\) equals the **area centroid** \((0,h_*/3)\). An independently forced second coincidence occurs for the equilateral height \(h=\sqrt3\). Thus equality of the perimeter-distance minimizer with the area centroid does not characterize equilateral triangles, even within the isosceles family.

Writing \(M_h=(0,hq(h))\), the strict signs \(q(1/10)>1/3\), \(q(1/8)<1/3\), \(q(1)<1/3\), and \(q(2)>1/3\) establish at least two changes in the centroid-relative order. The equilateral coincidence is transversal. The complete limiting behavior also satisfies
\[
q(h)=\frac12-\frac{1}{2\log(2/h)}+O\!\left(\frac1{\log^2(2/h)}\right)\quad(h\downarrow0),
\]
\[
q(h)=\frac12-\frac1{2h}+O\!\left(\frac{\log h}{h^2}\right)\quad(h\to\infty).
\]
These are statements about the arclength-uniform **boundary** measure, not the area-uniform geometric median and not the Fermat point of the three vertices. No claim is made that the listed coincidences are the only ones.

## Assumptions and scope
For each real \(h>0\), denote the filled triangle by \(T_h\), its boundary by \(\partial T_h\), and its perimeter by \(P_h=2+2\sqrt{1+h^2}\). For any point \(z\in\mathbb R^2\), define
\[
\Phi_h(z)=\int_{\partial T_h}\|z-w\|_2\,ds(w).
\]
Normalizing by \(P_h\) does not affect the minimizer. The geometric area centroid is \(G_h=(0,h/3)\). The minimizing point \(M_h\) is unique; \(q(h)\) is defined by \(M_h=(0,hq(h))\) and lies strictly between zero and one.

## Proof
**Uniqueness and scalar equation.** Each summand \(z\mapsto\|z-w\|_2\) is convex. Because the arclength measure on the three non-collinear sides is not concentrated on any line, \(\Phi_h\) is strictly convex. Reflection in the vertical axis and uniqueness place its minimizer on that axis. Parameterizing the base by \((x,0)\), \(-1\le x\le1\), and each equal side by \((1-t,ht)\), \(0\le t\le1\), gives
\[
\Phi_h(0,y)=2\int_0^1\sqrt{x^2+y^2}\,dx+2s\int_0^1\sqrt{(1-t)^2+(ht-y)^2}\,dt,
\quad s=\sqrt{1+h^2}.
\]
At \(y=0\) its right derivative is negative; at \(y=h\) its left derivative is positive. Strict convexity gives a unique \(y=hq\) with \(0<q<1\). Differentiation at an interior point yields
\[
\frac{1}{2h}\,\partial_y\Phi_h(0,hq)=B_h(q)
=q\operatorname{arsinh}\!\left(\frac{1}{hq}\right)
+s\int_0^1\frac{q-t}{\sqrt{(1-t)^2+h^2(t-q)^2}}\,dt.
\]
The integral has the exact closed form
\[
B_h(q)=q\operatorname{arsinh}\!\left(\frac1{hq}\right)+
\frac{s\bigl(\sqrt{1+h^2q^2}-h(1-q)\bigr)-(1-q)
\left[\operatorname{arsinh}\!\left(\frac{1+h^2q}{h(1-q)}\right)+\operatorname{arsinh}h\right]}{1+h^2}.
\tag{1}
\]
To verify (1), set \(u=1-t\), \(b=1-q\), and substitute \(v=(1+h^2)u-h^2b\); the denominator reduces to \(\sqrt{v^2+h^2b^2}/s\). The unique root of \(B_h(q)=0\) is \(q(h)\); its continuous dependence on \(h\) follows from strict convexity and the implicit-function theorem in the interior.

**A second, non-equilateral coincidence.** At the centroid, \(q=1/3\), rigorous outward-rounded interval evaluation of the elementary expression (1) gives
\[
-0.019708<B_{1/10}(1/3)<-0.019707,
\quad
0.028512<B_{1/8}(1/3)<0.028514,
\]
\[
0.105096<B_1(1/3)<0.105099,
\quad
-0.029819<B_2(1/3)<-0.029816.
\]
Since the derivative of the strictly convex objective is increasing in \(q\), negative values place \(q(h)\) above \(1/3\) and positive values place it below \(1/3\). Continuity forces at least one \(h_*\in(1/10,1/8)\) with \(q(h_*)=1/3\). Root solving gives \(h_*\approx0.10925302496981034\), quoted only as a numerical approximation. The supplied standalone verifier checks the four strict inequalities using outward-rounded interval arithmetic; it separately compares (1) against direct numerical integration.

At \(h=\sqrt3\), the triangle is equilateral; threefold rotational symmetry and uniqueness force its minimizer to equal its centroid. Direct differentiation of (1), with \(q=1/3\) held fixed, gives
\[
\left.\frac{\partial B_h(1/3)}{\partial h}\right|_{h=\sqrt3}
=-\frac12+\frac{\sqrt3}{6}\operatorname{arsinh}\sqrt3<0,
\]
where the final inequality follows from \(\operatorname{arsinh}t<t\) for \(t>0\). Hence the equilateral coincidence is a genuine sign-changing crossing, not a tangency.

**Two singular-shape limits.** On every compact subinterval of \(0<q<1\), expansion of (1) as \(h\downarrow0\), uniformly in \(q\), gives
\[
B_h(q)=(2q-1)\log(2/h)+1-q\log q+(1-q)\log(1-q)+o(1).
\]
The unique zero therefore tends to \(1/2\). Substituting \(q=1/2+o(1)\) and using the fact that the constant term equals \(1\) at \(q=1/2\) yields the stated logarithmic correction, with an \(O(\log^{-2}(2/h))\) remainder (the elementary expansion error is smaller). Similarly, uniformly for \(q\) in a compact subinterval of \((0,1)\), (1) gives
\[
B_h(q)=2q-1+\frac1h+O\!\left(\frac{\log h}{h^2}\right)
\quad(h\to\infty).
\]
The unique zero again tends to \(1/2\), and substitution gives the second claimed expansion. All statements concern each fixed positive \(h\); the degenerate limiting triangles are not included in the theorem.

## Verification
Run `python3 verify.py` with Python 3 and `mpmath` (version 1.3 or later). The program produces rigorous interval enclosures for the four signs, computes the non-equilateral root for numerical illustration, verifies the equilateral case, and checks the derivative expression against independent high-precision quadrature. The analytic proof supplies the existence and asymptotic claims; finite computations are not substituted for the limiting arguments or strict convexity.

## Relationship to prior work
Zhang and Carlsson (arXiv:1403.3715v1, publicly posted 2014-03-14) derive a general closed expression and a Weiszfeld-type solver for the Euclidean continuous Fermat–Weber problem with polygon-boundary arclength demand. Their full paper was inspected; it establishes the general optimization framework but does not state the present isosceles centroid coincidences, the two-sided asymptotic profile, or the rigorous centroid-order sign changes. Equation (1) is a specialized consequence of their integration framework, while the new geometric conclusions require the parameter comparison and singular-limit analysis above. Panov and Savvateev (arXiv:1811.07306v1, 2018) study the geometric median of a *filled* triangular domain under area measure; that different sampling measure does not imply the present boundary result. The geometric centroid and vertex Fermat point are also distinct notions.

## Limitations
The result proves existence of a non-equilateral coincidence in a certified interval, not uniqueness of that non-equilateral height or a complete count of all possible roots. The decimal parameter is an approximation, not an algebraic formula. The theorem concerns a one-parameter family of isosceles triangles with uniform perimeter measure; it does not classify all scalene triangles or weighted measures. Bibliographic search may miss an equivalent specialized older analysis, and no independent scientific audit has been performed.

## References
1. T. T. C. K. Zhang and J. G. Carlsson, *On the Continuous Fermat-Weber Problem for a Convex Polygon Using Euclidean Distance*, arXiv:1403.3715v1 (2014-03-14), https://arxiv.org/abs/1403.3715.
2. P. Panov and A. Savvateev, *On the geometric median of triangular domains and other median type points*, arXiv:1811.07306v1 (2018-11-18), https://arxiv.org/abs/1811.07306.
