# Global intersection nerve of singular components in cycle graphical-zonotope toric varieties

## Finding
Let \(n\ge4\) and let \(C_n\) be the labeled cycle with edges indexed by \([n]\) in cyclic order. Form its graphical zonotope \(Z_n=\sum_{i=1}^n[0,e_i-e_{i+1}]\), with cyclic indices, in the lattice \(M_0=\{u\in\mathbb Z^n:\sum_i u_i=0\}\). Let \(X_n\) be the normal projective toric variety of its normal fan, over any algebraically closed field \(k\).

Define a **balanced signed four-subset** to be \(\alpha=(P,Q)\), where \(P,Q\subset[n]\) are disjoint two-element sets. Two such labels are **compatible** if no edge index receives a plus sign from one label and a minus sign from the other. Write \(S(\alpha)=P\cup Q\).

The reduced singular locus of \(X_n\) has precisely \(6\binom n4\) distinct irreducible components \(Y_{P,Q}\), indexed by the balanced signed four-subsets. Each is a smooth codimension-three toric subvariety,
\[
Y_{P,Q}\cong (\mathbb P^1_k)^{n-4},
\]
and has the ordinary threefold conifold \(ab-cd=0\) as its generic transverse singularity. In particular its generic transverse Hilbert--Samuel multiplicity is two.

More strongly, for **every nonempty collection** \(\mathcal A\) of distinct balanced signed four-subsets, put \(U=\bigcup_{\alpha\in\mathcal A}S(\alpha)\). Then the **reduced set-theoretic intersection** satisfies
\[
\left(\bigcap_{\alpha\in\mathcal A}Y_\alpha\right)_{\mathrm{red}}=
\begin{cases}
\varnothing,&\text{if the signs are incompatible},\\
V(\sigma_{\mathcal A})\cong (\mathbb P^1_k)^{n-|U|},&\text{if compatible},
\end{cases}
\]
where \(\sigma_{\mathcal A}\) is the unique normal-fan cone carrying the combined nonzero signs on \(U\). Thus **all nonempty reduced intersections are smooth and irreducible**, and the entire intersection nerve is the flag complex of compatible balanced signed four-subsets.

The maximal simplices of this nerve correspond bijectively to full sign assignments with at least two signs of each kind. An assignment with \(p\) plus signs and \(n-p\) minus signs gives a maximal simplex with exactly \(\binom p2\binom{n-p}2\) vertices. Hence the nerve is nonpure for all \(n\ge6\). For \(n=5\), the singular locus is a union of 30 projective lines meeting at 20 torus-fixed points, with three lines through each; its point-line incidence graph is the Desargues graph, equivalently the inclusion graph of two- and three-element subsets of a five-element set.

## Assumptions and scope
All statements use the **normal fan**, not the face-cone fan of \(Z_n\), and the integral lattice dual to \(M_0\). The base field is algebraically closed, without characteristic restrictions. By an intersection above we mean its underlying reduced closed subvariety; no claim about scheme-theoretic intersection multiplicities is made. The nerve has one vertex per distinct irreducible singular component and a face precisely when the corresponding components have nonempty common intersection.

## Proof
**1. Integral sign-vector fan.** A normal-fan covector is an integral vertex potential \(w\in\mathbb Z^n/\mathbb Z(1,\ldots,1)\). The difference map \(w\mapsto\delta\), \(\delta_i=w_i-w_{i+1}\), identifies this lattice *integrally* with \(\{\delta\in\mathbb Z^n:\sum_i\delta_i=0\}\); surjectivity follows by cyclic successive summation. The graphical arrangement is \(\delta_i=0\). Therefore a nonzero normal-fan cone is uniquely represented by a vector \(s\in\{-1,0,+1\}^n\) having both signs, where \(s_i=0\) enforces \(\delta_i=0\) and a nonzero \(s_i\) enforces the corresponding weak sign. Such a cone has dimension \(|\operatorname{supp}(s)|-1\). One cone is a face of another exactly when all of its nonzero signs agree with the latter's signs. The zero cone is also present.

**2. Smoothness and the minimal singular cones.** For a cone with \(p\ge1\) positive and \(q\ge1\) negative signs, let \(E\) be its support, \(|E|=p+q\). The annihilator of its span splits off \(n-|E|\) invertible character directions. In the remaining lattice \(\mathbb Z^E/\mathbb Z(1,\ldots,1)\), the dual semigroup consists of classes of integral vectors satisfying \(u_i\ge u_j\) for positive \(i\) and negative \(j\). Choose the integral threshold \(c=\max_{j\text{ negative}}u_j\); subtracting \(c\) realizes every such vector as a nonnegative combination of the positive singleton classes \([e_i]\) and the negative singleton classes \([-e_j]\). The sole primitive relation is that the sum of all positive generators equals the sum of all negative generators. This proves saturation directly and gives the affine chart
\[
(\mathbb G_m)^{n-p-q}\times
\operatorname{Spec} k[x_1,\ldots,x_p,y_1,\ldots,y_q]
/(x_1\cdots x_p-y_1\cdots y_q).
\]
For \(p=1\) or \(q=1\), this chart is smooth. For \(p,q\ge2\), the Jacobian criterion (valid in every characteristic here) says its reduced singular locus is the union of coordinate spaces specified by choosing two distinct zero \(x\)'s and two distinct zero \(y\)'s. Thus a fan cone is nonsmooth exactly when it has at least two signs of either kind. Its **minimal** nonsmooth faces have exactly two signs of each kind: choose any such four signed positions as a face. The associated orbit closures are precisely the irreducible components of reduced singular support. Distinct signed supports determine distinct cones; their number is \(\binom n4\binom42=6\binom n4\). The four-variable chart is \(k[a,b,c,d]/(ab-cd)\), giving the generic conifold transverse germ and multiplicity two.

**3. Component geometry.** For a balanced four-support cone \(\sigma\), the saturated quotient lattice by \(\operatorname{span}(\sigma)\) maps isomorphically to \(\mathbb Z^{[n]\setminus S(\sigma)}\) by retaining the coordinates \(\delta_j\) outside its support. Its star fan has every combination of positive, negative, or zero signs on those \(n-4\) independent coordinates. This is the product of \(n-4\) complete one-dimensional fans, so its orbit closure is \((\mathbb P^1)^{n-4}\).

**4. All component intersections.** Fan orbit closures intersect exactly along orbit closures corresponding to common cofaces. If two prescribed signs conflict, no cone contains both, so the corresponding orbit closures are disjoint. If all signs agree on overlap, their union defines the unique smallest common cone \(\sigma_{\mathcal A}\), and any other common coface contains it. Thus the reduced intersection is exactly \(V(\sigma_{\mathcal A})\), not a union of components. Its quotient star fan again has unrestricted signs on the \(n-|U|\) unused edge coordinates, giving \((\mathbb P^1)^{n-|U|}\). Pairwise compatibility implies simultaneous compatibility, establishing the flag description.

**5. Maximal nerve faces.** Every compatible signed family extends to a full sign assignment. A maximal compatible family contains every balanced signed four-subset conforming to that assignment. Conversely, because each full assignment with at least two signs of each kind uses every index in some balanced signed four-subset, the assignment is recovered uniquely from the family and cannot be enlarged. The indicated facet cardinality is \(\binom p2\binom{n-p}2\). When \(n\ge6\), the cases \(p=2\) and \(p=3\) give different cardinalities, proving nonpurity.

**6. The five-cycle.** Every singular fixed-point assignment has either two or three positive signs, so the 20 triple-junction points are indexed by the ten two-subsets and ten three-subsets of \([5]\). A balanced four-support component leaves precisely one sign unassigned and therefore connects the two full assignments differing at that sign. Their positive sets form a nested pair of sizes two and three. Every inclusion of this form occurs exactly once, proving that the incidence graph is the Desargues graph.

## Verification
Run `python3 verify.py`. Its standard-library exact enumeration prints `VERIFY_OK` after comparing all admissible fan sign vectors through \(n=7\), classifying minimal nonsmooth cones, verifying all pairwise component intersections, checking star-fan cardinalities and nerve facets, and identifying the 30 incidence edges of the five-cycle. The universal conclusions rely on the preceding lattice and fan arguments, not on finite enumeration.

## Relationship to prior work
Postnikov--Reiner--Williams establish the cone--poset framework and Delzant criterion for simple generalized permutohedra; their graphical-zonotope section concerns simplicity and face enumeration. Hallam--Machacek analyze Gorenstein braid cones and biconnected Hasse-diagram structure. The published deformed-graphical-zonotope treatment gives the graphical-fan ordered-partition model. These results supply foundational descriptions but do not, in their inspected relevant sections, give the above all-parameter **global component-intersection nerve** or its product-of-projective-lines intersections. A prior local-chart analysis of the cycle family already determines its binomial charts and codimension-three singular support; neither the local equations nor that purity result is claimed as a new contribution here. The contribution is the exact global gluing and the Desargues incidence specialization.

## Limitations
This theorem concerns reduced singular supports, reduced intersections, and generic transverse nodes. It does **not** determine scheme-theoretic intersection multiplicities, the Jacobian singular scheme, every completed local germ at multiple intersections, or cohomology of the union. Although extensive mathematical-record and literature comparisons were made, equivalent global incidence information in unindexed sources remains a possibility. Independent mathematical validation has not been performed.

## References
1. A. Postnikov, V. Reiner, L. Williams, *Faces of Generalized Permutohedra*, arXiv:math/0609184 (first public version 2006-09-06), especially §§3 and 5.
2. J. Hallam, J. Machacek, *Gorenstein Braid Cones and Crepant Resolutions*, arXiv:2112.15308 (2021), especially §§1, 2, 4, and 6.
3. *Deformed Graphical Zonotopes*, Discrete & Computational Geometry, DOI:10.1007/s00454-023-00586-x, especially the graphical-fan ordered-partition description and the four-cycle example.
4. E. W. Weisstein, *Desargues Graph*, MathWorld (for the standard name of the inclusion graph \(H(5,2)\)).
