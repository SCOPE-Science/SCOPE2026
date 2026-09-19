# Sharp angular profile for facet-parallel central slices of the regular simplex

## Statement

Let
\[
\Delta_n=\operatorname{conv}\{e_0,\ldots,e_n\}
\subset \left\{x\in\mathbb R^{n+1}:\sum_{i=0}^n x_i=1\right\},
\qquad n\ge2,
\]
be the regular \(n\)-simplex of side length \(\sqrt2\). A central hyperplane is
\[
H_a=\{x:a\cdot x=0\},
\qquad
a\in \mathbf 1^\perp,\quad |a|=1.
\]
Write
\[
A(a)=\operatorname{vol}_{n-1}(\Delta_n\cap H_a).
\]

Orient the normal so that it lies in the one-vertex-separating chamber
\[
\mathcal C_0=
\{a\in\mathbf1^\perp:|a|=1,\ a_0>0,\ a_i\le0\ (1\le i\le n)\}.
\]
The facet-parallel normal in this chamber is
\[
u_0=
\sqrt{\frac n{n+1}}\,e_0
-\frac1{\sqrt{n(n+1)}}\sum_{i=1}^n e_i,
\]
and the corresponding section volume is
\[
A_*=
\frac{\sqrt n}{(n-1)!}
\left(\frac n{n+1}\right)^{n-1}.
\]
Ambrus and Gárgyán prove that the facet-parallel central sections are precisely the global minimizers of central section volume.

For \(a\in\mathcal C_0\), put
\[
\theta=\arccos\langle a,u_0\rangle.
\]
Then
\[
0\le\theta\le
\theta_{\max}:=
\arctan\sqrt{\frac{n-1}{n+1}}.
\]

**Theorem (sharp chamber-wise angular profile).**
For every \(a\in\mathcal C_0\),
\[
\boxed{
\frac{A(a)}{A_*}\ge \Phi_n(\theta)
}
\tag{1}
\]
where
\[
\boxed{
\Phi_n(\theta)=
\frac{\sec\theta}{
\left(1-\dfrac{\tan\theta}{\sqrt{n^2-1}}\right)^{n-1}
\left(1+\sqrt{\dfrac{n-1}{n+1}}\tan\theta\right)}
}.
\tag{2}
\]
The function \(\Phi_n\) is strictly increasing on \((0,\theta_{\max}]\).

For \(0<\theta\le\theta_{\max}\), equality in (1) holds exactly on the \(n\) great-circle arcs from \(u_0\) to
\[
w_{0j}=\frac{e_0-e_j}{\sqrt2},
\qquad 1\le j\le n.
\]
The endpoint \(w_{0j}\) is a Webb maximal-section normal. Thus the sharp fixed-angle minimum inside \(\mathcal C_0\) interpolates continuously from the facet-parallel global minimum to a Webb global maximum:
\[
\Phi_n(\theta_{\max})
=
\frac1{\sqrt2}
\left(\frac{n+1}{n}\right)^{n-\frac12}
=
\frac{A(w_{0j})}{A_*}.
\tag{3}
\]

A weaker but immediate consequence of (1) is
\[
\frac{A(a)}{A_*}\ge \sec\theta,
\tag{4}
\]
hence any \(a\in\mathcal C_0\) with \(A(a)\le(1+\varepsilon)A_*\) satisfies
\[
\theta\le \arccos\frac1{1+\varepsilon}.
\tag{5}
\]

Finally, the spherical Hessian at a facet-parallel minimizer is isotropic:
\[
\boxed{
\operatorname{Hess}_{S(\mathbf1^\perp)}
\log A\big|_{u_0}
=
\frac{2n+1}{n+1}\,g.
}
\tag{6}
\]
Equivalently, for every unit tangent direction \(v\in T_{u_0}S(\mathbf1^\perp)\),
\[
\frac{A(\cos t\,u_0+\sin t\,v)}{A_*}
=
1+\frac{2n+1}{2(n+1)}t^2+O(t^3).
\tag{7}
\]

## Proof

### 1. Exact section formula in the one-vertex chamber

Assume first that \(a_i<0\) for \(i\ge1\). The hyperplane \(H_a\) meets the edge \(e_0e_i\) at
\[
p_i=e_0+\lambda_i(e_i-e_0),
\qquad
\lambda_i=\frac{a_0}{a_0-a_i}.
\]
Hence
\[
\Delta_n\cap H_a=\operatorname{conv}\{p_1,\ldots,p_n\}.
\]

The simplex \(\operatorname{conv}\{e_0,p_1,\ldots,p_n\}\) has \(n\)-volume
\[
\left(\prod_{i=1}^n\lambda_i\right)\operatorname{vol}_n(\Delta_n).
\]
Because \(a\perp\mathbf1\) and \(|a|=1\), the distance from \(e_0\) to \(H_a\) inside the affine hull of \(\Delta_n\) is \(a_0\). Using
\[
\operatorname{vol}_n(\Delta_n)=\frac{\sqrt{n+1}}{n!}
\]
and the pyramid formula gives
\[
\boxed{
A(a)=
\frac{\sqrt{n+1}}{(n-1)!}
\frac{a_0^{\,n-1}}{\prod_{i=1}^n(a_0-a_i)}.
}
\tag{8}
\]
The same formula extends continuously to the closed chamber \(\mathcal C_0\).

Set
\[
\alpha=\sqrt{\frac n{n+1}},
\qquad
\beta=-\frac1{\sqrt{n(n+1)}},
\qquad
d=\alpha-\beta=\sqrt{\frac{n+1}{n}}=\frac1\alpha.
\]
For \(a=u_0\), formula (8) gives the stated \(A_*\).

### 2. Angular coordinates

For \(a\ne u_0\), write
\[
a=\cos\theta\,u_0+\sin\theta\,v,
\qquad
v\in T_{u_0}S(\mathbf1^\perp),\quad |v|=1.
\]
Since \(v\perp\mathbf1\) and \(v\perp u_0\),
\[
v_0=0,
\qquad
\sum_{i=1}^n v_i=0,
\qquad
\sum_{i=1}^n v_i^2=1.
\tag{9}
\]
Therefore
\[
a_0=\alpha\cos\theta,
\qquad
a_0-a_i=d\cos\theta-v_i\sin\theta.
\]
Substitution in (8) yields the exact identity
\[
\boxed{
\frac{A(a)}{A_*}
=
\frac{\sec\theta}{
\prod_{i=1}^n
\left(1-\frac{v_i}{d}\tan\theta\right)}.
}
\tag{10}
\]

The angle range is also explicit. Since the negative coordinates have total absolute value \(a_0\),
\[
\sum_{i=1}^n a_i^2\le a_0^2.
\]
Thus \(1\le2a_0^2\), while
\[
\cos\theta=\langle a,u_0\rangle=d\,a_0.
\]
Consequently
\[
\cos\theta\ge\sqrt{\frac{n+1}{2n}},
\]
which is equivalent to \(\theta\le\theta_{\max}\). Equality holds exactly when only one negative coordinate is nonzero, giving \(a=w_{0j}\).

### 3. Sharp optimization at fixed angle

Put
\[
z_i=\frac{v_i}{d}\tan\theta,
\qquad
x_i=1-z_i.
\]
The chamber condition gives \(x_i>0\), while (9) gives
\[
\sum_{i=1}^n x_i=n,
\qquad
\sum_{i=1}^n(x_i-1)^2
=
\frac n{n+1}\tan^2\theta=:s^2.
\tag{11}
\]

A sharp variance refinement of AM--GM due to Rodin states that, among positive \(n\)-tuples with fixed arithmetic mean and fixed nonzero variance, the geometric mean is maximal when \(n-1\) entries are equal and below the mean and the remaining entry is above the mean. Applied to (11), this gives
\[
\prod_{i=1}^n x_i
\le
\left(1-\frac{s}{\sqrt{n(n-1)}}\right)^{n-1}
\left(1+s\sqrt{\frac{n-1}{n}}\right).
\tag{12}
\]
Since
\[
s=\sqrt{\frac n{n+1}}\tan\theta,
\]
(12) becomes
\[
\prod_{i=1}^n x_i
\le
\left(1-\frac{\tan\theta}{\sqrt{n^2-1}}\right)^{n-1}
\left(1+\sqrt{\frac{n-1}{n+1}}\tan\theta\right).
\tag{13}
\]
Combining (10) and (13) proves (1).

The equality condition in Rodin's inequality gives, up to a permutation of \(1,\ldots,n\),
\[
v_j=-\sqrt{\frac{n-1}{n}},
\qquad
v_i=\frac1{\sqrt{n(n-1)}}\quad(i\ne j).
\tag{14}
\]
These are exactly the unit tangent directions of the great-circle arcs from \(u_0\) to \(w_{0j}\). For every \(0<\theta<\theta_{\max}\), the corresponding point remains in the open chamber, so the lower bound is attained at every allowed angle. At \(\theta=\theta_{\max}\), it reaches \(w_{0j}\).

To see monotonicity, put
\[
q=\frac{\tan\theta}{\sqrt{n^2-1}},
\qquad
0\le q\le\frac1{n+1}.
\]
Then
\[
\Phi_n(\theta)
=
\frac{\sqrt{1+(n^2-1)q^2}}
{(1-q)^{n-1}(1+(n-1)q)}.
\]
For \(q>0\), the logarithmic derivative is
\[
\frac{(n^2-1)q}{1+(n^2-1)q^2}
+
\frac{n-1}{1-q}
-
\frac{n-1}{1+(n-1)q}>0.
\]
This proves strict increase. Substituting \(q=1/(n+1)\) gives (3). The weaker estimate (4) follows already from ordinary AM--GM, because \(\prod_i x_i\le1\).

### 4. Isotropic local Hessian

From (10),
\[
L(t):=
\log\frac{A(\cos t\,u_0+\sin t\,v)}{A_*}
=
-\log\cos t
-\sum_{i=1}^n
\log\left(1-\frac{v_i}{d}\tan t\right).
\]
Using \(\sum v_i=0\), \(\sum v_i^2=1\), and \(d^{-2}=n/(n+1)\),
\[
L'(0)=0,
\qquad
L''(0)=1+\frac1{d^2}
=\frac{2n+1}{n+1},
\]
independently of the unit tangent direction \(v\). This proves (6) and (7).

## Context and novelty boundary

Ambrus--Gárgyán (2026) establish the sharp global minimum: central sections of the regular simplex have minimum volume exactly in facet-parallel directions. Webb's classical theorem gives the opposite extremum, the maximal central sections, and Myroshnychenko--Tang--Tatarko--Tkocz prove quantitative stability for that **maximal** problem. Dirksen gives general formulas and earlier partial estimates for the minimal problem.

The contribution claimed here, to the best of our knowledge, is the exact **fixed-angular-distance minimum inside a one-vertex-separating normal chamber**, including the closed formula (2), its equality arcs connecting a facet minimizer to Webb maximizers, and the isotropic Hessian (6). The geometric section formula (8), AM--GM, and Rodin's sharp fixed-variance product inequality are ingredients rather than originality claims.

Searches using minimum/minimal simplex slicing, facet-parallel stability, angular stability, one-vertex chambers, fixed-angle central sections, and equivalent volume-profile terminology did not locate this profile. The motivating minimum theorem is very recent; indexed sources available for its current version exposed the theorem and proof strategy but not the full text, so an unindexed statement in that preprint or a later revision remains the principal originality risk.

## Limitations

- The sharp profile is proved only in a one-vertex-separating chamber (and, by simplex symmetry and orientation reversal, its symmetric copies). It is not a global stability theorem over all sign patterns of the normal.
- The result does not reprove the global minimum theorem of Ambrus--Gárgyán; their theorem is used only to identify \(A_*\) as the global minimum beyond the chamber treated here.
- The fixed-variance AM--GM extremizer is prior work of Rodin.
- No dimension-free global deficit bound outside these chambers is claimed.
- The motivating minimum theorem is recent, and its full text was not inspected here; this leaves a concrete residual originality risk.

## References

1. Gergely Ambrus and Barnabás Gárgyán, *Minimal central slices of the regular simplex*, arXiv:2609.12714v1 (2026), https://arxiv.org/abs/2609.12714.
2. Sergii Myroshnychenko, Colin Tang, Kateryna Tatarko, and Tomasz Tkocz, *Stability of Simplex Slicing*, Discrete & Computational Geometry 76 (2026), 491--507, https://doi.org/10.1007/s00454-025-00758-x.
3. Hauke Dirksen, *Sections of the regular simplex -- Volume formulas and estimates*, Mathematische Nachrichten 290 (2017), 2567--2584, https://doi.org/10.1002/mana.201600109.
4. Simon P. Webb, *Central slices of the regular simplex*, Geometriae Dedicata 61 (1996), 19--28.
5. Burt Rodin, *Variance and the Inequality of Arithmetic and Geometric Means*, Rocky Mountain Journal of Mathematics 47 (2017), 2157--2168; arXiv:1409.0162, https://arxiv.org/abs/1409.0162.
