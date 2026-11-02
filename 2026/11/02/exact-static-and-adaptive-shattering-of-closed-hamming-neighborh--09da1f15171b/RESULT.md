# Exact static and adaptive shattering of closed Hamming neighborhoods

## Finding
For every pair of integers \(d\ge1\) and \(q\ge2\), let \(H(d,q)\) be the graph on \([q]^d\) in which two distinct vertices are adjacent precisely when they differ in one coordinate. Its closed radius-one neighborhood at \(c\) is \(B(c)=\{x\in[q]^d:d_H(x,c)\le1\}\). Regard the family \(\mathcal B_{d,q}=\{B(c):c\in[q]^d\}\) as a binary concept class under vertex-membership queries.

The exact dimensions are
\[
(\operatorname{VCdim}(\mathcal B_{d,q}),\operatorname{Ldim}(\mathcal B_{d,q}))=
\begin{cases}
(0,0),&d=1,\\
(1,1),&(d,q)=(2,2),\\
(2,3),&(d,q)=(2,3),\\
(3,3),&\text{otherwise}.
\end{cases}
\]
Thus the ternary two-dimensional rook graph is the unique full Hamming graph with a strict static/adaptive gap for closed neighborhoods. In particular, the optimal deterministic worst-case realizable online mistake bound is three in every remaining nondegenerate case, including the ternary rook graph, and is zero or one in the two elementary cases. Every induced subgraph of any Hamming graph has both dimensions at most three for its own closed-neighborhood concept class.

## Assumptions and scope
The alphabet \([q]=\{0,1,\ldots,q-1\}\) is finite, with integer \(q\ge2\). The dimension \(d\) is a positive integer. All centers and query vertices belong to the stated graph. The VC dimension is the largest size of a fixed query support whose every Boolean labeling occurs. Littlestone dimension is the largest depth of a complete binary decision tree whose internal nodes are membership queries and whose every root-to-leaf answer sequence is realized by a concept; dimension zero is assigned to a one-concept class. Answers use inclusive Hamming distance at most one, **not** open adjacency or distance exactly one.

## Proof
**Local geometry.** For distinct centers \(u,v\), the intersection \(B(u)\cap B(v)\) is a complete coordinate line of \(q\) vertices if \(d_H(u,v)=1\), consists of exactly two coordinate recombinations if \(d_H(u,v)=2\), and is empty if \(d_H(u,v)\ge3\). This follows by counting the positions where a center in both balls may disagree with each endpoint. A coordinate line \(L\) is the set of all words obtained by varying one chosen coordinate and fixing the others. For any query \(y\), its incidence on centers of \(L\) is either all of \(L\) (when \(y\in L\)), a singleton (when \(y\notin L\) differs from the fixed off-line coordinates in exactly one place), or empty. Consequently the concept subfamily whose centers lie in \(L\) has Littlestone dimension at most one, because no nontrivial query can split it into two non-singleton classes.

**Universal static upper bound.** Suppose four distinct queries \(A=\{a_1,a_2,a_3,a_4\}\) were shattered. A center \(u\) realizes all four positive labels. For each \(i\), a different center \(v_i\) realizes the three positive labels on \(A\setminus\{a_i\}\) and the negative label at \(a_i\). Since \(|B(u)\cap B(v_i)|\ge3\) and \(v_i\ne u\), the local geometry forces \(d_H(u,v_i)=1\), and the entire triple \(A\setminus\{a_i\}\) lies on a coordinate line \(L_i\) through \(u\). Any two such triples have two distinct vertices in common; two different coordinate lines through \(u\) intersect only at \(u\). Thus all \(L_i\) are the same line and \(A\) lies on that line. A ball intersects a coordinate line either in the entire line, a singleton, or the empty set, and so cannot realize a two-positive/two-negative trace on \(A\). Contradiction. Therefore \(\operatorname{VCdim}\le3\) for every parameter pair.

**Universal adaptive upper bound.** Fix an initial query \(u\). Its positive branch contains only hypotheses with centers in \(B(u)\). Consider any subsequent query \(v\) on this positive version space. If \(v=u\), the negative branch is empty. If \(d_H(u,v)=1\), its positive version space is a coordinate line, which has Littlestone dimension at most one by the preceding observation. If the distance is two, the positive version space contains only two centers and thus has Littlestone dimension at most one; if the distance is at least three it is empty. Hence the restricted family of hypotheses centered in \(B(u)\) cannot shatter a depth-three decision tree: every candidate root query has a branch of dimension at most one. Therefore this positive version space has Littlestone dimension at most two. Every putative depth-four tree for the full class would require its first positive branch to have depth three, which is impossible. Consequently \(\operatorname{Ldim}(\mathcal B_{d,q})\le3\) for all parameters.

**Lower bounds in the two universal embedding cases.** In \(H(3,2)\), the three fixed queries \((0,0,0),(0,0,1),(0,1,0)\) realize all eight answer triples as the eight centers run through \(\{0,1\}^3\). In \(H(2,4)\), the queries \((0,0),(0,1),(1,2)\) likewise realize all eight triples with centers in \(\{0,1,2,3\}^2\). Both assertions follow by direct substitution in the inclusive-distance rule and are checked in the attached verifier. Each \(H(d,q)\) with \(d\ge3\) contains a coordinate-preserving copy of \(H(3,2)\), and each \(H(2,q)\) with \(q\ge4\) contains one of \(H(2,4)\). Restricting to the corresponding centers and queries preserves all eight traces. These classes therefore have VC dimension three and, by the general lower bound \(\operatorname{VCdim}\le\operatorname{Ldim}\), also Littlestone dimension three.

**The three exceptional regimes.** If \(d=1\), every radius-one ball is the whole complete graph, giving both dimensions zero. If \((d,q)=(2,2)\), the graph is the four-cycle and its closed balls are the four complements of singletons: one query is shattered, no two are shattered, and any first query has a singleton negative branch, so both dimensions equal one.

For \((d,q)=(2,3)\), identify centers and queries with a three-by-three grid. The closed ball of a query is its row union its column. The two queries \((0,0),(0,1)\) are shattered. A hypothetical shattered triple must admit an all-zero center, so its three distinct query cells use at most two rows and at most two columns. They therefore occupy three corners of a two-by-two subgrid. One corner shares its row with one other queried cell and its column with the remaining queried cell. Any center whose ball includes that corner necessarily includes at least one of these two companions, so the singleton-positive trace at the corner is absent. Thus VC dimension is two.

To prove the Littlestone lower bound, the following complete depth-three tree is realized. At the root query \((0,0)\), both branches next query \((0,1)\). On the four length-two answer prefixes \((0,0)\), \((0,1)\), \((1,0)\), and \((1,1)\), the respective third queries are \((1,0)\), \((1,0)\), \((1,1)\), and \((1,0)\). The eight full answer paths and their center witnesses are:

| Path | Center witness |
| --- | --- |
| \((0,0,0)\) | \((2,2)\) |
| \((0,0,1)\) | \((1,2)\) |
| \((0,1,0)\) | \((2,1)\) |
| \((0,1,1)\) | \((1,1)\) |
| \((1,0,0)\) | \((2,0)\) |
| \((1,0,1)\) | \((1,0)\) |
| \((1,1,0)\) | \((0,1)\) |
| \((1,1,1)\) | \((0,0)\) |

Each row of the displayed table is verified by Hamming distance, and all centers are distinct. Thus the Littlestone dimension is three, matching the universal upper bound.

Finally, for an induced subgraph \(G\) of \(H(d,q)\), a closed neighborhood in \(G\) is the intersection of one ambient ball with \(V(G)\). Restriction of query coordinates and deletion of hypotheses cannot increase either shattering dimension, proving the inherited upper bound.

## Verification
Execute `python3 VERIFY.py` using Python 3 and its standard library. The program independently forms every closed-ball incidence mask, determines exact dimensions using subset enumeration and the recursive version-space minimax formula, checks fixed shattered supports, and checks all eight branches of the explicit ternary depth-three tree. Parameters independently enumerated are \((d,q)\in\{(1,2),(1,5),(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2)\}\). It reports `ALL_CLOSED_HAMMING_RADIUS_ONE_CHECKS_PASS cases= 9`. These finite computations verify boundary instances and witnesses; the all-parameter inequalities rest on the geometric proof above.

## Relationship to prior work
Adler, Benediktsson and Macpherson [1, Theorems 4.6--4.8] determine the VC behavior of **open** Hamming-graph neighborhoods and prove bounded VC dimension for closed neighborhoods only as a general logical consequence. Their full-text Hamming-section geometry supports our local comparisons but does not state the exact **closed** parameter-by-parameter VC/Littlestone classification. Open and closed dimensions cannot simply be equated: the published open-neighborhood theorem gives VC dimension two at \(H(3,2)\), whereas the present closed result gives three. Bhaskar [2] develops general adaptive shattering/thicket theory, not this graph-specific classification. The later open-neighborhood work of Housholder, Mangiapanello and Senger [3] studies size thresholds for induced subsets, rather than closed balls or adaptive dimension. Accessible literature and semantic-record searches did not identify a stronger theorem implying this exact statement; this is not proof of historical priority.

## Limitations
The theorem treats finite, full Hamming graphs with \(d\ge1\) and \(q\ge2\), and proves only an upper bound for arbitrary induced subgraphs. It concerns radius-one **closed** neighborhoods, not open neighborhoods, larger radii, or arbitrary product graphs. No independent scientific audit or comprehensive priority certification has been conducted.

## References
[1] I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik--Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, first posted 2020-07-31, especially Section 4, https://arxiv.org/abs/2007.16042.

[2] S. Bhaskar, *Thicket Density*, arXiv:1702.03956, first posted 2017-02-13, https://arxiv.org/abs/1702.03956.

[3] C. Housholder, L. Mangiapanello and S. Senger, *VC-dimension of subsets of Hamming graphs*, arXiv:2505.14641, first posted 2025-05-20, especially Introduction and Theorems 1.1--1.8, https://arxiv.org/abs/2505.14641.
