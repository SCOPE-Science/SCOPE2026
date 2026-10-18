# Smooth torus-fixed-point spectrum of wheel graphical-zonotope toric varieties

## Finding
Let \(m\ge3\), and let \(W_{m+1}=K_1*C_m\) be the wheel with \(m\) rim vertices and one hub. Write \(Z_m\) for its graphical zonotope in the lattice \(M=\{(u_0,\ldots,u_m)\in\mathbb Z^{m+1}:\sum u_i=0\}\):
\[
Z_m=\sum_{\{i,j\}\in E(W_{m+1})}[0,e_i-e_j].
\]
Let \(X_m\) be the projective toric variety defined by the normal fan of \(Z_m\), over an arbitrary algebraically closed field. A torus-fixed point is called smooth when its affine toric chart is regular.

There are exactly \(3^m-3\) torus-fixed points. Exactly
\[
s_m=4m-4+\left(\frac{3+\sqrt5}{2}\right)^m+\left(\frac{3-\sqrt5}{2}\right)^m+2\cos\left(\frac{m\pi}{3}\right)
\]
of them are smooth; thus precisely \(3^m-3-s_m\) are singular.

More precisely, orient the graph according to the chamber corresponding to a torus-fixed point, and let \(k\) be the number of its \(m\) spokes directed toward the hub. The exact number of smooth points in this stratum is \(S_{m,k}\), where
\[
S_{m,0}=S_{m,m}=2m,
\]
and, for each integer \(1\le k\le m-1\),
\[
S_{m,k}=m\sum_{r=1}^{\min\{k,m-k\}}\frac1r
\binom{k+r-1}{2r-1}\binom{m-k+r-1}{2r-1}.
\]
These formulae are integral counts, and \(s_m=\sum_{k=0}^m S_{m,k}\). In particular, for \(m=3,4,5,6\), the respective smooth counts are \(24,58,140,344\). The smooth fraction of fixed points tends exponentially to zero, at rate \(\bigl((3+\sqrt5)/6\bigr)^m\) up to a bounded ratio.

## Assumptions and scope
The graph is the simple wheel with rim length \(m\ge3\); for \(m=3\) it is the complete graph on four vertices. The lattice is the saturated type-A root lattice \(M\) specified above, with dual torus-cocharacter lattice \(N=\operatorname{Hom}(M,\mathbb Z)\). The zonotope is full-dimensional of dimension \(m\). No restriction on the characteristic is necessary: regularity of the affine toric chart is tested by a unimodular fan cone. The theorem concerns **torus-fixed points only**; it does not purport to describe every singular torus orbit or the irreducible components of the full singular locus.

The orientation associated with a chamber directs each edge from the smaller to the larger coordinate of an interior chamber vector. The Hasse diagram (transitive reduction) of the resulting reachability poset has the same vertex set as the wheel. A projective toric chart at the corresponding fixed point is smooth exactly when the Hasse diagram is a tree. The latter criterion follows because the primitive inequalities defining the chamber are the root differences attached to the cover edges: if there are \(m\) and the graph is a spanning tree, they form a basis of \(M\); if there are more than \(m\), the dual cone is not simplicial. This is the integral refinement of the cone-poset dictionary in Postnikov–Reiner–Williams, Sections 3 and 5.

## Proof
**1. Acyclic orientations and smoothness.** Acyclic orientations of the connected wheel correspond bijectively to maximal cones in the normal fan and hence to torus-fixed points of \(X_m\). In any orientation, the transitive reduction of the reachability poset consists precisely of the nontransitive directed edges of the graph. It is connected as an undirected graph, because transitive edges can be replaced by directed paths of covering edges. The maximal cone has one facet per Hasse edge. If its Hasse diagram has exactly \(m\) edges, it is a spanning tree; the differences \(e_i-e_j\) along a tree form a \(\mathbb Z\)-basis of \(M\), so the cone is smooth. With more edges, the cone has more than \(m\) facets and cannot be smooth.

**2. Both kinds of spokes present.** Let \(S\) be the nonempty set of rim vertices whose spokes point toward the hub, and let \(T\) be its nonempty complement. An oriented triangle is forbidden, so every rim edge meeting both \(S\) and \(T\) is forced to point from \(S\) toward \(T\). Conversely, these directions, together with arbitrary orientations of each maximal contiguous rim run of \(S\) or \(T\), make an acyclic orientation: no directed path can return from \(T\) to \(S\), nor traverse a directed cycle in a proper path run.

Let \(c\) be the number of boundary rim edges between unlike letters. Then \(c=2r\), with \(r\) runs of each type. Every boundary edge is transitive, via its two spokes and the hub. Every within-run rim edge is a cover relation, because the other way around the rim passes through the opposite type and cannot return, and the hub cannot serve as an alternative route between two vertices of the same type. Therefore there are exactly \(m-2r\) rim cover edges. Hub spokes are cover relations precisely at the sinks of the directed \(S\)-runs and the sources of the directed \(T\)-runs; every other spoke is transitive via another vertex of the same run. Every run has at least one such extremum. It follows that the Hasse diagram is a tree exactly when each \(S\)-run has a unique sink and each \(T\)-run has a unique source.

An undirected path on \(\ell\) vertices has exactly \(\ell\) orientations with a unique sink: choose the sink, and direct all edges toward it. Similarly it has exactly \(\ell\) orientations with a unique source. A run of length \(\ell\) therefore contributes weight \(\ell\).

**3. Stratified enumeration.** Fix \(k=|S|\) in the mixed case and let \(r\) count the \(S\)-runs. For an ordered choice of lengths \(a_1,\ldots,a_r\ge1\) summing to \(k\), the total orientation weight is \(\prod a_i\); hence its generating series is \(R(z)^r\), where
\[
R(z)=\sum_{\ell\ge1}\ell z^\ell=\frac{z}{(1-z)^2}.
\]
Likewise for the \(T\)-runs of total length \(m-k\). Selecting a distinguished beginning of an \(S\)-run counts each labeled cyclic arrangement \(r\) times, whereas the beginning can occupy any of \(m\) labeled rim vertices. Thus
\[
S_{m,k}=\sum_{r\ge1}\frac mr [z^k]R(z)^r\,[z^{m-k}]R(z)^r.
\]
The coefficient identity \([z^k]R(z)^r=\binom{k+r-1}{2r-1}\) gives the claimed finite sum (out-of-range coefficients are zero).

**4. Uniform-spoke cases.** If all spokes point into the hub (the case where all point outward is dual), the rim induces an acyclic orientation of \(C_m\). A directed rim edge is transitive precisely when the other \(m-1\) rim edges form a coherently directed alternative path. At most one rim edge has this property. If none does, the \(m\) rim cover edges plus at least one spoke cover edge prevent a tree. If exactly one does, the remaining \(m-1\) rim edges make a directed Hamiltonian path; there is a unique rim sink, giving precisely one additional hub-cover edge and hence a tree. There are \(m\) choices of the exceptional edge and two directions for the path, so \(S_{m,m}=2m\). Reversing all arrows gives \(S_{m,0}=2m\).

**5. Closed form.** Summing the mixed cases over \(k\),
\[
\sum_{k=1}^{m-1}S_{m,k}
=m[z^m]\sum_{r\ge1}\frac{R(z)^{2r}}r
=m[z^m]\bigl(-\log(1-R(z)^2)\bigr).
\]
Since
\[
1-R(z)^2=\frac{(1-3z+z^2)(1-z+z^2)}{(1-z)^4},
\]
we obtain the degree-\(m\) logarithmic coefficient
\[
\left(\frac{3+\sqrt5}{2}\right)^m+
\left(\frac{3-\sqrt5}{2}\right)^m+2\cos(m\pi/3)-4.
\]
Adding the uniform-spoke contribution \(4m\) proves the smooth formula. The chromatic polynomial of the wheel is \(t((t-2)^m+(-1)^m(t-2))\). Stanley's acyclic-orientation evaluation at \(t=-1\) gives \(3^m-3\) total orientations. Since \((3+\sqrt5)/2<3\), the smooth fraction decays exponentially, with leading factor \(((3+\sqrt5)/6)^m\).

## Verification
The self-contained Python 3 file `wheel_smooth_fixed_point_check.py` enumerates all \(2^{2m}\) directed edge assignments for each \(3\le m\le9\), checks acyclicity by topological sorting, computes the transitive reduction by directed reachability, and classifies smoothness using the spanning-tree criterion. It verifies both the closed formula and the complete incoming-spoke distribution against direct enumeration, and independently checks the acyclic total. The final line is `VERIFY_OK`. This finite test supports but does not establish the all-parameter proof given above. No external computational package or data file is needed.

## Relationship to prior work
Postnikov, Reiner, and Williams, *Faces of Generalized Permutohedra* (first public version 2006), establish the graphical-zonotope/acyclic-orientation correspondence, the tree-poset chamber criterion (Proposition 3.5), and the global simplicity classification (Proposition 5.2). Those foundations are used, not claimed as original. Their result says when **all** fixed points are smooth; it does not compute the detailed number of smooth fixed points in a nonsimple wheel family or their spoke-stratified distribution. Grujić, *Counting faces of graphical zonotopes* (first public version 2016), gives an arbitrary-graph face enumerator, but an ordinary face-number polynomial does not encode which particular vertex cones are smooth. Iriarte, *Acyclic Orientations and Spanning Trees* (2014 preprint), concerns orientation ideals and related non-crossing trees; its accessible full preprint does not give the wheel smooth-fixed-point formula. A closely related 2015 doctoral thesis was identified, but its repository PDF could not be accessed for a full comparison; its abstract alone does not resolve this question.

## Limitations
The result classifies torus-fixed-point regularity, **not** the whole singular locus; nonfixed singular torus orbits may occur. A strong proof of originality cannot rest solely on searching: an equivalent smooth-chamber count might appear under graphic-arrangement terminology or in inaccessible thesis material. The closed form resembles classical wheel spanning-tree Lucas expressions, but no identification of the two enumerated objects is asserted. The finite checker validates only \(3\le m\le9\). No independent mathematical audit has been performed.

## References
1. A. Postnikov, V. Reiner, L. Williams, *Faces of generalized permutohedra*, arXiv:math/0609184 (first public 2006-09-06), Sections 3, 5, https://arxiv.org/abs/math/0609184; full-text https://math.mit.edu/~apost/papers/genpermfaces.pdf.
2. V. Grujić, *Counting faces of graphical zonotopes*, arXiv:1604.06931 (first public 2016-04-23), https://arxiv.org/abs/1604.06931.
3. B. Iriarte Giraldo, *Acyclic Orientations and Spanning Trees*, arXiv:1412.8114 (first public 2014-12-28), https://arxiv.org/abs/1412.8114.
4. B. Iriarte Giraldo, *Combinatorics of acyclic orientations of graphs: algebra, geometry and probability*, doctoral thesis, Massachusetts Institute of Technology, 2015, https://hdl.handle.net/1721.1/99325 (full comparison not obtained).
