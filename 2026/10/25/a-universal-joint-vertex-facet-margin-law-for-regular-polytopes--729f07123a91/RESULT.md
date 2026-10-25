# A universal joint vertex–facet margin law for regular polytopes

## Finding
Let \(P\subset\mathbb R^d\) be a full-dimensional regular convex Euclidean polytope, with \(d\ge2\), edge length \(s>0\), and center at the origin. Let \(X\) be uniformly distributed with respect to \(d\)-dimensional volume on \(P\). Write \(a_1(X)\le a_2(X)\) for the smallest two values of \(\|X-v\|^2\) over distinct vertices \(v\), and \(b_1(X)\le b_2(X)\) for the smallest two distances \(h_F(X)=r-\langle n_F,X\rangle\), over the distinct facets \(F\). Here every \(n_F\) is an outward **unit** normal and \(r>0\) is the inradius of \(P\). The distances \(h_F\) are distances to complete supporting hyperplanes, not always distances to a finite facet as a set.

For any facet \(F\), let \(c_F\) be its center and let \(q\) be the second-smallest value of \(h_G(c_F)\) over facets \(G\). Regularity makes \(q>0\) independent of \(F\). Equivalently, if \(r_F\) denotes the inradius of the regular \((d-1)\)-polytope \(F\), and \(\theta\) is the angle between supporting hyperplanes of adjacent facets, then \(q=r_F\sin\theta\).

Define \(U=(a_2-a_1)/s^2\) and \(V=(b_2-b_1)/q\). Their **joint** survival function is
\[
\Pr(U>u,V>v)=\begin{cases}(1-u-v)^d,&u,v\ge0,\ u+v\le1,\\0,&u,v\ge0,\ u+v>1.\end{cases}
\]
Consequently, \((U,V)\) has density \(d(d-1)(1-u-v)^{d-2}\) on \(\{u\ge0,v\ge0,u+v\le1\}\). In particular, \(U+V\le1\) almost surely; both margins have the \(\operatorname{Beta}(1,d)\) law; and
\[
\mathbb E U=\mathbb EV=\frac1{d+1},\qquad
\operatorname{Cov}(U,V)=-\frac1{(d+1)^2(d+2)},\qquad
\operatorname{Corr}(U,V)=-\frac1d.
\]
As \(d\to\infty\) through any sequence of regular-polytopal dimensions, \((dU,dV)\) converges jointly to independent standard exponential random variables. The joint statement applies to all convex regular-polytope types, including exceptional types in dimensions three and four.

## Assumptions and scope
The term *regular* means flag-transitive by Euclidean isometries. All vertices lie on a common circumsphere, all facets are congruent regular polytopes tangent to a common centered insphere, and edges of a regular polytope are its shortest vertex-to-vertex distances. Values on measure-zero tie loci can be specified by nondecreasing order statistics, so tie-breaking is unnecessary. Uniform means normalized Euclidean volume. The analysis does not include arbitrary uniform or semiregular polytopes or distance to finite facet subsets.

## Proof
1. **Flag subdivision.** Fix a complete face flag consisting of a vertex \(v\), an edge \(E=[v,w]\), successively higher-dimensional incident faces, and final facet \(F\). Its characteristic simplex \(C\) has vertices the center \(o=0\) of \(P\), the centers of the flagged faces, and \(v\). The characteristic simplices tile \(P\), meeting only along lower-dimensional boundaries. Each is nondegenerate; a volume-uniform point conditional on membership in any \(C\) has barycentric coordinates \((\lambda_o,\lambda_v,\ldots,\lambda_F)\sim\operatorname{Dirichlet}(1,\ldots,1)\) with \(d+1\) ones.

2. **Nearest and second-nearest vertices.** For any two vertices \(v,w\), \(\|x-w\|^2-\|x-v\|^2=-2\langle x,w-v\rangle\), since all polytope vertices have equal squared norm. Thus every comparison is affine (indeed linear) in \(x\). At \(x=v\), the closest vertex is \(v\) and \(w\) is a second-closest vertex because edges realize the shortest vertex distances. At the center of any flagged face containing the edge \(E\), the vertices \(v,w\) are tied for the minimum distance to that center: the face center is the orthogonal projection of \(o\) onto the affine hull of that face, and its radial hyperplane exposes precisely that face. At \(o\), all vertices tie. Hence on the entire simplex \(C\), affine comparisons certify that \(v\) is nearest and \(w\) is second nearest. The affine function \(\|x-w\|^2-\|x-v\|^2\) equals \(s^2\) at \(v\) and vanishes at every other vertex of \(C\). Therefore \(U=\lambda_v\) throughout \(C\).

3. **Nearest and second-nearest supporting facets.** Let \(H\) be the flagged ridge \((d-2)\)-face inside \(F\), and \(G\ne F\) the other facet meeting \(F\) along \(H\). The corresponding distance difference is the affine function \(h_G(x)-h_F(x)=\langle n_F-n_G,x\rangle\). At the center \(o\), all facet slacks tie. At the centers of the flagged faces of dimension at most \(d-2\), both \(F\) and \(G\) contain that face; hence their slacks tie for the minimum. At \(c_F\), facet \(F\) has slack zero and \(G\) is second nearest. To see the last assertion, the outward unit facet normals are (up to scale) the vertices of the regular polar polytope; the closest distinct normal to \(n_F\) must be an edge-neighbor of that vertex, corresponding to a facet adjacent along a ridge to \(F\). Any such adjacent facet gives the same slack \(q\) at \(c_F=r n_F\). Since the supporting-hyperplane comparisons are affine, these endpoint inequalities imply that \(F\) is first and \(G\) second throughout \(C\). Their gap vanishes at all characteristic-simplex vertices except \(c_F\), where it equals \(q\). Therefore \(V=\lambda_F\) throughout \(C\).

4. **Joint integration and consequences.** On each characteristic simplex, \((U,V)=(\lambda_v,\lambda_F)\). The two coordinates of a uniform \(d\)-simplex follow \(\operatorname{Dirichlet}(1,1,d-1)\); integrating its density over \(U>u,V>v\) gives \((1-u-v)^d\). Because this law is identical on every characteristic simplex, mixing their volume weights does not change it. Standard Dirichlet moments give the moments and correlation stated above. Joint survival after replacing thresholds by \(u/d,v/d\) tends to \(e^{-u-v}\), which characterizes independent unit-rate exponentials.

5. **Geometric normalization.** In the affine hyperplane of \(F\), the restriction of the distance to the adjacent facet plane \(G\) increases perpendicular to their common ridge \(H\) with slope \(\sin\theta\). The face center \(c_F\) lies exactly \(r_F\) from every ridge of the regular facet, hence \(h_G(c_F)=r_F\sin\theta=q\). This establishes the nonzero scale directly and checks its invariance under regular-polytope symmetries.

## Verification
The proof does not use numerical extrapolation. A standalone script `verify_joint.py` uses independent random-volume sampling from centered facet-cones and checks 80,000 points in each of the regular tetrahedron, cube, octahedron, icosahedron and dodecahedron. It checks the joint-survival formula at \((u,v)=(0.2,0.15)\), the exact negative correlation \(-1/3\), the support constraint, and each marginal \(\operatorname{Beta}(1,3)\) law. Tolerances distinguish Monte Carlo evidence from proof. The script requires NumPy and SciPy and prints every geometric sample check. No finite experiment is claimed to verify all dimensions.

## Relationship to prior work
Bäsel (2012) derives regular-polygon chord and two-random-point distance laws; it does not examine a single interior point's ordered vertex and supporting-hyperplane margins, or their dependence. Kabluchko, Litvak and Zaporozhets (2015) study random directional projection widths and Gaussian maxima of regular polytopes, which are different observables and sampling measures. A previously documented nearest-vertex squared-distance **marginal** law for regular polytopes obtains \(U\sim\operatorname{Beta}(1,d)\), but it supplies neither the facet variable \(V\) nor their joint law, covariance, or support-exclusion phenomenon. The result proved here specifically contributes that joint primal–dual relationship; it does not claim that an isolated beta marginal is new. Public-record searches for equivalently normalized facet-support margins and joint laws did not identify a theorem implying the joint statement. Search incompleteness remains a bibliographic limitation.

## Limitations
The face centers and supporting-plane distances rely on Euclidean regularity, and joint universality need not extend to arbitrary tangential or merely vertex-transitive polytopes. Hyperplane distance is not generally Euclidean distance to the corresponding *finite* facet. The result concerns uniform volume, not uniform boundary points or random orientations. The search cannot establish absolute historical priority; no independent verification or audit is claimed.

## References
- U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, first submitted 2012-04-12, §§1–4.
- Z. Kabluchko, A. E. Litvak, D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479, first submitted 2015-11-26, §§1–3.
- H. S. M. Coxeter, *Regular Polytopes*, 3rd ed., Dover (1973), background on flags, duality and regularity. Only standard background facts are used; the book was not text-inspected in this review.
