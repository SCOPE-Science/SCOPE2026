# The exact John ellipsoid and contact transition of a circular frustum in every dimension

## Finding

For every integer \(d\ge2\) and every \(t\in[0,1]\), define the round frustum in \(\mathbb R^{d-1}\times\mathbb R\) by
\[
K_{d,t}=\bigl\{(x,z):0\le z\le1,\ \|x\|_2\le1-(1-t)z\bigr\}.
\]
The lower cross-section is a unit \((d-1)\)-ball and the upper cross-section is a ball of radius \(t\). The endpoints are the right circular cone and cylinder. Let \(\kappa_j=\pi^{j/2}/\Gamma(j/2+1)\), the volume of a unit \(j\)-ball.

**Theorem.** The unique maximum-\(d\)-volume ellipsoid contained in \(K_{d,t}\) is
\[
E_{d,t}=\left\{(x,z):\frac{\|x\|_2^2}{a_{d,t}^2}
       +\frac{(z-b_{d,t})^2}{b_{d,t}^2}\le1\right\},
\]
where, with \(t_c=(d-1)/(d+1)\),
\[
(a_{d,t}^2,b_{d,t})=
\begin{cases}
\left(\dfrac{d-1}{d+1},\ \dfrac{1}{(d+1)(1-t)}\right),
 &0\le t\le t_c,\\[6pt]
\left(t,\ \dfrac12\right),&t_c\le t\le1.
\end{cases}
\]
The branches agree at \(t_c\). For \(t<t_c\) the ellipsoid is tangent to the lower cap and the lateral boundary but misses the upper cap. At and beyond \(t_c\), it also touches the upper cap. Its horizontal semiaxis remains fixed in the first regime and increases as \(\sqrt t\) in the second.

Its exact occupied-volume fraction \(J_d(t)=\operatorname{vol}_d(E_{d,t})/\operatorname{vol}_d(K_{d,t})\) is
\[
J_d(t)=\frac{\kappa_d}{\kappa_{d-1}}
\begin{cases}
\displaystyle \frac{d}{d+1}\left(\frac{d-1}{d+1}\right)^{(d-1)/2}\frac{1}{1-t^d},
 &0\le t\le t_c,\\[8pt]
\displaystyle \frac d2\frac{t^{(d-1)/2}}{1+t+\cdots+t^{d-1}},
 &t_c\le t\le1.
\end{cases}
\]
For every fixed \(d\ge2\), **\(J_d(t)\) is strictly increasing on \([0,1]\)**. In particular its sharp endpoint values are
\[
J_d(0)=\frac{\kappa_d}{\kappa_{d-1}}
\frac{d}{d+1}\left(\frac{d-1}{d+1}\right)^{(d-1)/2},
\qquad
J_d(1)=\frac{\kappa_d}{2\kappa_{d-1}}.
\]
The formulas transfer by affine equivariance to all nondegenerate affine images of \(K_{d,t}\), including oblique frusta with homothetic ellipsoidal sections.

## Assumptions and scope

Here \(d\ge2\) is an integer and \(t\in[0,1]\) is arbitrary, including both boundary shapes and the transition value. An *ellipsoid* means a full-dimensional affine image of the Euclidean unit ball; its volume is the usual \(d\)-dimensional Lebesgue volume. The John ellipsoid means the unique inscribed ellipsoid maximizing that volume. No coaxiality or rotation assumption is imposed on competing ellipsoids. The normalization to unit height and unit lower radius does not restrict the affine-equivalence class. For \(t=0\), the upper cap is the single apex; for \(t=1\), the lateral boundary is cylindrical.

## Proof

**Step 1 (all competitors reduce to two semiaxes).** Existence and uniqueness of a maximal-volume inscribed ellipsoid in a convex body is the classical John-ellipsoid theorem, also stated in Güler and Gürtuna's Theorem 2.6. The body \(K_{d,t}\) is fixed by every horizontal orthogonal map \((x,z)\mapsto(Ux,z)\), where \(U\in O(d-1)\). Uniqueness forces the maximizing ellipsoid to be fixed by this whole group. Its center must lie on the \(z\)-axis; invariance of its defining quadratic form forces the cross block to vanish and the horizontal block to be a scalar identity. Thus the optimizer, without restriction on the initial competing ellipsoids, has the form
\[
E(a,b,c)=\left\{(x,z):\frac{\|x\|_2^2}{a^2}
       +\frac{(z-c)^2}{b^2}\le1\right\},\qquad a,b>0.
\]
(The same conclusion in \(d=2\) follows from reflection in the vertical axis.)

**Step 2 (exact feasibility).** Put \(k=1-t\in[0,1]\). The slab constraint \(0\le z\le1\) holds on \(E(a,b,c)\) precisely when \(b\le c\le1-b\), so \(0<b\le1/2\). The remaining cone-side constraint is \(\|x\|_2+kz\le1\). Its maximum over the ellipsoid is exactly
\[
\sup_{E(a,b,c)}(\|x\|_2+kz)
=kc+\sqrt{a^2+k^2b^2}.
\]
Indeed, for every horizontal unit vector \(u\), maximize the linear functional \(u\cdot x+kz\) over \(E\); its support value is the right-hand side, independent of \(u\). Taking the supremum over \(u\) is equivalent to maximizing \(\|x\|_2+kz\). Therefore
\[
E(a,b,c)\subset K_{d,t}
\iff b\le c\le1-b\ \text{and}\ 
kc+\sqrt{a^2+k^2b^2}\le1.
\]
When \(k>0\), decreasing \(c\) to \(b\) weakens the last constraint, allowing strictly larger \(a\) unless already \(c=b\). Hence every optimum has \(c=b\), and the maximal feasible \(a\) for a fixed \(b\) is characterized by
\[
a^2=(1-kb)^2-k^2b^2=1-2kb.
\]
This squared semiaxis is nonnegative throughout \(0<b\le1/2\), vanishing only at \(k=1,\ b=1/2\); that endpoint represents a zero-volume degenerate object and cannot maximize ellipsoid volume. If \(k=0\), the side constraint is simply \(a\le1\), and the volume is maximal at \(a=1,b=c=1/2\); thus the endpoint has the same reduced form.

**Step 3 (exact optimization and transition).** Up to the constant \(\kappa_d\), the ellipsoid volume is
\[
 f_k(b)=b(1-2kb)^{(d-1)/2},\qquad0<b\le1/2.
\]
For \(k>0\), its derivative has the sign of
\[
1-(d+1)kb,
\]
with all remaining derivative factors strictly positive. Consequently its unique maximum on \((0,1/2]\) is
\[
b_* =\min\left\{\frac{1}{(d+1)k},\frac12\right\}.
\]
The transition takes place exactly when \(k=2/(d+1)\), equivalently \(t=t_c=(d-1)/(d+1)\). In the first regime, \(a^2=1-2/(d+1)=(d-1)/(d+1)\); in the second, \(a^2=1-k=t\). Strictness of the maximization, together with uniqueness of the full-dimensional John ellipsoid, gives the full equality classification. For \(t<t_c\), its maximal height is \(2b_*<1\); thereafter \(2b_*=1\). The side constraint holds at equality and hence yields lateral contact in both regimes.

**Step 4 (volume fraction and monotonicity).** Integrating horizontal sections gives
\[
\operatorname{vol}_d(K_{d,t})=
\kappa_{d-1}\int_0^1 (1-(1-t)z)^{d-1}\,dz
=\frac{\kappa_{d-1}}d(1+t+\cdots+t^{d-1}).
\]
The ellipsoid volume is \(\kappa_d a_{d,t}^{d-1}b_{d,t}\). Substitution produces the displayed formula for \(J_d(t)\), including its limiting value at \(t=1\). On \([0,t_c]\), the only varying factor is \((1-t^d)^{-1}\), which is strictly increasing. On \((t_c,1)\), let \(S(t)=\sum_{j=0}^{d-1}t^j\). Differentiation gives
\[
\frac{d}{d\log t}\log\frac{t^{(d-1)/2}}{S(t)}
=\frac{d-1}{2}-\frac{\sum_{j=0}^{d-1}j t^j}{\sum_{j=0}^{d-1}t^j}>0.
\]
For \(0<t<1\), the final strict inequality holds because the weights \(t^j\) decrease strictly with \(j\), so paired terms \(j\) and \(d-1-j\) have a weighted mean below \((d-1)/2\). The branch formulas agree at \(t_c\), proving strict increase throughout. Endpoint evaluation is immediate. An invertible affine map sends the unique maximal-volume ellipsoid to that of its image and preserves the occupied-volume fraction.

## Verification

The complete argument above is analytic for all integer dimensions and every real \(t\in[0,1]\). A standalone Python verifier, `verify.py`, uses exact rational arithmetic to check both transition identities; compare the exact squared-volume objective against 14,263 rational competing semiaxis choices; and check strict monotonicity at 3,400 successive rational parameter pairs. It also performs 5,712 seeded geometric boundary diagnostics. These checks are finite corroboration, **not** substitutes for the universal arguments in Steps 1–4. Run from this directory with `python3 verify.py` using only the Python standard library.

## Relationship to prior work

Güler and Gürtuna, in their 2007 preprint and 2011 manuscript later published in *Optimization Methods & Software*, compute the **minimum-volume enclosing** ellipsoid of the same geometric class (truncated second-order cones or ellipsoidal cylinders). Their §7, Theorem 7.1, determines that opposite containment problem. In the introductory outline they explicitly state that they **do not solve the maximum-volume inscribed ellipsoid problem** for this second class. Their uniqueness theorem and symmetry reduction provide relevant classical tools, but neither their covering formula nor a statement about a ball-slab intersection gives the two-branch inscribed formula here by direct substitution. Brandenberg and König (2013 preprint) develop sharp general geometric inequalities using John symmetry; the inspected paper does not identify this exact frustum profile. Horwitz (2009) proves inequalities and uniqueness statements for ellipses *inscribed in the four-side-tangent sense* in convex quadrilaterals; it does not give the higher-dimensional truncated-cone contact transition. One published geometric result on the Santaló volume product of homothetic frusta concerns a different affine invariant and does not imply an extremal inscribed-ellipsoid profile.

## Limitations

This is an exact theorem for the homothetic-ellipsoidal frustum class and its affine images, **not** a theorem about general convex frusta with arbitrary sections. The proof uses the standard uniqueness theorem for inscribed maximum-volume ellipsoids and does not reconstruct that general theorem. The originality comparison concerns the inspected papers and available indexed records, not an exhaustive classification of all older literature; an unnoticed equivalent formula remains possible. No independent external validation has been performed.

## References

1. O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707, initially submitted 5 September 2007, especially the discussion preceding the truncated-cone covering theorem.
2. O. Güler and F. Gürtuna, *Symmetry of convex sets and its applications to the extremal ellipsoids of convex bodies*, *Optimization Methods & Software* 27 (2012), 735–759, DOI 10.1080/10556788.2011.626037, §§1 and 7.
3. R. Brandenberg and S. König, *Sharpening Geometric Inequalities using Computable Symmetry Measures*, arXiv:1310.4368, initially submitted 16 October 2013, especially §§3.2 and 7.
4. A. Horwitz, *An Area Inequality for Ellipses Inscribed in Quadrilaterals*, arXiv:0907.1647, 2009, §§1–2.
