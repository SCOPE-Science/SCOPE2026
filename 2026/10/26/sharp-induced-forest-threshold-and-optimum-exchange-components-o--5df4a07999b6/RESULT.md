# Sharp induced-forest threshold and optimum-exchange components of two-subset Kneser graphs

## Finding
For every integer \(n\ge5\), let \(G_n=\operatorname{KG}(n,2)\) be the graph on the two-element subsets of \([n]\), with two vertices adjacent precisely when the subsets are disjoint. Put \(f(G)=\max\{|F|:G[F]\text{ is a forest}\}\). Then
\[
f(G_n)=\max\{7,n\},\qquad \tau_{\mathrm{FVS}}(G_n)=\binom n2-\max\{7,n\}.
\]
Every maximum family is of one of the following two forms, with the indicated parameter conditions:

* **Four-clique with pendant edge**, \(C(U,c,d)=\binom U2\cup\{\{c,d\}\}\), where \(|U|=4\), \(c\in U\), and \(d\notin U\). This is a maximum family for \(5\le n\le7\), and there are \(4(n-4)\binom n4\) such families.
* **Complete star plus one edge**, \(S(c;a,b)=\{\{c,x\}:x\ne c\}\cup\{\{a,b\}\}\), where \(c,a,b\) are distinct. This is a maximum family for \(n\ge7\), and there are \(n\binom{n-1}2\) such families.

For each \(n\), form an exchange graph \(X_n\): vertices are the maximum families just defined, and two are adjacent if their symmetric difference has exactly two two-subsets of \([n]\) (one deletion and one insertion). Its complete graph decomposition is
\[
X_n\cong\begin{cases}
\binom n4 K_{4(n-4)},&5\le n\le6,\\
35K_{12}\,\sqcup\,7K_{15},&n=7,\\
nK_{\binom{n-1}2},&n\ge8.
\end{cases}
\]
In particular the exact transition occurs at \(n=7\), where both extremal shapes coexist, and all optimum-exchange components are cliques. No optimal exchange path joins distinct components.

## Assumptions and scope
All graphs are finite, simple, and undirected; \(n\) is any integer at least five. An induced forest forbids cycles of any length, not just induced cycles. Each selected vertex of \(G_n\) is a two-subset of \([n]\), equivalently an edge of an auxiliary simple graph on \([n]\). The exchange graph uses single-vertex replacement at fixed maximum cardinality; it is not the graph of arbitrary acyclic subsets.

## Proof
**Lemma 1 (intersecting pairs).** Every nonempty pairwise-intersecting family of distinct two-subsets is either contained in the star through some fixed ground element, or consists of the three edges of a triangle. To see this, take two different edges meeting at \(a\), say \(\{a,b\}\), \(\{a,c\}\). If some edge does not contain \(a\), it must be \(\{b,c\}\); any edge intersecting all three is then one of these three.

**Lemma 2 (sharp bound and equality).** Since every forest is bipartite, the vertices of any induced forest \(G_n[F]\) split into two (possibly empty) independent sets. Under the two-subset representation these are intersecting families \(A,B\), so Lemma 1 applies.

If both are triangles, \(|F|\le6\). Suppose one is a triangle on \(T=\{a,b,c\}\), and the other is a star with center \(u\). If \(u\in T\), the entire union lies in the full star at \(u\) together with the unique edge of the triangle not incident to \(u\), so \(|F|\le n\), and equality gives exactly \(S(u;a',b')\). If \(u\notin T\), two star edges with leaves outside \(T\) would both be disjoint from all three triangle edges and hence create a four-cycle in \(G_n[F]\). Thus at most one star leaf is outside \(T\), giving \(|F|\le3+4=7\); equality gives the full triangle on \(T\), the three edges from \(u\) to \(T\), and one extra edge from \(u\) to outside \(T\). This is exactly \(C(T\cup\{u\},u,d)\).

It remains to handle two stars. If they have a common center, \(|F|\le n-1\). Otherwise let their distinct centers be \(u,v\). Assign the possible shared edge \(\{u,v\}\) to neither star initially, and let \(r\) and \(s\) be the respective numbers of selected remaining edges centered at \(u\) and \(v\), with \(r\ge s\). Let \(\varepsilon\in\{0,1\}\) signal the selected edge \(\{u,v\}\). Then \(|F|=r+s+\varepsilon\) with \(r,s\le n-2\). When \(s\ge2\) and \(r\ge4\), any two edges of the second star have at least \(r-2\ge2\) common disjointness neighbors in the first star, making a four-cycle. If instead \(2\le s\le r\le3\), then \(|F|\le7\), and the sole putative equality \(r=s=3,\varepsilon=1\) cannot be a forest: the disjointness edges between the three \(u\)-edges and three \(v\)-edges number at least \(9-3=6\), hence those six vertices contain a cycle. Finally, if \(s\le1\), then \(|F|\le n\); equality requires all \(n-2\) edges \(\{u,x\}\) with \(x\notin\{u,v\}\), the edge \(\{u,v\}\), and one extra \(v\)-edge, exactly a type \(S\) family. Hence \(|F|\le\max\{7,n\}\), with equality only in the declared types.

Both types attain the bound when their sizes are maximal: the disjointness graph of \(C(U,c,d)\) is a seven-vertex subdivided claw (three paths of length two meeting at one vertex), and the disjointness graph of \(S(c;a,b)\) is \(K_{1,n-3}\sqcup 2K_1\). Thus both are forests. Their sizes are seven and \(n\) respectively. This proves the value formula and complete extremal classification. The minimum feedback-vertex-set identity follows by complementing maximum induced forests.

**Lemma 3 (counts and exchanges).** The six pairs inside \(U\) uniquely determine the four-point set \(U\) in any type \(C\) maximum; then the sole pair outside \(\binom U2\) determines \(c,d\). Therefore the number of type \(C\) families is \(\binom n4\,4(n-4)\). For fixed \(U\), any two such families share precisely the six inside pairs, so form a clique under single exchanges. For distinct four-sets \(U,U'\), at most three internal pairs are shared, and at most one exceptional pair from each family can be shared with the other's internal block; thus the intersection has size at most five, and no exchange is possible.

For type \(S\), the center is uniquely determined by its full degree \(n-1\) among selected pairs, and the off-star pair is arbitrary, yielding \(n\binom{n-1}2\) families. With fixed center any two families differ only by the off-star pair and hence are exchange-adjacent. Families with different centers share at most the center-to-center pair plus their respective off-star edges, therefore at most three pairs. At \(n=7\), there is also no edge from a type \(C\) family to a type \(S\) family: the former has maximum ground-graph degree four whereas the latter has a vertex of degree six, and their intersection has at most five pairs (at most four through the star center and at most one additional pair). Thus the two families lie in disjoint components.

Finally, for \(n=5,6\) only type \(C\) is maximum; for \(n=7\) both attain seven, with \(\binom74=35\) components of size \(4(7-4)=12\) and seven components of size \(\binom62=15\); and for \(n\ge8\) only type \(S\) is maximum. The stated clique decomposition follows.

## Verification
The accompanying standalone C++17 verifier, `verify_kneser_forest.cpp`, independently builds the disjointness graph; exhaustively tests all subsets at the proposed optimum and one greater for each \(n=5,6,7,8\); uses union-find to test forests and a separate depth-first-search cycle detector on each accepted optimum; reconstructs both extremal families from definitions; and independently enumerates all exchange edges and connected components. Successful outputs are exactly:

```
n=5 optimum=7 sets=20 components=5 edges=30 VERIFY_OK
n=6 optimum=7 sets=120 components=15 edges=420 VERIFY_OK
n=7 optimum=7 sets=525 components=42 edges=3045 VERIFY_OK
n=8 optimum=8 sets=168 components=8 edges=1680 VERIFY_OK
```

Compile with `c++ -O2 -std=c++17 verify_kneser_forest.cpp -o verify && ./verify`. These finite checks test boundaries but are not substituted for the all-parameter structural proof above.

## Relationship to prior work
Chappell and Pelsmajer (2013) study maximum induced forests and feedback vertex sets, primarily deriving bounds from bounded treewidth; their inspected introduction and main results do not provide this Kneser-family classification. Alishahi and Taherkhani (2018), Theorem 1 and especially Theorem 2, solve general forbidden-subgraph problems for Kneser graphs at sufficiently large or explicitly very large ground-set order. Specializing their forbidden graph to \(K_{2,2}\) already supplies **eventual** star-plus-one-edge extremality for a broader class (every forest is \(K_{2,2}\)-free). Thus eventual large-parameter extremality is **not** claimed as new. The present theorem sharpens that asymptotic result to the exact first threshold, includes all exceptional \(n=5,6,7\) configurations, and gives complete all-parameter optimum-preserving exchange components. The latter results are not supplied by the inspected source statements.

## Limitations
The domain is the pair case \(\operatorname{KG}(n,2)\), not higher-uniformity Kneser graphs. Exchange is restricted to one selected vertex replaced by one unselected vertex. Literature searches and primary-text comparison cannot exclude every unpublished computation or alternative-language older sharp theorem; the earlier \(K_{s,t}\)-free extremal-set literature is a specific residual originality risk. No independent audit has been performed.

## References
1. G. G. Chappell and M. J. Pelsmajer, *Maximum Induced Forests in Graphs of Bounded Treewidth*, Electronic Journal of Combinatorics 20(4), P8 (first published 2013-10-28), DOI: 10.37236/3826. Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i4p8/pdf.
2. M. Alishahi and A. Taherkhani, *Extremal G-free induced subgraphs of Kneser graphs*, arXiv:1801.03972 (initial version 2018-01-11), especially Theorems 1 and 2 and the discussion of \((s,t)\)-union-intersecting families. Full text: https://arxiv.org/pdf/1801.03972.
