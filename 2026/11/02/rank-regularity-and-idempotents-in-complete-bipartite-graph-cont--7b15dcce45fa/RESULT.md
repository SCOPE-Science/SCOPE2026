# Rank, regularity, and idempotents in complete-bipartite graph-continuous monoids

## Finding

**Theorem (complete bipartite case).** Let \(m,n\ge 2\). Write \(G=K_{m,n}\) for the simple graph whose disjoint vertex parts \(U,V\) have cardinalities \(m,n\). A partial transformation \(f:G\rightharpoonup G\) belongs to \(\operatorname{MR}(G)\) precisely when the inverse image of each vertex or edge (considered as a vertex subset) is empty, a singleton, or an edge. Let \(\operatorname{rank}(f)=|\operatorname{im}(f)|\). Then the complete rank distributions of elements, regular elements, and idempotents are the following exact integer formulas.

Define \((a)_b=a(a-1)\cdots(a-b+1)\) for \(0\le b\le a\), and \((a)_b=0\) otherwise; also set \((a)_0=1\). Put
\[
J(a,k)=\sum_{j=0}^{\min(a,k)}\binom aj(k)_j,
\qquad
F_{m,n}(k)=\sum_{j=0}^{k}(-1)^{k-j}\binom kjJ(m,j)J(n,j).
\]
For each \(1\le k\le m+n\) set
\[
\begin{aligned}
P_k&=\left(\binom mk+\binom nk\right)F_{m,n}(k),\\
R_k&=\left(\binom mk+\binom nk\right)
\left[(m)_kJ(n,k)+(n)_kJ(m,k)-(m)_k(n)_k\right],\\
M_k&=\sum_{j=1}^{k-1}\binom mj\binom n{k-j}
\left[(m)_j(n)_{k-j}+(n)_j(m)_{k-j}\right],\\
E_k&=\binom mk J(n,k)+\binom nk J(m,k)
+\sum_{j=1}^{k-1}\binom mj\binom n{k-j}.
\end{aligned}
\]
Here binomial coefficients are zero outside their ordinary ranges. For \(k\ge1\), the respective rank-\(k\) counts are
\[
\boxed{\#\operatorname{MR}_k(G)=P_k+M_k,\quad
\#\operatorname{Reg}_k(G)=R_k+M_k,\quad
\#\operatorname{Idem}_k(G)=E_k.}
\]
At rank zero, all three counts equal one (the empty map). Consequently, the full nonregular rank polynomial is
\[
\boxed{\mathcal N_{m,n}(t)=\sum_{k=2}^{m+n}(P_k-R_k)t^k.}
\]
Every mixed-image element (one whose image meets both vertex parts) is regular. An element whose image is contained in one vertex part is regular **if and only if** one of the two source-part restrictions maps onto the whole image. In particular, the number of nonregular elements of rank two is exactly
\[
\boxed{2mn\left(\binom m2+\binom n2\right).}
\]
The total idempotent count simplifies to
\[
\boxed{\#\operatorname{Idem}(\operatorname{MR}(K_{m,n}))
=1+\sum_{k=1}^{m}\binom mkJ(n,k)+\sum_{k=1}^{n}\binom nkJ(m,k)
+(2^m-1)(2^n-1).}
\]
No unstated genericity, parity, primality, or asymptotic assumption on \(m,n\) is required.

## Assumptions and scope

A partial transformation is specified by its domain, which may be empty, and a function from that domain into the full graph vertex set. Composition is the usual composition of partial functions. An edge is the two-element set joining one vertex of \(U\) to one vertex of \(V\). A singleton is also a simplex. A regular element is one admitting \(g\in\operatorname{MR}(G)\) with \(fgf=f\). Idempotent means \(f^2=f\). The theorem addresses the **full** continuous-map monoid rather than the smaller monoid of *strictly continuous* maps. The restriction \(m,n\ge2\) excludes the star boundary.

In the displayed formulas the symbol \(P_k\) counts maps with a nonempty image entirely within one part, \(R_k\) counts the regular maps among these, and \(M_k\) counts maps whose images meet both parts. Thus no map occurs in more than one summand. The \(E_k\) formula directly counts idempotents and does not denote a fourth disjoint stratum.

## Proof

**1. Classification by image type.** Fix \(f\in\operatorname{MR}(G)\). Every nonempty fiber of \(f\) is a vertex or an edge, hence meets each source part in at most one vertex. If \(\operatorname{im}f\subseteq U\) (or \(\subseteq V\)), this fiber restriction is also sufficient for continuity: the inverse image of a target edge meets the image in at most one target vertex and is therefore just a permitted fiber. Equivalently, both restrictions \(f|_U\) and \(f|_V\) are partial injections into the same target part, and their image sets may overlap.

If the image meets both target parts, every two fibers at opposite ends of a target edge together have at most two elements. Both fibers are nonempty, so each is a singleton. Thus \(f\) is injective. Moreover, source vertices mapping into opposite target parts must be adjacent, hence belong to opposite source parts. Since **every** target vertex on one side is adjacent to **every** target vertex on the other side, all source vertices mapping to one target part lie in a single common source part, opposite to the source part used by the other target part. Conversely, an injective map preserving or swapping the bipartition in this sense has vertex and edge inverse images that are vertices, edges, or empty. This proves both necessity and sufficiency of the two types.

**2. Counting pure-image maps.** Fix a \(k\)-element target set \(S\) contained in one target part. For an \(a\)-element source part, the number of arbitrary partial injections into a prescribed \(j\)-element set is \(J(a,j)\): choose the domain size \(h\) and then inject its \(h\) elements into the target set, giving \(\binom ah(j)_h\). The two source-part restrictions are independently chosen. To require their joint image to be *exactly* \(S\), apply inclusion-exclusion to the target vertices not covered by either restriction. This gives \(F_{m,n}(k)\). The number of choices for \(S\) is \(\binom mk+\binom nk\), yielding \(P_k\).

**3. Counting mixed-image maps.** Suppose \(j\) image vertices lie in target part \(U\) and \(k-j\) in target part \(V\), with \(1\le j\le k-1\). Choose both image subsets in \(\binom mj\binom n{k-j}\) ways. In the bipartition-preserving case choose injective preimages independently in \((m)_j(n)_{k-j}\) ways; in the swapping case the count is \((n)_j(m)_{k-j}\). Since both parts of the image are nonempty, the two cases are disjoint. Summing gives \(M_k\).

**4. A regularity lemma.** A continuous partial transformation \(f\) is regular if and only if it has a continuous partial section \(s:\operatorname{im}f\to\operatorname{dom}f\) satisfying \(f(s(y))=y\) for every \(y\) in its image. Indeed, if \(fgf=f\), then the restriction of \(g\) to the image of \(f\) is such a section; restrictions of continuous partial functions remain continuous because taking a subset of a simplex again gives a simplex or the empty set. Conversely a continuous section extended by being undefined elsewhere witnesses \(fsf=f\).

For a mixed-image map, the ordinary inverse injection (defined on the image) is a continuous section: both it and \(f\) preserve or swap the bipartition. Hence all \(M_k\) maps are regular. For a pure-image map with image \(S\) in one target part, a section \(s\) is defined on a set of pairwise nonadjacent vertices. If its image used vertices of both source parts, a source edge between the two chosen section values would have as its inverse image two different nonadjacent vertices of \(S\), contrary to continuity. Thus a section has image in a *single* source part. Conversely an injective section whose image lies entirely in one source part is continuous because no edge in the target graph can have two distinct preimages. A section therefore exists precisely when the restriction of \(f\) to one source part maps onto all of \(S\).

For fixed \(S\), the number of pure-image maps whose \(U\)-restriction covers \(S\) is \((m)_kJ(n,k)\): select a bijection from \(k\) selected vertices of \(U\) onto \(S\), then an arbitrary partial injection from \(V\) into \(S\). Analogously the number covered by the \(V\)-restriction is \((n)_kJ(m,k)\). Their intersection is counted twice and equals \((m)_k(n)_k\). Inclusion-exclusion and the number of choices of \(S\) give \(R_k\). All uncounted pure-image maps are nonregular.

**5. Idempotents.** For an arbitrary partial transformation, \(f^2=f\) means that every vertex of the image lies in the domain and is fixed. If the image \(S\) lies in \(U\), the restriction to \(U\) must be the identity on \(S\), undefined on all other vertices of \(U\), because a second vertex from \(U\) in any fiber is prohibited. The restriction from source part \(V\) is any partial injection into \(S\), in \(J(n,k)\) ways. There are \(\binom mk\) possible sets \(S\); swap \(U,V\) for the other summand. If the image meets both parts, the map is injective by Step 1; idempotence then forces it to be the partial identity on its domain, with nonempty chosen subsets in both parts. This yields \(\sum_{j=1}^{k-1}\binom mj\binom n{k-j}\) rank-\(k\) maps. Adding the unique empty map proves \(E_k\) and the stated total, using the binomial identity for mixed subsets.

**6. Rank-two nonregularity.** For image \(S\) with two vertices in a single target part, a nonregular map must have one image vertex covered only from source \(U\) and the other only from source \(V\); these are the only two ways for their image union to be \(S\) without either source-part restriction being onto. The source preimages can be selected in \(mn\) ways, giving \(2mn\) maps per fixed target two-set. Summing over \(\binom m2+\binom n2\) choices yields the displayed exact formula.

These steps jointly establish the complete theorem for every \(m,n\ge2\).

## Verification

The standalone `verify.py` independently generates every partial function on \(m+n\) labeled vertices, filters them by the original simplex-inverse-image condition (without using the image-type classification), and computes regularity by enumerating **all possible sections** and directly checking their continuity. It separately tests idempotence through the defining equation \(f^2=f\). It then compares every rank coefficient with the symbolic formulas.

The exhaustive tests cover \((m,n)=(2,2),(2,3),(3,2),(3,3)\), all within the theorem's new domain. For \((2,2)\), the total/regular/idempotent counts are \((169,153,36)\); for \((2,3)\), \((874,700,86)\); and for \((3,3)\), \((4489,3733,220)\). All per-rank coefficients agree, and the verifier prints `VERIFY_OK`. The general proof is combinatorial, not an inference from these finite checks.

## Relationship to prior work

Margolis and Rhodes (2021) define continuous partial maps by inverse images of simplices and, in Example 2.11, enumerate the **strictly continuous** maps on the balanced complete bipartite graph \(K_{r,r}\). Their count for nonempty singular strict maps of rank \(k\) is \(2\binom rk^3(k!)^2\). The present proof recovers that value: such maps have \(k\) doubleton edge-fibers and a pure-part image, giving \(2\binom rk(r)_k^2\), which equals the published expression. The strict submonoid is smaller than the full monoid treated here; the new regular/nonregular criterion, full rank counts, and full idempotent counts are not consequences of the strict-map enumeration alone.

Margolis and Rhodes' 2026 preprint investigates the full graph-continuous monoid and advertises explicit combinatorial enumerations for paths and cycles. Its accessible abstract does not mention a complete-bipartite classification. The complete text of that preprint was not accessible in this review, so comparison with uninspected portions remains a concrete priority risk; absence from its abstract is **not** used as proof of novelty. The present scope deliberately requires both parts to contain at least two vertices; no result about the star boundary is claimed.

## Limitations

The theorem determines element, regularity, nonregularity, and idempotent distributions but not every Green relation, generating set, or Krohn–Rhodes complexity of these monoids. The formulas concern the full continuous monoid, not the strict submonoid. The independent enumeration stops at six graph vertices; the unlimited range of \(m,n\) is proved symbolically. The 2026 preprint was checked at abstract level only, with full-text noncoverage unresolved. Independent external mathematical review has not occurred.

## References

1. S. Margolis and J. Rhodes, *Degree 2 transformation semigroups as continuous maps on graphs: Foundations and structure*, International Journal of Algebra and Computation 31 (2021), 1065–1091. DOI: 10.1142/S0218196721400051. Relevant portions: definition in Section 2, Example 2.11 (strict continuous maps on \(K_{r,r}\)). Author-posted readable text: https://www.researchgate.net/publication/352153447_Degree_2_transformation_semigroups_as_continuous_maps_on_graphs_Foundations_and_structure.
2. S. Margolis and J. Rhodes, *The Margolis–Rhodes Monoid of a Graph*, arXiv:2609.39370, first submitted 2026-09-30. https://arxiv.org/abs/2609.39370. Accessible abstract only in the present comparison.
