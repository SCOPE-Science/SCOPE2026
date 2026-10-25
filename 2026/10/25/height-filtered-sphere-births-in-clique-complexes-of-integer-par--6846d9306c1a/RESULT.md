# Height-filtered sphere births in clique complexes of integer partitions

## Finding

Let \(n\geq1\). The vertices of the partition-transfer graph \(G_n\) are the integer partitions \(\lambda\vdash n\), and two distinct vertices are adjacent when one is obtained from the other by transferring one unit between two (possibly newly created) parts and sorting. Let \(K_n=\operatorname{Cl}(G_n)\). For a partition \(\lambda=(\lambda_1,\ldots,\lambda_\ell)\), define its integer height and distinct-part support by
\[
h(\lambda)=\sum_{i=1}^{\ell}i\lambda_i,\qquad S(\lambda)=\{\lambda_1,\ldots,\lambda_\ell\},\qquad M(\lambda)=\max S(\lambda).
\]
For each integer \(t\), let \(F_t\subseteq K_n\) be the induced simplicial complex on partitions of height at least \(t\). The first nonempty stage is the single vertex \((1^n)\).

**Sphere-birth theorem.** At every subsequent height level, \(F_t\) is obtained from \(F_{t+1}\) by attaching cones on connected simplicial complexes homotopy equivalent to explicit bipartite graphs. Every attaching map is null-homotopic, and there is a homotopy equivalence compatible with the previous stage up to homotopy:
\[
F_t\simeq F_{t+1}\vee\bigvee_{\substack{\lambda\vdash n\\h(\lambda)=t}}\ \bigvee^{w(\lambda)}S^2,
\quad
w(\lambda)=\#\{(b,a)\in S(\lambda)^2:b+2\leq a<M(\lambda)\}.
\]
If the height level is empty, the added wedge is empty. There is also a **canonical integral filtration**: inclusion induces an injection on \(H_2(-;\mathbb Z)\), and the quotient at level \(t\) is naturally the direct sum of the cycle lattices \(H_1(B_\lambda;\mathbb Z)\) of the graphs defined below. These lattices are free, with respective ranks \(w(\lambda)\); the short exact sequences split as abelian groups, but not canonically.

In particular, the number of two-spheres in the final wedge admits a positive partition-theoretic interpretation:
\[
\operatorname{rank}\widetilde H_2(K_n;\mathbb Z)
=\sum_{\lambda\vdash n}w(\lambda).
\]
This counts quadruples consisting of a partition \(\lambda\) and two of its distinct part sizes \(b,a\), such that \(b+2\leq a<M(\lambda)\). Equivalently, with \((q;q)_M=\prod_{j=1}^M(1-q^j)\), the ranks have the positive formal-power-series expansion
\[
\sum_{n\geq1}\operatorname{rank}\widetilde H_2(K_n;\mathbb Z)q^n
=\sum_{M\geq4}\frac{q^M}{(q;q)_M}
\sum_{a=3}^{M-1}\sum_{b=1}^{a-2}q^{a+b}.
\]
The genuinely additional topological information is the *height-by-height location and survival of primitive integral homology classes*. The numerical Euler-characteristic series alone is not asserted as independently novel.

## Assumptions and scope

Partitions have positive integer parts in weakly decreasing order, with repetitions allowed. An admissible transfer must produce a distinct partition; the recipient is permitted to be a new part of size \(1\). Simplicial complexes and homology are ordinary, unreduced unless indicated, with coefficients \(\mathbb Z\); the empty wedge is a point. All assertions apply to every integer \(n\geq1\), not just the finitely checked cases. No equivariance under conjugation of partitions is asserted; the height filtration need not be invariant under that involution.

For \(\lambda\neq(1^n)\), define the bipartite graph \(B_\lambda\) with left vertices \(D_\lambda=\{a\in S(\lambda):a\geq2\}\), right vertices the *active* members of \(S(\lambda)\cup\{0\}\), and an edge from the donor part size \(a\) to the recipient part size \(b\) precisely when \(a\geq b+2\). The donor and recipient copies are disjoint even when they carry the same numerical label. The right vertex \(b\) is retained only when it is incident with an edge. Thus \(B_\lambda\) has no isolated vertices; its right vertex \(0\) is adjacent to every donor, and its maximum donor \(M(\lambda)\) is adjacent to every active recipient. Consequently \(B_\lambda\) is connected. For \(\lambda=(1^n)\) use the empty graph.

## Proof

**1. Heights and upper neighbors.** Each removable corner of the Ferrers diagram is indexed by a distinct part size \(a\), and each addable corner by a distinct existing part size \(b\) or the new-row choice \(b=0\). If the removable corner is in row \(r\) and the addable corner in row \(s\), elementary bookkeeping gives the height change \(h(\mu)-h(\lambda)=s-r\). This quantity is nonzero for every genuine transfer. A transfer raises height precisely when \(b<a\); if \(a=b+1\), the two modified part sizes are exchanged, so the result is unchanged and the transfer is inadmissible. Thus the strict upper neighbors of \(\lambda\) are in bijection with the edges \((a,b)\) of \(B_\lambda\). Their images are distinct: in conjugate partition coordinates a transfer changes exactly the entries indexed by \(a\) and \(b+1\), with different indices because \(a\geq b+2\). In particular, no edge of \(G_n\) joins partitions of equal height.

For \(\lambda\neq(1^n)\), the edge \((M(\lambda),0)\) always exists and raises height. Repeating such height-raising moves increases the number of parts until it reaches \((1^n)\). Hence \((1^n)\) is the unique maximum-height vertex, and descending height gives a well-defined filtration starting at a point.

**2. Upper-link classification.** Let \(L_\lambda\) be the full simplicial link of \(\lambda\) in the stage when it is added, i.e. the clique complex on its strictly higher neighbors. For two such neighbors, the elementary transfer difference in conjugate partition coordinates has the form
\[
(e_a-e_{b+1})-(e_c-e_{d+1}).
\]
It is a single admissible transfer difference precisely when the two donor sizes agree or the two recipient sizes agree (the star/top triangle criterion). Therefore the graph on strict upper neighbors is the line graph of \(B_\lambda\), and
\[
L_\lambda=\operatorname{Cl}(\operatorname{Line}(B_\lambda)).
\]
For each vertex \(v\) of \(B_\lambda\), its incident edges form a simplex in this line-graph clique complex. These simplices cover the complex: any pairwise-intersecting set of edges in a bipartite graph shares one endpoint. Every nonempty intersection of these covering simplices is a simplex, while the nerve of their cover is \(B_\lambda\) itself. The nerve lemma yields \(L_\lambda\simeq B_\lambda\). In particular, \(L_\lambda\) is connected and homotopy equivalent to a wedge of \(\beta_1(B_\lambda)\) circles.

**3. Null attachments and filtration.** Consider the level \(t\) with all vertices of height \(t\) added to \(F_{t+1}\). Since two distinct same-height vertices are never adjacent, their new stars are cones on the respective \(L_\lambda\), with pairwise intersections contained in \(F_{t+1}\). Suppose inductively that \(F_{t+1}\) is simply connected. Every attaching map \(L_\lambda\to F_{t+1}\) is null-homotopic because its source has the homotopy type of a connected graph and its target is simply connected. The homotopy-cofiber description of a cone attachment therefore gives, compatibly with the old subcomplex up to homotopy,
\[
F_t\simeq F_{t+1}\vee\bigvee_{h(\lambda)=t}\Sigma L_\lambda
\simeq F_{t+1}\vee\bigvee_{h(\lambda)=t}\bigvee^{\beta_1(B_\lambda)}S^2.
\]
The initial nonempty filtration stage is a point, so induction establishes simple connectivity of every nonempty stage and the wedge splitting at every subsequent step. The long exact sequence of each pair, or excision for all new cones at one level, gives
\[
0\longrightarrow H_2(F_{t+1};\mathbb Z)\longrightarrow H_2(F_t;\mathbb Z)
\longrightarrow \bigoplus_{h(\lambda)=t}H_1(B_\lambda;\mathbb Z)\longrightarrow0.
\]
The first map is injective because the relative third homology vanishes; the last map is onto because \(H_1(F_{t+1};\mathbb Z)=0\). The quotient identifies canonically via the pair boundary and the nerve homotopy equivalence. Each quotient is free, so each short exact sequence splits abstractly. No preferred null-homotopy, generator basis, or integral splitting is claimed.

**4. The cycle-rank formula.** Write \(S=S(\lambda)\), \(M=\max S\). Every donor \(a\geq2\) is attached to recipient \(0\). For each positive recipient \(b\in S\), let \(k_b=\#\{a\in S:a\geq b+2\}\). If \(k_b=0\), this recipient is absent; otherwise adding its vertex and \(k_b\) edges to the connected zero-recipient star creates exactly \(k_b-1\) independent cycles. Thus
\[
\beta_1(B_\lambda)=\sum_{b\in S\,:\,k_b\geq1}(k_b-1)
=\#\{(b,a)\in S^2:b+2\leq a<M\}=w(\lambda),
\]
since whenever \(k_b\geq1\), the maximum part size \(M\) is one of the \(k_b\) donors. This is an exact integral cycle-rank computation, not a numerical approximation.

**5. The partition generating function.** Fix positive integers \(1\leq b\leq a-2\) and \(a<M\). A partition counted with maximum part size \(M\) and containing part sizes \(M,a,b\) is obtained by taking one copy of each required size and then any partition with all parts at most \(M\). Its generating series is \(q^{M+a+b}/(q;q)_M\). Summing over all eligible triples counts each \(\lambda\) exactly \(w(\lambda)\) times and proves the stated formal identity. At the first nonzero case \(n=8\), the single responsible partition is \((4,3,1)\); its upper transfer graph is a four-cycle and creates one primitive two-sphere class.

## Verification

The complete standard-library checker `verify_partition_births.py` rebuilds the transfer graph from its definition, checks the upper-neighbor bijection, checks every pairwise upper-link adjacency against the line-graph rule, and checks the bipartite cycle rank. It verifies these claims for all \(4{,}507\) partitions with sizes \(1\) through \(22\). Independently it enumerates all cliques and their alternating Euler sum for every size in that range and compares with the local birth sum and the positive series. The first \(25\) coefficients also agree with the published table, and the series is expanded through \(n=60\). All tests passed. Execute `python3 verify_partition_births.py` from a directory containing the embedded checker. The checker uses only Python's standard library.

These finite checks do not prove the all-integer assertions. The infinite proof is the upper-link identification, graph-nerve equivalence, null-cofiber splitting and exact combinatorial cycle count above.

## Relationship to prior work

The original 2026 partition-transfer clique-complex paper [1] proved the nonequivariant two-sphere wedge form using a global good-cover/nerve and intersection-poset argument, and supplied the height function and star/top clique classification. The subsequent local-morphology paper [2] proved a line-graph description of the *full* neighborhood. Numerical-topology work [3] gave Euler, clique and nerve-counting frameworks. A later synthesis [4, Section 8.2, Open Problem 8.2] explicitly asked for a partition-theoretic interpretation of the bouquet rank and described the lack of a conceptual local allocation of homology.

The present finding instead uses a descending-height filtration whose **upper** links are connected line-graph complexes and proves that every stage adds an independently surviving integral two-sphere lattice. The support-pair count identifies where homology is born, not merely how many classes exist globally. An earlier exact complete face-vector generating series also determines the numerical Euler/bouquet series by alternating sum; hence the equality of numerical series is not claimed to be novel independently of the filtration and direct partition-support interpretation. The previously established global wedge type, local transfer dictionary, and general homotopy-cofiber lemma are used as known background rather than recast as new facts.

## Limitations

The splitting is a homotopy equivalence compatible with inclusion only up to homotopy and is generally **not canonical** as a wedge or as an integral direct-sum basis. The canonical statement is the filtration and its associated graded homology. No functoriality with respect to partition conjugation or graph automorphisms is asserted. The result concerns only these particular integer-partition transfer complexes, with no claim of an analogous theorem for arbitrary transfer graphs. Independent validation has not been performed. The published literature and indexed semantic searches cannot exclude unindexed equivalent treatments of the specific upper-link filtration.

## References

[1] F. B. Lyudogovskiy, *The homotopy type of the clique complex of the partition graph*, arXiv:2603.14370v1, publicly submitted 2026-03-15, https://arxiv.org/abs/2603.14370.

[2] F. B. Lyudogovskiy, *Local Morphology of the Partition Graph*, arXiv:2603.18696v1, publicly submitted 2026-03-19, https://arxiv.org/abs/2603.18696.

[3] F. B. Lyudogovskiy, *Numerical topology of the clique complex of the partition graph: Euler characteristic, clique counts, and sequence data*, arXiv:2603.26656v1, publicly submitted 2026-03-27, https://arxiv.org/abs/2603.26656.

[4] F. B. Lyudogovskiy, *Local Complexity, Overlap Control, and Global Simplicity in Partition Graphs*, arXiv:2606.20773v1, publicly submitted 2026-06-18, https://arxiv.org/abs/2606.20773.

[5] D. Kozlov, *Combinatorial Algebraic Topology*, Springer, 2008 (standard nerve and simplicial homotopy tools).
