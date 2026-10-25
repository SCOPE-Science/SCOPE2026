# Exact two-mode axial constant-width volume bound

## Finding

Let \(e\in\mathbb S^2\), put \(t=u\cdot e\), and define the Legendre polynomials
\[
P_3(t)=\frac{5t^3-3t}{2},\qquad P_5(t)=\frac{63t^5-70t^3+15t}{8}.
\]
Suppose a convex body \(K_{a,b}\subset\mathbb R^3\) has support function
\[
h(u)=1+aP_3(u\cdot e)+bP_5(u\cdot e),\qquad a,b\in\mathbb R.
\]
Then \(h(u)+h(-u)=2\), so the body has constant width \(2\). Its volume is exactly
\[
\operatorname{vol}(K_{a,b})=\frac{4\pi}{3}-\frac{20\pi}{7}a^2-\frac{56\pi}{11}b^2.
\]
Among all convex bodies in this two-mode family,
\[
\operatorname{vol}(K_{a,b})\ge\frac{128\pi}{105},
\]
with equality if and only if \((a,b)=(1/5,0)\) or \((-1/5,0)\). Thus adding the fifth axial Legendre mode cannot improve on the cubic endpoint within this family.

## Assumptions and scope

The statement concerns full-dimensional convex bodies in \(\mathbb R^3\) whose support function is exactly the displayed finite expansion, with the axis \(e\) fixed. The degree-three and degree-five Legendre polynomials are odd, which fixes the width at \(2\). The result does not assert a volume minimum over all constant-width bodies and does not resolve the three-dimensional Blaschke–Lebesgue problem.

## Proof

For a smooth axial support function \(h(t)\), the two eigenvalues of the spherical curvature-radius matrix \(\nabla^2_{\mathbb S^2}h+hI\) are
\[
r_{\mathrm{az}}(t)=h(t)-t h'(t),\qquad
r_{\mathrm{mer}}(t)=h(t)-t h'(t)+(1-t^2)h''(t).
\]
Convexity requires both eigenvalues to be nonnegative for every \(t\in[-1,1]\). Write
\[
A_j=P_j-tP_j',\qquad B_j=P_j-tP_j'+(1-t^2)P_j''.
\]
Direct differentiation gives
\[
\begin{aligned}
A_3(t)&=-5t^3,& B_3(t)&=15t-20t^3,\\
A_5(t)&=\frac{35t^3-63t^5}{2},&
B_5(t)&=\frac{-210t+455t^3-378t^5}{2}.
\end{aligned}
\]
Consequently, \(r_{\mathrm{mer}}=1+aB_3+bB_5\). At \(t=\pm1\), the values \(B_3(1)=-5\) and \(B_5(1)=-14\) imply
\[
|5a+14b|\le1.
\]
At \(t=\pm\tfrac12\), the values \(B_3(\tfrac12)=5\) and \(B_5(\tfrac12)=-119/32\) imply
\[
\left|5a-\frac{119}{32}b\right|\le1.
\]
These are necessary conditions for every convex member of the family. Set
\[
x=5a+14b,\qquad y=5a-\frac{119}{32}b.
\]
Then \((x,y)\in[-1,1]^2\), and solving for the coefficients gives
\[
b=\frac{32}{567}(x-y),\qquad a=\frac{119x+448y}{2835}.
\]
The four vertices of this containing parallelogram in the \((a,b)\)-plane are
\[
(1/5,0),\quad(-1/5,0),\quad(-47/405,64/567),\quad(47/405,-64/567).
\]
The volume formula for a smooth support function in three dimensions is
\[
V=\frac13\int_{\mathbb S^2}h\det(\nabla^2_{\mathbb S^2}h+hI)\,d\sigma
 =\frac{2\pi}{3}\int_{-1}^{1}h(t)r_{\mathrm{az}}(t)r_{\mathrm{mer}}(t)\,dt.
\]
Substitution of the displayed polynomials and exact integration yields
\[
V=\frac{4\pi}{3}-\frac{20\pi}{7}a^2-\frac{56\pi}{11}b^2.
\]
In particular, the volume deficit \(D=4\pi/3-V\) is the positive-definite quadratic form
\[
D(a,b)=\pi\left(\frac{20}{7}a^2+\frac{56}{11}b^2\right).
\]
A convex function on a compact polygon attains its maximum at a vertex; strict convexity makes the inequality strict away from the maximizing vertices. At each of \((\pm1/5,0)\), the deficit is \(4\pi/35\). At each mixed vertex it is \(9668\pi/93555\), smaller by exactly \(1024\pi/93555\). Therefore the maximum possible deficit over the containing parallelogram is \(4\pi/35\), and it occurs only at \((\pm1/5,0)\).

It remains to check that these two endpoints are actually convex support functions. For \((a,b)=(1/5,0)\),
\[
r_{\mathrm{az}}(t)=1-t^3=(1-t)(1+t+t^2)\ge0,
\]
\[
r_{\mathrm{mer}}(t)=1+3t-4t^3=(1-t)(2t+1)^2\ge0.
\]
For \((a,b)=(-1/5,0)\), the corresponding radii are
\[
r_{\mathrm{az}}(t)=1+t^3=(1+t)(1-t+t^2)\ge0,
\]
\[
r_{\mathrm{mer}}(t)=1-3t+4t^3=(1+t)(2t-1)^2\ge0.
\]
Thus both endpoints are feasible convex bodies. Since \(4\pi/3-4\pi/35=128\pi/105\), the stated bound and equality classification follow.

## Verification

The exact volume identity is obtained by integrating the explicit polynomial integrand, not by numerical sampling. The necessary curvature constraints use only four specified normal parameters. The attached `verify.py` independently reconstructs the rational polynomials, performs the integral using exact fractions, and checks the four vertex values and endpoint factorizations. No finite experiment is used as evidence for an infinite-dimensional statement; the conclusion is restricted to the stated two-mode family.

## Relationship to prior work

Hynd's study of extreme constant-width bodies develops the support-function and curvature-radius framework for axially symmetric bodies and gives an extremality criterion in terms of the generating planar shape. The present result addresses a different question: volume minimization in the simultaneous degree-three/degree-five axial family. It is a finite-mode benchmark and does not claim global optimality among all bodies of constant width.

## Limitations

The two curvature samples provide necessary constraints and need not describe the entire feasible coefficient region. This is sufficient for the volume bound because the quadratic deficit is maximized over the larger parallelogram at feasible cubic endpoints. The result does not classify every feasible pair \((a,b)\), does not treat higher odd harmonics, and does not settle the full three-dimensional constant-width volume problem.

## References

1. R. Hynd, “On Extreme Constant Width Bodies in \(\mathbb R^3\),” arXiv:2501.16940v1 (first public version submitted 2025-01-28); *Discrete & Computational Geometry* 76 (2026), 838–865. DOI: 10.1007/s00454-025-00779-6.
