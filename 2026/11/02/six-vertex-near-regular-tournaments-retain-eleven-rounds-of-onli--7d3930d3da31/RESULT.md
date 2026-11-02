# Six-vertex near-regular tournaments retain eleven rounds of online shattering

## Finding
Let \(\mathcal N_6\) consist of all tournaments on the fixed labeled vertex set \(\{0,1,2,3,4,5\}\) whose multiset of outdegrees is \(\{2,2,2,3,3,3\}\). A hypothesis answers each unordered-pair query with the direction of that edge. There are exactly \(2640\) distinct hypotheses. The complete polynomial enumerating VC-shattered edge-query supports is
\[
\Phi_{\mathcal N_6}(z)=1+15z+105z^2+455z^3+1335z^4+2697z^5+3355z^6+1185z^7.
\]
In particular,
\[
\operatorname{VCdim}(\mathcal N_6)=7,\qquad
\operatorname{Ldim}(\mathcal N_6)=11.
\]
The full binary online query tree of depth eleven uses only the fifteen edges of the six-vertex tournament; its \(2048\) leaves have distinct explicit valid tournament witnesses. Since \(2640<2^{12}\), no depth-twelve tree exists. Thus the static-to-adaptive gap is four. Removing one labeled vertex and its six incident edge queries from the analogous seven-vertex regular-tournament representation preserves the full eleven-round online capacity.

Exactly \(1185\) labeled seven-edge supports are shattered, forming precisely five isomorphism types. Listed by sorted support-graph degree sequence, triangle count, and labeled count, these types are:

| Degree sequence | Triangles | Labeled supports |
| --- | ---: | ---: |
| \((1,1,3,3,3,3)\) | 4 | 15 |
| \((1,2,2,3,3,3)\) | 1 | 360 |
| \((1,2,2,3,3,3)\) | 2 | 360 |
| \((2,2,2,2,3,3)\) | 1 | 360 |
| \((2,2,2,2,3,3)\) | 2 | 90 |

These signatures distinguish the five isomorphism types among maximum shattered supports; they are not asserted to classify arbitrary seven-edge graphs.

## Assumptions and scope
All tournaments are orientations of complete simple labeled graphs. Each edge is a distinct Boolean coordinate, and the chosen reference orientation affects neither shattering dimension. For a query support \(S\), VC shattering means that every one of its \(2^{|S|}\) directed-edge assignments extends to some hypothesis. Littlestone shattering means an adaptive full binary decision tree in which each root-to-leaf assignment is realized by a hypothesis; the queried edge may depend on earlier answers.

For context, on \(2m\) labeled vertices a **near-regular tournament** has exactly \(m\) vertices of outdegree \(m-1\) and \(m\) of outdegree \(m\), with the high-degree vertices not fixed in advance. The theorem above is the exact \(m=3\) case, including every shattered-support coefficient. The associated finite cut test below holds for all \(m\ge1\), but the stated polynomial and online depth are specifically for six vertices. A small-order check also gives the pairs \((\operatorname{VCdim},\operatorname{Ldim})=(1,1)\) for two vertices and \((3,4)\) for four vertices.

## Proof
**1. From near-regular to regular tournaments.** Given any near-regular tournament on \(2m\) vertices, adjoin a new vertex \(\ast\). Orient \(\ast\to v\) for each low-score vertex \(v\) of score \(m-1\), and \(v\to\ast\) for each high-score vertex of score \(m\). Every old vertex now has score \(m\), and \(\ast\) has score \(m\), so the resulting tournament on \(2m+1\) vertices is regular. Conversely, deleting \(\ast\) from any such regular tournament gives a near-regular tournament, and the removed orientations are uniquely reconstructible from the remaining degrees. This is a bijection, although the edge-query domains differ.

**2. A uniform support-feasibility criterion.** Let \(V\) have \(2m\) vertices and \(S\subseteq E(K_V)\). For \(U\subset V\), write \(\delta_S(U)\) for edges of \(S\) with precisely one endpoint in \(U\), and \(u=|U|\). The following criterion holds:
\[
S\text{ is shattered by all near-regular tournaments on }V
\quad\Longleftrightarrow\quad
|\delta_S(U)|\le\left\lfloor\frac{\min\{u(2m+1-u),(2m-u)(u+1)\}}{2}\right\rfloor
\quad\text{for every }U\subset V.
\]
To justify it, adjoin \(\ast\), so completion is to an orientation with prescribed score \(m\) at every vertex of \(K_{2m+1}\). Fix any directions on \(S\), and let \(F\) be the remaining undirected edges, which include all edges incident to \(\ast\). If \(s(v)\) is the already-forced score, the remaining edges must provide exactly \(m-s(v)\) wins at \(v\). The integral edge-to-vertex allocation lemma (proved by unit-capacity max-flow/min-cut, or by the usual prescribed-indegree orientation theorem) gives feasibility if and only if the total required wins equal \(|F|\) and for every \(W\subseteq V\cup\{\ast\}\),
\[
\sum_{v\in W}\bigl(m-s(v)\bigr)\ge |E_F(W)|.
\]
The totals agree automatically. Writing \(a_W\) for forced edges from the complement into \(W\), the displayed inequality simplifies to
\[
a_W\le m|W|-\binom{|W|}{2}=	frac12|W|(2m+1-|W|).
\]
For every orientation of \(S\) to extend, the maximum possible \(a_W\), namely \(|S\cap\delta(W)|\), must obey the inequality for all \(W\). Taking \(W=U\subseteq V\) and \(W=(V\setminus U)\cup\{\ast\}\) gives the two bounds in the claimed minimum. Conversely, the bounds make every possible assignment feasible. This completion reduction is standard background; novelty is not asserted for the general orientation-feasibility lemma itself.

**3. Exact six-vertex census.** Order the fifteen edges lexicographically and encode each orientation as a fifteen-bit integer, with bit one meaning that the smaller-index endpoint wins. Iterate over all \(2^{15}=32768\) encodings and retain exactly those in which the sorted score list is \((2,2,2,3,3,3)\). This yields \(2640\) distinct hypotheses. Independently iterate over all \(32768\) edge-support masks \(S\), and calculate the set of projected bit patterns \(\{h\mathbin{\&}S:h\in\mathcal N_6\}\). Its size is \(2^{|S|}\) precisely when \(S\) is shattered. Grouping the surviving masks by cardinality produces, from degrees zero to seven,
\[
(1,15,105,455,1335,2697,3355,1185),
\]
with no supports of size eight or greater. The independent universal cut test from step 2 gives the same counts on all \(32768\) masks. These loops are logically exhaustive finite proofs of the six-vertex numbers, not sampling or extrapolation.

For the extremal classification, identify the vertex relabeling orbit of every seven-edge shattered support by minimizing its adjacency bitmask over all \(6!=720\) permutations. Exactly five canonical masks occur, with orbit sizes \(15,90,360,360,360\). Directly counting degrees and triangles gives the five signatures in the table, which are pairwise distinct. This exhausts every maximum shattered support.

**4. Online depth.** The accompanying JSON certificate stores the complete depth-eleven tree in binary-heap order: 2047 internal edge-query indices and 2048 leaf orientations. The verifier reconstructs all \(2640\) valid score-constrained tournaments, checks that every leaf orientation is in the class, and verifies all eleven root-to-leaf answers against that leaf. The witnesses are pairwise distinct. This proves the lower bound of eleven by an explicit finite certificate. Every full depth-\(d\) tree requires \(2^d\) distinct hypotheses, so \(d=12\) is impossible from \(2640<4096\). Hence the online dimension is exactly eleven.

## Verification
Run `python verify_nearregular.py` with `nearregular_depth11_certificate.json` in the same directory (Python 3.8 or newer; standard library only). The program (i) directly enumerates all score-valid orientations, (ii) tests every edge support by its actual traces, (iii) independently checks all cut inequalities, (iv) constructs canonical graph-isomorphism types under every vertex permutation, (v) checks every path of the full online certificate, and (vi) independently checks the two- and four-vertex boundary cases. The final expected line is `ALL_NEARREGULAR_TOURNAMENT_CHECKS_PASS`. The explicit certificate and source are part of the present package; no outside data files or previous result's log is required.

## Relationship to prior work
Brualdi and Kiernan (2009, Theorem 3.1 and Corollary 3.2) already study completions of partial tournaments and specifically identify nearly regular even-order scores. Kolesnik and Sanchez (2020, arXiv:2009.09322, Theorem 5 and Corollary 6) give a more general graphic-zonotope treatment of score constraints. The cut test above is an application of that established completion theory and is not presented as a new principle.

Previously obtained results determine all-odd-order regular-tournament VC dimension and its extremal support structure, as well as the seven-vertex regular-tournament online dimension and its twenty-one-edge shattering polynomial. Those do **not** determine how many supports using only the fifteen edges avoiding one specified vertex are shattered, nor whether an eleven-deep online tree survives deletion of its six incident queries. These two restricted-coordinate questions are answered here by direct census and a new explicit query-tree certificate. No general near-regular all-order VC formula or online formula is claimed.

## Limitations
The exact polynomial, five maximum-support types, and online dimension are certified only for the six-vertex class, with two- and four-vertex boundary checks. The general cut-completion equivalence does not supply explicit coefficient formulas for all even orders. Computational exhaustion certifies the finite statement because its search domains are enumerated fully, but it does not establish any unbounded-size classification. Earlier equivalent computations under alternative score-constrained-orientation terminology remain a possible historical-priority risk.

## References
1. R. A. Brualdi and K. Kiernan, *Landau's and Rado's Theorems and Partial Tournaments*, Electronic Journal of Combinatorics 16 (2009), N2, Theorem 3.1 and Corollary 3.2. DOI: 10.37236/240.
2. B. Kolesnik and M. Sanchez, *The Geometry of Random Tournaments*, arXiv:2009.09322, first posted 2020-09-19; Theorem 5 and Corollary 6.
3. S. L. Hakimi, *On the degrees of the vertices of a directed graph*, Journal of the Franklin Institute 279 (1965), 290–308. Used for the standard prescribed-orientation principle.
