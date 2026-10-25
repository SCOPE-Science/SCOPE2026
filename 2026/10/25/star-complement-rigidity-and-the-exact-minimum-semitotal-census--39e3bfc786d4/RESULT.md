# Star-complement rigidity and the exact minimum semitotal census of subdivided bicliques

## Finding

Let \(H_{p,q}=\operatorname{S}(K_{p,q})\), the graph obtained by subdividing every edge of a complete bipartite graph exactly once, with integers \(p,q\ge2\). Let \(\mathcal M_{p,q}(u,v,w)\) count **minimum-cardinality semitotal dominating sets**, recording respectively the numbers of selected original vertices in the two sides and of selected subdivision vertices. For \((p,q)\ne(2,2)\), all minimum sets are independent and the polynomial is

\[
\mathcal M_{p,q}(u,v,w)=p u^{p-1}\big((v+w)^q-v^q-qv^{q-1}w-w^q\big)+q v^{q-1}\big((u+w)^p-u^p-pu^{p-1}w-w^p\big).
\]

Consequently their exact number is
\[
\mathcal M_{p,q}(1,1,1)=p(2^q-q-2)+q(2^p-p-2),
\]
while every minimum set has \(p+q-1\) vertices. For \(p=q=2\), the graph is the eight-cycle, its minimum size is four and it has exactly 30 minimum semitotal dominating sets, only two of which are independent. The minimum-cardinality formula is a specialization of the general subdivision theorem of Cabrera-Martínez and collaborators [3]; the **new statement here is the complete optimizer classification and trivariate enumeration** (including the exceptional endpoint and the fact that all other optimizers are independent).

## Assumptions and scope

All graphs are finite, simple and undirected. A set \(D\subseteq V(H)\) is dominating when each vertex outside \(D\) has a neighbor in \(D\). It is *semitotal dominating* when, in addition, each \(d\in D\) has a **distinct** witness \(d'\in D\) at graph distance at most two. The minimum cardinality is \(\gamma_{t2}(H)\). Each \(H_{p,q}\) has labeled original sides \(A=\{a_1,\ldots,a_p\}\), \(B=\{b_1,\ldots,b_q\}\), and labeled inserted vertices \(W=\{w_{ij}:1\le i\le p,1\le j\le q\}\), with edges precisely \(a_iw_{ij}\) and \(b_jw_{ij}\). The variables \(u,v,w\) mark the respective cardinalities \(|D\cap A|,|D\cap B|,|D\cap W|\); coefficients count labeled vertex subsets, not graph-isomorphism classes. The result applies for all \(p,q\ge2\), with the corner \((2,2)\) specified separately.

## Proof

**Step 1: forced subdivision vertices and the lower bound.** Write \(A_0=A\setminus D\), \(B_0=B\setminus D\), \(x=|A_0|\), \(y=|B_0|\). Any inserted vertex \(w_{ij}\) with \(a_i\in A_0\) and \(b_j\in B_0\) must belong to \(D\): otherwise it has neither endpoint selected and is undominated. Therefore, when \(x,y\ge1\),
\[
|D|\ge (p-x)+(q-y)+xy=p+q-1+(x-1)(y-1).
\]
If \(x=0\), each of the \(y\) unselected \(B\)-vertices requires a selected inserted neighbor in its own (distinct) column, so \(|D|\ge p+(q-y)+y=p+q\). The case \(y=0\) is symmetric. If \(x,y\ge2\), the displayed inequality gives \(|D|\ge p+q\). Hence every set with size at most \(p+q-1\) has \(x=1\) or \(y=1\) and consists of exactly the \((p-x)+(q-y)\) selected original vertices together with all \(xy\) forced inserted vertices (with no optional extras).

**Step 2: witness and domination restrictions.** Suppose \(x=1\), write \(A_0=\{a_i\}\), and let \(B_0=Y\) with \(|Y|=y\ge1\). All selected subdivision vertices are exactly \(\{w_{ij}:b_j\in Y\}\). When \(y=1\), this is one vertex whose two original endpoints are unselected; any other inserted vertex is at distance at least four from it, and the selected original vertices are at distance at least three. Thus this selected vertex lacks a distance-two witness. When \(y=q\), no original \(B\)-vertex is selected. Every selected original \(A\)-vertex then lacks a witness within distance two: its only potential original witnesses at distance two would lie in \(B\), while the selected inserted vertices are incident only with the one *unselected* \(a_i\). Consequently \(2\le y\le q-1\) is necessary. Conversely, when \(2\le y\le q-1\), every unselected original vertex is adjacent to a selected inserted vertex, every unselected inserted vertex has a selected endpoint, each selected inserted vertex has another selected inserted vertex at distance two through \(a_i\), and every selected original vertex has a selected opposite-side original vertex at distance two. Hence the described set is semitotal dominating. Moreover, no selected inserted vertex touches a selected original vertex, so it is independent. The symmetric argument for \(y=1\) gives \(2\le x\le p-1\). The two families are disjoint, as the first has \(x=1,y\ge2\) and the second has \(y=1,x\ge2\).

**Step 3: existence, rigidity and counting.** For \((p,q)\ne(2,2)\), at least one part has size at least three, so one of the two families above exists. These supply a set of size \(p+q-1\), meeting the universal lower bound. In the first family choose the omitted \(A\)-vertex in \(p\) ways and choose \(Y\subset B\) of size \(j\in\{2,\ldots,q-1\}\) in \(\binom qj\) ways. Such a set has \(p-1\) selected \(A\)-vertices, \(q-j\) selected \(B\)-vertices and \(j\) selected inserted vertices. Thus its contribution is \(p u^{p-1}\sum_{j=2}^{q-1}\binom qjv^{q-j}w^j\), precisely the first bracketed term. Symmetry yields the other term and proves the full trivariate identity. Substitution \(u=v=w=1\) proves the univariate total count. This is a classification of *every* minimum set, not merely a construction of some minimizers.

**Step 4: the exceptional eight-cycle.** If \(p=q=2\), Step 1 rules out a semitotal set of size at most three, so \(\gamma_{t2}(H_{2,2})\ge4\); all four original vertices form a size-four example. The graph is \(C_8\). For a four-element set on this cycle, list the four positive cyclic gaps between consecutive selected vertices. Domination is equivalent to every gap being at most three. A selected vertex has a distance-two witness precisely when the gap on at least one of its two sides is at most two; equivalently, there are **no adjacent gaps both equal to three**. The admissible ordered gap quadruples, whose entries sum to eight, are the single tuple \((2,2,2,2)\), all twelve permutations of \((3,2,2,1)\), and the two alternating tuples \((3,1,3,1)\) and \((1,3,1,3)\). They number fifteen. Choosing the labeled starting position in eight ways and dividing by four possible starting selected vertices gives \(8\cdot15/4=30\) distinct sets. An independent four-element subset of \(C_8\) must alternate around the cycle; there are exactly two. This completes all cases. \(\square\)

## Verification

The standalone standard-library script `verify.py` implements the graph from its original edge definition, computes genuine distances up to two, independently tests the semitotal condition, enumerates vertex subsets in increasing cardinality, and compares each minimum-size occupancy profile with the polynomial coefficients. Exhaustive parameter cases \((2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(4,4)\) agree exactly. This is a finite cross-check, not a proof for unbounded \(p,q\); the proof is Steps 1–4.

## Relationship to prior work

Alikhani and Zaherifar [1] developed cardinality-counting polynomials for semitotal dominating sets, including results on **unsubdivided** complete bipartite graphs. Tripathi, Pandey and Maheshwari [2] provided algorithmic results for strongly chordal graphs, which do not cover the induced eight-cycles present here. Most importantly, Cabrera-Martínez, López-Carmona, Rios-Villamar and Serrano-Díaz [3, Theorem 2.1] already proved the **general** formula \(\gamma_{t2}(\operatorname{S}(G))=i_{t2}(\operatorname{S}(G))=|V(G)|-p_3(G)\) for connected graphs. Therefore the present minimum-size identity, and the existence of an independent optimum, are NOT originality claims. Their general theorem does not give the full set of all minimizers or the three-variable census for the subdivided bicliques; in particular equality of the two minimum parameters does not imply that *every* minimum is independent. The new statement supplies exactly that equality-case classification and the exceptional eight-cycle count.

## Limitations

This result does not enumerate semitotal dominating sets above minimum size, generalize to arbitrary subdivisions, or assert a complexity consequence. Priority has been checked against accessible closely related primary texts and mathematical records, but unindexed equivalent enumerations remain a residual risk. Exhaustive computations cover only the indicated finite instances. All claims concern semitotal domination, not total domination; a selected vertex's distance-two witness can be nonadjacent.

## References

[1] S. Alikhani and H. Zaherifar, *On the semitotal dominating sets of graphs* (first posted 2021-07-03), arXiv:2107.01424, https://arxiv.org/abs/2107.01424.

[2] A. Tripathi, A. Pandey and P. Maheshwari, *A linear-time algorithm for semitotal domination in strongly chordal graphs* (2021), arXiv:2109.02142, https://arxiv.org/abs/2109.02142.

[3] A. Cabrera-Martínez, J. L. López-Carmona, I. Rios-Villamar and A. Serrano-Díaz, *On the (independent) semitotal domination in subdivision, middle, and central graphs* (first posted 2026-09-27), arXiv:2609.33932, especially Section 2 and Theorem 2.1, https://arxiv.org/abs/2609.33932.
