# Universal mean, sharp variance, and logarithmic law for side-sampled quadrilaterals

## Finding

Let \(Q=ABCD\) be a nondegenerate, strictly convex Euclidean quadrilateral with vertices listed counterclockwise, and let \(O=AC\cap BD\). Independently choose one point uniformly by arclength on each of the four **distinct sides**, in cyclic order, and let \(R\) be the area of their convex hull divided by the area of \(Q\). Define the two affine-invariant diagonal ratios
\[
p=\frac{|AO|}{|AC|},\qquad q=\frac{|BO|}{|BD|}.
\]
Then \(0<p,q<1\), and the **exact universal mean and variance** are
\[
\boxed{\mathbb E R=\frac12,\qquad
\operatorname{Var}(R)=\frac1{144}+\frac7{72}\left[(p-\tfrac12)^2+(q-\tfrac12)^2\right].}
\]
Consequently, over all strictly convex quadrilaterals, \(\operatorname{Var}(R)\ge1/144\), with equality exactly for parallelograms, and \(\sup\operatorname{Var}(R)=1/18\), not attained by a nondegenerate quadrilateral. The variance excess exactly measures squared diagonal-bisection asymmetry.

For every parallelogram, the **complete, shape-independent area law** is
\[
R\ \stackrel d=\ \frac{1+XY}{2},
\]
where \(X,Y\) are independent random variables with density \(1-|x|\) on \([-1,1]\). For \(0<r<1\), put \(z=|2r-1|\). Its density away from \(r=1/2\) is
\[
f_R(r)=4\left[-(1+z)\log z-2(1-z)\right].
\]
It diverges logarithmically at \(r=1/2\), is symmetric about \(1/2\), and vanishes at the support endpoints. Define \(H(z)=(2z+z^2)\log z+2z-\frac52z^2\) for \(0<z\le1\) and \(H(0)=0\). Then the exact cumulative distribution is
\[
F_R(r)=\begin{cases}0,&r\le0,\\
\tfrac12+H(1-2r),&0<r<\tfrac12,\\
\tfrac12,&r=\tfrac12,\\
\tfrac12-H(2r-1),&\tfrac12<r<1,\\
1,&r\ge1.
\end{cases}
\]
All centered odd moments vanish, and for every integer \(k\ge0\),
\[
\mathbb E[(R-\tfrac12)^{2k}]=\frac1{4^k((2k+1)(k+1))^2}.
\]
The sharp endpoint behavior is \(\Pr(R\le\varepsilon)=\frac43\varepsilon^4+O(\varepsilon^5)\) as \(\varepsilon\downarrow0\); the upper endpoint has the same tail by symmetry.

## Assumptions and scope

Uniform arclength on an individual straight side means its affine edge parameter is uniform on \([0,1]\). Samples on different sides are independent. This is a **stratified** four-point model: there is exactly one point per side. It is not the model of four identically distributed random points on the union of all sides. All formulae hold regardless of Euclidean side lengths or angles, because affine transformations preserve sidewise uniformity and the ratio of areas. Zero-length sides, nonconvex configurations and collinear successive vertices are excluded.

## Proof

**1. Exact corner decomposition.** Write the vertices cyclically as \(V_0,V_1,V_2,V_3\) and let \(U_i=(1-t_i)V_i+t_iV_{i+1}\), where indices are cyclic and \(t_0,\ldots,t_3\) are independent uniforms on \([0,1]\). Let \(A_Q\) denote the original area and set
\[
c_i=\frac{|\det(V_{i-1}-V_i,V_{i+1}-V_i)|}{2A_Q}.
\]
The four disjoint corner triangles between the original and inscribed quadrilaterals partition the discarded area. The triangle at \(V_i\) has normalized area \(c_i(1-t_{i-1})t_i\), because both of its adjacent edge portions scale independently. Therefore the following is an **exact samplewise identity**:
\[
R=1-\sum_{i=0}^3c_i(1-t_{i-1})t_i.\tag{1}
\]

**2. Diagonal-coordinate reduction.** Translate the diagonal intersection to the origin and use the two diagonal vectors as an affine basis. Then, after harmless scaling, the ordered vertices are
\[
(-p,0),\quad(0,q),\quad(1-p,0),\quad(0,q-1).
\]
The quadrilateral area is \(1/2\); direct determinants give \((c_0,c_1,c_2,c_3)=(p,q,1-p,1-q)\). Thus
\[
\sum_i c_i=2,\quad \sum_i c_i^2=1+2[(p-\tfrac12)^2+(q-\tfrac12)^2],\quad
\sum_i c_ic_{i+1}=1.\tag{2}
\]
Conversely, for any \(0<p,q<1\), these coordinates describe a strictly convex quadrilateral: all four successive turning determinants are positive. Hence no further constraints on \((p,q)\) are hidden.

**3. Mean and variance.** Put \(Z_i=(1-t_{i-1})t_i\). From the first two moments of a uniform variable,
\[
\mathbb E Z_i=\tfrac14,\quad
\operatorname{Var}(Z_i)=\tfrac19-\tfrac1{16}=\tfrac7{144}.
\]
Opposite \(Z_i\)'s are independent. Adjacent pairs share one edge parameter in complementary form, giving
\[
\mathbb E[Z_iZ_{i+1}]=\mathbb E(1-t_{i-1})\,\mathbb E[t_i(1-t_i)]\,\mathbb E t_{i+1}=\tfrac1{24},
\quad\operatorname{Cov}(Z_i,Z_{i+1})=-\tfrac1{48}.
\]
Substitution into (1), including both orientations of each adjacent covariance, yields
\[
\operatorname{Var}(R)=\tfrac7{144}\sum_i c_i^2-\tfrac1{24}\sum_i c_ic_{i+1}
=\tfrac1{144}+\tfrac7{72}[(p-\tfrac12)^2+(q-\tfrac12)^2].
\]
Also, \(\mathbb E R=1-\frac14\sum_i c_i=1/2\). The variance minimum is attained only at \(p=q=1/2\), which says both diagonals bisect each other, characterizing parallelograms. The open-square domain gives \((p-1/2)^2+(q-1/2)^2<1/2\), so the upper bound is \(1/144+(7/72)(1/2)=1/18\) and is approached at the corners of the domain, but never attained.

**4. Complete law at equality.** In a parallelogram the four \(c_i\) are \(1/2\). Rearranging (1) gives the exact algebraic factorization
\[
2R-1=(t_0+t_2-1)(t_1+t_3-1).
\]
The independent factors \(X=t_0+t_2-1\) and \(Y=t_1+t_3-1\) are sums of two independent uniform variables minus one and have the triangular density \(1-|x|\) on \([-1,1]\). For \(0<z<1\), the even product density is
\[
f_{XY}(z)=2\int_z^1(1-x)(1-z/x)\,\frac{dx}{x}
=2[-(1+z)\log z-2(1-z)].\tag{3}
\]
Scaling by \(1/2\) proves the displayed density. Integrating (3) from zero to \(z\) yields \(\int_0^z f_{XY}(u)du=-H(z)\), which gives the CDF by symmetry. As \(z\to0\), (3) behaves like \(-2\log z-4+o(1)\), proving the central logarithmic singularity. Near \(z=1\), the parenthetical expression in (3) is \((1-z)^3/6+O((1-z)^4)\). Substituting \(z=1-2\varepsilon\), integrating the resulting density of \(R\), gives the exact quartic endpoint coefficient \(4/3\).

Independence and \(\mathbb E[X^{2k}]=2\int_0^1x^{2k}(1-x)dx=1/((2k+1)(k+1))\) give all even centered moments. The odd ones vanish by sign symmetry. This completes all assertions.

## Verification

The standalone `checker.py` performs 325 exact rational corner-area identity checks on explicitly constructed convex quadrilaterals; verifies the covariance identities using rational fractions; differentiates the CDF numerically against the density at 499 interior thresholds; and tests 720,000 seeded boundary-sampling realizations across four diagonal-ratio pairs, including the predicted means, variances and equi-centred CDF values. The general theorem follows from the exact identities above; randomized checks are not substituted for universal proof. Reproduce with `python3 checker.py` from the extracted package directory; it has no third-party dependencies.

## Relationship to prior work

Maesumi, *Triangle Inscribed-Triangle Picking* (public version dated 2017-03-28; later arXiv:1804.11007), analyzes **three independently sampled points, one on each side of a triangle**, including normalized area moments and its distribution. This is a distinct simplex model. Reitzner, Schütt and Werner, *The Convex Hull of Random Points on the Boundary of a Simple Polytope* (arXiv:1911.05917, first public 2019-11-14), study **independent identically distributed samples over the entire polytope boundary** and asymptotic expected volume defects, rather than a fixed four-point one-per-side distribution. Neither cited primary result supplies the displayed diagonal-ratio variance classification or parallelogram product law. The exact diagonal ratios also occur in other deterministic quadrilateral invariants, but the observables and conclusions are different.

## Limitations

These statements concern only strict convex quadrilaterals with one independent uniform-arclength point from each *distinct* side. The full probability density for arbitrary non-parallelograms is not derived here; only the first two moments are universal in closed form. The sup variance belongs to a degenerate boundary limit, not an admissible proper quadrilateral. Literature comparisons are based on the identified accessible original texts and targeted searches; an unindexed prior equivalent calculation cannot be excluded. This work has not received an independent mathematical audit.

## References

1. A. Maesumi, *Triangle Inscribed-Triangle Picking*, viXra:1703.0273v1, 2017-03-28, https://www.vixra.org/pdf/1703.0273v1.pdf; later arXiv:1804.11007, https://arxiv.org/abs/1804.11007.
2. M. Reitzner, C. Schütt and E. M. Werner, *The Convex Hull of Random Points on the Boundary of a Simple Polytope*, arXiv:1911.05917, https://arxiv.org/abs/1911.05917; *Discrete & Computational Geometry* 69 (2023), 453–504, https://doi.org/10.1007/s00454-022-00460-2.
