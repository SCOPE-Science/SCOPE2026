# A boundary atom increases the sharp norm of linear-spline projection on equilateral stars

## Finding

Let \(m\ge2\) be an integer. Join \(m\) copies of \([0,1]\) at their left endpoints to form a compact metric star \(\Gamma_m\), with center \(o\) and leaves \(p_1,\ldots,p_m\). On each edge use ordinary arclength measure and add an atom of mass \(w>0\) at the **single leaf** \(p_1\):
\[
\mu_w=\sum_{j=1}^m dt\big|_{[o,p_j]}+w\delta_{p_1}.
\]
Let \(V_m\) consist of all continuous real functions that are affine on each edge, and let \(P_{m,w}\) be the orthogonal projector from \(L^2(\Gamma_m,\mu_w)\) to \(V_m\), regarded also as an operator from \(L^\infty(\mu_w)\) to continuous functions.

Define the positive rational function
\[
\Lambda_m(w)=\frac{N_m(w)}{3\,[m+(3m+1)w]\,(1+2w)\,[m+1+(3m+4)w]},
\]
where
\[
\begin{aligned}
N_m(w)={}&7m^2+3m+(56m^2+38m+3)w\\
&+(147m^2+137m+26)w^2+(126m^2+150m+48)w^3.
\end{aligned}
\]
Then, for every \(m\ge2\) and every \(w>0\),
\[
\boxed{\|P_{m,w}\|_{L^\infty\to L^\infty}=\Lambda_m(w).}
\]
**Exactly the unweighted leaves** \(p_2,\ldots,p_m\) are norming evaluation locations. The norming data at any such leaf are exactly the two signs of its reproducing kernel, modulo \(\mu_w\)-null sets. There are no norming interior-edge points, no norming center, and no norming atom-bearing leaf.

Moreover, \(\Lambda_m(w)\) is strictly increasing in \(w\), and
\[
\Lambda_m(0)=\frac{7m+3}{3(m+1)},\qquad
\lim_{w\to\infty}\Lambda_m(w)=\frac{21m^2+25m+8}{(3m+1)(3m+4)}<\frac73.
\]
The exact worst positivity loss is
\[
\boxed{\inf_{0\le f\le1}\ \min_{x\in\Gamma_m}(P_{m,w}f)(x)
=-\frac{\Lambda_m(w)-1}{2}.}
\]
An equality witness is the indicator of the negative set of a reproducing kernel at any unweighted leaf. Its value at the atom is zero.

For \(m=2\), the norm crosses \(2\) exactly once, at the unique positive root \(w_*=2.5218700740\ldots\) of
\[
12w^3-24w^2-15w-2=0.
\]
Thus \(\Lambda_2(w)<2\) below that root and \(\Lambda_2(w)>2\) above it. For \(m=3\) the norm is strictly greater than \(2\) for every \(w>0\); for \(m\ge4\) it is already strictly greater than \(2\) at zero atom mass. Finally \(\lim_{m\to\infty}\Lambda_m(w)=7/3\) for every fixed \(w\ge0\).

## Assumptions and scope

All data and spline coefficients are real. Edge lengths are exactly one; the added atom is supported at precisely one outer leaf, not the common center. The arclength measure is unnormalized, which does not change orthogonal projection. The \(L^\infty(\mu_w)\) norm includes the atomic input value at \(p_1\); outputs have continuous representatives. No boundary conditions are imposed other than continuity at the center. The theorem is not about affine functions on the entire ambient Euclidean space or about spline spaces with additional edge-interior knots.

## Proof

**1. Reproducing kernel.** Denote the standard hat functions by \(\phi_0,\phi_1,\ldots,\phi_m\), with \(\phi_0(o)=1\) and \(\phi_j(p_k)=\delta_{jk}\). On edge \(j\), at coordinate \(t\in[0,1]\), the only nonzero hats are \(\phi_0=1-t\) and \(\phi_j=t\). The arclength Gram matrix \(G_0\) obeys
\[
(G_0)_{00}=\frac m3,\quad (G_0)_{0j}=\frac16,\quad (G_0)_{jk}=\frac13\delta_{jk},
\]
with exact inverse
\[
(G_0^{-1})_{00}=\frac4m,\qquad
(G_0^{-1})_{0j}=-\frac2m,\qquad
(G_0^{-1})_{jk}=3\delta_{jk}+\frac1m.
\]
The atom changes only \((G_w)_{11}\): \(G_w=G_0+w e_1 e_1^{\mathsf T}\). Sherman--Morrison applies because \(G_0\) is strictly positive definite. Write
\[
q=\frac{w}{m+(3m+1)w},\qquad 0<q<\frac1{3m+1}.
\]
The first-atom update has the exact form
\[
G_w^{-1}=G_0^{-1}-mq\,(G_0^{-1}e_1)(G_0^{-1}e_1)^{\mathsf T}.
\]
At any vertex \(v\), its reproducing kernel \(K_v(y)=\sum_{i,j}\phi_i(v)(G_w^{-1})_{ij}\phi_j(y)\) integrates to one against \(\mu_w\), since constants are in \(V_m\).

**2. Absolute kernel integrals.** Fix an unweighted leaf \(p_k\) with \(k\ge2\). Its continuous kernel on each edge is linear in \(t\). It has the common negative value \(-a\) at \(o\), where \(a=2(1-q)/m\). Its positive leaf-end values are
\[
 b_1=\frac{1-(3m+1)q}{m},\qquad
 b_k=3+\frac{1-q}{m},\qquad
 b_j=\frac{1-q}{m}\quad(j\notin\{1,k\}).
\]
The atom contributes \(wK_{p_k}(p_1)=q>0\) to the absolute kernel integral. Since all \(b_j>0\), the following elementary integral is valid without exceptional sign cases:
\[
J(a,b)=\int_0^1|{-a}+(a+b)t|\,dt=\frac{a^2+b^2}{2(a+b)}\quad(a,b>0).
\]
Therefore the leaf-kernel \(L^1(\mu_w)\) norm is exactly
\[
R_k=J(a,b_1)+J(a,b_k)+(m-2)J\!\left(a,\frac{1-q}{m}\right)+q.
\]
Putting the above \(q\) into this expression, taking common denominators, and cancelling gives \(R_k=\Lambda_m(w)\). At the atom-bearing leaf the same computation (or scaling the old kernel by \([1+w(3+1/m)]^{-1}\)) yields
\[
R_1=\frac{7m^2+3m+(9m^2+12m+3)w}
{3(m+1)[m+(3m+1)w]},
\]
and at the center it yields
\[
R_0=\frac{5m+(25m+5)w+(30m+18)w^2}
{3(1+2w)[m+(3m+1)w]}.
\]
These formulas include the atomic contribution to the kernel integral, as required.

**3. Exact dominance and equality points.** Let \(D=3[m+(3m+1)w](1+2w)[m+1+(3m+4)w]\). Direct expansion gives
\[
R_k-R_0=\frac{2A_m(w)}{D},
\]
where
\[
\begin{aligned}
A_m(w)={}&m(m-1)+(8m^2-6m-1)w\\
 &+(21m^2-13m-6)w^2+(18m^2-12m-12)w^3.
\end{aligned}
\]
Every coefficient is positive for every integer \(m\ge2\); this is explicit on setting \(m=k+2\), \(k\ge0\): the successive coefficients become \(k^2+3k+2\), \(8k^2+26k+19\), \(21k^2+71k+52\), and \(18k^2+60k+36\). Likewise,
\[
R_k-R_1=\frac{4wB_m(w)}{(m+1)D},
\]
where
\[
\begin{aligned}
B_m(w)={}&3m^3+4m^2+2m\\
&+(15m^3+24m^2+13m+2)w\\
&+(18m^3+33m^2+21m+6)w^2.
\end{aligned}
\]
Thus both differences are strictly positive. For an evaluation point on edge \([o,p_j]\) at coordinate \(t\), the kernel is \((1-t)K_o+tK_{p_j}\). Its \(L^1\) norm is convex in \(t\), so its maximum occurs at a vertex. Indeed it is strictly below the larger endpoint norm whenever \(0<t<1\), because \(K_o\) and \(K_{p_j}\) have opposite signs on a positive-measure neighborhood of the center. Only \(p_2,\ldots,p_m\) remain norming. At each, the reproducing kernel is nonzero except at finitely many edge positions, and is nonzero at the atom; hence equality in the integral duality bound forces the input to be its sign up to an overall sign and null sets.

**4. Strict monotonicity, limits, and the crossover.** Differentiation of the rational formula gives
\[
\frac{d\Lambda_m(w)}{dw}=
\frac{4E_m(w)}{3(1+2w)^2[m+(3m+1)w]^2[m+1+(3m+4)w]^2},
\]
where
\[
\begin{aligned}
E_m(w)={}&m^2+(2m^3+14m^2+4m)w\\
 &+(17m^3+76m^2+37m+2)w^2\\
 &+(48m^3+184m^2+118m+12)w^3\\
 &+(45m^3+165m^2+128m+20)w^4.
\end{aligned}
\]
All coefficients are positive, so the norm increases strictly. The displayed limits follow by comparing leading coefficients. For \(m=2\), direct simplification yields
\[
\Lambda_2(w)-2=\frac{12w^3-24w^2-15w-2}
{3(1+2w)(7w+2)(10w+3)}.
\]
Its strict monotonicity and the signs at zero and infinity prove existence and uniqueness of the positive crossing. For \(m\ge3\), the sign follows from the value at \(w=0\) and strict monotonicity.

**5. Sharp positivity defect.** Because \(\int K_x\,d\mu_w=1\), for every \(x\),
\[
\inf_{0\le f\le1}(P_{m,w}f)(x)=\int_{K_x<0}K_x\,d\mu_w
=\frac{1-\int|K_x|\,d\mu_w}{2}.
\]
Taking the infimum over \(x\) and using the preceding norm classification proves the displayed defect and all witnesses. At an unweighted norming leaf the atom coefficient is \(q>0\), so the negative-kernel witness vanishes at \(p_1\).

## Verification

Running `python verify_leaf_atom.py` with Python 3.10+ and SymPy at least 1.12 verifies the exact symbolic equalities for the three vertex norms, dominance factorizations, derivative, and limits. It also independently inverts rational Gram matrices and integrates all signed kernels for 63 cases, using exact rational arithmetic rather than floating-point quadrature. The certificate output ends with `ALL_LEAF_ATOM_SPLINE_CHECKS_PASSED`. The proof above establishes the all-integer/all-positive-parameter assertions independently of this finite collection of cases.

## Relationship to prior work

Univariate spline theory studies the endpoint norm of the orthogonal projector and boundedness under arbitrary knot sequences. Oswald (2006) examines exact mass-matrix structure and unboundedness on certain higher-dimensional simplicial triangulations. Hangelbroek, Narcowich, Sun, and Ward (2010) establish operator bounds for kernel-generated least-squares spaces on manifolds. Neither result specifies the sharp norm on a one-edge-per-arm metric star with **one boundary-supported atomic perturbation**, its movement of all norming points to other leaves, or the unique two-arm crossover.

A known atom-free metric-star formula applies only when \(w=0\); a different hub-atom model places the atomic mass at the common center instead of at an outer leaf. The present exact variation and strict-increase law concern neither of those previously treated measures. The general kernel-integration method is standard and is not claimed as a new technique.

## Limitations

The formula is for equal-length edges and one outer-leaf Dirac atom, with no other point masses and no interior knots. It does not determine the corresponding exact norm on arbitrary unequal-edge stars with a leaf atom, on graphs with cycles, or on higher-degree spline spaces. An equivalent formula in unindexed or inaccessible specialist literature cannot be excluded solely by the documented searches.

## References

1. Peter Oswald, *A counterexample concerning the \(L_2\)-projector onto linear spline spaces*, arXiv:math/0611573, first posted 2006-11-19. https://arxiv.org/abs/math/0611573
2. T. Hangelbroek, F. J. Narcowich, X. Sun, and J. D. Ward, *Kernel Approximation on Manifolds II: The \(L_\infty\) norm of the \(L_2\) projector*, arXiv:1005.2424, first posted 2010-05-13. https://arxiv.org/abs/1005.2424
