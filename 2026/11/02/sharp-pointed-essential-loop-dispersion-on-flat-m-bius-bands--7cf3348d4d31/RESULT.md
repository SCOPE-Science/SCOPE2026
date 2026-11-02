# Sharp pointed essential-loop dispersion on flat Möbius bands

## Finding
Let \(L,H>0\), and form the intrinsic Euclidean flat Möbius band
\[
M_{L,H}=\bigl(\mathbb R\times[-H/2,H/2]\bigr)/\langle g\rangle,
\qquad g(x,y)=(x+L,-y).
\]
For \(p\in M_{L,H}\), define \(\lambda(p)\) to be the infimum of the lengths of **based rectifiable loops at \(p\) representing a nonzero element of** \(\pi_1(M_{L,H},p)\cong\mathbb Z\). This is the pointed essential-loop length; the loops need not be smooth at their designated basepoint, and nonprimitive winding classes are included.

If \(P\) is distributed uniformly with respect to intrinsic area, set
\[
r=\frac{H}{\sqrt3L},\qquad
X=\frac{\lambda(P)^2/L^2-1}{3}.
\]
Then the **complete probability law** is
\[
\boxed{X\ \overset{\mathrm{law}}=\ \min(1,Q^2),\qquad
Q\sim\operatorname{Unif}[0,r].}
\]
Equivalently, for \(0\le z<\min(1,r^2)\),
\[
\Pr(X\le z)=\frac{\sqrt z}{r},
\]
with probability one by \(z=\min(1,r^2)\). For \(r>1\) there is an atom of mass \(1-1/r\) at \(X=1\); for \(r\le1\) the law is continuous.

The area-normalized variance of squared pointed loop length is
\[
\boxed{
W(r):=\frac{\operatorname{Var}(\lambda(P)^2)}{\operatorname{area}(M_{L,H})^2}
=\begin{cases}
\frac4{15}r^2,&0<r\le1,\\[3pt]
\frac8{5r^3}-\frac4{3r^4},&r\ge1.
\end{cases}}
\]
It satisfies the **globally sharp and rigid bound**
\[
\boxed{0<W(r)\le\frac{729}{2500},\qquad
W(r)=\frac{729}{2500}\iff r=\frac{10}{9}.}
\]
Thus exactly one similarity shape maximizes this variance: 
\[
\boxed{\frac HL=\frac{10\sqrt3}{9}.}
\]
At this shape precisely one tenth of the intrinsic area consists of points whose shortest nontrivial based loops wind **twice**, rather than once, around the Möbius generator.

## Assumptions and scope
The metric is the intrinsic quotient of a Euclidean strip, not the induced metric of a ribbon embedded in three-space. Both \(L\) and \(H\) are arbitrary positive real numbers; no thin-strip assumption is imposed. Uniform sampling uses the area element inherited from the Euclidean strip. The area equals \(LH\). The minimization allows all nonzero based homotopy classes, including powers of the generator; restricting to primitive classes gives a different invariant. Boundary basepoints are allowed but have zero sampling probability.

## Proof
**1. Exact covering-space minimization.** The strip is simply connected and convex. Every essential loop at a lift \((x,y)\) represents a deck power \(g^k\), \(k\in\mathbb Z\setminus\{0\}\). Any lift of that loop joins \((x,y)\) to \(g^k(x,y)\), hence has length at least their Euclidean distance. The straight joining segment stays in the strip and attains that distance. For nonzero even \(k\),
\[
\|g^k(x,y)-(x,y)\|^2=k^2L^2,
\]
whose minimum is \(4L^2\). For odd \(k\),
\[
\|g^k(x,y)-(x,y)\|^2=k^2L^2+4y^2,
\]
whose minimum is \(L^2+4y^2\). Consequently, for every point,
\[
\boxed{\lambda(p)^2=\min\{4L^2,L^2+4y^2\}
=L^2+\min\{3L^2,4y^2\}.}
\]
The shortest winding class is odd (primitive) when \(2|y|<\sqrt3L\), even with winding \(\pm2\) when \(2|y|>\sqrt3L\), and both are minimizing on the transition levels.

**2. The probability distribution and exact moments.** A fundamental rectangle is \([0,L)\times[-H/2,H/2]\); thus, for area-uniform \(P\), its vertical coordinate \(Y\) is uniform on \([-H/2,H/2]\). Therefore \(Q=2|Y|/(\sqrt3L)\) is uniform on \([0,r]\), and the identity in the Finding follows. Let \(Z=\min(1,Q^2)\). Direct integration of its defining uniform density gives
\[
\mathbb E Z=\begin{cases}r^2/3,&r\le1,\\1-2/(3r),&r\ge1,\end{cases}
\qquad
\mathbb E Z^2=\begin{cases}r^4/5,&r\le1,\\1-4/(5r),&r\ge1.\end{cases}
\]
As \(\lambda(P)^2=L^2(1+3Z)\) and \(\operatorname{area}(M_{L,H})^2=3L^4r^2\),
\[
W(r)=\frac{3\operatorname{Var}(Z)}{r^2},
\]
which simplifies to the displayed two-branch formula, with agreement at \(r=1\).

**3. Global optimization and equality.** On \(0<r\le1\), \(W(r)=4r^2/15\le4/15<729/2500\). On \(r\ge1\), the following exact polynomial identity holds:
\[
\boxed{
\frac{729}{2500}-W(r)
=\frac{(9r-10)^2(27r^2+60r+100)}{7500r^4}.}
\]
Its right-hand side is nonnegative for all \(r\ge1\), vanishing exactly at \(r=10/9\). This proves the sharp inequality, the unique maximizing similarity class, and strictness elsewhere. The atom at that point has mass \(1-9/10=1/10\). Finally, \(W(r)\to0\) as \(r\downarrow0\) or \(r\to\infty\), so the upper extremum is global rather than a local artifact. \(\square\)

## Verification
The supplementary standalone file `checker.py` runs exact-rational tests of 504 deck images, eleven exact truncated-moment cases, the universal sharp-deficit polynomial identity and the optimal atom mass. It also independently evaluates eight parameters by numerical quadrature of the defining distribution. Running `python checker.py` ends with `ALL_CHECKS_PASSED`. The covering-space and factorization proofs above establish the statements for all allowed real parameters; finite testing is corroborative only.

## Relationship to prior work
The Euclidean twisted-strip model is standard. Kalvoda, Krejčiřík and Zahradová (public preprint, December 11, 2019) analyze the flat Möbius strip's Laplacian and spectrum rather than the area distribution of pointed essential-loop lengths. Sabourau and Yassine study global systolic inequalities for Möbius bands with Finsler metrics (2015); their minimization is over unbased closed curves and they do not state the present variance extremum. Katz and Sabourau (2019) analyze systolic flat bands in extremal closed surfaces, a different object. Eyll (public preprint in 2025) investigates fixed-conformal-class systolic stability on Möbius strips and Klein bottles; its variances are of conformal factors, not the squared length of shortest loops based at area-uniform points.

A two-independent-point intrinsic distance distribution on the flat Möbius band is mathematically distinct: it samples two free endpoints, whereas the present invariant imposes a deck-nontrivial return to a fixed basepoint. Pointwise injectivity-radius distributions on closed flat manifolds similarly impose a different deck group and have no boundary strip. Such results can motivate the covering-space method but do not imply the displayed area-normalized variance law. Searches of published mathematical records and these primary sources revealed no equivalent full distribution plus unique sharp optimizing-width statement; this is not a proof of absolute historical priority.

## Limitations
The claims are only for the intrinsic Euclidean family with a glide-reflection identification and include all nonzero based winding classes. The pointed essential-loop length is not the shortest smooth closed geodesic through each point and should not be confused with injectivity radius on a manifold with boundary. The result does not cover curved Möbius metrics, extrinsic embedded ribbon distances, or uniform stability under metric perturbations. Historical originality is provisional and no independent mathematical audit is claimed.

## References
- T. Kalvoda, D. Krejčiřík, K. Zahradová, *Effective quantum dynamics on the Möbius strip*, arXiv:1912.05365, first posted December 11, 2019. https://arxiv.org/abs/1912.05365
- S. Sabourau, Z. Yassine, *Optimal systolic inequalities on Finsler Mobius bands*, arXiv:1503.01282, first posted March 4, 2015. https://arxiv.org/abs/1503.01282
- M. Katz, S. Sabourau, *Systolically extremal nonpositively curved surfaces are flat with finitely many singularities*, arXiv:1904.00730, first posted April 1, 2019. https://arxiv.org/abs/1904.00730
- J. Eyll, *Stability of systolic inequalities for the Möbius strip and Klein bottle*, arXiv:2502.13715, first posted February 19, 2025. https://arxiv.org/abs/2502.13715
