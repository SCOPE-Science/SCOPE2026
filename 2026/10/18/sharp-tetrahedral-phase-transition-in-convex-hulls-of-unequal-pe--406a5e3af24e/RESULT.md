# Sharp tetrahedral phase transition in convex hulls of unequal perpendicular disks

## Finding
Let \(D_R=\{(x,y,0):x^2+y^2\le R^2\}\) and \(E_r=\{(x,0,z):x^2+z^2\le r^2\}\), where \(R\ge r>0\), and put \(K_{R,r}=\operatorname{conv}(D_R\cup E_r)\). The largest Euclidean volume of a tetrahedron contained in \(K_{R,r}\) has the exact two-branch expression
\[
M(R,r)=\max\left\{\frac{\sqrt3}{4}R^2r,\;\frac23(s+t)\sqrt{R^2-s^2}\sqrt{r^2-t^2}\right\},
\]
where
\[
q=R/r,\quad k=\frac{q^2-1+\sqrt{(q^2-1)^2+16q^2}}4,\quad
 t=\frac r{\sqrt{2+k}},\quad s=kt.
\]
The first branch dominates at sufficiently small \(r/R\), the second at sufficiently large \(r/R\), with precisely one transition. With \(\rho=r/R\), it occurs at the uniquely determined \(\rho_0\in(0,1)\) where the branches agree, numerically \(\rho_0\approx0.67116753624\). Both constructions occur as genuine contained tetrahedra.

## Assumptions and scope
The disks have a common center, perpendicular planes, positive radii, and \(R\ge r\). Tetrahedra may have arbitrary positions and shapes; there is no assumption that their vertices are preassigned to the two disks. For \(R<r\), interchange their roles. No classification of every possible maximizer is claimed.

## Proof
**Localization.** Write six times the signed tetrahedral volume as the determinant of four homogeneous columns \((1,v_i)\). For each vertex separately, the signed determinant is affine. Since \(K_{R,r}\) is the convex hull of the union of the two disks, maximizing either sign of the determinant, successively in its four vertices, gives a maximizing tetrahedron with vertices on the two circular boundaries. Four vertices in one disk have zero volume, leaving distributions \(3+1\) and \(2+2\).

**Three-plus-one.** For three vertices on \(D_R\), the base triangle area is at most \(3\sqrt3R^2/4\), with equality at an inscribed equilateral triangle. The remaining vertex in \(E_r\) has distance at most \(r\) from the base plane. Thus the maximum tetrahedral volume of this type is \(\sqrt3R^2r/4\). Interchanging the disks gives at most \(\sqrt3r^2R/4\), no larger since \(R\ge r\).

**Two-plus-two.** Let the two chords in the respective disks have midpoint vectors \(m_1,m_2\) with lengths \(s,t\), and full chord vectors \(v_1,v_2\). The determinant identity for their four endpoints yields
\[
6V=|\det(v_1,v_2,m_2-m_1)|
\le4(s+t)\sqrt{R^2-s^2}\sqrt{r^2-t^2}.
\]
Here the first bound is Hadamard's determinant inequality and \(\|m_2-m_1\|\le s+t\); a chord of a radius-\(R\) disk at midpoint distance \(s\) has length at most \(2\sqrt{R^2-s^2}\), with the analogous bound for \(r,t\). Every inequality is simultaneously attained by taking the chord midpoints at \(s\) and \(-t\) on the common \(x\)-axis, the first chord along the \(y\)-axis, and the second along the \(z\)-axis. Therefore the precise optimum of this type is
\[
\max_{0\le s\le R,\;0\le t\le r}\frac23(s+t)\sqrt{R^2-s^2}\sqrt{r^2-t^2}.
\]
After scaling \(u=s/R\), \(v=t/r\), and \(\rho=r/R\), the dimensionless objective becomes
\[
G_\rho(u,v)=\frac23(u+\rho v)\sqrt{1-u^2}\sqrt{1-v^2}.
\]
For every \(\rho>0\), it has a unique maximizer with \(0<u,v<1\): its logarithm is strictly concave on the positive square, its maximum cannot occur where either coordinate equals one, and the derivatives into the square at either zero boundary are positive. The first-order equations, in unscaled variables, are
\[
R^2=2s^2+st,\qquad r^2=2t^2+st.
\]
Putting \(k=s/t>0\) and \(q=R/r\), division gives \(q^2=(2k^2+k)/(2+k)\). The unique positive root is the stated radical \(k\), and then \(t=r/\sqrt{2+k}\) and \(s=kt\). This proves the exact second branch.

**The phase transition.** The maximum \(H(\rho)=\max_{[0,1]^2}G_\rho(u,v)\) is continuous in \(\rho\). It is strictly increasing for \(0<\rho\le1\): evaluate the larger-\(\rho\) function at the unique interior maximizer for the smaller \(\rho\), whose \(v\)-coordinate is strictly positive. At \(\rho=0\), \(H(0)=1/3\), whereas \(H(1)=8/(9\sqrt3)\); the latter is achieved by \(u=v=1/\sqrt3\). Since
\[
\frac13<\frac{\sqrt3}4<\frac8{9\sqrt3},
\]
there is exactly one \(\rho_0\in(0,1)\) with \(H(\rho_0)=\sqrt3/4\). The desired tetrahedral volume is \(R^2r\max\{\sqrt3/4,H(\rho)\}\), which establishes all asserted regimes.

## Verification
Independent direct numerical optimization over four circle angles was performed at radius ratios \(1,0.8,0.6,0.4,0.2,0.1\); the maxima agree with the two-chord branch at the precision of optimization, and the comparison with the triangular construction changes sign between \(0.6\) and \(0.8\). Numerical solution of the scalar threshold equation gives \(\rho_0\approx0.67116753624\). These finite computations check, but do not replace, the determinant and concavity proof. Reproduction requires only evaluation of the displayed radical and scalar bisection of \(H(\rho)-\sqrt3/4\).

## Relationship to prior work
Finch's 2012 analysis of convex hulls of perpendicular disks establishes ambient volume, surface area, and mean-width geometry, rather than maximizing inscribed tetrahedra. Nash, Pir, Sottile, and Ying's 2016 study classifies algebraic boundaries, stationary bisecants, and spectrahedral aspects of convex hulls of two circles; its conclusions do not imply the tetrahedral phase formula. General largest-simplex principles justify studying four-point determinants but do not fix the unequal-radius transition. Closely ranked existing results about maximal tetrahedra in cube–cross-polytope intersections, the Steinmetz bicylinder (the polar geometry in the equal-radius case), and intrinsic volumes of three-disk hulls concern different optimization domains or invariants and give no direct implication for this formula.

## Limitations
The formula assumes concentric perpendicular disks and covers exactly the tetrahedral-volume objective. It does not address off-center disks, other dihedral angles, a full classification of non-circle-supported maximizers, or independent historical-priority certification. More obscure literature on extremal tetrahedra in orthogonal disk hulls may exist.

## References
1. S. R. Finch, *Convex Hull of Two Orthogonal Disks*, arXiv:1211.4514, first submitted 19 November 2012.
2. E. D. Nash, A. F. Pir, F. Sottile, and L. Ying, *Convex Hull of Two Circles in R³*, arXiv:1612.09382, first submitted 30 December 2016.
