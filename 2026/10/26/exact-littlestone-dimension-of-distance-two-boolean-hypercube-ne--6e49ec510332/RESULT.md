# Exact Littlestone dimension of distance-two Boolean hypercube neighborhoods

## Finding
For every integer \(d\ge1\), let \(Q_d=\{0,1\}^d\) with Hamming distance \(\operatorname{dist}_H\), and let
\[
\mathcal H_d=\bigl\{h_c:Q_d\to\{0,1\}:c\in Q_d\bigr\},\qquad
h_c(x)=1\iff \operatorname{dist}_H(x,c)=2.
\]
Here duplicate functions, if any, count as one hypothesis. In deterministic realizable online learning with arbitrary vertex queries and Boolean membership labels, the exact Littlestone dimension is
\[
\operatorname{Ldim}(\mathcal H_d)=
\begin{cases}
0,&d=1,\\
1,&d=2,\\
2,&d=3,4,\\
4,&d=5,6,\\
5,&d\ge7.
\end{cases}
\]
In particular, the sharp bound five is independent of ambient dimension, and the dimension jumps directly from two to four between dimensions four and five. For the same class, the known exact ordinary VC-dimension computation in a distinct result has value three at dimension five: online/adaptive shattering genuinely detects a stronger obstruction there.

## Assumptions and scope
All dimensions are finite positive integers and the alphabet is exactly binary. The **exact** radius-two sphere is used, not a radius-at-most-two closed ball, distance-one adjacency, or an arbitrary-radius family. A Littlestone tree of depth \(t\) is a complete binary tree of height \(t\), with an instance attached to every internal vertex, such that for every leaf there exists one hypothesis realizing every zero/one label on its root-to-leaf path. Queries may depend on earlier labels; no query restrictions are imposed. In the finite case, a depth-\(t\) shattered tree requires at least \(2^t\) distinct hypotheses. A class consisting of a single Boolean function has dimension zero.

## Proof
**A. The universal upper bound.** Fix any query \(x\in Q_d\). If its answer is one, the remaining possible centers are the \(\binom d2\) vectors at distance exactly two from \(x\). Translating centers and queries by coordinatewise XOR with \(x\), identify these vectors with the two-subsets (edges) of \([d]\). Call the restricted family \(\mathcal E_d\). For a further query with support \(Z\), an edge \(e\) answers one if and only if
\[
|Z\mathbin\triangle e|=2\quad\Longleftrightarrow\quad |Z|=2|Z\cap e|.
\]
Thus a nonconstant test on \(\mathcal E_d\) has \(|Z|=2\) or \(|Z|=4\). If \(|Z|=4\), its positive subset is the six edges internal to \(Z\), so cannot shatter a binary tree of depth three (and hence cannot shatter depth four). If \(|Z|=2\), its positive subset consists exactly of the edges crossing the cut between that two-set and its complement: a complete bipartite edge family \(K_{2,d-2}\).

We claim that, under the same distance-two tests, every such family \(K_{2,m}\) has Littlestone dimension at most three, uniformly in \(m\ge0\). Write its edges as \((a,u),(b,u)\) for \(u\) in a set \(U\) of size \(m\). A weight-zero query returns one on all of them. A weight-four query returns one on at most four of them, since its support contains at most two vertices from \(\{a,b\}\) and at most four vertices altogether. A weight-two query contained in \(U\) returns one on at most four; the query \(\{a,b\}\) returns one on all edges. The remaining weight-two queries are of the form \(\{a,u\}\) or \(\{b,u\}\). By symmetry consider \(\{a,u\}\): its positive subset is
\[
\mathcal F=\{(a,v):v\in U\setminus\{u\}\}\cup\{(b,u)\}.
\]
For every further query, at least one of its two branches in \(\mathcal F\) contains at most three hypotheses. To check this directly: weights other than zero, two, four give the empty positive branch; weight zero gives an empty negative branch; a weight-four query has at most three positive edges in \(\mathcal F\); a weight-two query \(\{a,v\}\) has at most two negative edges (zero when \(v=u\)); and every other weight-two query has at most two positive edges, except \(\{a,b\}\), which is constantly positive. This exhausts the query supports. Consequently \(\mathcal F\) cannot shatter depth three, since each child of a depth-three tree would have to support four distinct hypotheses. Therefore every test in \(K_{2,m}\) has a branch of rank at most two or fewer than eight hypotheses, and \(\operatorname{Ldim}(K_{2,m})\le3\).

Returning to \(\mathcal E_d\): a putative depth-five shattered tree would need *both* children of its first test to shatter depth four. The zero-weight test is constant; the weight-four positive child has just six hypotheses; and the weight-two positive child is \(K_{2,d-2}\), of dimension at most three. All other weights have empty positive child. Hence \(\operatorname{Ldim}(\mathcal E_d)\le4\). Every depth-six shattered tree of \(\mathcal H_d\) would have to shatter depth five in the positive branch of its root. Since that branch is a translate of \(\mathcal E_d\), this is impossible. Thus \(\operatorname{Ldim}(\mathcal H_d)\le5\) for all \(d\ge1\).

**B. The small-dimensional improvements.** For \(d=1\), every hypothesis is constantly zero. For \(d=2\), every positive branch has only one center, so depth two is impossible. For \(d=3\), every positive branch has only three centers, so depth three is impossible. In dimension four, the hypothesis of a center \(c\) is identical to that of its bitwise complement \(\overline c\), because \(\operatorname{dist}_H(x,\overline c)=4-\operatorname{dist}_H(x,c)\). Every positive root branch comprises six centers grouped into three complement pairs, hence has at most three distinct hypotheses and cannot shatter depth two. It follows that depth three is impossible in dimension four. For dimensions five and six, the positive branch has respectively ten and fifteen centers, both fewer than sixteen; depth five is impossible. These bounds yield \(0,1,2,2,4,4\) for the first six dimensions once the lower bounds are supplied.

**C. Exact lower bounds.** The accompanying `shell2_witnesses.json` contains full labelled binary mistake trees for \((d,t)=(2,1),(3,2),(5,4),(7,5)\). Every internal node specifies its query as the integer encoding of a binary vector; each terminal node specifies a center. The path checks use precisely the predicate \(\operatorname{bitcount}(c\oplus x)=2\). The file `verify_shell2.py` verifies all \(2+4+16+32=54\) leaf paths separately, their full depths, and uniqueness of their witnessing centers. Adding zero coordinates to every query and center preserves each exact Hamming distance. Consequently the witnessed dimensions persist upon increasing the ambient dimension: the witness at three also works at four, at five also works at six, and at seven works at every larger dimension. Combining with parts A and B proves the formula.

## Verification
Run `python3 verify_shell2.py` beside `shell2_witnesses.json` under Python 3.10 or later. The script checks all 54 leaf paths of four complete shattered trees and independently recomputes the exact dimensions in dimensions one through seven using a memoized recursion over all possible query/answer splits; the output is supplied in `verify_shell2_output.txt`. It also verifies the size of each possible positive intersection with the weight-two layer for dimensions five through twelve. The infinite-dimensional upper bound does **not** rely on this finite enumeration: it is the symbolic classification of the weight-zero, weight-two and weight-four tests in the proof.

## Relationship to prior work
Adler, Benediktsson and Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs* (arXiv:2007.16042, first posted 2020-07-31), study the **distance-one edge relation** in Hamming graphs and obtain a sharp VC-dimension bound; its Section 4 also studies intersections of graph neighborhoods and two-neighborhood structure. Their parameter is neither the Littlestone dimension nor the exact distance-two sphere concept family. The 2021 preprint by Malliaris and Moran, *Agnostic Online Learning and Excellent Sets* (arXiv:2108.05569, first posted 2021-08-12), develops a general connection between Littlestone dimension, online learning and stable graphs, but does not compute this particular finite family. An earlier exact VC-dimension computation for the **same** distance-two sphere family obtains the piecewise VC dimensions \(0,1,2,2,3,4,5\) at dimensions \(1,2,3,4,5,6,\ge7\), respectively. VC dimension does not imply the displayed Littlestone values; notably the strict gap at dimension five needs a separate adaptive tree. Chase and Mehalel (arXiv:2609.21445, 2026, Section 5) use the name *d-Hamming spheres*, but their concepts encode fixed-size sparse subsets on tagged coordinate blocks; their claimed growing Littlestone dimension is for that distinct concept family, not for the distance-two sphere incidence on all Boolean cube vertices. Searches for the exact Littlestone rank of halved-cube/distance-two neighborhoods found no directly covering theorem, but this is not a proof of historical priority.

## Limitations
This result concerns deterministic realizable mistake-tree complexity with arbitrary instance queries; it makes no claim about randomized learners, proper-only learners, closed balls, nonbinary Hamming spaces, or higher exact radii. The all-dimensional bound is mathematical; the finite witness checks are not evidence for the infinite bound by themselves. The original-literature comparison has a residual priority risk, especially if a result is recorded under the alternative terminology *halved cubes*, *binary two-spheres*, *online mistake trees*, or *thicket dimension*. Independent audit and independent replication are not claimed.

## References
- Isolde Adler, Bjarki Geir Benediktsson and Dugald Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042v1, 2020-07-31; Section 4 (Hamming-graph edge neighborhoods). https://arxiv.org/abs/2007.16042
- Maryanthe Malliaris and Shay Moran, *Agnostic Online Learning and Excellent Sets*, arXiv:2108.05569v1, 2021-08-12; especially the definition of Littlestone dimension and its relation to graph stability. https://arxiv.org/abs/2108.05569
- Zachary Chase and Idan Mehalel, *Optimal Randomized Proper Online Learning*, arXiv:2609.21445v1, 2026-09-21; Section 5 (different d-sparse block concept family). https://arxiv.org/abs/2609.21445
