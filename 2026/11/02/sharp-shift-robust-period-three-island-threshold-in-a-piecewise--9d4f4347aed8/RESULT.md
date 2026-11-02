# Sharp shift-robust period-three island threshold in a piecewise symplectic torus family

## Finding

For the two-branch McMillan–Hénon map on the side-two torus given below, the complete positive-area period-three region is an explicit union of convex polygons. Its area is a periodized quadratic cardinal B-spline, and it survives *every* vertical shift precisely when the length \(h\) of the slope-\(-1\) branch satisfies \(h>2/3\). At the original equal-width parameter, its normalized area ranges sharply from \(1/16\) to \(3/16\) as the vertical shift varies. No claim about all periods outside these polygons is made.

Write \(u_+=\max\{u,0\}\) and define
\[
 B_h(t)=\tfrac12\big[t_+^2-3(t-h)_+^2+3(t-2h)_+^2-(t-3h)_+^2\big].
\]
For every real shift \(d\) and branch point \(c\) with \(0<c<2\), put \(h=2-c\) and \(t_k=d-2c+2k\), where \(k\in\mathbb Z\). If \(\lambda\) is normalized Haar probability on the torus and \(\mathrm{Per}_3\) denotes the points of *least* period three, then
\[
 \boxed{\lambda(\mathrm{Per}_3)=\tfrac14\sum_{k\in\mathbb Z} B_h(t_k).}
\]
The sum is finite. The number of distinct open, positive-area components of the all-slope-\(-1\) period-three island set is exactly
\[
 \boxed{\#\{k\in\mathbb Z:0<t_k<3h\}.}
\]
The components are triangles when \(0<t_k\le h\) or \(2h\le t_k<3h\), and hexagons when \(h<t_k<2h\); at the two intermediate equalities they are triangles, not hexagons. Each contains exactly one fixed point, and every other point has least period three. In particular,
\[
 \boxed{\lambda(\mathrm{Per}_3)>0\ \text{for every }d\in\mathbb R\iff c<4/3.}
\]
At \(c=4/3\), at least one congruence class of shifts has zero period-three area; for \(c>4/3\), the set of such shifts has nonempty interior modulo two.

For \(c=1\) and \(\delta=d\bmod2\in[0,2)\), the *unnormalized* island area \(A(\delta)=4\lambda(\mathrm{Per}_3)\) is
\[
 A(\delta)=\begin{cases}
 \tfrac12\big[\delta^2+(1-\delta)^2\big],&0\le\delta\le1,\\[2pt]
 1-\tfrac12\big[(\delta-1)^2+(2-\delta)^2\big],&1\le\delta<2.
 \end{cases}
\]
It follows that \(\min_d\lambda(\mathrm{Per}_3)=1/16\), attained at \(\delta=1/2\), and \(\max_d\lambda(\mathrm{Per}_3)=3/16\), attained at \(\delta=3/2\). At \(\delta=0\), the known reference configuration has period-three probability \(1/8\).

## Assumptions and scope

Represent \(\mathbb T_2^2=(\mathbb R/2\mathbb Z)^2\) by \([0,2)^2\). For \(0<c<2\) and \(d\in\mathbb R\), set
\[
 f_{c,d}(y)=\begin{cases}d,&0\le y<c,\\ d+c-y,&c\le y<2,\end{cases}
 \qquad F_{c,d}(x,y)=\big(y,-x+f_{c,d}(y)\big)\pmod2.
\]
This is a measurable invertible, piecewise-affine, piecewise-symplectic torus transformation, with possible discontinuity at the torus seam. Claims concerning differentiability exclude the finitely many branch lines and their relevant preimages; measure statements are unaffected by these null sets. A three-cycle has *least* period three unless it is a fixed point. The results concern this entire two-parameter family, not merely maps with a globally polygonal first integral.

Define \(H=(c,2)\), \(z=(d+c-x-y)\bmod2\) with representative in \([0,2)\), and
\[
 E_{c,d}=\{(x,y)\in H^2:z\in H\}.
\]
For any integer \(k\), the component \(P_k\) is the relative open polygon in \(H^2\) satisfying
\[
 x+y+z=d+c+2k,\quad z=d+c+2k-x-y\in H.
\]
The area formula concerns the (possibly empty) union of all these \(P_k\); other three-periodic points, if present on branch boundaries or affine exceptional lines, have zero two-dimensional Haar measure.

## Proof

**1. The region and exact three-step return.** On \(H\) the force is \(d+c-y\). If \(x,y,z\in H\) as above, then exact evaluation gives
\[
 F_{c,d}(x,y)=(y,z),\quad F_{c,d}(y,z)=(z,x),\quad F_{c,d}(z,x)=(x,y).
\]
Thus \(F_{c,d}^3=\operatorname{id}\) on \(E_{c,d}\). The three coordinates of each such point have the fixed real sum \(d+c+2k\) for one integer \(k\), and every cyclic permutation has the same sum. Consequently each nonempty \(P_k\) is itself invariant under \(F_{c,d}\).

**2. Completeness up to an area-zero set.** Off the finitely many branch boundaries of the first three iterates, the Jacobian of a single step equals one of
\[
 A_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
 A_1=\begin{pmatrix}0&1\\-1&-1\end{pmatrix}.
\]
Their elementary relations are \(A_0^2=-I\), \(A_1^3=I\), \(A_1A_0^2=-A_1\ne I\), and \(A_1^2A_0=\begin{psmallmatrix}1&-1\\0&1\end{psmallmatrix}\ne I\). Cyclic permutations of an invertible matrix word have conjugate products, hence the only three-letter word with identity derivative is \(111\). On every other full-dimensional word cell, the equation \(F_{c,d}^3(x,y)=(x,y)\pmod2\) is a nontrivial affine linear system. Its solution set is a finite union of lines or isolated points, thus is two-dimensional Lebesgue null. The branch boundaries and their preimages are also finite unions of lines. Therefore all remaining period-three points outside \(E_{c,d}\) are null. Every nonempty \(P_k\) has precisely one fixed point: the unique solution of \(x=y=z\), namely \((x,y)=(c+t_k/3,c+t_k/3)\); the other points in \(P_k\) have least period three. Removing finitely many fixed points does not change area.

**3. Exact polygon section and area.** Substituting \(x=c+u\), \(y=c+v\), and \(z=c+w\), the component \(P_k\) is parametrized by
\[
 0<u,v,w<h,\qquad u+v+w=t_k,\qquad w=t_k-u-v.
\]
It is a nonempty open convex two-dimensional polygon exactly when \(0<t_k<3h\). The plane cuts the three-dimensional cube into a triangle for \(0<t_k\le h\) and \(2h\le t_k<3h\), and a hexagon for \(h<t_k<2h\). Its projected \((u,v)\)-area is the convolution
\[
 \operatorname{area}(P_k)=\int_0^h\!\int_0^h\mathbf1_{(0,h)}(t_k-u-v)\,du\,dv=B_h(t_k).
\]
The final expression follows by integrating the inclusion–exclusion formula for three unit-step intervals; endpoint conventions do not affect area. Since \(F_{c,d}\) has inverse \((x',y')\mapsto(f_{c,d}(x')-y',x')\pmod2\) and determinant \(1\) on both affine branches, normalized Haar probability is invariant. The torus has area four. Summing the disjoint component areas and using Step 2 proves the claimed exact probability.

**4. Shift-robust threshold.** The interval \((0,3h)\) contains at least one representative of every residue modulo two if and only if its length is strictly greater than two. At length exactly two, the endpoint residue is omitted, and for length less than two a positive-length gap is omitted. Since the \(t_k\) run over all representatives of \(d-2c\pmod2\), island survival for all \(d\) is equivalent to \(3h>2\), i.e. \(c<4/3\). The stated zero-area sets at and above the boundary follow from the same open-interval condition.

**5. Equal-branch sharp area.** Set \(h=1\) and \(\delta=d\bmod2\). For \(0<\delta<1\), the contributing spline terms are at arguments \(\delta\) and \(\delta+2\), giving \(A=[\delta^2+(1-\delta)^2]/2\). At the endpoints \(\delta=0,1\) the same formula holds by continuity, with a vanishing spline term. For \(1<\delta<2\) exactly one nonzero term occurs, at argument \(\delta\), giving \(A=1-[(\delta-1)^2+(2-\delta)^2]/2\). Elementary completion of squares yields the stated unique minima and maxima modulo two.

## Verification

The included `verify_period3.py` uses only Python's standard library and exact rational arithmetic. Executing `python3 verify_period3.py` checks all eight derivative branch words, 552 independent polygon-clipping versus spline area and positivity comparisons, 3,168 three-step orbit identities on the strict islands, and the equal-branch extremizers. The mathematical proof above, not a finite test, establishes the all-parameter statements. The checker does not enumerate every orbit or prove global integrability of the family.

## Relationship to prior work

Zolkin, Kharkov and Nagaitsev introduced McMillan–Hénon symplectic maps with piecewise forces and, in arXiv:2311.17616, the equal-width torus map `d1`, with force notation \([\{0,1\},\{-1,1\};2]\) after setting lattice length two. Their Section III.1 states that this special degenerate map has three- and seven-periodic orbits. This is credited, not claimed as new. The 2022 predecessor arXiv:2201.13133 studies polygon-invariant plane maps and the general one- and two-piece affine mechanisms. Here the new, narrower invariant is the exact *two-parameter Haar area and component geometry* of all three-periodic islands, especially the sharp branch-width threshold for survival under every shift. Both the reference map's existing cycle statement and its drawings are compatible with, but do not supply, this complete shift-width formula. Similar area studies of other piecewise maps do not imply it without identifying this torus map's triple-sum geometry.

## Limitations

The theorem is a classification of the positive-area least-period-three set, **not** of every zero-area exceptional cycle, nor of the period spectrum outside it. The result does not assert global integrability for arbitrary \(c,d\) or smooth symplecticity at branch discontinuities. Complete equivalence checks against literature not publicly indexed cannot be guaranteed; the area computation is based on elementary cube-section geometry and could independently appear elsewhere. Independent mathematical auditing and external certification have not been performed.

## References

- T. Zolkin, Y. Kharkov and S. Nagaitsev, *Integrable symplectic maps with a polygon tessellation*, arXiv:2311.17616 (first posted 2023-11-29), *Physical Review Research* **6**, 023324 (2024), https://arxiv.org/html/2311.17616v3 , https://doi.org/10.1103/PhysRevResearch.6.023324 . Relevant equations and discussion: Sections II.1, II.2, III.1–III.3.
- T. Zolkin, Y. Kharkov and S. Nagaitsev, *Machine-assisted discovery of integrable symplectic mappings*, arXiv:2201.13133 (first posted 2022-01-31), *Physical Review Research* **5**, 043241 (2023), https://arxiv.org/html/2201.13133v4 . Relevant discussion: Sections II, IV.
