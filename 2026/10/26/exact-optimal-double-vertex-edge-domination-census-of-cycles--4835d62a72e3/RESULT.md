# Exact optimal double vertex-edge domination census of cycles

## Finding
For every integer \(n\ge3\), let \(C_n\) be the simple cycle with individually labeled vertices \(0,1,\ldots,n-1\) in cyclic order. A set \(D\subseteq V(C_n)\) *double vertex-edge dominates* when every edge \(uv\) satisfies
\[
|D\cap(N[u]\cup N[v])|\ge2,
\]
where the closed neighborhoods are taken in \(C_n\). Let \(\gamma_{\mathrm{dve}}(C_n)\) be the least such cardinality and let \(M_n\) count all minimum sets (vertex labels are fixed and sets are unlabelled).

Then
\[
\gamma_{\mathrm{dve}}(C_n)=\left\lceil\frac n2\right\rceil,
\qquad
M_n=\begin{cases}
6,&n\equiv0\pmod4,\\
2,&n\equiv2\pmod4,\\
n\left\lfloor\frac{n+3}{4}\right\rfloor,&n\text{ odd}.
\end{cases}
\]
Moreover, all minimum sets have the following **complete gap classification**. Write their selected vertices in positive cyclic order and let \(d_1,\ldots,d_k\) be the positive forward spacings between successive selected vertices, where \(k=\lceil n/2\rceil\) and \(\sum_i d_i=n\). Up to cyclic rotation of the gap list:

1. For even \(n\), every gap equals \(2\), or (only when \(4\mid n\)) the gaps alternate \(1,3,1,3,\ldots\).
2. For odd \(n\), choose exactly one integer \(r\) with \(0\le r\le\lfloor(k-1)/2\rfloor\). The gap list consists of one consecutive alternating run \(1,3,1,3,\ldots,3,1\) containing \(r\) threes and \(r+1\) ones, with all remaining gaps equal to \(2\). The run may occupy the whole cyclic list.

For odd \(n\), each choice of \(r\) yields exactly \(n\) labeled minimum sets, forming one rotation orbit. For even \(n\), there is one orbit if \(n\equiv2\pmod4\), and two orbits (of sizes \(2\) and \(4\)) if \(n\equiv0\pmod4\).

## Assumptions and scope
Graphs are finite, undirected, simple, and without loops. The cycle \(C_n\) has length \(n\ge3\); the closed neighborhood is \(N[v]=\{v\}\cup\{u:uv\in E\}\). The word 'double' means *two distinct selected vertices* dominate each edge, not two incidences or two paths. This is the \(k=2\) case of \(k\)-vertex-edge domination. Counts distinguish the named cycle vertices; sets are not ordered and color labels are not involved.

## Proof
**1. Local coverage and the minimum size.** For \(n\ge5\), the closed-neighborhood union of the edge between vertices \(i\) and \(i+1\) (indices modulo \(n\)) is exactly \(\{i-1,i,i+1,i+2\}\). Hence a subset is feasible precisely when every cyclic block of four consecutive vertices contains at least two selected vertices. Each vertex belongs to four of these \(n\) blocks, so double counting their selected incidences gives \(4|D|\ge2n\). Alternating selected vertices attain the bound for even \(n\); for odd \(n\), selecting the positions \(0,2,4,\ldots,n-1\) has one adjacent selected pair and every four-block contains at least two. Thus \(\gamma_{\mathrm{dve}}(C_n)=\lceil n/2\rceil\) for \(n\ge5\). When \(n=3,4\), every edge's closed-neighborhood union is all of \(V(C_n)\), so any two-vertex set works; the same minimum formula holds.

**2. Gap characterization.** Assume \(n\ge5\) and \(D\) is a minimum set with \(k=|D|\ge3\). The four-block constraint is equivalent to
\[
d_i+d_{i+1}\le4\qquad(1\le i\le k),
\]
with cyclic gap indices. Indeed, if two consecutive gaps sum to at least five, the four vertices immediately after the first of their three selected endpoints contain at most one selected vertex. Conversely, a bad four-block, containing zero or one selected vertex, produces three successive selected endpoints whose first-to-third distance is at least five. Since each gap is positive, the inequality also forces \(d_i\in\{1,2,3\}\).

Put \(e_i=2-d_i\). Then
\[
e_i\in\{-1,0,1\},\qquad e_i+e_{i+1}\ge0,
\qquad\sum_i e_i=2k-n.
\]
Consequently a \(-1\) can only be adjacent to \(+1\), never to \(0\) or another \(-1\).

For even \(n\), the displayed sum is zero. If any zero is present, each nonempty maximal cyclic run of nonzeros starts and ends with \(+1\) and has at least one more plus than minus, which contradicts zero total sum. Thus all entries are zero, or there are no zeros at all. In the latter case nonadjacency of minuses and equal plus/minus counts force strict cyclic alternation, possible precisely when \(k\) is even, equivalently \(4\mid n\). Translating back gives the two asserted even-gap patterns.

For odd \(n\), the sum is one. If a zero occurs, the same run argument forces exactly one nonzero run, of excess exactly one. Nonadjacent minuses and plus endpoints then force its signs to alternate \(+1,-1,+1,\ldots,-1,+1\). If no zero occurs, the plus count exceeds the minus count by one; since minuses are nonadjacent, the cyclic word has exactly one adjacent-plus seam, and cutting at that seam again gives the same alternating run occupying the entire list. Setting \(r\) equal to the number of negative entries yields precisely the indicated range and gap structure. This proves necessity, and reversing the steps gives sufficiency. The exceptional cycles \(n=3,4\) satisfy the same listed patterns by direct inspection of their two-vertex subsets.

**3. Counting and rotation orbits.** For even \(n\), the all-two gap list determines the two alternating vertex sets. If \(4\mid n\), cyclically alternating gaps \(1,3\) determine four additional, distinct vertex sets. Hence the even cases give \(2\) or \(6\).

For odd \(n\), fix \(r\) in the allowed range. Let a selected vertex be marked as the first vertex and read the \(k\) gaps from it. There are exactly \(k\) possible gap words of this type: the unique alternating run can start at any of the \(k\) gap indices (including the no-zero full-run case, which has a unique adjacent-\(1\) seam). Choosing the position of the marked vertex gives \(nk\) marked pairs \((D,v)\); each unmarked minimum set occurs exactly \(k\) times. Thus each \(r\) yields exactly \(n\) sets. There are \(\lfloor(k+1)/2\rfloor=\lfloor(n+3)/4\rfloor\) permitted values of \(r\). Rotation acts transitively within each fixed-\(r\) family, while distinct \(r\) cannot be rotations of one another. This proves the count and orbit assertions. \(\square\)

## Verification
The accompanying standalone program `verify.py` uses two structurally distinct finite checks. First it constructs the actual closed-edge-neighborhood unions of each labeled cycle and exhaustively tests all vertex subsets of every size up to the claimed minimum for \(3\le n\le18\); it also checks the gap characterization on every optimum. Second it implements the weighted trace of an eight-state binary length-four constraint graph, independently counting optimum cyclic words for every \(5\le n\le80\). Running `python verify.py` completes with `PASS` and all counts agree with the formula. The mathematical proof above establishes the infinite-family theorem; no finite test substitutes for it.

## Relationship to prior work
The double vertex-edge domination parameter originates in Krishnakumari, Chellali, and Venkatakrishnan (2017), and the broader \(k\)-vertex-edge framework is treated by Bhattacharya and Paul (2023). The scalar optimum \(\lceil n/2\rceil\) is elementary and is **not asserted to be new**. The present claim is the complete structural description and exact cardinality/rotation-orbit census of **all** optimum cycle solutions. The inspected 2023 primary paper develops complexity and algorithms for trees, without reporting this minimum-set census. The accessible 2017 publisher abstract describes general bounds and tree results; its complete text was not accessible, so the priority comparison there remains limited. Related double *edge-vertex* results select edges to dominate vertices, whereas the present problem selects vertices to dominate edges; swapping those notions is not a valid implication.

## Limitations
This theorem applies to simple cycles only and to the requirement of two distinct dominating vertices per edge. It does not determine the polynomial counting feasible sets of all cardinalities or a general-graph algorithm. The exact literature-priority status is subject to the accessibility limitation for the 2017 source and to potential unindexed publications.

## References
1. B. Krishnakumari, M. Chellali, and Y. B. Venkatakrishnan, *Double vertex-edge domination*, Discrete Mathematics, Algorithms and Applications 9 (2017), 1750045. DOI: `10.1142/S1793830917500458`. Publisher first-public date displayed as 2017-07-11.
2. D. Bhattacharya and S. Paul, *On k-vertex-edge domination of graph*, arXiv:`2310.07452` (first public 2023-10-11), later published in Bulletin of the Malaysian Mathematical Sciences Society.
3. F. Miao, W. Fan, M. Chellali, R. Khoeilar, S. M. Sheikholeslami, and M. Soroudi, *On Two Open Problems on Double Vertex-Edge Domination in Graphs*, Mathematics 7 (2019), 1010. DOI: `10.3390/math7111010`.
