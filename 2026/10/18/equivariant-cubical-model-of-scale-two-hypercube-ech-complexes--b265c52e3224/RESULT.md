# Equivariant cubical model of scale-two hypercube Čech complexes

## Finding

For every integer \(n\geq1\), let \(Q_n\) be the graph on \(\mathbb F_2^n\) with edges joining vectors at Hamming distance one. The scale-two **intrinsic graph Čech complex** \(X_n=\mathcal N(Q_n,2)\) has as facets the closed graph neighborhoods \(N[v]=\{v,v+e_1,\ldots,v+e_n\}\). The full graph automorphism group \(G_n=\mathbb F_2^n\rtimes S_n\) acts on \(X_n\) by affine coordinate symmetries.

Let \(C_n\) be the **closed cubical two-skeleton** of the ordinary \((n+1)\)-cube \([0,1]^{n+1}\): all its vertices, edges and square faces. Each \(g=(a,\pi)\in G_n\), acting on binary strings by \(x\mapsto a+\pi x\), acts on the vertices of \(C_n\) by
\[
 (x,t)\longmapsto\bigl(a+\pi x,\ t+\operatorname{par}(a)\bigr),
 \qquad \operatorname{par}(a)=\sum_i a_i\pmod2,
\]
and this extends to the geometric cube by the corresponding coordinate permutations and reflections. **There is a \(G_n\)-equivariant homotopy equivalence**
\[
\boxed{\quad \mathcal N(Q_n,2)\simeq_{G_n} C_n.\quad}
\]
More precisely, an explicitly constructed incidence-cone simplicial complex equivariantly deformation-retracts onto \(X_n\) and equivariantly simplicially collapses onto the standard triangulation of \(C_n\) that uses the diagonal between the two right-part vertices in each square.

The equivalence gives genuinely nonlinear fixed-point information. For every **nonzero pure translation** \(a\in\mathbb F_2^n\), the fixed-point space of its action on \(X_n\) has homotopy type
\[
\boxed{
 X_n^{\langle a\rangle}\simeq
 \begin{cases}
   \displaystyle\coprod_{j=1}^{2^{n-1}}\mathrm{pt},&\operatorname{wt}(a)\in\{1,2\},\\
   \varnothing,&\operatorname{wt}(a)\geq3.
 \end{cases}}
\]
Here fixed points mean points of the **geometric realization**, not merely fixed vertices. For another consequence involving coordinate permutations, let \(n\ge3\) and let \(\rho\in S_n\) be a three-cycle acting on three coordinates and fixing the remaining coordinates. Its geometric fixed-point space has the **two-component classification**
\[
\boxed{\quad X_n^{\langle\rho\rangle}\simeq
 (I^{n-2})^{(2)}\;\sqcup\;(I^{n-2})^{(2)},\quad}
\]
where \((I^d)^{(2)}\) is the complete two-skeleton of the \(d\)-cube. In particular, for \(n=5\), this fixed-point space has homotopy type \(S^2\sqcup S^2\); more generally for \(n\ge5\) each of the two components is a wedge of \(2^{n-5}(n^2-9n+22)-1\) two-spheres. This is not a claim of an equivariant sphere-wedge splitting of \(X_n\).

## Assumptions and scope

The graph has unit-length edges and its geometric realization carries the shortest-path metric. Čech scale two means closed metric balls of radius one centered at graph vertices, **not** Euclidean balls centered at hypercube corners. Lemma 2.2 of Adams–Shukla–Singh gives the indicated closed-neighborhood description. All statements concern every integer \(n\geq1\), the entire affine graph-automorphism group, and geometric group actions on finite CW spaces. Every sum in a binary-coordinate action is modulo two. The cubical two-skeleton is the union of cells of dimension at most two, not the two-skeleton of the abstract simplex on all hypercube vertices.

## Proof

**1. An equivariant incidence-cone intermediary.** Use two disjoint copies of \(\mathbb F_2^n\), with vertices \(r_w\) (right) and \(c_v\) (centers). Define
\[
Y_n=\bigcup_{v\in\mathbb F_2^n}\left(c_v*\Delta(N[v])\right),
\]
where \(\Delta(N[v])\) is the full simplex on the right vertices \(r_w\), \(w\in N[v]\), and different center cones intersect only in right-vertex faces. Their union of right faces is precisely \(X_n\). Send \(c_v\) to the barycenter of \(\Delta(N[v])\), fix every \(r_w\), and extend affinely over each cone. The straight-line homotopy from the identity is contained in that cone, glues along right faces, and is equivariant under the permutation of centers and right vertices. Thus \(Y_n\) has a \(G_n\)-equivariant strong deformation retraction onto \(X_n\).

**2. Canonical equivariant elementary collapses.** If \(u\ne v\), elementary Hamming geometry gives
\[
|N[u]\cap N[v]|=
\begin{cases}2,&d(u,v)\in\{1,2\},\\0,&d(u,v)\geq3.
\end{cases}
\]
(In the second case \(d(u,v)=2\), the intersection consists of the two intermediate cube vertices.) Hence a right-only simplex on at least three vertices belongs to exactly one generating neighborhood. For each such simplex \(\sigma\subset N[v]\), pair its right-only face \(\sigma\) with \(\sigma\cup\{c_v\}\). Delete the pairs in descending order of \(|\sigma|\). When a pair is removed, its smaller face has no other surviving coface, because all higher-cardinality right extensions have already been deleted. All pairs of the same cardinality can be deleted as a \(G_n\)-stable collection: the unique center of \(\sigma\) is preserved by its stabilizer, and distinct pairs do not interfere. This produces a \(G_n\)-equivariant collapse to a two-dimensional simplicial complex \(Z_n\).

The vertices of \(Z_n\) are the \(c_v,r_w\). Its edges are \(\{c_v,r_w\}\) for \(d(v,w)\leq1\), and \(\{r_w,r_z\}\) when \(w\ne z\) occur together in some \(N[v]\). Its triangles are exactly \(\{c_v,r_w,r_z\}\) for distinct \(w,z\in N[v]\); there are no faces of higher dimension. This describes the entire surviving complex.

**3. Identify the complete extra-dimensional cubical skeleton.** Write \(p(v)=\sum_i v_i\pmod2\). Map the vertices of \(Z_n\) into \(\mathbb F_2^{n+1}\) by
\[
 c_v\longmapsto(v,p(v)),\qquad
 r_w\longmapsto(w,1+p(w)).
\]
These are precisely the even- and odd-parity vertices, respectively, of the \((n+1)\)-cube. A left-right incidence edge is mapped to an actual cube edge: if \(v=w\), only the last coordinate changes; if \(d(v,w)=1\), just that original coordinate changes. All edges of the \((n+1)\)-cube arise uniquely in this fashion.

For any right vertices \(r_w,r_z\) spanning an edge of \(Z_n\), either \(d(w,z)=1\) or \(d(w,z)=2\). In either case they have exactly **two** common center neighbors. The four vertices, two right and two center, therefore form one and only one elementary square in the \((n+1)\)-cube, with the right-right edge as its diagonal. The two incident triangles of \(Z_n\) are exactly the two triangles obtained by cutting that square along this diagonal. Conversely every elementary square of the \((n+1)\)-cube has two right and two center corners, so arises in this fashion. Hence \(Z_n\) is *simplicially isomorphic* to the specified triangulation of \(C_n\).

For \(g=(a,\pi)\), the Hamming parity identity \(p(a+\pi v)=p(v)+p(a)\) shows that both vertex formulas intertwine the original \(G_n\)-action with the lifted cubical action. The deformation retraction, collapse, and final triangulation are therefore genuinely \(G_n\)-equivariant. This proves the boxed equivalence.

**4. Fixed points under translations.** For a nonzero translation \(a\), its lifted action on \([0,1]^{n+1}\) reflects precisely \(h=\operatorname{wt}(a)+\operatorname{par}(a)\) coordinate axes. This number equals two exactly for weights one and two; for weights at least three, it is at least four. A geometric fixed point has all reflected coordinates equal to \(1/2\). Inside the cubical two-skeleton, a point can have **at most two** coordinates strictly between zero and one. If \(h\geq4\), there are no fixed points. If \(h=2\), both reflected coordinates must equal \(1/2\) and every other coordinate must be zero or one. Thus the fixed set is precisely \(2^{(n+1)-2}=2^{n-1}\) isolated square centers. For the coordinate three-cycle \(\rho\), a point of the geometric cubical skeleton is fixed exactly when its three cycled coordinates share one common value. If that value were in \((0,1)\), the point would have at least three interior coordinates, contrary to membership in a two-skeleton. Thus these three coordinates must all equal zero or all equal one. In either case the remaining \(n-2\) coordinates range over a complete cubical two-skeleton, and the two options form disjoint components. For \(n=5\), the remaining cube is three-dimensional, whose two-skeleton is the boundary \(S^2\). For larger \(n\), the standard cellular counts of zero-, one-, and two-cells and simple connectivity give each sphere-wedge multiplicity displayed above. Equivariant homotopy equivalences restrict to homotopy equivalences on geometric fixed-point subspaces, completing the proof.

## Verification

The standalone Python 3 program `verify.py` uses only the standard library and rebuilds the Čech complex directly from closed neighborhoods, with distinct center vertices. It verifies every elementary free-face pair and the exact residual face set, independently reconstructs every square of the higher-dimensional cube and its two triangles, and checks the equivariance of the vertex identification. All graph automorphisms are checked for \(n=1,2,3,4\), with a deterministic sample for \(n=5\). A separate orbit-barycenter triangulation directly computes the three-cycle fixed-point complexes for \(n=3,4,5\); their mod-two Betti vectors have two components and respectively zero, zero, and two two-dimensional generators, matching the claimed lower-cube models. The resulting **492** affine-automorphism checks also compare direct signed simplicial Lefschetz traces with independently computed signed cubical chain traces, serving as a separate compatibility diagnostic. The test output ends in `VERIFY_OK total_automorphism_cases=492`.

For dimensions \(n=1,2,3,4,5\), the exact numbers of collapsed face pairs are respectively \(0,4,40,256,1344\), and the reconstructed square counts are \(1,6,24,80,240\), matching \(2^{n-1}\binom{n+1}{2}\). The same tests give degree-two Betti ranks \(0,1,7,31,111\). Separate orbit-complex computations for a coordinate three-cycle give mod-two Betti vectors \((2,0)\), \((2,0,0)\), and \((2,0,2,0)\) at \(n=3,4,5\), respectively, in agreement with the two lower-cube components. Finite tests are *not* used to infer the all-dimensional result; the free-face argument and explicit geometric identification prove it for every \(n\).

## Relationship to prior work

Adams, Shukla and Singh [1] define the finite vertex-centered intrinsic graph Čech nerve, prove its closed-neighborhood description (Lemma 2.2), and determine the **nonequivariant** sphere-wedge homotopy type of \(\mathcal N(Q_n,2)\) (Theorem 4.1). The known degree-two Betti rank is \(2^{n-2}(n^2-3n+4)-1\) for \(n\geq2\). This rank and the nonequivariant sphere wedge are not new claims here.

Previous results have also determined the rational translation character and the full affine-automorphism character on degree-two homology, as well as a general **nonequivariant** square-completion decomposition of neighborhood Čech complexes of triangle-free graphs. The present theorem does **not** reclaim those results: a homology representation and a nonequivariant splitting do not specify the fixed-point homotopy types of the entire action. The prior translation-character argument in particular counts translation-invariant edges, from which the translation fixed-point corollary above can already be derived. Its inclusion here is a consistency check, **not** a separate originality assertion. The contribution is the explicit, coherent \(G_n\)-equivariant identification with the higher-dimensional cubical two-skeleton; it determines fixed-point spaces of coordinate permutations and larger subgroups, including the two sphere components for a three-cycle when \(n=5\).

Matsushita [2] develops general equivalences and structural results for closed-neighborhood complexes, but its inspected statements do not supply this specific all-dimensional equivariant cubical model. Standard Vietoris–Rips results for hypercubes concern a different nerve and do not cover this model. We have not claimed a bibliographically exhaustive absence of equivalent formulations.

## Limitations

The result is specific to the finite graph Čech scale \(2\) and hypercube graphs. It yields an equivariant homotopy equivalence, not an equivariant **homeomorphism of the original simplicial complex**, not a canonical equivariant wedge decomposition, and not an explicit closed formula for arbitrary subgroup fixed-point spaces beyond the cubical model. It makes no statement at other Čech scales. The direct finite checks cover \(n\leq5\); the general proof uses exact combinatorial arguments rather than extrapolation. It does not provide independent external validation or establish literature-wide uniqueness, and an unindexed equivalent cubical description remains a residual bibliographic risk.

## References

[1] Henry Adams, Samir Shukla, Anurag Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871, first public 2022-12-12, especially Lemma 2.2, Lemma 3.1 and Theorem 4.1; https://arxiv.org/pdf/2212.05871.

[2] Takahiro Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608; https://arxiv.org/pdf/2511.12608.
