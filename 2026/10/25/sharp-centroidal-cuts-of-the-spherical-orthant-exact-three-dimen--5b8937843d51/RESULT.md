# Sharp centroidal cuts of the spherical orthant: exact three-dimensional spectrum and a dimensional law

## Finding

Let \(Q_d=\mathbb S^{d-1}\cap[0,\infty)^d\), \(d\ge2\), carry normalized spherical measure and spherical centroid \(c_d=(1,\ldots,1)/\sqrt d\). For every unit vector \(u\perp c_d\), set
\[
P_d(u)=\frac{\sigma_{d-1}(\{x\in Q_d:\langle u,x\rangle\ge0\})}{\sigma_{d-1}(Q_d)}.
\]

**Exact three-dimensional spectrum.** The complete range of \(P_3\) is the sharp interval
\[
\boxed{\quad m\le P_3(u)\le1-m,\qquad
m=\frac4\pi\arctan\!\left(\frac{3-\sqrt5}{2}\right)=0.4645590543975\ldots.\quad}
\]
The upper bound is attained exactly for the positive multiples, subject to unit normalization, of permutations of \((1,1,-2)\); the lower bound is attained exactly for permutations of \((2,-1,-1)\). These are the only extremizers.

More precisely, if two coordinates of \(u\) are nonnegative and the third is negative, permute and rescale the normal to \((a,1-a,-1)\), \(0\le a\le1\). Then its complete cut profile is
\[
\boxed{\quad P_3(u)=1-\frac4\pi\arctan\!\left[
  (\sqrt{1+a^2}-a)(\sqrt{1+(1-a)^2}-(1-a))\right].\quad}
\]
The profile is symmetric under \(a\mapsto1-a\), is strictly concave, equals \(1/2\) at both endpoints, and is uniquely largest at \(a=1/2\). Normal reversal replaces the value by its complement; any normal with a zero coordinate gives exactly \(1/2\).

**Canonical cut in every dimension.** For \(d\ge2\), let
\[
u_d=\frac{(1,\ldots,1,-(d-1))}{\sqrt{d(d-1)}},\qquad p_d=P_d(u_d).
\]
Writing \(H_1,H_2,\ldots\) for independent half-normal variables \(H_i=|Z_i|\), \(Z_i\sim N(0,1)\), one has the exact probabilistic representation
\[
\boxed{\quad p_d=\mathbb E\operatorname{erf}\!\left(
  \frac{H_1+\cdots+H_{d-1}}{(d-1)\sqrt2}\right).\quad}
\]
Moreover the sequence is strictly increasing and has the sharp limit
\[
\boxed{\qquad \frac12=p_2<p_3<p_4<\cdots<
\lim_{d\to\infty}p_d=\operatorname{erf}(1/\sqrt\pi)
=0.5750625163166\ldots.\qquad}
\]
In particular, the three-dimensional upper extremizer belongs to this dimension-uniform family. The claim of global optimality is made **only in dimension three**.

## Assumptions and scope

Spherical measure \(\sigma_{d-1}\) is ordinary unnormalized surface measure on the unit sphere. The ratio cancels its normalization. The spherical centroid is the normalized surface-moment vector. All cuts are closed central hemispheres with outward unit normals orthogonal to this centroid; boundaries have zero spherical area. The spherical orthant is a geodesically convex body contained in an open hemisphere. In dimension three it is the all-right spherical triangle of area \(\pi/2\).

## Proof

**1. Centroid and probability model.** Coordinate permutations preserve \(Q_d\) and its surface measure; hence its moment vector has equal positive components, so its normalized centroid is exactly \(c_d\). For independent standard Gaussians \(Z_i\), the random point
\[
X=\frac{(|Z_1|,\ldots,|Z_d|)}{(Z_1^2+\cdots+Z_d^2)^{1/2}}
\]
is uniform on \(Q_d\). Therefore the cut event depends only on the sign of the corresponding weighted sum of independent half-normal variables.

**2. Every normal in dimension three.** Since \(u_1+u_2+u_3=0\), every nonzero normal has both a nonpositive and a nonnegative coordinate. If no coordinate vanishes, either two are positive and one negative or vice versa. Reversing the normal complements the cut up to a measure-zero great-circle boundary. If a coordinate vanishes, the other two have equal and opposite values; interchanging those two coordinates maps the chosen half to its complement, so its fraction is \(1/2\). The two-positive case has the unique parameterization specified in the finding, up to permutation.

**3. Exact solid angle.** Fix a rescaled normal \((a,b,-1)\) with \(b=1-a\) and \(0\le a,b\le1\). The complementary portion \(Q_3\cap\{a x_1+b x_2-x_3\le0\}\) is a spherical triangle, with unnormalized generators
\[
r_0=(0,0,1),\qquad r_1=(1,0,a),\qquad r_2=(0,1,b).
\]
The elementary solid-angle identity for the triangle determined by nonzero generators \(r_i\) with positive denominator is
\[
\Omega=2\arctan\frac{|\det(r_0,r_1,r_2)|}
{\|r_0\|\|r_1\|\|r_2\|+\sum_{0\le i<j\le2}(r_i\cdot r_j)\|r_k\|},
\]
where \(k\) is the index not equal to \(i,j\). Here the determinant is one and the denominator factors exactly as
\[
(\sqrt{1+a^2}+a)(\sqrt{1+b^2}+b).
\]
Thus \(\Omega=2\arctan((\sqrt{1+a^2}-a)(\sqrt{1+b^2}-b))\), using \((\sqrt{1+t^2}+t)^{-1}=\sqrt{1+t^2}-t\). Since \(\sigma_2(Q_3)=\pi/2\), subtracting \(\Omega/(\pi/2)\) from one proves the boxed profile, including its boundary values by continuity.

**4. Strict optimization, without relying on a numerical plot.** In spherical coordinates \(x=(\sin\theta\cos t,\sin\theta\sin t,\cos\theta)\) on \(Q_3\), where \(0\le t,\theta\le\pi/2\), set \(q_a(t)=a\cos t+(1-a)\sin t\). Direct integration of the area element \(\sin\theta\,d\theta\,dt\) shows independently that
\[
P_3(a)=\frac2\pi\int_0^{\pi/2}\frac{q_a(t)}{\sqrt{1+q_a(t)^2}}\,dt.
\]
Differentiation twice under the integral sign is valid on the compact rectangle and gives
\[
P_3''(a)=-\frac6\pi\int_0^{\pi/2}
\frac{q_a(t)(\cos t-\sin t)^2}{(1+q_a(t)^2)^{5/2}}\,dt<0
\qquad(0\le a\le1).
\]
The inequality is strict because the integrand before its negative prefactor is positive on a set of positive measure. Substituting \(t\mapsto\pi/2-t\) proves \(P_3(a)=P_3(1-a)\). Consequently the unique maximum occurs at \(a=1/2\), and the only minima on the compact interval occur at its two endpoints. At either endpoint \(P_3=1/2\). At \(a=b=1/2\), each reciprocal factor above equals \((\sqrt5-1)/2\), whose square is \((3-\sqrt5)/2\). This gives the exact global bounds and all equality cases after accounting for permutations and normal reversal. Continuity of the profile supplies every intermediate value.

For completeness, the exact minimum is strictly larger than the general spherical Grünbaum bound \(4/9\) in dimension three. Indeed, with \(x=(3-\sqrt5)/2\), one has \(3/8<x<2/5\). Therefore \(\arctan x>x-x^3/3>1061/3000>22/63>\pi/9\), using \(\pi<22/7\). Multiplying by \(4/\pi\) gives \(m>4/9\).

**5. The dimension-uniform sequence.** For \(u_d=(1,\ldots,1,-(d-1))/\sqrt{d(d-1)}\), the Gaussian model turns the cut event into
\[
H_d\le \overline H_{d-1},\qquad
\overline H_n=\frac1n\sum_{i=1}^{n}H_i.
\]
The half-normal distribution function is \(g(t)=\operatorname{erf}(t/\sqrt2)\) for \(t\ge0\), proving the expectation formula. Since
\[
g''(t)=-\sqrt{\frac2\pi}\,t e^{-t^2/2}<0\quad(t>0),
\]
\(g\) is strictly concave on the positive half-line. Given \(n+1\) independent positive observations, their full sample mean is the arithmetic average of the \(n+1\) distinct leave-one-out means of size \(n\). Strict Jensen concavity, followed by expectation, yields
\[
\mathbb E g(\overline H_{n+1})>\mathbb E g(\overline H_n)
\]
for every \(n\ge1\), because the observations are almost surely not all equal. Symmetry of two independent observations gives \(p_2=1/2\). Finally the strong law gives \(\overline H_n\to\mathbb E H_1=\sqrt{2/\pi}\) almost surely, and bounded convergence applies to \(0\le g\le1\). Its limit is \(g(\sqrt{2/\pi})=\operatorname{erf}(1/\sqrt\pi)\), proving the final assertion.

## Verification

The two area representations above were derived independently: one from a solid-angle formula and the other by integrating spherical coordinates. The accompanying `verify.py` checks their equality at a set of interior and boundary parameters; independently samples the spherical orthant through absolute Gaussian directions; checks the strict curvature sign at test parameters; and samples selected higher-dimensional cuts. All these checks passed. Their finite scope supplements, but does not replace, the analytic proof. Run with `python3 verify.py` in an environment with NumPy and SciPy.

## Relationship to prior work

Myroshnychenko, Ryabogin, Tatarko and Yaskin prove the universal spherical Grünbaum lower bound \((1-1/d)^{d-1}\) for arbitrary spherical convex bodies, but this inequality does not determine the optimal centroidal cut ratio for a prescribed spherical orthant, its extremizing normal, or the higher-dimensional one-versus-rest cut sequence. Basit, Hoehner, Lángi and Ledford prove a spherical Winternitz-type reduction to a triangle, not the exact angular profile of the fixed all-right triangle. The solid-angle expression used in the proof is classical; its elementary identity alone does not establish the directional optimizer or dimensional monotonicity. The readily searchable literature and indexed mathematical records inspected contained no matching complete statement. An unindexed classical worked example remains a legitimate priority risk.

## Limitations

The theorem solves the full centroidal-cut optimization only for the spherical orthant in \(d=3\). For \(d\ge4\), it evaluates and orders a distinguished family of directions and does **not** prove that these directions are globally extremal. This result supplies a fixed-body quantitative test of spherical Grünbaum's theorem, not a new universal bound for arbitrary convex bodies. The independence and full historical priority of this argument have not been externally audited.

## References

1. S. Myroshnychenko, D. Ryabogin, K. Tatarko, V. Yaskin, *The Spherical Grünbaum Inequality*, arXiv:2607.16924v1 (first posted July 18, 2026), https://arxiv.org/abs/2607.16924.
2. B. Basit, S. Hoehner, Z. Lángi, J. Ledford, *Steiner symmetrization on the sphere*, arXiv:2406.10614 (first posted June 15, 2024), https://arxiv.org/abs/2406.10614, especially Section 4.
3. F. Eriksson, *On the measure of solid angles*, Mathematics Magazine 63 (1990), 184–187. The solid-angle identity is also independently checkable by the spherical-coordinate integral used above.
