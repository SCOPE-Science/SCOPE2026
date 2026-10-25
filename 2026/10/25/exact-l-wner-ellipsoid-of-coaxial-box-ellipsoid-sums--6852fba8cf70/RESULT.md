# Exact Löwner ellipsoid of coaxial box–ellipsoid sums

## Finding

For every integer \(d\ge2\), let \(a_i,b_i>0\), and form the Minkowski sum of an axis-aligned box and a coaxial, nondegenerate ellipsoid:

\[
K(a,b)=\prod_{i=1}^d[-a_i,a_i]+\left\{y\in\mathbb R^d:\sum_{i=1}^d\frac{y_i^2}{b_i^2}\le1\right\}.
\]

There is a unique \(\kappa>0\) such that, upon defining

\[
q_i=\frac{\sqrt{a_i^2+4\kappa b_i^2}-a_i}{2}>0,
\qquad \sum_{i=1}^d\frac{q_i^2}{b_i^2}=1,
\]

the unique minimum-volume enclosing ellipsoid (Löwner ellipsoid) of \(K(a,b)\) is

\[
\boxed{\quad E_* =\left\{x:\sum_{i=1}^d\frac{x_i^2}{d(a_i+q_i)^2}\le1\right\}.\quad}
\]

Its complete set of contacts with the rounded box is exactly

\[
\boxed{\quad\partial K(a,b)\cap\partial E_*
=\left\{(\varepsilon_i(a_i+q_i))_{i=1}^d:
\varepsilon_i\in\{-1,+1\}\right\}.\quad}
\]

The volume normalized by that of the unit ball is exactly

\[
\frac{\operatorname{vol}_d(E_*)}{\operatorname{vol}_d(B_2^d)}
=d^{d/2}\prod_{i=1}^d(a_i+q_i).
\]

This is a global optimum among every translated and rotated ellipsoid, not only axis-aligned candidates.

## Assumptions and scope

The dimension \(d\) is any integer at least two. All box half-widths and input ellipsoid semiaxes are strictly positive real numbers. The axis directions of the box and input ellipsoid agree; arbitrary relative rotations are not covered. Translation of both summands is immaterial by translation covariance. The same formulas include the Euclidean rounded orthotope when all \(b_i\) agree. The endpoint with a vanishing half-width follows by a limit in the formula but is not needed for the asserted exact contact classification.

## Proof

**1. Existence of the scalar parameter.** For \(\kappa>0\), the unique nonnegative root of \(q_i(a_i+q_i)=\kappa b_i^2\) is

\[
q_i(\kappa)=\frac{2\kappa b_i^2}{a_i+\sqrt{a_i^2+4\kappa b_i^2}}.
\]

Each \(q_i(\kappa)\) is continuous and strictly increasing, with limit zero at \(\kappa\downarrow0\) and infinity as \(\kappa\uparrow\infty\). Therefore \(\sum_i q_i(\kappa)^2/b_i^2\) increases continuously and strictly from zero to infinity; exactly one parameter gives one. Write \(s_i=a_i+q_i\), so \(q_i s_i=\kappa b_i^2\).

**2. An exact nonnegative containment certificate.** For every \(t\in\mathbb R^d\) the following polynomial identity holds:

\[
\boxed{
1-\frac1d\sum_{i=1}^d\frac{(a_i+t_i)^2}{s_i^2}
=\frac{1-\sum_i t_i^2/b_i^2}{d\kappa}
+\sum_{i=1}^d\frac{a_i(t_i-q_i)^2}{d\kappa b_i^2s_i}.}
\]

For direct verification, expand the right-hand side and substitute \(q_i s_i=\kappa b_i^2\) and \(\sum_iq_i^2/b_i^2=1\); the quadratic, linear, and constant coefficients match term by term. In particular, whenever \(\sum_i t_i^2/b_i^2\le1\) and \(t_i\ge0\), both terms on the right are nonnegative. Since \(a_i>0\), equality holds exactly when \(t_i=q_i\) for every coordinate.

Every \(x\in K(a,b)\) can be written \(x=v+y\) with \(|v_i|\le a_i\) and \(\sum_i(y_i/b_i)^2\le1\). Put \(t_i=|y_i|\). Then \(|x_i|\le a_i+t_i\), and the identity shows

\[
\sum_i\frac{x_i^2}{d s_i^2}\le
\sum_i\frac{(a_i+t_i)^2}{d s_i^2}\le1.
\]

Thus \(K(a,b)\subseteq E_*\). Equality requires \(t=q\), coordinatewise equality in \(|v_i+y_i|\le a_i+|y_i|\), and hence \(v_i=\varepsilon_i a_i\), \(y_i=\varepsilon_i q_i\) for some signs \(\varepsilon_i\). Conversely every such sum belongs to \(K(a,b)\) because \(\sum_i q_i^2/b_i^2=1\), and lies on \(\partial E_*\). This proves the complete contact classification.

**3. Global uniqueness certificate.** Rescale coordinates by \(z_i=x_i/(\sqrt d\,s_i)\), taking \(E_*\) to the Euclidean unit ball and all its \(2^d\) contact points to \(z_\varepsilon=\varepsilon/\sqrt d\). Uniform averaging over independent signs gives

\[
\mathbb E z_\varepsilon=0,
\qquad \mathbb E(z_\varepsilon z_\varepsilon^{\mathsf T})=I_d/d.
\]

Let any possibly translated or rotated ellipsoid \(E'\) containing all the contacts be given in transformed coordinates by \((z-c)^{\mathsf T}Q^{-1}(z-c)\le1\), where \(Q\) is positive definite. Averaging its contact inequalities yields

\[
\frac{\operatorname{tr}(Q^{-1})}{d}+c^{\mathsf T}Q^{-1}c\le1.
\]

The arithmetic–geometric mean inequality for the positive eigenvalues of \(Q^{-1}\) implies \(\det(Q)\ge1\). Therefore \(E'\) has volume at least that of the transformed unit ball. Equality forces \(c=0\) and all eigenvalues of \(Q^{-1}\) to be one, so \(E'\) equals the unit ball. Undoing the rescaling proves the asserted unique global optimum. The product-of-semiaxes volume formula follows immediately.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It reconstructs the scalar by monotone bisection, checks the defining equations, verifies every one of the \(2^d\) sign contacts for each of 210 independently sampled parameter tuples, checks the exact polynomial certificate and random interior containments, and independently tests sampled support-function inequalities. Its execution produced \(29{,}400\) numerical diagnostics passing, plus the equal-width rounded-cube benchmark. Numerical tests do not prove the universal statements; the algebraic identity and trace–determinant argument do.

## Relationship to prior work

The contact-point criterion and global uniqueness principle are classical; Güler and Gürtuna (2007), Section 2, give a modern account. Their explicit solved bodies are slabs, truncated cones and ellipsoidal cylinders, rather than box–ellipsoid Minkowski sums. Halder (2018) studies minimum-volume optimization within parameterized outer ellipsoid families for Minkowski sums of ellipsoids; its main derivations do not state this true global optimum and its complete contact classification for a nondegenerate box plus a coaxial ellipsoid. Courteaux and coauthors (2025) address the exact box–ellipsoid sum as a set but propose intersections of bounding boxes for efficient enclosure, not the minimum-volume containing ellipsoid. These distinctions concern the mathematical implication of each claim, not differences in titles.

## Limitations

The result requires common principal axes; relative rotations of the box and input ellipsoid may require a different method. No extension to unequal rounding norms beyond the specified coaxial ellipsoid is claimed. Independent historical-priority checking is not performed; older specialized ellipsoidal containment treatments could conceivably include an equivalent scalar formula. The full text of the 2025 comparison was not accessible during inspection, so its cited sections and abstract support the stated narrower comparison but not a whole-document exclusion.

## References

1. O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707, first public 5 September 2007. https://arxiv.org/abs/0709.0707
2. A. Halder, *On the Parameterized Computation of Minimum Volume Outer Ellipsoid of Minkowski Sum of Ellipsoids*, arXiv:1803.08157, first public 21 March 2018. https://arxiv.org/abs/1803.08157
3. M. Courteaux et al., *Lightweight Implicit Approximation of the Minkowski Sum of an N-Dimensional Ellipsoid and Hyperrectangle*, Mathematics 13 (2025), 1326, https://doi.org/10.3390/math13081326.
