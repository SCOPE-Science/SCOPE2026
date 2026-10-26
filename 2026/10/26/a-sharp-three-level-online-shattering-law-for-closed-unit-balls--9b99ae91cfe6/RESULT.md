# A sharp three-level online-shattering law for closed unit balls of finite trees

## Finding

Let \(T=(V,E)\) be any finite nonempty undirected simple tree with \(n=|V|\). For each \(v\in V\), let its closed unit ball be \(N[v]=\{v\}\cup\{u:uv\in E\}\). Set \(\mathcal C_T=\{\mathbf 1_{N[v]}:v\in V\}\), identifying coincident indicator functions. Write \(d_T(v)\) for the ordinary graph degree and \(B_v=V\setminus N[v]\).

**Exact classification.** The Littlestone dimension of this finite concept class is
\[
\operatorname{Ldim}(\mathcal C_T)=
\begin{cases}
0,&n\le2,\\
1,&n=3,\\
3,&n\ge4\text{ and there are }v,w\in V\text{ with }d_T(v)\ge3\text{ and }2\le |N[w]\cap B_v|\le |B_v|-2,\\
2,&\text{otherwise}.
\end{cases}
\]
The quantified criterion is purely graph-theoretic. In particular, the dimension is computable from an adjacency list in \(O(n^2)\) time: for each \(v\), form \(B_v\), and for each \(w\), count its intersection with \(N[w]\). All dimensions are at most three.

The threshold for dimension three is sharp: no tree of order at most seven has it, and an eight-vertex tree does. Among the 23 isomorphism classes of eight-vertex trees, exactly 12 have dimension three (an exhaustive finite classification with a reproducible checker). Every tree-unit-ball concept class has \(\operatorname{VCdim}\le2\). Hence the eight-vertex witness has strict separation \(\operatorname{VCdim}=2<\operatorname{Ldim}=3\).

## Assumptions and scope

The graph is finite, connected, acyclic, loopless and undirected. A concept's **instance** is a vertex \(x\in V\); the concept with center \(v\) labels it one iff \(x=v\) or \(xv\in E\). A depth-\(k\) Littlestone tree is a complete binary tree of height \(k\) whose internal nodes are labeled by instances, with each root-to-leaf binary answer sequence consistent with at least one concept. This is the standard realizable binary online mistake-tree convention. Singleton classes have dimension zero. The class contains closed *radius-one* balls, not balls of variable radius, all subtrees, or shortest-path vertex sets.

For \(n\ge3\), all \(N[v]\) are distinct: if \(N[u]=N[v]\) for distinct vertices, then \(uv\in E\), and a third vertex adjacent to one of \(u,v\) produces an unequal neighborhood (a tree has no triangle). For \(n=2\), the two neighborhoods coincide.

## Proof

**Lemma 1 (a two-round split criterion).** If \(\mathcal H\) is a finite family of distinct binary functions, then \(\operatorname{Ldim}(\mathcal H)\ge1\) exactly when \(|\mathcal H|\ge2\). Also \(\operatorname{Ldim}(\mathcal H)\ge2\) exactly when there is an instance \(x\) for which each of the zero and one branches contains at least two functions.

*Proof.* Distinct functions admit an instance separating any two of them, proving the first statement. A depth-two tree necessarily has a root whose two branches each shatter a depth-one tree and hence each contain two distinct functions. Conversely, two or more functions on each branch can be separated by an instance specific to that branch, giving a depth-two tree. \(\square\)

**Lemma 2 (one-positive-query geometry).** Fix a tree \(T\) with \(n\ge3\) and a vertex \(v\). Restrict the possible centers to \(N[v]\), that is, retain only the concepts responding positively to query \(v\). This family has Littlestone dimension at most two. Its dimension equals two if and only if \(d_T(v)\ge3\).

*Proof.* A second query at \(v\) includes every remaining center. If a second query is at a neighbor \(w\) of \(v\), exactly the two centers \(v,w\) answer positively, because no two distinct neighbors of \(v\) are adjacent. For a query at distance two from \(v\), exactly its neighbor on the path toward \(v\) answers positively among \(N[v]\). Farther-away queries have no positive centers. Thus in every nontrivial split one side contains at most two hypotheses, and the side cannot sustain depth two; a depth-three tree in the restricted class is impossible.

If \(d_T(v)\le2\), at most three hypotheses remain, so depth two is impossible. If \(d_T(v)\ge3\), query any neighbor \(w\) of \(v\): its positive branch consists of the two distinct centers \(v,w\); its negative branch contains the other at least two distinct neighbor-centers. Both branches have dimension at least one by Lemma 1. \(\square\)

**Lemma 3 (negative branch).** For \(n\ge3\), the family of centers responding negatively to query \(v\) has Littlestone dimension at least two if and only if there exists a vertex \(w\) satisfying
\[
2\le |N[w]\cap B_v|\le |B_v|-2.
\]
*Proof.* The negative centers are precisely \(B_v\). They induce distinct functions (their original closed neighborhoods remain distinct on the full instance domain). Apply Lemma 1 with a subsequent query \(w\). \(\square\)

**Theorem.** The claimed classification holds.

*Proof.* At the root of any proposed depth-four Littlestone tree, say query \(v\), both branches must have dimension at least three. But the positive branch is at most two by Lemma 2. Hence \(\operatorname{Ldim}(\mathcal C_T)\le3\) for every tree of size at least three.

For dimension three, its root must have both depth-two branches. By Lemma 2 the positive branch has depth two exactly when \(d_T(v)\ge3\). By Lemma 3 the negative branch has depth two exactly when there is \(w\) with the displayed two-sided inequality. Conversely, any such \(v,w\) supply the two depth-two branches, and adjoining them to the root \(v\) gives depth three.

For \(n=1\) the unique function yields dimension zero. For \(n=2\) both closed neighborhoods equal \(V\), again dimension zero. For \(n=3\) there are three distinct concepts; a leaf query separates them, giving dimension one, while depth two requires at least four concepts. For every \(n\ge4\), take a leaf \(\ell\) and query it. Its positive branch has exactly the centers \(\ell\) and its unique neighbor, and its negative branch has \(n-2\ge2\) distinct centers. Lemma 1 gives dimension at least two, completing the trichotomy. \(\square\)

**First sharp order and explicit witness.** If the dimension-three criterion holds, then \(d_T(v)\ge3\) and \(|B_v|\ge4\); since \(n=d_T(v)+1+|B_v|\), necessarily \(n\ge8\). For equality, take vertices \(\{0,1,\ldots,7\}\) and edges
\[
\{\{0,1\},\{0,2\},\{0,3\},\{1,4\},\{1,5\},\{2,6\},\{2,7\}\}.
\]
A complete shattered tree of depth three queries vertex \(0\) at the root, then vertex \(1\) at both children. At the third level, query \(2\) after answer prefixes \((1,1)\) or \((1,0)\), vertex \(4\) after \((0,1)\), and vertex \(6\) after \((0,0)\). Every one of the eight binary root-to-leaf paths is realized: for the sequences \(000,001,010,011,100,101,110,111\), the respective center witnesses are \(7,6,5,4,3,2,1,0\). In particular, the two query vertices \(1\) and \(2\) have four traces, realized by centers \(0,1,6,3\); therefore \(\operatorname{VCdim}=2\) for this witness.

**VC upper bound.** Suppose three distinct vertices \(a,b,c\) are all in \(N[z]\) for some center \(z\). If \(z\notin\{a,b,c\}\), all three are neighbors of \(z\) and no center can contain exactly two of them: two different neighbors of \(z\) have distance two with unique common center \(z\). If \(z\in\{a,b,c\}\), say \(z=a\), then \(b,c\) are neighbors of \(a\), and again the unique center meeting both \(b,c\) is \(a\), which also meets \(a\). Either way the trace \(\{b,c\}\) (or a corresponding two-element trace) is unavailable, so no three-vertex set is shattered. Hence \(\operatorname{VCdim}(\mathcal C_T)\le2\). \(\square\)

## Verification

The accompanying `verify.py` uses only Python's standard library and implements the complete Littlestone recursion over subsets of distinct center hypotheses, independently of the graph-theoretic criterion. It enumerates **all** labeled trees through order eight using every Prüfer sequence, collapses them to unlabeled classes using center-rooted canonical encodings, and compares exact dimensions with the formula. For order eight, all \(8^6=262144\) labeled Prüfer sequences were processed, giving 23 unlabeled types, 11 of dimension two and 12 of dimension three. It also directly checks the VC upper bound on each canonical representative and every one of the eight witness paths. The execution transcript ends `ALL_CHECKS_PASS`.

These finite tests do not prove the all-order theorem; Lemmas 1–3 and the theorem proof do. The counts of order-eight isomorphism classes rely on the explicit finite enumeration, Prüfer-tree correspondence, and center-rooted canonical encoding.

## Relationship to prior work

Chalopin, Chepoi, Mc Inerney, Ratel and Vaxès, *Sample compression schemes for balls in graphs* (first posted 2022), analyze the same tree-ball families, including all fixed-radius families, and construct size-two proper labeled sample-compression schemes. They also state the established VC-dimension bound of two for tree balls. The present result credits that static bound; its different invariant is exact *adaptive* Littlestone dimension for closed radius-one balls, with a necessary-and-sufficient branching test. A sample-compression bound does not itself supply this exact depth classification: for example, ordered thresholds on an arbitrarily long finite chain have a proper labeled two-example compression scheme (retain the last positive and first negative sample), yet their Littlestone dimension grows logarithmically with the chain length.

Coudert, Csikós, Ducoffe and Viennot, *Practical Computation of Graph VC-Dimension* (2024), study closed-neighborhood set systems on graphs and algorithms for static VC dimension. Its objects overlap exactly with ours on trees, but its stated algorithms and bounds concern static shattering, not binary-tree online shattering. The tree-path and descendant-cone concept classes, while related in their underlying trees, use different vertex predicates and do not imply the present unit-ball theorem.

## Limitations

The upper bound and test require *trees* and *radius one*. They are not asserted for arbitrary graphs, varying-radius ball families, open neighborhoods, or disconnected forests. The finite order-eight census is a computationally checked count; it is not a classification of all minimal forbidden induced subtrees. Novelty is conditional on the literature and searchable-record comparisons listed in the review materials; absolute publication priority is not established. Independent audit has not been performed.

## References

1. J. Chalopin, V. Chepoi, F. Mc Inerney, S. Ratel, Y. Vaxès. *Sample compression schemes for balls in graphs*. arXiv:2206.13254, first public version June 27, 2022. https://arxiv.org/abs/2206.13254 . See the extended HTML version, Section 3: https://arxiv.org/html/2206.13254v2 .
2. D. Coudert, M. Csikós, G. Ducoffe, L. Viennot. *Practical Computation of Graph VC-Dimension*. SEA 2024, LIPIcs 301, Article 8, July 11, 2024. DOI:10.4230/LIPIcs.SEA.2024.8 . https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SEA.2024.8 .
