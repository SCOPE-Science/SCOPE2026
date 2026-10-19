# Critical parabolic three-cycle arcs in a non-monotonic toral shear

## Finding
Consider the continuous area-preserving torus map \(H\) at the critical shear parameter \(\eta=1/3\) of Myers Hill--Sturman--Wilson [1,2]. Its complete set of points whose period divides three is
\[
\operatorname{Fix}(H^3)=\{(0,0),(0,2/3)\}\ \cup\
\bigcup_{j=0}^{2}H^j\!\left(J_1\cup J_2\cup\{p_1,p_2\}\right),
\]
where all coordinates are taken modulo one and
\[
\begin{aligned}
J_1&=\{(x,2/9):2/9\le x\le4/9\},\\
J_2&=\{(x,4/9):5/9\le x\le7/9\},\\
p_1&=(0,4/27),\qquad p_2=(0,14/27).
\end{aligned}
\]
The points \((0,0)\) and \((0,2/3)\) are precisely the fixed points. Both \(p_1\) and \(p_2\) generate isolated primitive three-cycles; all points of the two segment families generate primitive three-cycles. The two intervals parameterize different cycles, with no repetitions modulo cyclic exchange. There are no other primitive three-cycles.

At every interior point of these six periodic arcs away from branch boundaries the three-step derivative has the double multiplier \(1\) and is nontrivially unipotent. Both isolated three-cycles are hyperbolic saddles. The entire period-dividing-three set has zero planar area but exact one-dimensional Hausdorff measure, for the standard unit flat torus,
\[
\boxed{\mathcal H^1\bigl(\operatorname{Fix}(H^3)\bigr)
=\frac49\bigl(1+\sqrt2+\sqrt5\bigr).}
\]

## Assumptions and scope
The object is the torus \(\mathbb T^2=(\mathbb R/\mathbb Z)^2\), represented by \([0,1)^2\). Set
\[
 f(y)=\begin{cases}
 (3/2)y,&0\le y\le2/3,\\
 3(1-y),&2/3\le y<1,
 \end{cases}
 \qquad H(x,y)=\bigl(\{x+f(y)\},\{y+x+f(y)\}\bigr),
\]
with \(\{\cdot\}\) the fractional part. The formulas agree on their shared boundary modulo one; \(f(0)=f(1)=0\) on the torus. All assertions concern this exact critical value, not a neighborhood in parameter space. An isolated primitive cycle is meant relative to the period-three set; no claim about general orbits follows.

## Proof
**The two parabolic families.** On the lower and upper shear pieces the affine derivatives are, respectively,
\[
 A=\begin{pmatrix}1&3/2\\1&5/2\end{pmatrix},
 \qquad B=\begin{pmatrix}1&-3\\1&-2\end{pmatrix}.
\]
The upper branch has integer translation \((3,3)\) before reduction modulo one. Direct multiplication gives
\[
 B^2A=\begin{pmatrix}1&9/2\\0&1\end{pmatrix}.
\]
On the relative interiors of \(J_1\) and \(J_2\), the successive branch itinerary is lower--upper--upper. The integer translations introduced by reducing the first and second iterates modulo one disappear in the final torus coordinates because \(B\) has integer entries. Thus the three-step return is \((x,y)\mapsto(x+(9/2)y,y)\pmod1\). Since \((9/2)(2/9)=1\) and \((9/2)(4/9)=2\), both intervals consist of period-three points. The same holds at their endpoints by continuity. None is fixed (direct substitution). The displayed matrix is a nonidentity unipotent Jordan shear, proving the stated neutral multipliers on smooth interiors. Conjugation by the invertible one-step derivatives gives the same spectral type for their other phases.

**Two hyperbolic cycles and two fixed points.** Direct substitution gives the distinct three-cycles
\[
(0,4/27)\to(2/9,10/27)\to(7/9,4/27)\to(0,4/27),
\]
\[
(0,14/27)\to(7/9,8/27)\to(2/9,14/27)\to(0,14/27).
\]
Each lies strictly in the lower shear piece throughout its orbit. The two eigenvalues of \(A\) are \((7\pm\sqrt{33})/4\), one below one and the other above one, hence the multipliers of \(A^3\) make both cycles hyperbolic saddles. Substitution also gives the two fixed points in the statement.

**Exhaustiveness, including discontinuous coordinate representatives.** The standalone standard-library program `checker.py` provides an exact-rational finite polyhedral certificate. Start from the closed unit square and, for each of three steps, split each convex polygon by the affine preimage of the shear switching line and the two integer-coordinate reduction grids. Retain the exact affine lift \(z\mapsto Mz+t\) and exact polygon vertices. The successive full-dimensional cell counts are \(7,32,128\); at every depth their areas sum **exactly** to one. The cells have disjoint interiors, so the finite closed union covers the entire square, including all branch and modulo boundaries. The map's continuity on the torus justifies either limiting branch on a shared boundary.

For each of the \(128\) cells, the fixed-point condition on the torus is \((M-I)z=k-t\) with \(k\in\{-1,0,1\}^2\); these are the only possible wrap differences because the initial and third-step representatives lie in the closed unit square. The checker exhaustively solves each two-by-two rational affine system, using exact half-plane intersections when it has rank one, and verifies consistency of dependent equations. It finds \(32\) raw point representatives (with duplicates on polygon and torus boundaries) and \(12\) nondegenerate segment pieces. It checks **each** point against the displayed fixed points, isolated cycles, or one of the two three-cycle segment families. For every segment piece it exhibits an affine image under one of its first three phases lying wholly within one of the specified base intervals, so no unclassified point remains. It explicitly excludes positive-area fixed polygons. Thus the displayed union contains the entire fixed set. The direct identities in the preceding paragraphs establish the reverse inclusion for every point, not only for sampled parameters. This completes the global classification.

**One-dimensional measure.** Each base segment has Euclidean length \(2/9\). Its three images have tangent vectors \((1,0)\), \((1,1)\), and \((-2,-1)\), respectively, hence lengths \((2/9)(1+\sqrt2+\sqrt5)\) per family. Different phases have slopes \(0,1,1/2\), so cannot overlap in a positive-length subset; same-phase images of the two disjoint segments are disjoint because \(H\) is invertible. The six isolated-cycle points and two fixed points have zero length. Additivity gives the formula.

## Verification
From the directory containing this document run `python3 checker.py`; it uses only Python's standard library with `fractions.Fraction` for all geometric and algebraic computations. In the present verification it returned PASS for exhaustive rational partitions, all rational fixed-set candidates, all six proposed periodic arcs, and the two special fixed points. No floating-point trajectory count or asymptotic extrapolation is used. The proof's topological coverage and exact affine return identities explain why the finite certificate is exhaustive for all real points.

## Relationship to prior work
Myers Hill, Sturman and Wilson [1,2] introduced this continuous two-shear torus family and proved Bernoulli mixing in open parameter windows. They identified the parameter \(\eta=1/3\) as the loss-of-hyperbolicity boundary of a three-step matrix and discussed period-three elliptic islands immediately above it, but the inspected manuscript and journal version do not supply the exact full critical period-three set, the two independent closed families and their endpoints, the two additional hyperbolic three-cycles, or its Hausdorff length. More general historical work on non-ergodic piecewise-affine toral maps [3] studies a different family and does not imply the stated coordinate-level classification. The neutral-fiber phenomena in other baker-like systems likewise do not imply this shear-specific formula.

## Limitations
This theorem does not settle ergodicity, mixing, or stability under parameter perturbation at or near the critical parameter. The unipotent linearization is not a nonlinear stability claim. At orbit points lying on switching lines, the full derivative need not exist. A complete bibliographic uniqueness guarantee is not asserted: an equivalent treatment might appear under other names or in unindexed sources. The critical parameter and the source's map are fixed; no all-parameter periodic-orbit census is claimed.

## References
[1] J. Myers Hill, R. Sturman, M. C. T. Wilson, *A Continuous Family of Non-Monotonic Toral Mixing Maps*, arXiv:2112.07346v1 (14 December 2021), https://arxiv.org/html/2112.07346v1 .

[2] J. Myers Hill, R. Sturman, M. C. T. Wilson, *A Family of Non-Monotonic Toral Mixing Maps*, Journal of Nonlinear Science **32**, article 31 (2022), DOI:10.1007/s00332-022-09790-0, https://eprints.whiterose.ac.uk/id/eprint/185263/7/s00332-022-09790-0.pdf .

[3] R. Adler, B. Kitchens, C. Tresser, *Dynamics of non-ergodic piecewise affine maps of the torus*, Ergodic Theory and Dynamical Systems (2001); general background, not the same shear family.
