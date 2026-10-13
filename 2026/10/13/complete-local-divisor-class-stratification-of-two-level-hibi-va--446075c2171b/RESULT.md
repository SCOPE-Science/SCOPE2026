# Complete local divisor-class stratification of two-level Hibi varieties

## Finding
Let \(a,b\ge2\). Let \(X_{a,b}\) be the normal complex projective toric variety of the stable-set polytope of \(K_{a,b}\), equivalently of the order polytope of a complete two-level poset with \(a\) upper and \(b\) lower elements. Every local Weil-divisor class group at a closed point of \(X_{a,b}\) is **free abelian**, and its rank is determined exactly by the torus orbit containing that point, as follows.

Write the polytope in variables \(u_i\) (upper, \(1\le i\le a\)) and \(v_j\) (lower, \(1\le j\le b\)) as
\[
P_{a,b}=\{(u,v):0\le v_j\le u_i\le1\text{ for all }i,j\}.
\]
Each orbit corresponds to a nonempty face \(F\) of \(P_{a,b}\). Choose a point \(w\) in the relative interior of \(F\), and calculate \(p=\#\{i:u_i(w)=0\}\) and \(q=\#\{j:v_j(w)=1\}\). Then \(p\) and \(q\) cannot both be positive. For any closed point \(z\) of that orbit, the class group is
\[
\operatorname{Cl}(\mathcal O_{X_{a,b},z})\simeq\begin{cases}
\mathbb Z^{p(b-1)},&p>0,\\
\mathbb Z^{q(a-1)},&q>0,\\
\mathbb Z^{(r-1)(s-1)},&p=q=0,\ \min_i u_i(w)=\max_jv_j(w)=t\in(0,1),\\
0,&\text{otherwise},
\end{cases}
\]
where, in the third line, \(r=\#\{i:u_i(w)=t\}\) and \(s=\#\{j:v_j(w)=t\}\). This is independent of the chosen relative-interior point.

In particular, **the locally \(\mathbb Q\)-factorial locus and smooth locus coincide**. At a torus-fixed point corresponding to a nonempty independent set \(S\) in the \(a\)-vertex part, with \(|S|=k\), its class group is \(\mathbb Z^{k(b-1)}\); for a nonempty \(k\)-set in the \(b\)-vertex part the rank is \(k(a-1)\). The empty-set fixed point is smooth. The largest local class-group rank among torus-fixed points is \(ab-\min(a,b)\). By Friedl’s general global class-group formula, \(\operatorname{Cl}(X_{a,b})\simeq\mathbb Z^{ab}\); thus the global rank exceeds even the largest fixed-point local rank by exactly \(\min(a,b)\).

## Assumptions and scope
Everything is over \(\mathbb C\). Parameters \(a,b\) are arbitrary integers at least two. Class groups mean Weil divisors modulo principal divisors in the indicated *local normal rings*, not the global class group of the projective variety or its homogeneous coordinate ring. Statements about orbits use the standard face-orbit correspondence: a face of polytope \(P\) yields an orbit of dimension \(\dim F\). No independent audit is asserted.

## Proof
**1. Polytope, normality, and facets.** For the complete bipartite graph \(K_{a,b}\), an independent set lies entirely in one part. Its stable-set polytope has inequalities \(x_i\ge0\), \(y_j\ge0\), \(x_i+y_j\le1\). Set \(u_i=1-x_i\) and \(v_j=y_j\) to obtain the displayed order polytope. All \(a+b+ab\) inequalities \(u_i\le1\), \(v_j\ge0\), \(u_i\ge v_j\) define facets for \(a,b\ge2\). Their primitive inward normals are, up to the orientation convention, \(-e_{u_i}\), \(e_{v_j}\), and \(e_{u_i}-e_{v_j}\). Normality follows from the integer decomposition property: for \((x,y)\in kP\cap\mathbb Z^{a+b}\), put \(M=\max_i x_i\) and \(N=\max_jy_j\). Then \(M+N\le k\). Allocate \(M\) disjoint positions to left-only independent sets and \(N\) to right-only independent sets, filling the remaining positions with the empty set; choose occurrences of vertex \(i\) in exactly \(x_i\) of the left positions, and vertex \(j\) in exactly \(y_j\) right positions. Thus every such point is a sum of \(k\) lattice vertices of \(P\), proving normality of the associated toric semigroup.

**2. Active incidence graph.** Add formal boundary nodes \(0,1\). The facet normals are columns of the oriented incidence matrix of the graph with edges \(0-v_j\), \(v_j-u_i\), and \(u_i-1\), after deleting the rows for the two boundary nodes. On a face \(F\), the active edges are precisely those for which the corresponding endpoint values agree when \(0\) and \(1\) have values zero and one. There can be no active path joining the boundary nodes, since it would force \(0=1\). The active submatrix is totally unimodular (node-edge incidence matrices and their submatrices are totally unimodular), and therefore its nonzero maximal minors have gcd one. Its image is saturated in the lattice spanned by the active normals.

**3. Local toric divisor sequence.** Let \(E_F\) be the active facets. The normal cone at \(F\) has one primitive extremal ray for each element of \(E_F\), and these are all its rays. After splitting the torus factor along \(F\), the toric divisor exact sequence yields
\[
\mathbb Z^{\operatorname{codim} F}\longrightarrow\mathbb Z^{E_F}\longrightarrow \operatorname{Cl}(\mathcal O_{X_{a,b},z})\longrightarrow0.
\]
The left map is the character-to-invariant-divisor pairing with the active primitive normals. It has rank \(\operatorname{codim}F\). Total unimodularity implies its cokernel has no torsion. Thus the class-group rank is \(|E_F|-\operatorname{codim}F\), the cycle rank of the active-edge graph, since deleting an anchor row from each component does not change that rank.

**4. Classify cyclic active blocks.** Evaluate the coordinates at any relative-interior \(w\in F\). If \(p>0\) upper coordinates are zero, every lower coordinate must also be zero. The nontrivial active component consists of the boundary node \(0\), those \(p\) upper nodes, and all \(b\) lower nodes. It is the complete bipartite graph \(K_{p+1,b}\), with \((p+1)b\) edges and \(p+b+1\) vertices. Its cycle rank is \((p+1)b-(p+b)=p(b-1)\). All other active components are trees or isolated nodes. Dually, if \(q>0\) lower coordinates equal one, every upper coordinate equals one. The active component \(K_{q+1,a}\) has cycle rank \(q(a-1)\).

If neither boundary case holds, any active edge \(v_j-u_i\) must have a common value \(t=\min_i u_i(w)=\max_jv_j(w)\in(0,1)\). The active interior block is \(K_{r,s}\), with cycle rank \(rs-(r+s-1)=(r-1)(s-1)\). No other interior mixed block can exist: the inequalities \(v_j\le u_i\) for every pair force all cross equalities to have this same extremal value. Boundary edges, if present, form stars disjoint from this block, so contribute zero cycles. If there is no cross equality and no boundary block, the graph is a forest. This proves all cases.

**5. Smoothness and factoriality.** A toric orbit is smooth exactly when its normal cone is regular. Every simplicial active cone is unimodular by total unimodularity, so regularity is equivalent to absence of active cycles. Equivalently the displayed class-group rank is zero. In a normal toric local ring, \(\mathbb Q\)-factoriality is equivalent to the local divisor-class group being torsion. Since the group here is free, it is torsion exactly when it vanishes. Hence the locally \(\mathbb Q\)-factorial and smooth loci are equal. For fixed points, the independent-set vertices have all coordinates in \(\{0,1\}\). Their active graphs are the two boundary cases, yielding the stated ranks and maximum.

## Verification
The standalone file `checks/facecheck.py` enumerates all faces as facet intersections with rational arithmetic; for the pairs \((a,b)=(2,2),(3,2),(2,3),(3,3),(4,2),(2,4)\), it verifies for **every face** that the rank of active primitive facet normals plus face dimension equals \(a+b\), and that the cycle-rank formula equals the claimed piecewise expression. It also cross-checks fixed-point ranks and maximal singular-face support. See `checks/facecheck_output.txt` for observed counts. Finite calculations do not constitute the proof for general \(a,b\); the incidence-matrix and graph arguments above do.

## Relationship to prior work
Friedl, *Divisors on Projective Hibi Varieties* (arXiv:1506.02407), Theorem 8 computes the **global** class group of an arbitrary projective Hibi variety, and Lemma 12 gives a criterion for global divisors to be locally principal. Those are established general inputs, not new here. Lakshmibai–Mukherjee, *Singular Loci of Hibi Toric Varieties* (arXiv:0706.2686), gives general singular-orbit methods. The present theorem does not claim to determine the singular-component decomposition or generic transverse Segre and node germs; it instead determines every orbit's *local Weil-divisor class group*, proves absence of local torsion at all points, and identifies the locally \(\mathbb Q\)-factorial locus from explicit rank formulas. General toric exact sequences alone do not present this closed stratification without the active-graph calculation.

## Limitations
The formulas classify local divisor groups, not the complete local analytic equations at the nongeneric orbit intersections, and they do not determine intersection multiplicities or a minimal resolution. A general class-group formula can in principle be specialized to this family, so a previously published equivalent specialization remains a residual originality risk. The computations test finite parameter pairs only; arbitrary parameters are covered by the symbolic proof. No independent mathematical review has been performed.

## References
1. T. Friedl, *Divisors on Projective Hibi Varieties*, arXiv:1506.02407 (first posted 2015-06-08), Theorem 8 and Lemma 12.
2. V. Lakshmibai and H. Mukherjee, *Singular Loci of Hibi Toric Varieties*, arXiv:0706.2686 (first posted 2007-06-18).
3. D. Cox, J. Little, H. Schenck, *Toric Varieties* (2011), Section 4.1, toric divisor-class exact sequence.
