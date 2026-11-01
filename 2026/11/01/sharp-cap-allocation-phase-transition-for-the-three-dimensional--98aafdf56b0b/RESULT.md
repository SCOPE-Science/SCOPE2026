# Sharp cap-allocation phase transition for the three-dimensional Godbersen ratio

## Finding

Let \(T\) be any nondegenerate tetrahedron with barycentric coordinates \(\lambda_0,\lambda_1,\lambda_2,\lambda_3\). For \(s,t\geq 0\), \(s+t\leq 1\), and \(s^3+t^3<1\), form the two-corner truncation
\[
K_{s,t}=\{x\in T:\lambda_1(x)\leq 1-s,\ \lambda_2(x)\leq 1-t\}.
\]
The two removed corner tetrahedra have disjoint interiors, and their combined relative volume is \(c=s^3+t^3\). Define
\[
\rho(s,t)=\frac{V_3(K_{s,t},K_{s,t},-K_{s,t})}{\operatorname{vol}_3(K_{s,t})}.
\]
Here \(V_3\) is the symmetric, Minkowski-multilinear mixed volume normalized by \(V_3(K,K,K)=\operatorname{vol}_3(K)\).

**Exact two-parameter profile.** For all the indicated real parameters,
\[
\boxed{\rho(s,t)=\frac{(1-s)(1-t^2)+(1-t)(1-s^2)+1-s^2-t^2}{1-s^3-t^3}.}
\]
In particular \(\rho(s,t)\geq5/3\), with equality if and only if \(s+t=1\). Thus the entire nondegenerate edge-contact locus has the same normalized mixed volume \(5/3\), independently of how asymmetric the two caps are.

**Sharp fixed-removed-volume range.** For any fixed \(0<c<1\), put \(w=c^{1/3}\). Among all \(s,t\geq0\) with \(s+t\leq1\) and \(s^3+t^3=c\), the largest ratio is
\[
\boxed{\rho_{\max}(c)=\frac{3+2w}{1+w+w^2},}
\]
attained exactly at \((s,t)=(w,0)\) or \((0,w)\). The smallest ratio is
\[
\boxed{\rho_{\min}(c)=\begin{cases}
\displaystyle\frac{3-2r-4r^2+2r^3}{1-2r^3},&0<c\leq\frac14,\quad r=(c/2)^{1/3},\\[2mm]
\displaystyle\frac53,&\frac14\leq c<1.
\end{cases}}
\]
For \(c<1/4\), its unique parameter pair is \(s=t=(c/2)^{1/3}\). For \(c>1/4\), the two minimizing pairs (up to swapping coordinates) are
\[
(s,t)=\left(\frac{1+\sqrt{(4c-1)/3}}2,\frac{1-\sqrt{(4c-1)/3}}2\right)
\]
and its reversal. At \(c=1/4\), the two branches coincide at \(s=t=1/2\). Hence precisely one quarter of the tetrahedron's volume is the phase boundary between balanced, disjoint caps and edge-contact minimizers.

## Assumptions and scope

A tetrahedron is nondegenerate if its affine span has dimension three. The cap at vertex \(v_1\) is the part with \(\lambda_1>1-s\), and similarly for \(v_2\). When either parameter is zero, that cap is absent. The condition \(s+t\leq1\) makes the cap interiors disjoint; at equality their boundaries meet on the original edge \([v_1,v_2]\). For \(0<c<1\), the remaining polytope has strictly positive volume even along the edge-contact locus. The expressions are invariant under any invertible affine transformation of \(T\).

The volume deficit \(c\) is measured relative to the original tetrahedron, not relative to the truncated body. The theorem minimizes and maximizes the *normalized opposite-body mixed volume* within this natural two-corner truncation family. It does not assert an optimum among all polytopes of a given volume.

## Proof

**1. Affine normalization and volume.** By affine invariance of the quotient, take \(T=\operatorname{conv}(0,e_1,e_2,e_3)\). Then
\[
K_{s,t}=\{x_i\geq0,\ x_1+x_2+x_3\leq1,\ x_1\leq1-s,\ x_2\leq1-t\}.
\]
The removed sets are homothetic corner tetrahedra with volumes \(s^3/6\) and \(t^3/6\). Their interiors are disjoint when \(s+t\leq1\), whence
\[
\operatorname{vol}_3(K_{s,t})=\frac{1-s^3-t^3}{6}>0.
\]

**2. Mixed-area calculation.** For a full-dimensional polytope \(K\), the standard mixed-area formula is
\[
V_3(K,K,-K)=\frac13\sum_F\operatorname{area}_2(F)\,h_{-K}(n_F),
\]
where \(F\) ranges over facets and \(n_F\) is the outward Euclidean unit normal. The support function is \(h_{-K}(n)=-\min_{x\in K}\langle n,x\rangle\). The three facets with outward normals \(-e_i\) have support values \(1-s,1-t,1\), respectively. All remaining facet normals are proportional to \(e_1,e_2,(1,1,1)\), and their support values vanish because \(0\in K\) and all coordinates of \(K\) are nonnegative. The Euclidean areas of the coordinate facets are
\[
\frac{1-t^2}{2},\qquad\frac{1-s^2}{2},\qquad\frac{1-s^2-t^2}{2}.
\]
The last identity uses the disjointness of the two planar corner caps; it remains true at touching. Thus
\[
6V_3(K_{s,t},K_{s,t},-K_{s,t})
=(1-s)(1-t^2)+(1-t)(1-s^2)+1-s^2-t^2=:N(s,t).
\]
Dividing by the volume proves the exact profile.

**3. Exact plateau and its equality case.** Put \(u=s+t\), \(v=st\), and \(c=s^3+t^3\). Direct expansion yields
\[
N=3-u-2u^2+(4+u)v,\qquad c=u^3-3uv.
\]
A polynomial identity gives
\[
\rho(s,t)-\frac53
=\frac{(1-u)\bigl((1-u)(5u+4)+12v\bigr)}{3(1-c)}.
\]
Since \(u\leq1\), \(v\geq0\), and \(1-c>0\), this is nonnegative and is zero exactly when \(u=1\).

**4. Optimization at fixed removed volume.** Fix \(0<c<1\). Feasible parameters are uniquely determined up to exchange by their sum \(u\) because \(v=(u^3-c)/(3u)\). The inequalities \(v\geq0\), \(4v\leq u^2\), and \(u\leq1\) are equivalent to
\[
c^{1/3}\leq u\leq\min\{(4c)^{1/3},1\}.
\]
Substituting \(v=(u^3-c)/(3u)\) into \(N\), differentiating with \(c\) fixed, and using \(c\leq u^3\), gives
\[
\frac{dN}{du}=-1-\frac43u+u^2+\frac{4c}{3u^2}
\leq u^2-1<0\quad(0<u<1).
\]
At \(u=1\) this derivative is also strictly negative because \(c<1\). The denominator \(1-c\) is fixed; therefore the ratio strictly decreases with \(u\). Its maximum is at \(u=c^{1/3}\), equivalent to \(st=0\). The numerator there factors as \((1-w)(3+2w)\), and the denominator as \((1-w)(1+w+w^2)\), proving \(\rho_{\max}\). If \(c\leq1/4\), the greatest possible \(u\) is \((4c)^{1/3}\), which is equivalent to \(s=t=r=(c/2)^{1/3}\). If \(c\geq1/4\), the greatest possible \(u\) is one, and the quadratic equations \(s+t=1\) and \(st=(1-c)/3\) yield the stated minimizing pair and the \(5/3\) plateau. The equality characterizations follow from strict monotonicity and the quadratic discriminant.

## Verification

An accompanying standalone Python 3 standard-library program, `verify_double_caps.py`, reconstructs the eight possible vertices of the truncated tetrahedron and independently forms its difference body from all vertex differences. The program enumerates every supporting facet by exact integer plane-side tests, triangulates its polygonal facets using integer 2D convex hulls, and computes volume by exact integer determinants. For each sample it checks
\[
\operatorname{vol}_3(K-K)=2\operatorname{vol}_3(K)+6V_3(K,K,-K),
\]
where the identity follows from mixed-volume polarization and reflection symmetry in dimension three. The program does *not* invoke the mixed-area facet formula for the verification of the difference-body volume.

Executed output: `VERIFY_OK exact difference-body polytope reconstruction: 11 independent instances; 66 monotonicity/identity instances`. This is finite validation; the assertions for every admissible real pair are proved above by the analytic facet formula, factorization, and derivative inequality.

Run locally with `python3 verify_double_caps.py`. No third-party Python packages or downloaded data are needed.

## Relationship to prior work

Godbersen's inequality in dimension three gives \(V_3(K,K,-K)\leq3\operatorname{vol}_3(K)\); the 2026 resolution identifies the simplex as the only full-dimensional equality case. That result alone does not determine the sharp two-cap profile at a prescribed removed volume. Sadovsky's coordinate-projection formula for anti-blocking bodies, which includes the present family, gives a general route to computing the mixed volume and is explicitly acknowledged as prior technique; our claim is **not** a new general mixed-volume identity for anti-blocking bodies. The additional conclusion here is the exact fixed-volume redistribution optimization, its sharp threshold at relative removal \(1/4\), and the entire edge-contact \(5/3\) equality locus.

Existing one-corner and symmetric all-corner truncation calculations address distinct parameter slices and do not imply the sharp two-corner allocation law without additional analysis. Literature searches for double-truncated tetrahedra, Godbersen ratios, difference-body volumes, and equivalent sharp cap-allocation statements did not identify the same fixed-volume optimization. Absence from the searches does not establish publication priority.

## Limitations

The theorem is limited to three-dimensional simplices truncated at **at most two** vertices by parallel-to-opposite-facet cuts whose removed cap interiors do not overlap. It does not cover cuts with \(s+t>1\), arbitrary convex bodies, or higher-dimensional Godbersen ratios. It does not establish a new global Godbersen inequality, nor an independent review of its mathematics. Priority remains subject to older sources or terminology not identified by the checked searches.

## References

- F. Fryš, J. Kotrbatý, M. A. Mouamine, and S. Wang, *Higher-order Godbersen inequality and a characterization of simplices via the face lattice*, arXiv:2610.06806v1 (first public 2026-10-05), https://arxiv.org/abs/2610.06806 .
- O. Friedland, E. Putterman, and M. Szusterman, *The equality case in Godbersen's inequality and its generalizations*, arXiv:2610.04527v1 (2026-10-03), https://arxiv.org/abs/2610.04527 .
- S. Sadovsky, *Godbersen's conjecture for locally anti-blocking bodies*, arXiv:2312.03473v1 (2023-12-06), https://arxiv.org/abs/2312.03473 . Particularly the coordinate-projection mixed-volume formula, Lemma 2.1 in v3.
- J. Kotrbatý, *On a generalization of Godbersen's conjecture*, arXiv:2502.02149v1 (2025-02-04), https://arxiv.org/abs/2502.02149 .
