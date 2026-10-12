# Paired-domination resilience and matching counts under bipartite matching deletion

## Finding

Let \(m,n\ge2\) and \(0\le t\le\min\{m,n\}\). Delete the edges of any \(t\)-edge matching \(M_t\) from the complete bipartite graph \(K_{m,n}\), and write
\[
G=K_{m,n}-M_t.
\]
Let \(A\) and \(B\) denote its two independent sides. The paired-dominating sets of \(G\) have the exact following description:

* Every vertex set \(D\) with \(|D\cap A|=|D\cap B|=s\ge2\) is paired-dominating, regardless of which vertices it selects and of the deleted matching.
* A two-vertex set \(D=\{a,b\}\), with \(a\in A\) and \(b\in B\), is paired-dominating precisely when neither selected vertex belongs to the deleted matching \(M_t\).
* No other vertex set is paired-dominating.

Define the paired-domination polynomial by
\[
P_{\mathrm{pr}}(G;x)=\sum_{D\text{ paired-dominating}}x^{|D|}.
\]
Then
\[
\boxed{P_{\mathrm{pr}}(K_{m,n}-M_t;x)
=(m-t)(n-t)x^2+
\sum_{s=2}^{\min\{m,n\}}\binom ms\binom ns x^{2s}.}
\]
In particular, **deleting an arbitrary matching affects only the degree-two coefficient** of the paired-domination polynomial. The number of paired-dominating sets is
\[
\boxed{P_{\mathrm{pr}}(G;1)=\binom{m+n}{m}-1-t(m+n-t).}
\]
The minimum paired-domination number is
\[
\boxed{\gamma_{\mathrm{pr}}(G)=
\begin{cases}
2,&t<m\text{ and }t<n,\\
4,&t=m\text{ or }t=n.
\end{cases}}
\]
When the minimum is \(2\), it is attained by exactly \((m-t)(n-t)\) vertex sets. When the minimum is \(4\), it is attained by exactly \(\binom m2\binom n2\) sets.

The vertex-set polynomial hides a second kind of robustness. The number of distinct perfect matchings that can pair a selected paired-dominating set generally decreases after edge deletion even when the set itself remains feasible. Define the **pairing-weighted enumerator**
\[
Q_{\mathrm{pr}}(G;x)=
\sum_{D\text{ paired-dominating}}
\operatorname{pm}(G[D])\,x^{|D|},
\]
where \(\operatorname{pm}(H)\) is the number of perfect matchings of \(H\). Then
\[
\boxed{
Q_{\mathrm{pr}}(G;x)
=(m-t)(n-t)x^2+
\sum_{s=2}^{\min\{m,n\}}x^{2s}
\sum_{j=0}^{\min\{t,s\}}(-1)^j
\binom tj\binom{m-j}{s-j}
\binom{n-j}{s-j}(s-j)!.
}
\]
Thus set feasibility survives all disjoint edge faults beyond size two, whereas the exact multiplicity of compatible backup pairings obeys a rook-polynomial inclusion-exclusion law.

## Assumptions and scope

All graphs are finite, simple, and undirected. A vertex set \(D\) dominates \(G\) when every vertex outside \(D\) has a neighbor in \(D\). It is *paired-dominating* when, in addition, \(G[D]\) has a perfect matching. A perfect matching is not required to be induced.

The two sides of \(K_{m,n}\) have sizes \(m\) and \(n\), both at least two. The removed edges form a matching, so no vertex loses more than one neighbor. The boundary \(t=0\) gives the original complete bipartite graph, and \(t=m=n\) gives a crown graph. The theorem does not impose connectivity, so it also covers the legitimate boundary \(K_{2,2}-M_2\), which is a disjoint union of two edges.

## Proof

Write \(D_A=D\cap A\) and \(D_B=D\cap B\). If \(G[D]\) has a perfect matching, every matching edge joins the two bipartition classes. Hence there is an integer \(s\ge1\) with
\[
|D_A|=|D_B|=s.
\]
Conversely, suppose \(s\ge2\). Every vertex of \(G\) is incident with at most one deleted edge. Therefore each vertex outside \(D\) has at least \(s-1\ge1\) neighbors among the selected vertices of the opposite side. Thus \(D\) dominates \(G\).

Next, the induced bipartite graph \(G[D]\) is obtained from \(K_{s,s}\) by deleting a matching of at most \(s\) edges. It always has a perfect matching when \(s\ge2\). Indeed, for any one selected vertex its neighborhood has at least \(s-1\ge1\) vertices. For a subset \(X\) containing at least two vertices on the same side, every vertex on the opposite side is adjacent to at least one vertex of \(X\), since at most one edge incident to that opposite vertex was removed. Thus \(N(X)\) is the whole opposite side and
\[
|N(X)|=s\ge |X|.
\]
Hall's marriage theorem proves the required perfect matching. This proves that every balanced \(2s\)-set with \(s\ge2\) is paired-dominating.

Now let \(s=1\), with \(D=\{a,b\}\), \(a\in A\), \(b\in B\). If \(a\) is incident with a removed edge \(ab'\), then \(b'\) has no selected neighbor on \(A\). If \(b'=b\), \(D\) is not even an edge and cannot contain a perfect matching. If \(b'\ne b\), the vertex \(b'\) is outside \(D\) and undominated. In either case \(D\) cannot be paired-dominating. The same argument applies when \(b\) is incident with a removed edge. Conversely, if neither is incident with a removed edge, \(ab\) is present and each selected vertex is adjacent to every vertex on the opposite side. Hence \(D\) dominates and its one edge is a perfect matching. This completes the structural characterization.

There are \(m-t\) vertices of \(A\) and \(n-t\) vertices of \(B\) not incident with the deletion matching. They give exactly \((m-t)(n-t)\) feasible two-vertex sets. For each \(s\ge2\), the \(s\) selected vertices on each side can be chosen independently, giving
\[
\binom ms\binom ns
\]
paired-dominating sets of cardinality \(2s\). This proves the first polynomial.

At \(x=1\), the Vandermonde identity
\[
\sum_{s=0}^{\min\{m,n\}}\binom ms\binom ns
=\binom{m+n}{m}
\]
gives
\[
P_{\mathrm{pr}}(G;1)
=\binom{m+n}{m}-1-mn+(m-t)(n-t)
=\binom{m+n}{m}-1-t(m+n-t).
\]
Since \(m,n\ge2\), the coefficient of \(x^4\) is positive; therefore the first nonzero coefficient is either that of \(x^2\) or that of \(x^4\), giving the minimum and minimum-set counts above.

For the pairing-weighted polynomial, fix \(s\ge2\). Each pair \((D,F)\), where \(D\) has \(s\) vertices on each side and \(F\) is a perfect matching of \(G[D]\), corresponds bijectively to an \(s\)-edge matching \(F\) of \(G\): its endpoint set is \(D\). Thus the coefficient of \(x^{2s}\) in \(Q_{\mathrm{pr}}(G;x)\) equals the number of \(s\)-edge matchings of the edge-deleted biclique.

Count all \(s\)-edge matchings of the original \(K_{m,n}\) while excluding the \(t\) forbidden matching edges. Inclusion-exclusion over these forbidden edges is particularly simple because they are pairwise disjoint. For a specified subset of \(j\) forbidden edges to be present, choose the remaining \(s-j\) endpoints on each side and match them bijectively. The count is
\[
\binom{m-j}{s-j}\binom{n-j}{s-j}(s-j)!.
\]
There are \(\binom tj\) ways to prescribe the \(j\) deleted edges. Inclusion-exclusion therefore yields
\[
\sum_{j=0}^{\min\{t,s\}}(-1)^j
\binom tj\binom{m-j}{s-j}
\binom{n-j}{s-j}(s-j)!
\]
valid matchings of size \(s\), for every \(s\ge2\). For \(s=1\), only the \((m-t)(n-t)\) surviving edges joining two untouched vertices have paired-dominating endpoint sets, and each contributes one matching. This proves the second polynomial.

## Verification

The standalone Python script `artifacts/verify.py` constructs every graph \(K_{m,n}-M_t\) with
\[
2\le m,n\le6,\qquad 0\le t\le\min\{m,n\}.
\]
For every vertex subset it directly tests domination against graph adjacency and determines the number of perfect matchings in the induced graph using recursive exact enumeration. Independently, it tests the structural characterization, the paired-domination polynomial coefficientwise, and the rook inclusion-exclusion formula for pairing counts.

The actual replay returned:

`ALL CHECKS PASSED; profiles=105; subsets_checked=86384; paired_set_matching_pairs_checked=125039; m,n=2..6; all matching deletions`

These finite checks corroborate the exact formulas but do not constitute a proof for arbitrary part sizes. The Hall and inclusion-exclusion arguments above cover every \(m,n,t\) in the stated domain.

## Relationship to prior work

Haynes and Slater introduced paired domination by requiring a dominating set to admit a perfect matching. Recent work of Henning and Ralaivaosaona (first public May 23, 2025, MSC \(05C69\)) gives a linear-time algorithm and limiting distribution for paired domination in trees, highlighting active interest in the matching constraint. Lu and Wu's September 2026 paper proves a sharp paired-domination bound for cubic bipartite graphs, rather than enumerating the effect of deleted matching edges.

The crown-graph endpoint \(t=m=n\) has an already known **scalar** paired-domination number \(4\); it is stated, for example, in work on independent-transversal paired domination, and an earlier paired-domination-energy paper explicitly takes a four-vertex minimum paired-dominating set on the crown graph. That scalar endpoint is not claimed here as new. The new theorem determines every paired-dominating vertex set simultaneously for all rectangular sizes and all matching-deletion counts, and additionally counts every compatible backup matching.

The already available paired-domination polynomial for complete multipartite graphs includes the undeleted biclique \(t=0\), but no nontrivial matching-deleted biclique is complete multipartite. A chain-graph paired-domination polynomial is also known; when at least two matching edges are deleted, the resulting graph contains an induced \(2K_2\) and is not a chain graph. Thus neither graph-family theorem implies the deletion-resilience statement or its rook inclusion-exclusion refinement.

A 2016 conference record introduces paired-domination polynomials and advertises formulas for unspecified standard families, but the accessible document is a one-page abstract and not a full list of graph classes. It cannot establish absence of a differently worded earlier result, and remains a documented originality risk. Targeted searches under “matching-deleted biclique,” “crown graph,” “almost complete bipartite,” paired-domination polynomial, and matching-count terminology did not reveal a covering all-\(t\) theorem.

## Limitations

The robustness is specific to **deleted matchings**: allowing two removed edges to share a vertex can destroy domination or Hall's condition even for selected sets of size at least four. No corresponding statement is claimed for general sparse faults.

The family includes disconnected graphs at a small boundary, but all its graphs in the stated domain are isolate-free. The theorem counts paired-dominating sets and separately counts their perfect matchings; it does not count minimal paired-dominating sets under inclusion or inequivalent sets under graph automorphisms.

Originality is based on actual database and literature comparisons, not a guarantee of uniqueness. The full text behind the 2016 paired-domination-polynomial conference abstract was not accessible through the inspected route; it might contain a special-case coefficient identity. The complete deletion-resilience statement with pairing multiplicities was not found in the checked material.

## References

1. M. A. Henning and D. Ralaivaosaona, “Paired domination in trees: A linear algorithm and asymptotic normality,” arXiv:2505.17672v1, first public May 23, 2025; primary MSC \(05C69\).
2. C. Lu and Q. Wu, “Paired Domination in Cubic Bipartite Graphs,” arXiv:2609.30152v1, first public September 24, 2026.
3. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” Networks 32 (1998), 199–206, DOI 10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F.
4. K. B. Murthy, “The independent transversal paired domination in graphs,” International Journal of Pure and Applied Research in Engineering and Technology 4(5) (2015), 13–27, Proposition 2.6.
5. Puttaswamy and S. R. Nayaka, “The Minimum Paired Dominating Energy of a Graph,” International Journal of Mathematical Analysis and Applications (2016), Theorem 3.3.
6. Puttaswamy, A. Alwardi, and S. R. Nayaka, “Introduction to Paired Domination Polynomial of a Graph,” ICMAGT 2016 conference abstract, International Journal of Physical and Mathematical Sciences 10(9) (2016).
