# Sharp facet-height angular profiles under Vaaler face-distance constraints

## Finding

Let \(n\ge2\) and let \(P\subset\mathbb R^n\) be a full-dimensional compact convex polytope containing the origin in its interior. Assume that every nonempty proper face \(G\) of codimension \(k\) satisfies
\[
\operatorname{dist}(0,\operatorname{aff}G)\ge\sqrt{k}.
\tag{1}
\]
For a facet \(F\), write \(h_F=\operatorname{dist}(0,\operatorname{aff}F)\ge1\) and let \(\omega_F\) be the fraction of directions from the origin meeting \(F\) first. Thus \(\omega_F\) is the normalized spherical measure of the cone \(\operatorname{pos}(F)\), with \(\sum_F\omega_F=1\).

For \(s\ge1\), define coefficients
\[
q_1^*(s)=s,\qquad
q_j^*(s)=(j-s)_+-(j-1-s)_+\quad(2\le j\le n),
\]
where \(t_+=\max(t,0)\). For \(q_j\ge0\) with \(q_1>0\) set
\[
\mathcal I_n(q)=\int_{z_1>z_2>\cdots>z_n>0}
  \exp\!\left(-\frac12\sum_{j=1}^{n}q_jz_j^2\right)\,dz,
\qquad
I_n^0=\mathcal I_n(1,\ldots,1)=
\frac{\pi^{n/2}}{2^{n/2}n!}.
\]
The integral remains finite when some coefficients other than the first vanish. Define the height profile
\[
\boxed{\Psi_n(h)=\frac{h\,\mathcal I_n(q^*(h^2))}{I_n^0}},\qquad h\ge1.
\tag{2}
\]
**Facet-height angular inequality.** For every such \(P\), and separately for every one of its facets,
\[
\boxed{
\frac{\mathcal H^{n-1}(F)}{\omega_F}
\ge\frac{n2^n}{\Psi_n(h_F)}.}
\tag{3}
\]
Consequently the surface area has the strengthened face-resolved lower bound
\[
\boxed{
\mathcal H^{n-1}(\partial P)
\ge n2^n\sum_{F}\frac{\omega_F}{\Psi_n(h_F)}
\ge n2^n.}
\tag{4}
\]
The last inequality is strict if any facet has \(h_F>1\). The centered cube of side length two attains equality throughout (3)--(4).

**Sharp analytic profile and threshold structure.** \(\Psi_n\) is continuous and strictly decreasing from \(\Psi_n(1)=1\). It is real analytic away from the \(n-1\) heights
\[h=\sqrt2,\sqrt3,\ldots,\sqrt n,\]
and has a strict downward jump in its first derivative at each of them. For \(h\ge\sqrt n\), the formula simplifies *exactly* to
\[
\boxed{\Psi_n(h)=\frac{n\,2^{n-1}\Gamma(n/2)}{\pi^{n/2}\,h^{n-1}}.}
\tag{5}
\]
Hence (3) in this regime is
\[
\boxed{\mathcal H^{n-1}(F)\ge
\frac{2\pi^{n/2}}{\Gamma(n/2)}h_F^{n-1}\omega_F.}
\tag{6}
\]
The coefficient in (3) is the **best possible coefficient from the Gaussian orthoscheme comparison at fixed facet height**, i.e. the supremum over all positive coefficient vectors meeting the prefix conditions is exactly \(\Psi_n(h)\). For every \(n\ge2\) and \(h\ge\sqrt n\), (6) is sharp **even geometrically** among admissible polytopes as an infimum, approached by shrinking corner truncations of cubes.

**Complete planar sharpness.** For \(n=2\),
\[
\boxed{
\Psi_2(h)=
\begin{cases}
\displaystyle\frac4{\pi\sqrt{2-h^2}}
\arctan\!\left(\frac{\sqrt{2-h^2}}h\right),&1\le h<\sqrt2,\\[2mm]
\displaystyle\frac4{\pi h},&h\ge\sqrt2.
\end{cases}}
\tag{7}
\]
For every \(1\le h<\sqrt2\), a concrete admissible trapezoid has a facet at distance \(h\) attaining equality in (3). For \(h\ge\sqrt2\), the bound is an optimal infimum approached by small-facet corner truncations. Thus (3) gives the exact optimal facet-length-to-visual-angle ratio for **every** planar height \(h\ge1\).

## Assumptions and scope

The condition (1) includes vertices (codimension \(n\)) and all intermediate proper faces. The face distance is to its entire affine hull, not to the face itself. A facet has positive \((n-1)\)-measure and positive visual solid-angle mass because the origin lies in the interior of \(P\). Spherical solid angle here is normalized to total mass one, not measured in steradians.

The best-possible statement for general dimensions below \(\sqrt n\) concerns the Gaussian orthoscheme parameter comparison; it is **not** a claim that equality in (3) is geometrically attainable for every intermediate height when \(n\ge3\). The planar theorem and the high-height regime provide the separately proved geometric sharpness assertions.

## Proof

### 1. A fixed-height optimum for ordered Gaussian integrals

For \(q_j>0\) let \(r_k=\sum_{j\le k}q_j\) and suppose
\[
q_1=s\ge1,\qquad r_k\ge k\quad(1\le k\le n).
\tag{8}
\]
Since the remaining coefficients are positive, \(r_k\ge s\) as well. The minimal feasible prefix vector in the nonnegative closure is therefore
\[
r_k^*=\max(k,s)\quad(1\le k\le n).
\tag{9}
\]
Its successive differences are precisely the coefficients \(q_j^*(s)\) in (2), including \(q_1^*=s\). Their nonnegativity is immediate; the Gaussian integral is finite because \(z_j<z_1\) for all \(j\).

Write \(z_{n+1}=0\). Abel summation gives the pointwise identity
\[
\sum_{j=1}^n(q_j-q_j^*)z_j^2
=\sum_{k=2}^n(r_k-r_k^*)(z_k^2-z_{k+1}^2)\ge0
\tag{10}
\]
on the ordered integration chamber. Hence \(\mathcal I_n(q)\le\mathcal I_n(q^*)\). Conversely, \(q_1=q_1^*\) and \(q_j=q_j^*+\varepsilon\) for \(j\ge2\) satisfy (8) with strictly positive entries and converge to \(q^*\). Dominated convergence proves
\[
\boxed{
\sup_{\substack{q_j>0,\ q_1=s\\r_k\ge k}}
\frac{\sqrt s\,\mathcal I_n(q)}{I_n^0}
=\Psi_n(\sqrt s).}
\tag{11}
\]
This is an optimization over genuine \(n\)-dimensional Gaussian integrals, not a finite enumeration.

### 2. Strict decrease and the \(n-1\) phase thresholds

Apply the ordered-square change of variables from the sharp Vaaler surface-area proof to the integral for \(q^*\):
\[
w_1^2=s z_1^2-(s-1)z_2^2,\qquad w_j=z_j\quad(j\ge2).
\]
It bijects the open ordered chamber onto itself. After multiplication by \(\sqrt s\), the transformed Jacobian factor is
\[
J_s(w)=\frac{w_1}{\sqrt{w_1^2+(s-1)w_2^2}}.
\]
The transformed cumulative quadratic coefficients are \(\widetilde r_1=1\) and \(\widetilde r_k=r_k^*=\max(k,s)\) for \(k\ge2\). Summation by parts therefore yields the exact probability representation
\[
\boxed{
\Psi_n(\sqrt s)=
\mathbb E\left[
\frac{W_1}{\sqrt{W_1^2+(s-1)W_2^2}}
\exp\!\left(-\frac12\sum_{k=2}^{n}(s-k)_+
(W_k^2-W_{k+1}^2)\right)
\right],}
\tag{12}
\]
where \((W_1,\ldots,W_n)\) is a standard normal vector conditioned on \(W_1>\cdots>W_n>0\), and \(W_{n+1}=0\). Every term is positive. For each interior ordered point, the prefactor decreases strictly in \(s\) and the exponential factor is nonincreasing. Thus \(\Psi_n(1)=1\), \(0<\Psi_n(h)<1\) for \(h>1\), and \(\Psi_n\) is strictly decreasing.

The coefficient functions \(q^*(s)\) are affine on the intervals cut out by the integers \(2,\ldots,n\); differentiation under the Gaussian integral is justified by the positive first coefficient and ordering. At \(s=k\in\{2,\ldots,n\}\), the derivative of the quadratic form with respect to \(s\) acquires exactly the positive term \(z_k^2-z_{k+1}^2\). Consequently the derivative of \(s\mapsto\Psi_n(\sqrt s)\) has the strictly negative jump
\[
\boxed{
\left.\frac{d\Psi_n(\sqrt s)}{ds}\right|_{s=k+}
-\left.\frac{d\Psi_n(\sqrt s)}{ds}\right|_{s=k-}
=-\frac{\sqrt k}{2I_n^0}\int_{D_n}(z_k^2-z_{k+1}^2)
 e^{-\frac12\sum_jq_j^*(k)z_j^2}\,dz<0.}
\tag{13}
\]
The same strict derivative jump holds in the \(h\)-variable by the smooth positive change \(s=h^2\). These are thresholds in the *optimal analytic comparison*, not asserted to be changes in the combinatorial structure of a given polytope.

For \(s\ge n\), all \(q_j^*(s)\) with \(j\ge2\) vanish. Integrating \(z_2,\ldots,z_n\) first,
\[
\mathcal I_n(q^*(s))
=\frac1{(n-1)!}\int_0^\infty
 z_1^{n-1}e^{-s z_1^2/2}\,dz_1
=\frac{2^{n/2-1}\Gamma(n/2)}{(n-1)!s^{n/2}}.
\]
Using \(I_n^0=\pi^{n/2}/(2^{n/2}n!)\) proves (5).

### 3. From the optimal Gaussian comparison to individual facets

First assume a generic origin as in the standard Rogers--Karasev flag decomposition: successive orthogonal projections onto the affine hulls of incident faces are distinct. Each maximal flag \(P=F_0\supset F_1\supset\cdots\supset F_n\), with \(\operatorname{codim}F_k=k\), determines a flag simplex \(A=\operatorname{conv}\{0,a_{F_1},\ldots,a_{F_n}\}\), where \(a_G\) is the point of \(G\) nearest the origin. Nondegenerate flag simplices partition \(P\) in volume, and their opposite facets partition each facet of \(P\) in surface measure.

Let \(B\) be the associated orthoscheme of orthogonal projections onto \(\operatorname{aff}F_k\). The Rogers--Karasev contraction and the exact orthoscheme calculation (Zwierzyński, Propositions 2.3 and 3.2, displayed formulas (7) and (18)) give
\[
\frac{\mathcal H^{n-1}(\operatorname{base}A)}{\operatorname{vol}_n(A\cap\mathbb B^n)}
\ge \frac{(2\pi)^{n/2}}{(n-1)!\kappa_n\,\sqrt{q_1}\mathcal I_n(q)},
\tag{14}
\]
where \(\mathbb B^n\) is the unit Euclidean ball, \(\kappa_n=\operatorname{vol}_n(\mathbb B^n)\), \(q_1=h_{F_1}^2\), and \(r_k=\operatorname{dist}(0,\operatorname{aff}F_k)^2\ge k\). From (11) and the normalization of \(I_n^0\), (14) is at least
\[
\frac{n2^n}{\kappa_n\Psi_n(h_{F_1})}.
\tag{15}
\]
Summing (15) only over flags whose first proper face is a fixed facet \(F\) gives the left side \(\mathcal H^{n-1}(F)\). Since \(h_F\ge1\), the unit-ball portions of those pyramids coincide with their radial cone sectors; their union is \(\mathbb B^n\cap\operatorname{pos}(F)\) up to measure zero, of volume \(\kappa_n\omega_F\). Thus (3) follows separately for each facet, and summing gives (4).

For nongeneric origins, translate by \(v\) with \(|v|<\varepsilon\), away from the finite exceptional affine hyperplanes, and enlarge by the factor \((1-\varepsilon)^{-1}\) exactly as in the source generic-center reduction. A codimension-\(k\) face then has affine distance at least \((\sqrt{k}-\varepsilon)/(1-\varepsilon)\ge\sqrt{k}\). Corresponding facet measures, heights, and their normalized cone angles converge as \(\varepsilon\downarrow0\). Therefore each facet inequality passes to the original polytope. This argument does not assume that all nearest face points are relative interior points.

### 4. Sharpness and the planar formula

For a facet in an affine hyperplane at distance \(h\), direct radial projection gives
\[
\omega_F=\frac1{|\mathbb S^{n-1}|}
\int_F\frac{h}{|x|^n}\,d\mathcal H^{n-1}(x),
\qquad
|\mathbb S^{n-1}|=\frac{2\pi^{n/2}}{\Gamma(n/2)}.
\tag{16}
\]
In particular, the right side of (6) is the familiar universal radial-projection lower bound. The key point here is that the stronger Vaaler-type profile (3) joins that bound at the exact threshold \(h=\sqrt n\), with \(n-1\) explicit preceding analytic transitions.

For any fixed \(h\ge\sqrt n\), put \(a=h/\sqrt n+\varepsilon\), with \(\varepsilon>0\) small, and form the truncated cube
\[
P_\varepsilon=[-a,a]^n\cap
\left\{x:\sum_{i=1}^n x_i\le h\sqrt n\right\}.
\tag{17}
\]
Its new facet \(F_\varepsilon\) lies at distance exactly \(h\). Every other proper face lies in an old coordinate face (distance at least \(a\sqrt{k}\) if it has codimension \(k\)) or lies in the new cutting hyperplane (distance at least \(h\ge\sqrt n\)); therefore (1) holds. The new facet is an \((n-1)\)-simplex whose vertices tend to \((h/\sqrt n,\ldots,h/\sqrt n)\). On this facet, \(|x|\to h\) uniformly. Dividing the radial identity (16) by its facet area shows
\[
\lim_{\varepsilon\downarrow0}
\frac{\mathcal H^{n-1}(F_\varepsilon)}{\omega_{F_\varepsilon}}
=|\mathbb S^{n-1}|h^{n-1},
\]
which agrees with (3) and (5). It is an infimum limit of genuine positive-area facets, not an equality claim for a degenerate face.

For \(n=2\), integrate in polar coordinates \(z_1=r\cos\theta\), \(z_2=r\sin\theta\), \(0<\theta<\pi/4\):
\[
\mathcal I_2(q_1,q_2)
=\int_0^1\frac{dt}{q_1+q_2t^2}
=\begin{cases}
\displaystyle\frac{\arctan\sqrt{q_2/q_1}}{\sqrt{q_1q_2}},&q_2>0,\\[1mm]
\displaystyle\frac1{q_1},&q_2=0.
\end{cases}
\]
Putting \(q_1=h^2\), \(q_2=(2-h^2)_+\) yields (7).

To show *attainment* for every \(1\le h<\sqrt2\), let
\[
b=\sqrt{2-h^2},\qquad u=(h-b)/2,\qquad v=(h+b)/2.
\]
Then \(u\ge0\), \(v>0\), \(u^2+v^2=1\), and \(uh+vb=1\). For any \(A\ge\sqrt2\), the trapezoid
\[
T_{h,A}=\{(x,y):-A\le x\le h,\quad ux+vy\le1,\quad ux-vy\le1\}
\tag{18}
\]
contains the origin. Its four supporting lines have distances \(A,h,1,1\), and its right vertices \((h,\pm b)\) have distance \(\sqrt2\) from the origin; its left vertices have distance at least \(A\ge\sqrt2\). So (1) holds. The right facet has length \(2b\) and normalized visual angle \(\arctan(b/h)/\pi\). By (7),
\[
\frac{2b}{\arctan(b/h)/\pi}
=\frac8{\Psi_2(h)},
\]
which proves equality in (3). Combining this with the shrinking-truncation construction covers the entire planar range.

## Verification

Run `python3 verify.py`. It uses only the Python standard library. It checks exact rational prefix-sum identities and Abel summation over 1,068 admissible parameter configurations; the planar closed formula and fixed-height variational inequality; the high-height gamma-function normalization and radial-projection constant in multiple dimensions; derivative change at the planar threshold; exact planar trapezoid identities; and high-dimensional shrinking-facet radius bounds. The completed script reports 2,082 passing checks.

These tests establish consistency, not completeness of an infinite proof. The proof of (3) depends on the cited Rogers--Karasev contraction and flag subdivision, which are explicitly stated and checked against the primary source. All further calculations are displayed above.

## Relationship to prior work

Zwierzyński, *A Sharp Surface-Area Extension of Vaaler's Theorem*, arXiv:2609.27798v1, proves the uniform bound \(\mathcal H^{n-1}(\partial P)\ge n2^n\) from (1) and the per-flag constant estimate \(n2^n/\kappa_n\). It does **not** state the optimal conditional height profile (2), the facetwise bound (3), the piecewise thresholds, or its planar complete sharpness. The proof here retains and optimizes the Gaussian prefactor rather than replacing it by one.

Karasev, *Rogers's proof of Vaaler's theorem*, arXiv:2505.16247, proves the surface inequality for dimensions two and three and establishes the underlying flag contraction. The previously published *Rigidity of the ordered-square comparison behind the sharp Vaaler surface bound* establishes an equality-only characterization at the same Gaussian comparison: all Gaussian coefficients must be one. It does not provide a fixed-height optimum or face-by-face quantitative inequality. None of these earlier statements implies the new height profile by direct specialization.

The radial-projection estimate (16) is classical and is **not** claimed as new. The new content is the exact, all-dimensional interpolation from the Vaaler local bound to that radial bound, including the \(n-1\) analytically sharp thresholds, geometric sharpness at and beyond the final threshold, and the complete planar sharpness construction.

## Limitations

The geometric bound is proved under the full face-distance hypotheses (1), not for arbitrary polytopes near the unit ball. In dimensions \(n\ge3\), optimal geometric constants for fixed heights \(1<h<\sqrt n\) are not claimed; the optimization there is exact only within the Gaussian orthoscheme class. The argument does not classify every global equality polytope when all facet heights equal one. The threshold points describe the coefficient function, not an actual combinatorial transition for every given polytope. Definitive historical priority and independent mathematical validation remain open.

## References

1. M. Zwierzyński, *A Sharp Surface-Area Extension of Vaaler's Theorem*, arXiv:2609.27798v1, first-public source date 2026-08-19, primary MSC2020 52A38. https://arxiv.org/abs/2609.27798
2. R. Karasev, *Rogers's proof of Vaaler's theorem*, arXiv:2505.16247v1, first posted 2025-05-22; later v3 inspected. https://arxiv.org/abs/2505.16247
3. *Rigidity of the ordered-square comparison behind the sharp Vaaler surface bound*, public mathematical record, 2026-10-11. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-rigidity-of-the-ordered-square-comparison-behind-the-sharp-vaale--3834d9e544a5
