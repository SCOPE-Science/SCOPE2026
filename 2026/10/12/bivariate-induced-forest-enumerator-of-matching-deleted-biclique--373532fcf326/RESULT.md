# Bivariate induced-forest enumerator of matching-deleted bicliques

## Finding

Let \(p,q\ge 2\) and \(0\le t\le\min\{p,q\}\) be integers. Obtain \(H_{p,q,t}\) from the complete bipartite graph \(K_{p,q}\) by deleting any matching of \(t\) edges. Define
\[
\Phi_{p,q,t}(x,y)=\sum_{\substack{S\subseteq V(H_{p,q,t})\\H_{p,q,t}[S]\text{ is a forest}}}x^{|S|}y^{\kappa(H_{p,q,t}[S])},
\]
where \(\kappa\) is the number of connected components and \(\kappa(\varnothing)=0\). Then, for every permitted triple,
\[
\begin{aligned}
\Phi_{p,q,t}(x,y)
={}&(1+xy)^p+(1+xy)^q-1\\
&+xy\Big[(p-t)((1+x)^q-1)+(q-t)((1+x)^p-1)\\
&\qquad+t((1+x)^{q-1}-1)+t((1+x)^{p-1}-1)\Big]\\
&+t x^2y^2\big((1+x)^{p-1}+(1+x)^{q-1}\big)\\
&-x^2\big((pq-t)y+t y^2\big)\\
&+\big[t(p-1)(q-1)-t(t-1)\big]x^4y\\
&+\binom{t}{2}x^4y^2+\binom{t}{2}(p+q-4)x^5y.
\end{aligned}
\]

This is a full two-variable enumeration, not just an extremal bound. In particular, the number of vertex-induced copies of the four-vertex and five-vertex paths is respectively
\[
N_{P_4}=t(p-1)(q-1)-t(t-1),\qquad
N_{P_5}=\binom{t}{2}(p+q-4),
\]
and no induced path has more than five vertices. In the balanced family \(p=q=n\) with \(0<t\le n\), the exact difference is
\[
N_{P_4}-N_{P_5}=t(n-1)(n-t).
\]
Thus, for \(n\ge3\), equality of the two positive path counts holds precisely at full-matching deletion \(t=n\), when both equal \(n(n-1)(n-2)\). (Without any deleted edge, both counts are zero.)

The maximum size of an induced forest is the largest of \(p+1\) and \(q+1\), together with \(4\) if \(t\ge1\), and \(5\) if \(t\ge2\) and \(\max\{p,q\}\ge3\). Hence the feedback vertex set number is \(p+q\) minus this maximum; its number of minimum solutions is the coefficient of that maximum power of \(x\) in \(\Phi_{p,q,t}(x,1)\). For crown graphs \(H_{n,n,n}\), there are \(6\), \(32\), and \(2n\) maximum induced forests when respectively \(n=3\), \(n=4\), and \(n\ge5\).

## Assumptions and scope

Graphs are finite, simple, undirected, and have distinct labeled vertices in two parts \(A\) and \(B\), of sizes \(p\) and \(q\). Missing edges form a matching: their endpoints are distinct, and no additional edges are deleted. The polynomial counts vertex subsets, not isomorphism classes. A singleton contributes one component; the empty graph contributes zero components. The domain includes \(t=0\) and \(t=\min\{p,q\}\) without additional connectivity assumptions.

## Proof

For a selected vertex set let \(a=|S\cap A|\), \(b=|S\cap B|\), and let \(d\) be the number of deleted-matching edges whose two endpoints are selected. The induced subgraph has exactly \(ab-d\) edges, with \(d\le\min\{a,b,t\}\).

If \(a,b\ge3\), choosing any three vertices from each part produces a six-vertex induced subgraph with at least \(9-3=6\) edges. Since a forest on six vertices has at most five edges, this contains a cycle. Likewise, if \(a=2\) and \(b\ge4\), two left and four right vertices induce at least \(8-2=6\) edges on six vertices, hence contain a cycle. The symmetric case is identical. If \((a,b)=(2,3)\) or \((3,2)\), the five-vertex graph is a forest exactly when both possible deleted-matching edges occur among its endpoints: for fewer than two deletions there are at least five edges, while with two deletions the graph is an induced five-vertex path. If \((a,b)=(2,2)\), zero deleted edges give a four-cycle, one gives a four-vertex path, and two give two disjoint edges. All subsets with \(\min\{a,b\}\le1\) induce forests.

It remains to count these mutually exhaustive cases. Subsets lying entirely in one part contribute \((1+xy)^p+(1+xy)^q-1\). For subsets with exactly one vertex on the \(p\)-side and a nonempty selection on the \(q\)-side, a selected unmatched vertex has a connected star with \(\binom qj\) choices of \(j\) other vertices. A selected endpoint of a missing edge has a star when its matched partner is absent, with \(\binom{q-1}{j}\) choices, and a star together with one isolated vertex when that partner is included, with \(\binom{q-1}{j-1}\) choices. Weighting by order and components yields
\[
xy\big[(p-t)((1+x)^q-1)+t((1+x)^{q-1}-1)\big]
+t x^2y^2(1+x)^{q-1}.
\]
Interchanging \(p\) and \(q\) supplies the symmetric term. Exactly-one-vertex selections on each side have been counted twice, so subtract \(x^2((pq-t)y+t y^2)\): there are \(pq-t\) adjacent pairs and \(t\) nonadjacent matched pairs.

A selected \(2\)-by-\(2\) biclique with exactly one missing matching edge can be counted by first selecting that deleted edge and then another vertex in each part; this yields \(t(p-1)(q-1)\) choices, but each of the \(\binom t2\) pairs of deleted edges contributes twice and must be removed from this one-deletion class. Thus the one-deletion count is \(t(p-1)(q-1)-2\binom t2\), and the two-deletion count is \(\binom t2\). Their component counts are one and two respectively. Finally, selected \(2\)-by-\(3\) and \(3\)-by-\(2\) five-vertex paths require the two missing edges and any one additional vertex on the larger side. They number \(\binom t2[(q-2)+(p-2)]\) and are connected. Summing gives the displayed polynomial.

The path formulas select precisely the connected \(2\)-by-\(2\) one-deletion and \(2\)-by-\(3\)/\(3\)-by-\(2\) two-deletion cases. Other connected induced forests are stars on at most one vertex of a part, so there are no longer induced paths. The balanced path-count difference follows by substitution. The maximum induced-forest order is attained among the exhaustive size classes: at most \(p+1\) or \(q+1\) in the one-small-side cases, four in the \(2\)-by-\(2\) case, and five in the \(2\)-by-\(3\) cases. The stated conditions ensure those exceptional sizes are attainable. For crowns the leading coefficients follow from the same formula, distinguishing the degree-five contribution at \(n=3,4\) from the single-small-side maximum at \(n\ge5\).

## Verification

The separate finite test in `verify.py` constructs every vertex-induced subgraph by an edge-by-edge union-find cycle test and counts its connected components. It compares the resulting complete bivariate coefficient dictionaries with the formula for every \(2\le p,q\le7\) and \(0\le t\le\min\{p,q\}\). It also independently checks induced paths via degree and connectivity tests. Running `python3 verify.py` prints

```text
VERIFY_OK parameter_triples=163 subsets=413040 path_type_checks=326 crown_balance_tests=5 max_vertices=14
```

These finite checks validate the displayed small instances only; the classification and case-counting argument above proves the all-integer formula.

## Relationship to prior work

Chappell and Pelsmajer (2013) study maximum induced forests under graph-class constraints and connect the maximum forest order to feedback vertex sets. Their main results are lower bounds for graph classes of bounded treewidth, not coefficients for missing-matching bicliques. Axenovich, Dörr, Rollin and Ueckerdt (2018), in their treatment of induced arboricity, note that every induced forest of \(K_{k,k+1}\) is a star. This is the unperturbed, connected situation and does not count vertex subsets or address how a deleted matching creates induced four- and five-vertex paths. The claim here is the exact matching-deletion interpolation and simultaneous order/component distribution, including the positive-path-count balance criterion for crowns.

## Limitations

No claim is made for arbitrary removed edge sets, for induced forests with prescribed edge colors, or for independent external validation. The exhaustive computer checks end at \(p,q\le7\); their scope is not confused with the general proof. The novelty comparison depends on accessible indexed and examined literature and may miss an earlier poorly indexed specialization. The combinatorial formula itself does not resolve general feedback vertex set complexity.

## References

1. Glenn G. Chappell and Michael J. Pelsmajer, *Maximum Induced Forests in Graphs of Bounded Treewidth*, Electronic Journal of Combinatorics **20** (2013), #P8, published 2013-10-28. DOI: 10.37236/3826. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i4p8/pdf/ . Primary MSC 05C35 in the article.
2. Maria Axenovich, Philip Dörr, Jonathan Rollin and Torsten Ueckerdt, *Induced and Weak Induced Arboricities*, arXiv:1803.02152 (2018-03-06), especially Proposition 3 and its proof. https://arxiv.org/pdf/1803.02152 .
