# Euclidean thickness and a two-orbit phase transition for hypersimplices

## Finding
For integers \(n\geq 3\) and \(1\leq k\leq n-1\), let
\[
\Delta_{n,k}=\operatorname{conv}\{\mathbf 1_S:S\subseteq[n],\ |S|=k\}
=\{x\in[0,1]^n:\textstyle\sum_i x_i=k\}.
\]
Equip its affine hull with the Euclidean metric inherited from \(\mathbb R^n\). Put \(m=\min\{k,n-k\}\) and \(q=\lfloor n^2/4\rfloor\). The minimum Euclidean width, taken over all unit vectors tangent to its affine hull, is
\[
\boxed{\displaystyle
 w(\Delta_{n,k})=\min\left\{\sqrt{\frac{n}{n-1}},\;m\sqrt{\frac{n}{q}}\right\}.}
\tag{1}
\]
All minimizing unit normals belong to the following two explicitly described families, and no others:

* Coordinate family: \(\pm\bigl(e_i-\mathbf1/n\bigr)/\sqrt{(n-1)/n}\), one for each \(i\in[n]\). This family minimizes precisely when the first quantity in (1) does not exceed the second.
* Balanced-sign family: choose \(S\subset[n]\) of cardinality \(s\in\{\lfloor n/2\rfloor,\lceil n/2\rceil\}\), and put \(u_i=\sqrt{(n-s)/(ns)}\) on \(S\), \(u_i=-\sqrt{s/(n(n-s))}\) off \(S\). This family minimizes precisely when the second quantity in (1) does not exceed the first. Sign reversal is included by complementing \(S\).

Both families are present if and only if \(n=4m^2-1\). In particular, the first genuinely distinct tie occurs at \((n,m)=(15,2)\), and the next at \((35,3)\). There is no such tie in even dimension parameter \(n\geq4\).

There is also an exact difference-body description, valid for every admissible pair:
\[
\boxed{\displaystyle
\Delta_{n,k}-\Delta_{n,k}
=\left\{z\in\mathbb R^n:\sum_i z_i=0,\ \|z\|_\infty\leq1,\ \|z\|_1\leq2m\right\}.}
\tag{2}
\]
The width in (1) equals the radius of the largest centered Euclidean ball in (2), and that radius is globally maximal among all centers.

## Assumptions and scope
The unit normals lie in \(H_0=\{u\in\mathbb R^n:\sum_i u_i=0\}\). The width in direction \(u\in H_0\) with \(\|u\|_2=1\) is
\[
W_{n,k}(u)=\max_{x\in\Delta_{n,k}}\langle u,x\rangle
-\min_{x\in\Delta_{n,k}}\langle u,x\rangle.
\]
The stated minimum is \(\min_{\|u\|_2=1,u\in H_0}W_{n,k}(u)\). The ambient-coordinate zero-sum condition is essential; allowing normals perpendicular to the affine hull would give width zero. A hypersimplex is nondegenerate in its intrinsic affine hull for all specified parameters. The claims include the simplex boundary cases \(k=1\) and \(k=n-1\), but the two-family transition is substantive for \(m\geq2\).

## Proof
**Step 1: the difference body.** Let \(D=\Delta_{n,k}-\Delta_{n,k}\). Every \(z=x-y\in D\) has zero coordinate sum, \(|z_i|\leq1\), and
\[
\tfrac12\|z\|_1=\sum_{z_i>0}z_i\leq k,
\qquad
\tfrac12\|z\|_1=\sum_{z_i<0}(-z_i)\leq n-k.
\]
For the second inequality, apply the first to \(\mathbf1-x\) and \(\mathbf1-y\). Hence \(D\) lies in the set on the right of (2).

Conversely, suppose \(z\) satisfies the three constraints in (2), and write \(t=\sum_{z_i>0}z_i=\sum_{z_i<0}(-z_i)\). Choose \(y_i\) from the nonempty intervals
\[
\max\{0,-z_i\}\ \leq\ y_i\ \leq\ \min\{1,1-z_i\}.
\]
The lower endpoints sum to \(t\), and the upper endpoints to \(n-t\). Since \(t\leq m\), we have \(t\leq k\leq n-t\). Continuity of interval sums therefore permits \(\sum_i y_i=k\). Then \(y\in\Delta_{n,k}\) and \(x=y+z\in\Delta_{n,k}\), proving (2).

**Step 2: support and inscribed ball.** For \(u\in H_0\), the support function of \(D\) is
\[
h_D(u)=h_{\Delta_{n,k}}(u)+h_{\Delta_{n,k}}(-u)=W_{n,k}(u).
\]
As \(D\) is origin-symmetric and convex, the radius \(r\) of its largest centered Euclidean ball in \(H_0\) is exactly \(\min_{\|u\|_2=1,u\in H_0}h_D(u)\), hence equals the desired width. The symmetry and convexity also show that no off-center Euclidean ball can have larger radius: averaging any such ball with its reflected copy yields an origin-centered ball of the same radius.

By (2), the centered ball of radius \(r\) lies in \(D\) if and only if
\[
r\max_{\substack{u\in H_0\\\|u\|_2=1}}\|u\|_\infty\leq1,
\qquad
r\max_{\substack{u\in H_0\\\|u\|_2=1}}\|u\|_1\leq2m.
\tag{3}
\]

**Step 3: the coordinate barrier.** Orthogonally projecting each coordinate functional to \(H_0\) gives \(p_i=e_i-\mathbf1/n\), with \(\|p_i\|_2^2=(n-1)/n\). Thus
\[
\max_{\substack{u\in H_0\\\|u\|_2=1}}\|u\|_\infty
=\sqrt{\frac{n-1}{n}}.
\tag{4}
\]
Equality in Cauchy–Schwarz holds exactly for \(u=\pm p_i/\|p_i\|_2\) for some \(i\). This gives the first candidate radius and precisely the coordinate normals.

**Step 4: the signed-sum barrier.** Write \(S=\{i:u_i>0\}\), \(s=|S|\), and \(t=\sum_{i\in S}u_i=-\sum_{i\notin S}u_i=\|u\|_1/2\). For unit \(u\in H_0\), Cauchy–Schwarz on each sign block yields
\[
1=\|u\|_2^2\geq t^2\left(\frac1s+\frac1{n-s}\right)
=\frac{nt^2}{s(n-s)}.
\]
Consequently
\[
\|u\|_1\leq2\sqrt{\frac{s(n-s)}n}
\leq2\sqrt{\frac{\lfloor n^2/4\rfloor}{n}}.
\tag{5}
\]
Equality first forces every positive component to have one common value and every negative component to have another; equality second forces the cardinalities to be as balanced as possible. Normalizing gives exactly the balanced-sign family in the finding. Equation (5) gives the second radius in (1).

**Step 5: equality directions and arithmetic transition.** Equality in (3) for the *active, smaller radius* requires equality in the corresponding norm maximization (4) or (5). If both barriers are active, their union is exactly the complete normal set. Equality of the two squared radii is equivalent to
\[
m^2(n-1)=\lfloor n^2/4\rfloor.
\tag{6}
\]
For odd \(n\), (6) reduces to \(4m^2=n+1\). For even \(n\geq4\), (6) would imply
\[
(n-2m^2)^2=4m^2(m^2-1).
\]
If \(m\geq2\), this is impossible because \(m^2-1\) lies strictly between the consecutive squares \((m-1)^2\) and \(m^2\); if \(m=1\), it forces \(n=2\), excluded. This proves the exact transition classification and all equality claims.

## Verification
The standalone program `verify_width.py` requires Python, NumPy, and SciPy. Run `python verify_width.py` to reproduce eight independent low-dimensional convex-hull facet computations (the two-dimensional through five-dimensional intrinsic cases), 3,250 random normal-support comparisons, and 2,449 exact rational tests of the arithmetic phase condition. The independent facet computation enumerates all differences of hypersimplex vertices, projects to an orthonormal zero-sum basis, constructs the convex hull, and reads the least distance from the origin to its supporting hyperplanes; it does not implement the norm argument from the proof. All tests passed. These are finite numerical and exact-rational checks, not a substitute for Steps 1–5.

Boundary checks include \(\Delta_{3,1}\), where the two families coincide, \(\Delta_{4,2}\), where the coordinate family alone wins, and \(\Delta_{15,2}\), where the two geometrically different families tie.

## Relationship to prior work
Har-Peled and Robson (2023), revisiting older work of Alexander and Gritzmann–Klee, give the exact minimum width of a regular simplex. The case \(k=1\) of (1) agrees with their formula after accounting for the standard coordinate simplex having edge length \(\sqrt2\). That earlier simplex theorem does not imply the new proper-hypersimplex formula, the exact difference-body description (2), or the two-orbit phase transition.

Grande, Padrol, and Sanyal (2016) study the same hypersimplex family, obtaining extension-complexity and realization-space results, not Euclidean width. Hibi and Solus (2016) determine facet structures of the more general stable hypersimplices and Gorenstein conditions. Those results supply useful geometric context but do not determine the minimum support-width of the *difference body* in (2). Existing explicit intrinsic inradius results for uniform-matroid base polytopes refer to the original hypersimplex; the present width equals an inradius of its difference body, an essentially different quantity. Likewise, known combinatorial graph metrics of cube–cross-polytope intersection balls do not imply the intrinsic zero-sum Euclidean width here.

The numerical value and all minimizers were compared against targeted mathematical-record searches for hypersimplex thickness, matroid base polytope width, difference bodies, and two-level normal directions, and against accessible prior research claims. No statement covering the combined all-dimensional (1)–(2) and the tie classification was identified. Search absence is not a proof of global novelty.

## Limitations
The metric is Euclidean in the canonical coordinate embedding of the uniform-matroid base polytope; it is not invariant under arbitrary affine transformations. The minimum width is not the mean width, lattice width, or intrinsic inradius of the original hypersimplex. This work does not classify minimum-width directions for arbitrary nonuniform matroid base polytopes. An overlooked older formula for the central section of a cube–cross-polytope intersection could imply part of (1), so independent bibliographic verification remains useful. No independent mathematical audit has been performed.

## References
1. Sariel Har-Peled and Eliot W. Robson, *On the Width of the Regular n-Simplex*, arXiv:2301.02616, first public version 2023-01-06, https://arxiv.org/abs/2301.02616. Complete three-page open paper examined.
2. Francesco Grande, Arnau Padrol, and Raman Sanyal, *Extension complexity and realization spaces of hypersimplices*, arXiv:1601.02416, first posted 2016-01-11, https://arxiv.org/abs/1601.02416.
3. Takayuki Hibi and Liam Solus, *Facets of the r-Stable (n, k)-Hypersimplex*, *Annals of Combinatorics* 20 (2016), 815–829, DOI:10.1007/s00026-016-0325-x. Open-access full text examined.
4. P. Gritzmann and V. Klee, *Inner and outer j-radii of convex bodies in finite-dimensional normed spaces*, *Discrete & Computational Geometry* 7 (1992), 255–280, cited as classical background by Har-Peled and Robson; not independently inspected in full.
