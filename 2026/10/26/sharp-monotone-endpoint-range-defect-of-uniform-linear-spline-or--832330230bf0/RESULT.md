# Sharp monotone endpoint range defect of uniform linear-spline orthogonal projection

## Finding
For each integer \(n\ge1\), denote by \(P_n\) the \(L^2[0,1]\)-orthogonal projector onto continuous, piecewise-affine functions with equal subintervals and nodes \(j/n\), \(0\le j\le n\). Define
\[
r_1=\frac12,\quad r_{n+1}=\frac1{4-r_n},\qquad
\delta_n=\frac3{(2-r_n)(1+r_n)}-1.
\]
Every real, a.e. nondecreasing \(f\) with \(0\le f\le1\) a.e. satisfies the **sharp** endpoint inequalities
\[
-\delta_n\le (P_nf)(0)\le1,\qquad 0\le(P_nf)(1)\le1+\delta_n.
\]
The lower bound at the left endpoint is attained by \(f(t)=\mathbf1_{\{t\ge s_n\}}\) where \(s_n=1/[n(1+r_n)]\). The upper bound at the right endpoint is attained by the reflected step \(f(t)=\mathbf1_{\{t>1-s_n\}}\) (the jump convention on one point is irrelevant). The other endpoint bounds are attained by constant functions. The values are
\[
\delta_1=\frac13,\quad\delta_2=\frac{13}{36},\quad
\delta_3=\frac{181}{495},\qquad
\delta_n\nearrow\frac{\sqrt3-1}{2}.
\]
The limit is the smallest uniform-in-\(n\) constant for these boundary inequalities and is strictly larger than every finite-grid value.

## Assumptions and scope
The domain is the closed interval with Lebesgue measure; the projection is the genuine continuous piecewise-linear \(L^2\)-orthogonal projection, **not** nodal interpolation. Point evaluation applies to the continuous projected spline. The input may have jumps and is interpreted as an equivalence class in \(L^2\). Monotonicity means that a nondecreasing representative exists. The statement is for every finite integer \(n\ge1\) and all such real inputs. Rescaling to \([0,n]\) does not change projector coefficients or the dimensionless range inequalities.

## Proof
**1. Endpoint kernel and its sign structure.** On the rescaled interval \([0,n]\), let \(\phi_j\) be the standard hat functions. Their Gram matrix is \(M=T/6\), with \(T_{00}=T_{nn}=2\), \(T_{jj}=4\) for \(1\le j<n\), and \(T_{j,j+1}=T_{j+1,j}=1\). If \(B=M^{-1}\), the reproducing kernel at the left endpoint is \(K(t)=\sum_{j=0}^n B_{0j}\phi_j(t)\). Write \(B_{0j}=(-1)^j a_j\). The first row of \(TB=6I\) gives
\[
2a_0-a_1=6,\quad a_{j-1}-4a_j+a_{j+1}=0\ (1\le j<n),\quad a_{n-1}=2a_n.
\]
With \(\rho=2-\sqrt3\), the unique solution is
\[
a_j=c_n(\rho^j+\rho^{2n-j}),\quad
r_n=\frac{a_1}{a_0}=\frac{\rho+\rho^{2n-1}}{1+\rho^{2n}},\quad
a_0=\frac6{2-r_n},\quad c_n=\frac{a_0}{1+\rho^{2n}}.
\]
These formulas yield \(a_0>a_1>\cdots>a_n>0\). The successive differences \(d_j=a_j-a_{j+1}\) are positive and strictly decreasing for \(0\le j<n\); this follows directly from \(d_j=c_n(1-\rho)(\rho^j-\rho^{2n-j-1})\). Eliminating one terminal cell in the positive recurrence gives \(r_1=1/2\), \(r_{n+1}=1/(4-r_n)\).

**2. Monotone data reduce to one jump.** Put \(E(s)=\int_s^n K(t)\,dt\). Since constants are reproduced, \(E(0)=1\) and \(E(n)=0\). Every bounded nondecreasing \(f\) is, up to a null set, a nonnegative constant plus a positive mixture of right-hand step indicators, with total weight at most one. Thus it suffices to bound the scalar step response \(E(s)\) for \(0\le s\le n\). The normalized jump location on \([0,1]\) is \(s/n\).

**3. The first cell gives the precise worst undershoot.** On \(0\le t\le1\), \(K(t)=a_0-(a_0+a_1)t\). The tail \(E(s)\) has its unique minimum on this cell at \(u_n=a_0/(a_0+a_1)=1/(1+r_n)\); its value is
\[
E(u_n)=1-\frac{a_0^2}{2(a_0+a_1)}=-\delta_n,
\quad \delta_n=\frac3{(2-r_n)(1+r_n)}-1.
\]
Elsewhere on the first cell, \(-\delta_n\le E(s)\le1\).

**4. No later cell can produce a competing extreme.** For integers \(1\le j\le n\), the alternating-series estimate gives
\[
E(j)=\frac12\sum_{k=j}^{n-1}(-1)^k d_k,
\qquad |E(j)|\le\frac{d_j}{2}\le\frac{d_1}{2}
\quad (j<n),\qquad E(n)=0.
\]
Every cell contains exactly one zero of \(K\); the additional critical value of \(E\) in cell \([j,j+1]\) is
\[
E\!\left(j+\frac{a_j}{a_j+a_{j+1}}\right)
=E(j+1)+(-1)^{j+1}\frac{a_{j+1}^2}{2(a_j+a_{j+1})}.
\]
For \(j\ge1\), its magnitude is at most \(a_{j+1}\): use \(|E(j+1)|\le d_{j+1}/2\le a_{j+1}/2\), or \(E(n)=0\) at the final cell, and the triangular area is at most \(a_{j+1}/2\). For \(n\ge3\), the recurrence and \(\rho<r_n\le r_3=7/26\) imply
\[
\frac{d_1}{2}=\frac{3(1-3r_n)}{2-r_n}
\le9-5\sqrt3<\frac{181}{495}\le\delta_n,
\qquad
a_2=\frac{6(4r_n-1)}{2-r_n}\le\frac4{15}<\delta_n.
\]
Since the \(a_j\) decrease, every boundary and critical value in every cell after the first lies in \([-\delta_n,\delta_n]\). For \(n=2\), the only later-cell boundary and critical values are \(-1/4,\ 1/12,\ 0\), whereas \(\delta_2=13/36\). For \(n=1\), there are no later cells. Therefore \(-\delta_n\le E(s)\le1\) throughout \([0,n]\). The first-cell minimum is the unique global minimum, proving sharpness by a single jump.

**5. Both endpoints and the all-grid limit.** The monotone-mixture representation gives \(-\delta_n\le(P_nf)(0)\le1\). Reflection \(t\mapsto1-t\), followed by \(f\mapsto1-f\), yields \(0\le(P_nf)(1)\le1+\delta_n\) and its sharp step witness. The map \(r\mapsto1/(4-r)\) strictly decreases \(r\) when \(2-\sqrt3<r\le1/2\), and its stable fixed point is \(\rho=2-\sqrt3\). The function \(r\mapsto3/[(2-r)(1+r)]-1\) decreases for \(\rho\le r<1/2\); hence \(\delta_n\) strictly increases to its value at \(r=\rho\), namely \((\sqrt3-1)/2\). As the finite values are strictly smaller, no finite grid attains the all-grid constant.

## Verification
The standalone script `spline_boundary_verify.py` uses Python standard-library exact rational arithmetic. For every \(1\le n\le120\), it reconstructs the endpoint Gram-inverse row from the stated rational recurrence, tests the alternating coefficients and terminal equation, enumerates every cell boundary and every stationary point of the step response, and verifies exactly that its minimum is \(-\delta_n\) and its maximum is \(1\). SymPy independently checked the identities \(\delta_1=1/3\), \(\delta_2=13/36\), \(\delta_3=181/495\), the limit, and the decisive symbolic inequalities. These finite calculations are supplementary; the proof above treats all \(n\).

## Relationship to prior work
Oswald (2006) records classical, input-unrestricted \(L^\infty\)-stability of one-dimensional linear-spline \(L^2\) projection and studies unboundedness phenomena in higher dimensions. Passenbrunner (2011) discusses the sharp uniform-mesh unrestricted projector norm \(2\) and computes related Gram-kernel quantities in a periodic Franklin setting. An unrestricted norm bound \(2\) yields a generic nonnegative-input range \([-1/2,3/2]\), not the sharper, sharp monotone **boundary** range here. Previously studied finite-knot unrestricted positivity defects and periodic spline projection norms likewise neither state nor logically imply the monotone boundary extremum. This work does not assert novelty for the underlying inverse Gram matrix, its linear recurrence, or the classical \(L^\infty\) projector bound.

## Limitations
Only a uniform **one-dimensional** grid and the **two endpoint evaluations** are classified. Interior nodal values, continuous evaluation throughout the interval, nonuniform grids, higher-degree splines, and unrestricted bounded inputs are not covered. The originality comparison is limited by one relevant 2013 spline-projection chapter for which full text was not accessible; its abstract focuses on triangulations and norm bounds rather than order-constrained endpoint evaluations. Possible unindexed equivalent calculations remain a risk. No independent review or external certification is claimed.

## References
1. P. Oswald, *A counterexample concerning the L2-projector onto linear spline spaces*, arXiv:math/0611573v1, first posted 2006-11-19, https://arxiv.org/abs/math/0611573.
2. M. Passenbrunner, *The Lebesgue Constant for the Periodic Franklin System*, arXiv:1103.1950v1, first posted 2011-03-10, https://arxiv.org/abs/1103.1950.
3. P. Oswald, *L-infinity Bounds for the L2-Projection onto Linear Spline Spaces*, Springer Proceedings in Mathematics & Statistics 25 (2013), pp. 303–316, DOI: 10.1007/978-1-4614-4565-4_24 (full text not inspected).
